from __future__ import annotations

import json
import datetime as dt
from pathlib import Path
from typing import Any

import frontmatter

from tools.storyops.common.git_utils import utc_now
from tools.storyops.common.llm import generate_text, parse_json_payload


VOICE_GUIDE = "Grounded hard-sci-fi voice with restrained lyricism, emotionally precise beats, and continuity-safe references only."
GENERATOR_LOG = Path("generated/logs/story-generator.log")


def _log(message: str) -> None:
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    line = f"[{stamp}] [story-generator] {message}"
    print(line)
    GENERATOR_LOG.parent.mkdir(parents=True, exist_ok=True)
    with GENERATOR_LOG.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def _load_markdown(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        post = frontmatter.loads(raw)
        return {"path": str(path), "meta": dict(post.metadata), "content": post.content}
    except Exception:
        return {"path": str(path), "meta": {}, "content": raw}


def _scene_sort_key(scene: dict[str, Any]) -> tuple[str, str]:
    meta = scene["meta"]
    return (str(meta.get("last_updated", "9999-12-31")), scene["path"])


def _relevant_paths_for_scene(scene_text: str) -> list[Path]:
    roots = [Path("knowledge/characters"), Path("knowledge/locations"), Path("knowledge/technology"), Path("knowledge/magic-systems")]
    corpus = scene_text.lower()
    selected: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            token = path.stem.replace("_", " ").lower()
            if any(part and part in corpus for part in token.split()):
                selected.append(path)
    return selected[:16]


def _mock_story(scene: dict[str, Any]) -> dict[str, Any]:
    title = scene["meta"].get("title", Path(scene["path"]).stem)
    chapter = f"# {title}\n\nJace watched the station lights tremble against the black and counted each breath before he spoke. The mission felt procedural on paper, but every sound on deck carried an edge now.\n\nMei met him at the hatch and kept her voice even. \"We stay on plan,\" she said, calm but urgent. Jace nodded, aware that calm had become a costume everyone wore to keep panic contained.\n\nBy shift-end, the crew moved with practiced rhythm again, though no one pretended the fear was gone."
    return {
        "chapter_markdown": chapter,
        "voice_style": VOICE_GUIDE,
        "beats": [
            {
                "scene_id": scene["meta"].get("id", scene["path"]),
                "summary": "Crew stabilizes after anxiety spike while preserving operational discipline.",
                "dialogue": [
                    {"speaker": "Mei", "line": "We stay on plan.", "emotion": "controlled urgency", "action": "blocks hatchway"},
                    {"speaker": "Jace", "line": "Copy.", "emotion": "contained fear", "action": "checks HUD status"},
                ],
            }
        ],
    }


def generate_chapter(item: dict[str, Any]) -> str | None:
    _log(f"Queue item '{item.get('id')}' starting.")
    out = Path(item["output_file"])
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and not item.get("overwrite", False):
        _log(f"Skipping '{item.get('id')}' because output exists and overwrite is false: {out}")
        return None

    scenes = [_load_markdown(path) for path in sorted(Path("knowledge/scenes").glob("*.md"))]
    scenes.sort(key=_scene_sort_key)
    max_scenes = int(item.get("max_scenes", 2))
    chosen = scenes[:max_scenes]
    if item.get("scene_ids"):
        requested = set(item["scene_ids"])
        chosen = [s for s in scenes if s["meta"].get("id") in requested]
    if not chosen:
        chosen = [{"path": "knowledge/scenes/<none>", "meta": {"id": "scene_missing"}, "content": "No scenes available."}]
    _log(f"Selected {len(chosen)} scene(s) for '{item.get('id')}'.")

    scene_packets = []
    source_files = {"knowledge/MASTER-SYNOPSIS.md"}
    for scene in chosen:
        relevant = _relevant_paths_for_scene(scene["content"])
        _log(
            "Scene packet built for "
            f"scene_id={scene['meta'].get('id', '<missing>')} "
            f"with {len(relevant)} relevant knowledge docs."
        )
        for r in relevant:
            source_files.add(str(r))
        source_files.add(scene["path"])
        scene_packets.append(
            {
                "scene": scene["meta"],
                "notes": scene["content"][:5000],
                "relevant_knowledge": [{"path": str(r), "snippet": _load_markdown(r)["content"][:600]} for r in relevant],
            }
        )

    system = "You are a meticulous novel coauthor. Return strict JSON with keys: chapter_markdown, voice_style, beats."
    user_prompt = json.dumps(
        {
            "chapter_title": item.get("chapter_title", "Generated Chapter Draft"),
            "voice_style": item.get("voice_style", VOICE_GUIDE),
            "requirements": [
                "Write one coherent chapter with clear emotional beats.",
                "Keep continuity with timeline order of provided scenes.",
                "Include concise but vivid dialogue.",
                "beats must include speaker, line, action, emotion metadata for downstream audio/video generation.",
            ],
            "scene_packets": scene_packets,
        },
        default=str,
    )

    llm_response = generate_text(system, user_prompt)
    _log(
        f"LLM response received provider={llm_response.provider} model={llm_response.model} "
        f"chars={len(llm_response.content)}"
    )
    payload = _mock_story(chosen[0]) if llm_response.provider == "mock" else parse_json_payload(llm_response.content)
    _log(
        "Payload parsed with keys="
        f"{sorted(payload.keys()) if isinstance(payload, dict) else '<not-dict>'}; "
        f"beats={len(payload.get('beats', [])) if isinstance(payload, dict) else 0}"
    )

    chapter_text = payload.get("chapter_markdown", "# Generated Chapter\n\n[No content returned]")
    frontmatter_lines = [
        "---",
        f"id: {item['id']}",
        "type: generated_chapter",
        "status: Draft_v_1",
        f"generated_at: '{utc_now()}'",
        "canon_status: generated",
        f"llm_provider: {llm_response.provider}",
        f"llm_model: {llm_response.model}",
        f"voice_style: \"{payload.get('voice_style', item.get('voice_style', VOICE_GUIDE))}\"",
        f"source_files: {sorted(source_files)}",
        "---\n",
    ]
    out.write_text("\n".join(frontmatter_lines) + chapter_text + "\n", encoding="utf-8")
    _log(f"Chapter markdown written to {out}.")

    meta_path = out.with_suffix(".meta.json")
    meta_path.write_text(
        json.dumps(
            {
                "chapter_id": item["id"],
                "chapter_file": str(out),
                "generated_at": utc_now(),
                "voice_style": payload.get("voice_style", VOICE_GUIDE),
                "beats": payload.get("beats", []),
                "scenes_used": [s["meta"].get("id") for s in chosen],
                "llm": {"provider": llm_response.provider, "model": llm_response.model},
                "missing_knowledge_suggestions": [
                    "Character voiceprint tokens (pitch, cadence, lexical style).",
                    "Location sensory palette (smells, ambient sounds, lighting).",
                    "Scene-level emotional target curve (start/mid/end valence-arousal).",
                    "Dialogue language/register preferences per faction.",
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    _log(f"Metadata written to {meta_path}. Source files used={len(source_files)}")
    return str(out)
