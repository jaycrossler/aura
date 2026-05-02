"""
Chapter Weaver — Pipeline Step 3.

Takes the chapter outline (Step 1) and assembled scene packets (Step 2) and
calls the LLM to write the full prose chapter.

Returns WovenChapter which contains:
  - chapter_markdown: the actual prose
  - beats[]: rich metadata per scene beat including:
      - dialogue with speaker, line, emotion, action, subtext, ssml_hints
      - sensory palette (sight/sound/smell/touch/taste)
      - emotional arc (valence, tension, start/end states)
      - characters present, location
  - continuity_flags: things the LLM flagged as continuity risks
  - missing_knowledge: knowledge docs it wished it had

The beat metadata is the key downstream asset — it feeds:
  - artifact_exporter.py (audiobook SSML, graphic novel panels, animation)
  - version_manager.py (meta.json)
  - status_reporter.py (beat coverage, dialogue density)
  - External tools like ElevenReader for voice casting
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from tools.storyops.scene_assembler import AssembledChapter, ScenePacket
from tools.storyops.common.llm import generate_text, parse_json_payload
from tools.storyops.common.story_logger import StoryLogger, PipelineStage


# ── Data models ───────────────────────────────────────────────────────────────

@dataclass
class DialogueLine:
    speaker:    str    # character id, e.g. "jace", "mei"
    line:       str    # exact spoken text (quotation marks not included)
    emotion:    str    # speaker's emotional state
    action:     str    # stage direction / physical action
    subtext:    str    # what they really mean / aren't saying
    ssml_hints: str    # "pace=slow pitch=low pause_before=long" etc.


@dataclass
class BeatMetadata:
    scene_id:           str
    beat_summary:       str
    word_count:         int
    valence:            float     # -1.0 … +1.0
    tension:            float     # 0.0 … 1.0
    emotional_start:    str
    emotional_end:      str
    characters_present: list[str]
    location:           str
    dialogue:           list[DialogueLine]
    sensory_palette:    dict[str, str]   # sight, sound, smell, touch, taste


@dataclass
class WovenChapter:
    chapter_id:         str
    chapter_markdown:   str
    voice_style:        str
    pov:                str
    word_count:         int
    beats:              list[BeatMetadata]
    continuity_flags:   list[str]    # LLM-raised continuity risks
    missing_knowledge:  list[str]    # knowledge docs LLM wished it had


# ── Helpers ───────────────────────────────────────────────────────────────────

def _scene_packets_payload(packets: list[ScenePacket]) -> list[dict]:
    """Serialize scene packets for the LLM prompt (capped for context budget)."""
    result = []
    for p in packets:
        result.append({
            "scene_id": p.scene_id,
            "registry": {
                "title":           p.registry_entry.get("title", ""),
                "pov":             p.registry_entry.get("pov", ""),
                "timeline_anchor": p.registry_entry.get("timeline_anchor", ""),
                "tags":            p.registry_entry.get("tags", []),
                "characters":      p.registry_entry.get("characters", []),
                "location":        p.registry_entry.get("location", ""),
                "notes":           p.registry_entry.get("notes", "")[:400],
            },
            "source_notes": p.source_notes[:3000],
            "beat": {
                "summary":            p.beat.beat_summary,
                "emotional_start":    p.beat.emotional_start,
                "emotional_end":      p.beat.emotional_end,
                "valence":            p.beat.valence,
                "tension":            p.beat.tension,
                "pov_notes":          p.beat.pov_notes,
                "key_dialogue_hooks": p.beat.key_dialogue_hooks,
            },
            "knowledge": [
                {
                    "category": k.category,
                    "title":    k.title,
                    "content":  k.content[:600],
                }
                for k in p.knowledge[:8]  # cap per-scene to keep prompt bounded
            ],
        })
    return result


# ── Main function ─────────────────────────────────────────────────────────────

def weave_chapter(
    assembled:    AssembledChapter,
    render_profile: dict[str, Any],
    pov_override: str | None,
    pov_notes:    str | None,
    log:          StoryLogger,
) -> WovenChapter:
    """
    Call the LLM to write the full chapter prose and return rich beat metadata.

    Args:
        assembled:       AssembledChapter from assemble_chapter()
        render_profile:  Active render profile dict
        pov_override:    If set, override the chapter's default POV character
        pov_notes:       Guidance for the alternate POV (when pov_override is set)
        log:             Job-scoped StoryLogger
    """
    log.set_stage(PipelineStage.WEAVE)

    outline         = assembled.outline
    pov             = pov_override or outline.pov
    format_type     = render_profile.get("format", "prose")
    content_filter  = render_profile.get("content_filter", "standard")
    tone_variant    = render_profile.get("tone_variant", "standard")

    log.info(f"Weaving chapter '{outline.chapter_id}'", {
        "pov":              pov,
        "pov_overridden":   bool(pov_override),
        "format":           format_type,
        "tone_variant":     tone_variant,
        "content_filter":   content_filter,
        "word_count_target": outline.word_count_target,
        "scene_count":      len(assembled.scene_packets),
    })

    # ── System prompt ─────────────────────────────────────────
    system = (
        "You are an acclaimed science fiction author writing a chapter of a novel. "
        "Your prose is precise, emotionally intelligent, and scientifically grounded. "
        "You write from deep inside a single POV character's sensory and emotional experience — "
        "the reader lives in this character's body and mind. "
        "You do not explain; you show. You do not summarize; you render. "
        f"Tone variant: {tone_variant}. "
        f"Content filter: {content_filter}. "
        "Return ONLY strict JSON matching the requested schema. No preamble. No markdown fences."
    )

    # ── User prompt ───────────────────────────────────────────
    user_payload: dict[str, Any] = {
        "task": (
            "Write the full chapter prose as chapter_markdown. "
            "Also return rich beat metadata for each scene beat — "
            "this metadata will be used for audiobook performance, "
            "graphic novel adaptation, and animation storyboarding."
        ),
        "chapter": {
            "id":                    outline.chapter_id,
            "title":                 outline.chapter_title,
            "pov":                   pov,
            "pov_override_notes":    pov_notes or "",
            "emotional_arc_summary": outline.emotional_arc_summary,
            "opening_image":         outline.opening_image,
            "closing_image":         outline.closing_image,
            "pacing_notes":          outline.pacing_notes,
            "word_count_target":     outline.word_count_target,
            "continuity_anchors":    outline.continuity_anchors,
            "continuity_setup":      outline.continuity_setup,
        },
        "render_profile": {
            "voice_style":    render_profile.get("voice_style"),
            "tone_variant":   tone_variant,
            "focus":          render_profile.get("focus"),
            "format":         format_type,
            "content_filter": content_filter,
            "voice_cast_notes": render_profile.get("voice_cast_notes", {}),
        },
        "master_synopsis_excerpt": assembled.synopsis_snippet,
        "scene_packets": _scene_packets_payload(assembled.scene_packets),
        "return_schema": {
            "chapter_markdown": (
                "Full chapter prose as a markdown string. Use ## for scene break headings "
                "only if the chapter has a clear structural break. Otherwise continuous prose."
            ),
            "voice_style":        "The voice style you actually used (may refine from the profile)",
            "word_count":         "integer — approximate word count of chapter_markdown",
            "continuity_flags":   [
                "List any continuity risks you noticed — unresolved references, "
                "timeline inconsistencies, character knowledge that shouldn't exist yet, etc."
            ],
            "missing_knowledge":  [
                "List knowledge files that would have improved this chapter if they existed "
                "(e.g. 'character voiceprint for mei', 'sensory palette for mars_long_burn_bar')"
            ],
            "beats": [
                {
                    "scene_id":           "string — must match a scene_id from scene_packets",
                    "beat_summary":       "string — 1-sentence summary of what happened in the prose",
                    "word_count":         "integer — word count of this beat's prose",
                    "valence":            "float -1.0 to 1.0",
                    "tension":            "float 0.0 to 1.0",
                    "emotional_start":    "string",
                    "emotional_end":      "string",
                    "characters_present": ["list of character ids present in this beat"],
                    "location":           "string — location id or descriptive name",
                    "sensory_palette": {
                        "sight":  "string — dominant visual",
                        "sound":  "string — dominant sound",
                        "smell":  "string — dominant smell (or 'none registered')",
                        "touch":  "string — dominant tactile",
                        "taste":  "string (or null)",
                    },
                    "dialogue": [
                        {
                            "speaker":    "character id",
                            "line":       "exact spoken text (no quotation marks)",
                            "emotion":    "emotional state of speaker",
                            "action":     "physical stage direction",
                            "subtext":    "what speaker really means / is not saying",
                            "ssml_hints": (
                                "space-separated hints: pace=slow|normal|fast "
                                "pitch=low|normal|high pause_before=none|short|long"
                            ),
                        }
                    ],
                }
            ],
        },
    }

    user_prompt = json.dumps(user_payload, default=str)
    log.llm_call(PipelineStage.WEAVE, "configured-model", len(user_prompt), len(system))

    response = generate_text(system, user_prompt)
    log.llm_response(response.provider, response.model, len(response.content), [])

    payload   = parse_json_payload(response.content)
    raw_beats = payload.get("beats", [])

    log.info("Prose received", {
        "word_count":        payload.get("word_count", 0),
        "beats":             len(raw_beats),
        "continuity_flags":  len(payload.get("continuity_flags", [])),
        "missing_knowledge": len(payload.get("missing_knowledge", [])),
    })

    for flag in payload.get("continuity_flags", []):
        log.continuity_flag(flag)

    if payload.get("missing_knowledge"):
        log.missing_knowledge(payload["missing_knowledge"])

    # ── Parse beats ───────────────────────────────────────────
    beats: list[BeatMetadata] = []
    for b in raw_beats:
        dialogue: list[DialogueLine] = []
        for d in b.get("dialogue", []):
            dialogue.append(DialogueLine(
                speaker    = d.get("speaker", "unknown"),
                line       = d.get("line", ""),
                emotion    = d.get("emotion", ""),
                action     = d.get("action", ""),
                subtext    = d.get("subtext", ""),
                ssml_hints = d.get("ssml_hints", "pace=normal pitch=normal pause_before=none"),
            ))

        beats.append(BeatMetadata(
            scene_id           = b.get("scene_id", ""),
            beat_summary       = b.get("beat_summary", ""),
            word_count         = int(b.get("word_count", 0)),
            valence            = float(b.get("valence", 0.0)),
            tension            = float(b.get("tension", 0.5)),
            emotional_start    = b.get("emotional_start", ""),
            emotional_end      = b.get("emotional_end", ""),
            characters_present = b.get("characters_present", []),
            location           = b.get("location", ""),
            dialogue           = dialogue,
            sensory_palette    = b.get("sensory_palette", {}),
        ))

    return WovenChapter(
        chapter_id        = outline.chapter_id,
        chapter_markdown  = payload.get("chapter_markdown", "# Chapter\n\n[No content returned.]"),
        voice_style       = payload.get("voice_style", render_profile.get("voice_style", "")),
        pov               = pov,
        word_count        = int(payload.get("word_count", 0)),
        beats             = beats,
        continuity_flags  = payload.get("continuity_flags", []),
        missing_knowledge = payload.get("missing_knowledge", []),
    )
