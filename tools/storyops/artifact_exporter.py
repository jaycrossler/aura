"""
Artifact Exporter — Pipeline Step 4.

Takes a WovenChapter and a render profile and produces a format-specific artifact.

Formats:
  prose            — clean markdown, no extra LLM call
  audiobook        — annotated script with SSML hints, speaker cast, performance notes
  graphic_novel    — panel-by-panel script with visual descriptions and balloon text
  animation_storyboard — shot-by-shot storyboard with camera, blocking, music cues

Each non-prose format makes one additional LLM call using the existing beat metadata
as structured input, so the LLM is translating/adapting rather than generating from
scratch. This keeps the variants consistent with the prose.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from tools.storyops.chapter_weaver import WovenChapter, BeatMetadata
from tools.storyops.common.llm import generate_text, parse_json_payload
from tools.storyops.common.story_logger import StoryLogger, PipelineStage


FORMAT_PROSE         = "prose"
FORMAT_AUDIOBOOK     = "audiobook"
FORMAT_GRAPHIC_NOVEL = "graphic_novel"
FORMAT_ANIMATION     = "animation_storyboard"


@dataclass
class ExportedArtifact:
    format:   str
    content:  str
    metadata: dict[str, Any]


# ── prose ─────────────────────────────────────────────────────────────────────

def _prose_export(chapter: WovenChapter) -> ExportedArtifact:
    """Prose needs no additional LLM call — the woven markdown IS the artifact."""
    return ExportedArtifact(
        format   = FORMAT_PROSE,
        content  = chapter.chapter_markdown,
        metadata = {
            "word_count":  chapter.word_count,
            "pov":         chapter.pov,
            "voice_style": chapter.voice_style,
        },
    )


# ── audiobook ─────────────────────────────────────────────────────────────────

def _audiobook_export(
    chapter: WovenChapter,
    render_profile: dict[str, Any],
    log: StoryLogger,
) -> ExportedArtifact:
    """
    Annotate the prose for audio performance.
    Uses dialogue metadata from beats so the LLM has structured speaker/emotion data.
    Output: annotated script with [NARRATOR], [CHARACTER: name], [PAUSE], [TONE] tags.
    """
    log.set_stage(PipelineStage.EXPORT)
    log.info("Exporting audiobook format", {"chapter_id": chapter.chapter_id})

    voice_cast_notes = render_profile.get("voice_cast_notes", {})

    # Flatten dialogue for the prompt
    all_dialogue = []
    for beat in chapter.beats:
        for d in beat.dialogue:
            all_dialogue.append({
                "speaker":    d.speaker,
                "line":       d.line,
                "emotion":    d.emotion,
                "action":     d.action,
                "ssml_hints": d.ssml_hints,
            })

    system = (
        "You are a professional audiobook director annotating a novel chapter for recording. "
        "Insert performance markup into the prose. "
        "Tags to use (inline, on their own line or within text): "
        "[NARRATOR] — narrator voice, "
        "[CHARACTER: name] — switch to character voice, "
        "[PAUSE: short|long] — explicit pause, "
        "[PACE: slow|normal|fast] — pacing instruction, "
        "[VOLUME: quiet|normal|loud] — volume, "
        "[TONE: tense|warm|cold|grief|wonder|flat] — emotional tone shift. "
        "Return ONLY strict JSON: "
        "{annotated_script: string, speaker_cast: [{character, voice_direction, sample_line}], "
        "total_estimated_runtime_minutes: float}"
    )

    user_payload = {
        "prose":               chapter.chapter_markdown[:8000],
        "voice_cast_notes":    voice_cast_notes,
        "dialogue_metadata":   all_dialogue,
        "emotional_arc": [
            {
                "scene_id":       b.scene_id,
                "valence":        b.valence,
                "tension":        b.tension,
                "emotional_start": b.emotional_start,
                "emotional_end":  b.emotional_end,
            }
            for b in chapter.beats
        ],
    }

    user_prompt = json.dumps(user_payload, default=str)
    log.llm_call(PipelineStage.EXPORT, "configured-model", len(user_prompt), len(system))
    response = generate_text(system, user_prompt)
    log.llm_response(response.provider, response.model, len(response.content), [])

    payload = parse_json_payload(response.content)
    log.info("Audiobook annotation complete", {
        "speakers":                 len(payload.get("speaker_cast", [])),
        "runtime_est_min":          payload.get("total_estimated_runtime_minutes"),
    })

    return ExportedArtifact(
        format   = FORMAT_AUDIOBOOK,
        content  = payload.get("annotated_script", chapter.chapter_markdown),
        metadata = {
            "speaker_cast":                    payload.get("speaker_cast", []),
            "total_estimated_runtime_minutes": payload.get("total_estimated_runtime_minutes"),
            "dialogue_count":                  len(all_dialogue),
            "word_count":                      chapter.word_count,
        },
    )


# ── graphic novel ─────────────────────────────────────────────────────────────

def _graphic_novel_export(
    chapter: WovenChapter,
    log: StoryLogger,
) -> ExportedArtifact:
    """
    Convert the chapter into a panel-by-panel graphic novel script.
    Each beat maps to one or more pages; each page has panels with visual
    descriptions, camera angles, dialogue balloons, and caption boxes.
    """
    log.set_stage(PipelineStage.EXPORT)
    log.info("Exporting graphic novel format", {"chapter_id": chapter.chapter_id})

    system = (
        "You are a graphic novel scriptwriter adapting a prose chapter. "
        "Convert the prose and beat metadata into a page-by-page, panel-by-panel script. "
        "Each panel needs: visual_description (what the artist draws), "
        "camera_angle (wide/medium/close/extreme_close/bird's_eye/worm's_eye), "
        "lighting (describe quality and direction), characters_visible, "
        "dialogue_balloons [{speaker, text, balloon_type: speech|thought|caption}], "
        "and caption_box (optional narrator text). "
        "Use splash pages and double-page spreads for major emotional moments. "
        "The corridor walk after the diagnosis: nine panels, no dialogue, no captions. "
        "Return ONLY strict JSON: "
        "{pages: [{page_num, layout: single|splash|double_spread, panels: [{...}]}], "
        "total_pages: int, total_panels: int}"
    )

    user_payload = {
        "prose": chapter.chapter_markdown[:6000],
        "beats": [
            {
                "scene_id":           b.scene_id,
                "beat_summary":       b.beat_summary,
                "location":           b.location,
                "sensory_palette":    b.sensory_palette,
                "characters_present": b.characters_present,
                "valence":            b.valence,
                "tension":            b.tension,
                "dialogue": [
                    {"speaker": d.speaker, "line": d.line, "emotion": d.emotion}
                    for d in b.dialogue
                ],
            }
            for b in chapter.beats
        ],
    }

    user_prompt = json.dumps(user_payload, default=str)
    log.llm_call(PipelineStage.EXPORT, "configured-model", len(user_prompt), len(system))
    response = generate_text(system, user_prompt)
    log.llm_response(response.provider, response.model, len(response.content), [])

    payload = parse_json_payload(response.content)
    pages   = payload.get("pages", [])
    log.info("Graphic novel script complete", {
        "total_pages":  payload.get("total_pages", len(pages)),
        "total_panels": payload.get("total_panels"),
    })

    # Render as readable script text
    script_lines = [
        f"# GRAPHIC NOVEL SCRIPT: {chapter.chapter_id.upper()}\n",
        f"# POV: {chapter.pov}  |  Panels: {payload.get('total_panels', '?')}"
        f"  |  Pages: {payload.get('total_pages', len(pages))}\n\n",
    ]
    for page in pages:
        layout = page.get("layout", "single")
        script_lines.append(f"{'='*60}\n")
        script_lines.append(f"PAGE {page.get('page_num', '?')}  [{layout.upper()}]\n")
        script_lines.append(f"{'='*60}\n\n")
        for panel in page.get("panels", []):
            script_lines.append(f"  PANEL {panel.get('panel_num', '?')}\n")
            script_lines.append(f"  ANGLE: {panel.get('camera_angle', '')}\n")
            script_lines.append(f"  LIGHT: {panel.get('lighting', '')}\n")
            script_lines.append(f"  VISUAL: {panel.get('visual_description', '')}\n")
            for balloon in panel.get("dialogue_balloons", []):
                btype = balloon.get("balloon_type", "speech").upper()
                script_lines.append(f"  [{btype} — {balloon.get('speaker', '')}]: "
                                    f'"{balloon.get("text", "")}"\n')
            if panel.get("caption_box"):
                script_lines.append(f"  CAPTION: {panel['caption_box']}\n")
            script_lines.append("\n")

    return ExportedArtifact(
        format   = FORMAT_GRAPHIC_NOVEL,
        content  = "".join(script_lines),
        metadata = {
            "total_pages":  payload.get("total_pages", len(pages)),
            "total_panels": payload.get("total_panels", 0),
        },
    )


# ── animation storyboard ──────────────────────────────────────────────────────

def _animation_export(
    chapter: WovenChapter,
    log: StoryLogger,
) -> ExportedArtifact:
    """
    Produce shot-by-shot animation storyboard notes with camera directions,
    character blocking, suggested visual metaphors, and music cue suggestions.
    """
    log.set_stage(PipelineStage.EXPORT)
    log.info("Exporting animation storyboard format", {"chapter_id": chapter.chapter_id})

    system = (
        "You are an animation director storyboarding a chapter from a hard sci-fi novel. "
        "Produce shot-by-shot notes. For each shot: "
        "shot_type (establishing/medium/close_up/insert/reaction/aerial), "
        "camera_movement (static/pan/tilt/dolly_in/dolly_out/handheld/crane), "
        "character_blocking (describe body positions and movement), "
        "visual_metaphor (optional — how does the visual composition mirror theme), "
        "music_cue (describe mood/instrumentation, not a specific song), "
        "duration_seconds (estimated). "
        "Return ONLY strict JSON: "
        "{sequences: [{scene_id, shots: [{shot_num, shot_type, camera_movement, "
        "character_blocking, visual_metaphor, music_cue, duration_seconds, "
        "dialogue_overlay: string|null}]}], "
        "total_runtime_seconds: int}"
    )

    user_payload = {
        "prose": chapter.chapter_markdown[:5000],
        "beats": [
            {
                "scene_id":           b.scene_id,
                "location":           b.location,
                "sensory_palette":    b.sensory_palette,
                "characters_present": b.characters_present,
                "valence":            b.valence,
                "tension":            b.tension,
                "emotional_start":    b.emotional_start,
                "emotional_end":      b.emotional_end,
            }
            for b in chapter.beats
        ],
    }

    user_prompt = json.dumps(user_payload, default=str)
    log.llm_call(PipelineStage.EXPORT, "configured-model", len(user_prompt), len(system))
    response = generate_text(system, user_prompt)
    log.llm_response(response.provider, response.model, len(response.content), [])

    payload    = parse_json_payload(response.content)
    sequences  = payload.get("sequences", [])
    total_secs = payload.get("total_runtime_seconds", 0)
    log.info("Animation storyboard complete", {
        "sequences":              len(sequences),
        "total_runtime_seconds":  total_secs,
        "total_shots":            sum(len(s.get("shots", [])) for s in sequences),
    })

    # Render as readable notes
    notes = [
        f"# ANIMATION STORYBOARD: {chapter.chapter_id.upper()}\n",
        f"# Estimated runtime: {total_secs // 60}m {total_secs % 60}s\n\n",
    ]
    for seq in sequences:
        notes.append(f"SEQUENCE: {seq.get('scene_id', '?')}\n{'─'*40}\n")
        for shot in seq.get("shots", []):
            notes.append(f"  SHOT {shot.get('shot_num', '?')}"
                         f"  [{shot.get('shot_type', '')} / {shot.get('camera_movement', '')}]"
                         f"  ~{shot.get('duration_seconds', '?')}s\n")
            notes.append(f"  BLOCKING: {shot.get('character_blocking', '')}\n")
            if shot.get("visual_metaphor"):
                notes.append(f"  METAPHOR: {shot['visual_metaphor']}\n")
            notes.append(f"  MUSIC: {shot.get('music_cue', '')}\n")
            if shot.get("dialogue_overlay"):
                notes.append(f"  VO/DIALOGUE: {shot['dialogue_overlay']}\n")
            notes.append("\n")

    return ExportedArtifact(
        format   = FORMAT_ANIMATION,
        content  = "".join(notes),
        metadata = {
            "total_runtime_seconds": total_secs,
            "total_shots":           sum(len(s.get("shots", [])) for s in sequences),
        },
    )


# ── Dispatch ──────────────────────────────────────────────────────────────────

def export_artifact(
    chapter:        WovenChapter,
    render_profile: dict[str, Any],
    log:            StoryLogger,
) -> ExportedArtifact:
    """Route to the correct exporter based on render_profile.format."""
    fmt = render_profile.get("format", FORMAT_PROSE)

    if fmt == FORMAT_PROSE:
        return _prose_export(chapter)
    elif fmt == FORMAT_AUDIOBOOK:
        return _audiobook_export(chapter, render_profile, log)
    elif fmt == FORMAT_GRAPHIC_NOVEL:
        return _graphic_novel_export(chapter, log)
    elif fmt == FORMAT_ANIMATION:
        return _animation_export(chapter, log)
    else:
        log.warn(f"Unknown format '{fmt}' — falling back to prose")
        return _prose_export(chapter)
