"""
Chapter Generator — Pipeline Orchestrator.

Replaces the original chapter_generator.py. Drives the full four-step pipeline:

  Step 1: chapter_planner   → beat-by-beat chapter outline (LLM call)
  Step 2: scene_assembler   → RAG-assembled scene packets
  Step 3: chapter_weaver    → full prose + beat metadata (LLM call)
  Step 4: artifact_exporter → format-specific artifact (optional LLM call)
  Final:  version_manager   → versioned save + manifest update

Each step is independently logged so you can inspect what happened at any stage.
The per-step outputs are also embedded in the .meta.json sidecar.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from tools.storyops.common.config import load_yaml
from tools.storyops.common.story_logger import StoryLogger, PipelineStage
from tools.storyops.chapter_planner import plan_chapter, ChapterOutline
from tools.storyops.scene_assembler import assemble_chapter, AssembledChapter
from tools.storyops.chapter_weaver import weave_chapter, WovenChapter
from tools.storyops.artifact_exporter import export_artifact
from tools.storyops.version_manager import save_version, get_latest


# ── Config paths ──────────────────────────────────────────────────────────────
STRUCTURE_PATH = Path("control/story-structure.yaml")
REGISTRY_PATH  = Path("control/scene-registry.yaml")
PROFILES_PATH  = Path("control/render-profiles.yaml")

DEFAULT_VOICE = (
    "Grounded hard-sci-fi with restrained lyricism. "
    "Third-person intimate, deep inside a single POV's sensory and emotional experience. "
    "Emotionally precise beats. Scientific plausibility is sacred."
)


# ── Config loading ────────────────────────────────────────────────────────────

def _load_structure() -> dict[str, Any]:
    return load_yaml(STRUCTURE_PATH) if STRUCTURE_PATH.exists() else {}


def _load_registry() -> dict[str, Any]:
    """Returns registry keyed by scene id."""
    raw = load_yaml(REGISTRY_PATH) if REGISTRY_PATH.exists() else {}
    return {s["id"]: s for s in raw.get("scenes", [])}


def _load_profiles() -> dict[str, Any]:
    """Returns profiles keyed by profile id."""
    raw = load_yaml(PROFILES_PATH) if PROFILES_PATH.exists() else {}
    return {p["id"]: p for p in raw.get("profiles", [])}


def _find_chapter(structure: dict[str, Any], chapter_id: str) -> dict[str, Any] | None:
    for ch in structure.get("chapters", []):
        if ch["id"] == chapter_id:
            return ch
    return None


def _prior_chapter_excerpt(structure: dict[str, Any], chapter_id: str) -> str:
    """Load a short excerpt from the previous chapter's latest prose version."""
    chapters = structure.get("chapters", [])
    for i, ch in enumerate(chapters):
        if ch["id"] == chapter_id and i > 0:
            prev_id   = chapters[i - 1]["id"]
            prev_path = Path(f"generated/versions/{prev_id}_manifest.json")
            if prev_path.exists():
                manifest = json.loads(prev_path.read_text(encoding="utf-8"))
                latest   = manifest.get("latest_file")
                if latest and Path(latest).exists():
                    text = Path(latest).read_text(encoding="utf-8")
                    # Strip frontmatter, return last ~1500 chars
                    if "---" in text:
                        parts = text.split("---", 2)
                        body  = parts[2] if len(parts) >= 3 else text
                    else:
                        body = text
                    return body.strip()[-1500:]
    return ""


# ── Main entry point ──────────────────────────────────────────────────────────

