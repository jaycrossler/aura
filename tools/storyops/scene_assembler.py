"""
Scene Assembler — Pipeline Step 2.

For each scene in the chapter outline, assembles a full context packet:
  - Registry metadata (title, tags, POV, timeline anchor)
  - Source file content (if the scene file exists in /knowledge/scenes/)
  - RAG-matched knowledge docs (characters, locations, technology, factions, etc.)

The assembled packets feed Step 3 (weaving) so the LLM has grounded context
rather than generating from nothing.

RAG strategy: keyword matching on scene tags, title tokens, and notes text.
Extend _rag_search() to use embedding similarity if/when the knowledge base
grows large enough to warrant it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import frontmatter

from tools.storyops.chapter_planner import ChapterOutline, BeatPlan
from tools.storyops.common.story_logger import StoryLogger, PipelineStage


# ── Knowledge base roots (extend as the project grows) ───────────────────────

KNOWLEDGE_ROOTS: dict[str, Path] = {
    "characters":    Path("knowledge/characters"),
    "locations":     Path("knowledge/locations"),
    "technology":    Path("knowledge/technology"),
    "factions":      Path("knowledge/factions"),
    "timeline":      Path("knowledge/timeline"),
    "magic_systems": Path("knowledge/magic-systems"),
    "lore":          Path("knowledge/lore"),
}

SYNOPSIS_PATH = Path("knowledge/MASTER-SYNOPSIS.md")

# Max knowledge snippets per scene (keep prompts bounded)
MAX_KNOWLEDGE_PER_SCENE = 10
# Character budget per snippet (chars)
SNIPPET_CHARS = 700


# ── Data models ───────────────────────────────────────────────────────────────

@dataclass
class KnowledgeSnippet:
    category: str
    path:     str
    title:    str
    content:  str    # trimmed to SNIPPET_CHARS


@dataclass
class ScenePacket:
    scene_id:       str
    registry_entry: dict[str, Any]
    source_notes:   str           # content of the scene source file, if it exists
    knowledge:      list[KnowledgeSnippet]
    beat:           BeatPlan


@dataclass
class AssembledChapter:
    outline:          ChapterOutline
    scene_packets:    list[ScenePacket]
    synopsis_snippet: str
    all_source_files: list[str]   # sorted de-duped list for version manifest


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_md(path: Path, max_chars: int = SNIPPET_CHARS) -> str:
    if not path.exists():
        return ""
    try:
        post = frontmatter.loads(path.read_text(encoding="utf-8"))
        return post.content[:max_chars]
    except Exception:
        return path.read_text(encoding="utf-8")[:max_chars]


def _tokenize(text: str) -> set[str]:
    """Produce a set of meaningful lowercase tokens from a string."""
    tokens = set()
    for part in text.replace("_", " ").replace("-", " ").lower().split():
        cleaned = part.strip(".,;:!?()'\"")
        if len(cleaned) > 2:
            tokens.add(cleaned)
    return tokens


def _rag_search(corpus: str, log: StoryLogger) -> list[KnowledgeSnippet]:
    """
    Keyword-match knowledge files against the scene corpus text.
    Returns up to MAX_KNOWLEDGE_PER_SCENE snippets ranked by match density.
    """
    corpus_tokens = _tokenize(corpus)
    scored: list[tuple[int, KnowledgeSnippet]] = []

    for category, root in KNOWLEDGE_ROOTS.items():
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            file_tokens = _tokenize(path.stem)
            # Also scan first 200 chars of file for topic tokens
            first_chunk = path.read_text(encoding="utf-8")[:200].lower() if path.exists() else ""
            file_tokens |= _tokenize(first_chunk)
            
            match_count = len(file_tokens & corpus_tokens)
            if match_count > 0:
                content = _load_md(path, SNIPPET_CHARS)
                if content:
                    snippet = KnowledgeSnippet(
                        category = category,
                        path     = str(path),
                        title    = path.stem.replace("_", " ").replace("-", " ").title(),
                        content  = content,
                    )
                    scored.append((match_count, snippet))

    # Sort by match density descending, cap at MAX_KNOWLEDGE_PER_SCENE
    scored.sort(key=lambda x: x[0], reverse=True)
    results = [s for _, s in scored[:MAX_KNOWLEDGE_PER_SCENE]]

    if not results:
        log.debug("No knowledge docs matched for this scene corpus")

    return results


# ── Main function ─────────────────────────────────────────────────────────────

def assemble_chapter(
    outline: ChapterOutline,
    scene_registry: dict[str, Any],
    log: StoryLogger,
) -> AssembledChapter:
    """
    Build a full context packet for every beat/scene in the chapter outline.

    Args:
        outline:        ChapterOutline from plan_chapter()
        scene_registry: Full scene registry dict keyed by scene_id
        log:            Job-scoped StoryLogger
    """
    log.set_stage(PipelineStage.ASSEMBLE)

    scene_packets:    list[ScenePacket] = []
    all_source_files: set[str]          = set()

    # Load master synopsis for overall story grounding
    synopsis_snippet = ""
    if SYNOPSIS_PATH.exists():
        synopsis_snippet = _load_md(SYNOPSIS_PATH, max_chars=1500)
        all_source_files.add(str(SYNOPSIS_PATH))
        log.info("Master synopsis loaded", {"chars": len(synopsis_snippet)})
    else:
        log.warn("MASTER-SYNOPSIS.md not found — LLM will lack story-level context")

    # Build a beat lookup so we can pair beats with scene IDs
    beat_map: dict[str, BeatPlan] = {b.scene_id: b for b in outline.beats}

    for beat in outline.beats:
        scene_id   = beat.scene_id
        reg_entry  = scene_registry.get(scene_id, {})

        if not reg_entry:
            log.warn(f"Scene '{scene_id}' missing from registry — assembling with empty metadata")

        # ── Load source file ──────────────────────────────────
        source_notes = ""
        source_file  = reg_entry.get("source_file")
        if source_file:
            sp = Path(source_file)
            if sp.exists():
                source_notes = _load_md(sp, max_chars=4000)
                all_source_files.add(source_file)
                log.info(f"Source file loaded for '{scene_id}'",
                         {"path": source_file, "chars": len(source_notes)})
            else:
                log.warn(f"Source file for '{scene_id}' not found at '{source_file}' — "
                         "using registry notes only")
        else:
            log.debug(f"No source file registered for '{scene_id}'")

        # Fallback: use registry notes
        if not source_notes:
            source_notes = reg_entry.get("notes", "")

        # ── Build RAG corpus ──────────────────────────────────
        rag_corpus = " ".join(filter(None, [
            reg_entry.get("title", ""),
            reg_entry.get("notes", ""),
            source_notes,
            beat.beat_summary,
            " ".join(reg_entry.get("tags", [])),
            " ".join(reg_entry.get("characters", [])),
            reg_entry.get("location", ""),
        ]))

        knowledge = _rag_search(rag_corpus, log)
        for k in knowledge:
            all_source_files.add(k.path)

        log.scene_assembled(
            scene_id      = scene_id,
            knowledge_docs = len(knowledge),
            source_chars   = len(source_notes),
        )

        scene_packets.append(ScenePacket(
            scene_id       = scene_id,
            registry_entry = reg_entry,
            source_notes   = source_notes,
            knowledge      = knowledge,
            beat           = beat,
        ))

    log.info("Assembly complete", {
        "scene_packets":    len(scene_packets),
        "total_source_files": len(all_source_files),
        "total_knowledge_snippets": sum(len(p.knowledge) for p in scene_packets),
    })

    return AssembledChapter(
        outline          = outline,
        scene_packets    = scene_packets,
        synopsis_snippet = synopsis_snippet,
        all_source_files = sorted(all_source_files),
    )
