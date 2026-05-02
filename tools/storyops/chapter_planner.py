"""
Chapter Planner — Pipeline Step 1.

Takes a chapter definition from story-structure.yaml and generates a detailed
beat-by-beat outline: emotional arc, opening/closing images, pacing notes,
continuity anchors, and per-scene beat cards.

This is a pure planning step — no prose yet. The output drives Step 2 (assembly)
and Step 3 (weaving), and is stored in the chapter .meta.json for inspection.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from tools.storyops.common.llm import generate_text, parse_json_payload
from tools.storyops.common.story_logger import StoryLogger, PipelineStage


# ── Data model ───────────────────────────────────────────────────────────────

@dataclass
class BeatPlan:
    scene_id:            str
    beat_summary:        str
    emotional_start:     str       # e.g. "excited, certain"
    emotional_end:       str       # e.g. "shaken, numb"
    valence:             float     # -1.0 (dread/grief) … +1.0 (joy/wonder)
    tension:             float     # 0.0 … 1.0
    pov_notes:           str
    key_dialogue_hooks:  list[str]


@dataclass
class ChapterOutline:
    chapter_id:           str
    chapter_title:        str
    pov:                  str
    emotional_arc_summary: str
    opening_image:        str      # first literal sensory moment
    closing_image:        str      # last literal sensory moment
    beats:                list[BeatPlan]
    pacing_notes:         str
    continuity_anchors:   list[str]   # from prior chapters — reference these
    continuity_setup:     list[str]   # set up here for future payoff
    word_count_target:    int


# ── Main function ─────────────────────────────────────────────────────────────

def plan_chapter(
    chapter_def: dict[str, Any],
    scene_registry: dict[str, Any],
    render_profile: dict[str, Any],
    log: StoryLogger,
    prior_chapter_summary: str = "",
) -> ChapterOutline:
    """
    Call the LLM to produce a beat-by-beat chapter outline.

    Args:
        chapter_def:           Chapter entry from story-structure.yaml
        scene_registry:        Full scene registry dict keyed by scene_id
        render_profile:        Active render profile dict
        log:                   Job-scoped StoryLogger
        prior_chapter_summary: Excerpt of previous chapter for continuity context
    """
    log.set_stage(PipelineStage.PLAN)

    chapter_id = chapter_def["id"]
    scene_ids  = chapter_def.get("scenes", [])

    # Gather scene metadata from registry
    scenes_for_chapter: list[dict] = []
    for sid in scene_ids:
        entry = scene_registry.get(sid)
        if entry:
            scenes_for_chapter.append({
                "id":               sid,
                "title":            entry.get("title", ""),
                "pov":              entry.get("pov", ""),
                "timeline_anchor":  entry.get("timeline_anchor", ""),
                "arc":              entry.get("arc", ""),
                "tags":             entry.get("tags", []),
                "notes":            entry.get("notes", ""),
                "status":           entry.get("status", "unknown"),
            })
            log.info(f"Scene '{sid}' loaded for planning", {"status": entry.get("status")})
        else:
            log.warn(f"Scene '{sid}' not found in registry — chapter outline may be incomplete")

    log.info(f"Planning chapter '{chapter_id}'", {
        "scene_count": len(scenes_for_chapter),
        "pov_default": chapter_def.get("pov_default"),
        "render_profile": render_profile.get("id"),
        "tone_variant": render_profile.get("tone_variant"),
    })

    # ── System prompt ─────────────────────────────────────────
    system = (
        "You are a meticulous novel editor and chapter planner. "
        "Your task is to produce a precise beat-by-beat chapter outline. "
        "You think in emotional arcs, pacing rhythm, sensory imagery, and narrative function. "
        "Every beat should have a clear emotional start and end state, a tension level, "
        "and specific dialogue hooks to guide the prose writer. "
        "The opening and closing images should be vivid, concrete, and sensory — not abstract. "
        "Return ONLY strict JSON matching the schema provided. No preamble. No markdown fences."
    )

    # ── User prompt ───────────────────────────────────────────
    user_payload = {
        "task": "Generate a detailed chapter outline with emotional arc and beat cards.",
        "chapter": {
            "id":               chapter_id,
            "title":            chapter_def.get("title"),
            "subtitle":         chapter_def.get("subtitle"),
            "pov_default":      chapter_def.get("pov_default"),
            "timeline_span":    chapter_def.get("timeline_span"),
            "arc":              chapter_def.get("arc"),
            "tone_notes":       chapter_def.get("tone_notes"),
            "pacing":           chapter_def.get("pacing"),
            "target_word_count": chapter_def.get("target_word_count", 2500),
            "pov_exceptions":   chapter_def.get("pov_exceptions", []),
        },
        "render_profile": {
            "id":            render_profile.get("id"),
            "voice_style":   render_profile.get("voice_style"),
            "tone_variant":  render_profile.get("tone_variant"),
            "focus":         render_profile.get("focus"),
            "format":        render_profile.get("format"),
            "content_filter": render_profile.get("content_filter"),
        },
        "scenes": scenes_for_chapter,
        "prior_chapter_summary": prior_chapter_summary[:1500] if prior_chapter_summary else "",
        "return_schema": {
            "chapter_title":          "string",
            "pov":                    "string (character id, e.g. 'jace')",
            "emotional_arc_summary":  "string — one paragraph describing the emotional shape of the chapter",
            "opening_image":          "string — the literal first sensory moment (specific, concrete)",
            "closing_image":          "string — the literal last sensory moment (specific, concrete)",
            "pacing_notes":           "string — guidance for the prose writer on rhythm and compression",
            "word_count_target":      "integer",
            "continuity_anchors":     ["list of specific things from prior chapters to reference"],
            "continuity_setup":       ["list of specific things set up here for future payoff"],
            "beats": [
                {
                    "scene_id":           "string — must match a scene id from the scenes list",
                    "beat_summary":       "string — 1-2 sentence description of what happens",
                    "emotional_start":    "string — character's emotional state entering the beat",
                    "emotional_end":      "string — character's emotional state leaving the beat",
                    "valence":            "float -1.0 to 1.0 (dread=-1, neutral=0, joy=1)",
                    "tension":            "float 0.0 to 1.0",
                    "pov_notes":          "string — specific POV guidance for this beat",
                    "key_dialogue_hooks": ["list of suggested dialogue threads or lines to include"],
                }
            ],
        },
    }

    user_prompt = json.dumps(user_payload, default=str)
    log.llm_call(PipelineStage.PLAN, "configured-model", len(user_prompt), len(system))

    response = generate_text(system, user_prompt)
    log.llm_response(response.provider, response.model, len(response.content), [])

    payload = parse_json_payload(response.content)
    raw_beats = payload.get("beats", [])

    log.info("Chapter outline received", {
        "beats":             len(raw_beats),
        "word_count_target": payload.get("word_count_target"),
        "continuity_anchors": len(payload.get("continuity_anchors", [])),
        "continuity_setup":  len(payload.get("continuity_setup", [])),
        "opening_image":     (payload.get("opening_image", "")[:80] + "…"),
    })

    # ── Parse beats ───────────────────────────────────────────
    beats: list[BeatPlan] = []
    for b in raw_beats:
        beats.append(BeatPlan(
            scene_id           = b.get("scene_id", ""),
            beat_summary       = b.get("beat_summary", ""),
            emotional_start    = b.get("emotional_start", ""),
            emotional_end      = b.get("emotional_end", ""),
            valence            = float(b.get("valence", 0.0)),
            tension            = float(b.get("tension", 0.5)),
            pov_notes          = b.get("pov_notes", ""),
            key_dialogue_hooks = b.get("key_dialogue_hooks", []),
        ))

    return ChapterOutline(
        chapter_id            = chapter_id,
        chapter_title         = payload.get("chapter_title", chapter_def.get("title", "")),
        pov                   = payload.get("pov", chapter_def.get("pov_default", "jace")),
        emotional_arc_summary = payload.get("emotional_arc_summary", ""),
        opening_image         = payload.get("opening_image", ""),
        closing_image         = payload.get("closing_image", ""),
        beats                 = beats,
        pacing_notes          = payload.get("pacing_notes", ""),
        continuity_anchors    = payload.get("continuity_anchors", []),
        continuity_setup      = payload.get("continuity_setup", []),
        word_count_target     = int(payload.get("word_count_target",
                                               chapter_def.get("target_word_count", 2500))),
    )