def generate_chapter(item: dict[str, Any]) -> str | None:
    """
    Run the full generation pipeline for one queue item.

    Args:
        item: A single queue entry from generation-queue.yaml

    Returns:
        Path to the output file, or None if skipped/failed.
    """
    job_id = item.get("id", f"job_{int(time.time())}")
    log    = StoryLogger(job_id)
    t0     = time.monotonic()

    log.set_stage(PipelineStage.ORCHESTRATE)
    log.info(f"Pipeline starting: '{job_id}'", {
        "chapter_id":     item.get("chapter_id"),
        "render_profile": item.get("render_profile"),
        "pov_override":   item.get("pov_override"),
        "overwrite":      item.get("overwrite", True),
    })

    # ── Load all config ───────────────────────────────────────
    structure = _load_structure()
    registry  = _load_registry()
    profiles  = _load_profiles()

    if not structure:
        log.error("story-structure.yaml not found or empty — aborting")
        return None

    log.info("Config loaded", {
        "chapters":          len(structure.get("chapters", [])),
        "scenes_in_registry": len(registry),
        "render_profiles":   len(profiles),
    })

    # ── Resolve chapter ───────────────────────────────────────
    chapter_id  = item.get("chapter_id")
    if not chapter_id:
        log.error("Queue item has no chapter_id — aborting")
        return None

    chapter_def = _find_chapter(structure, chapter_id)
    if not chapter_def:
        log.error(f"chapter_id '{chapter_id}' not found in story-structure.yaml — aborting")
        return None

    # ── Resolve render profile ────────────────────────────────
    profile_id    = item.get("render_profile", "standard")
    render_profile = profiles.get(profile_id)
    if not render_profile:
        log.warn(f"Render profile '{profile_id}' not found — using inline fallback")
        render_profile = {
            "id":             profile_id,
            "voice_style":    item.get("voice_style", DEFAULT_VOICE),
            "tone_variant":   "standard",
            "format":         "prose",
            "content_filter": "standard",
            "focus":          "narrative",
        }
    log.info("Render profile resolved", {
        "profile":      profile_id,
        "format":       render_profile.get("format"),
        "tone_variant": render_profile.get("tone_variant"),
    })

    # ── Overwrite guard ───────────────────────────────────────
    fmt     = render_profile.get("format", "prose")
    latest  = get_latest(chapter_id, fmt=fmt)
    if latest and not item.get("overwrite", True):
        log.pipeline_skipped(
            f"Chapter '{chapter_id}' [{fmt}] already has v{latest.version_num:03d} "
            "and overwrite=false"
        )
        return latest.file_path

    # ── Step 1: Plan ──────────────────────────────────────────
    prior_excerpt = _prior_chapter_excerpt(structure, chapter_id)
    try:
        outline: ChapterOutline = plan_chapter(
            chapter_def          = chapter_def,
            scene_registry       = registry,
            render_profile       = render_profile,
            log                  = log,
            prior_chapter_summary = prior_excerpt,
        )
    except Exception as exc:
        log.pipeline_error("chapter_planner failed", exc)
        raise

    log.info("Step 1 complete — outline", {
        "beats":             len(outline.beats),
        "word_count_target": outline.word_count_target,
        "opening_image":     outline.opening_image[:80],
    })

    # ── Step 2: Assemble ──────────────────────────────────────
    try:
        assembled: AssembledChapter = assemble_chapter(
            outline        = outline,
            scene_registry = registry,
            log            = log,
        )
    except Exception as exc:
        log.pipeline_error("scene_assembler failed", exc)
        raise

    log.info("Step 2 complete — scene assembly", {
        "packets":           len(assembled.scene_packets),
        "knowledge_total":   sum(len(p.knowledge) for p in assembled.scene_packets),
        "source_files":      len(assembled.all_source_files),
    })

    # ── Step 3: Weave ─────────────────────────────────────────
    pov_override = item.get("pov_override")
    pov_notes    = item.get("pov_notes")
    try:
        woven: WovenChapter = weave_chapter(
            assembled      = assembled,
            render_profile = render_profile,
            pov_override   = pov_override,
            pov_notes      = pov_notes,
            log            = log,
        )
    except Exception as exc:
        log.pipeline_error("chapter_weaver failed", exc)
        raise

    log.info("Step 3 complete — prose woven", {
        "word_count":       woven.word_count,
        "beats":            len(woven.beats),
        "continuity_flags": len(woven.continuity_flags),
        "missing_knowledge": len(woven.missing_knowledge),
    })

    # ── Step 4: Export ────────────────────────────────────────
    try:
        artifact = export_artifact(
            chapter        = woven,
            render_profile = render_profile,
            log            = log,
        )
    except Exception as exc:
        log.pipeline_error("artifact_exporter failed", exc)
        raise

    log.info("Step 4 complete — artifact exported", {"format": artifact.format})

    # ── Version save ──────────────────────────────────────────
    log.set_stage(PipelineStage.VERSION)
    record = save_version(
        chapter_id        = chapter_id,
        content           = artifact.content,
        queue_item_id     = job_id,
        render_profile_id = profile_id,
        pov               = woven.pov,
        fmt               = artifact.format,
        source_files      = assembled.all_source_files,
        word_count        = woven.word_count,
        beat_count        = len(woven.beats),
        log               = log,
        pass_type         = item.get("pass_type", "raw_draft"),
        note              = item.get("note", ""),
        meta = {
            "chapter_id":       chapter_id,
            "queue_item_id":    job_id,
            "render_profile_id": profile_id,
            "outline": {
                "emotional_arc_summary": outline.emotional_arc_summary,
                "pacing_notes":          outline.pacing_notes,
                "continuity_anchors":    outline.continuity_anchors,
                "continuity_setup":      outline.continuity_setup,
            },
            "beats": [
                {
                    "scene_id":           b.scene_id,
                    "beat_summary":       b.beat_summary,
                    "word_count":         b.word_count,
                    "valence":            b.valence,
                    "tension":            b.tension,
                    "emotional_start":    b.emotional_start,
                    "emotional_end":      b.emotional_end,
                    "characters_present": b.characters_present,
                    "location":           b.location,
                    "sensory_palette":    b.sensory_palette,
                    "dialogue": [
                        {
                            "speaker":    d.speaker,
                            "line":       d.line,
                            "emotion":    d.emotion,
                            "action":     d.action,
                            "subtext":    d.subtext,
                            "ssml_hints": d.ssml_hints,
                        }
                        for d in b.dialogue
                    ],
                }
                for b in woven.beats
            ],
            "continuity_flags":  woven.continuity_flags,
            "missing_knowledge": woven.missing_knowledge,
            "source_files":      assembled.all_source_files,
            "artifact_metadata": artifact.metadata,
        },
    )

    duration = time.monotonic() - t0
    log.pipeline_complete(record.file_path, record.version_num, duration)

    return record.file_path
