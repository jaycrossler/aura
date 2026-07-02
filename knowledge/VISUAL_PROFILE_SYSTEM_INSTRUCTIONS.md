---
last_updated: 2026-06-28
---

## FILES IN THIS SYSTEM

### Visual Profile Files (`visual_profiles/`)

One file per subject (character, location, ship, creature, faction).

**Naming:** `visual_profile_{subject_id}.md`

**Completeness rating:** Each file carries a `completeness: N` field (0–100).
- 0–30: Almost no data; do not attempt image generation
- 31–60: Partial; image generation on hold pending author input
- 61–80: Good; image generation can proceed with noted gaps
- 81–100: Fully specified; image generation unrestricted

**Status of current files:**

| File | Subject | Completeness | Status |
|---|---|---|---|
| `visual_profile_jace_apollo.md` | Jace Grant | 60% | Hold on eye color, HUD details |
| `visual_profile_kael.md` | Kael | 55% | Hold on skin, hair, armor color |
| `visual_profiles_sophia_jin_nick_cerberus.md` | Sophia/Jin/Nick/Cerberus | 25–45% | Most on hold |
| `visual_profiles_locations.md` | Fortuna Station / Falcon | 55–75% | Fortuna near-ready; Falcon needs work |

**To check:** Run `project_knowledge_search` for `visual_profile` to find all
current files and their completeness ratings.

### Scene Metadata Files (`scenes/metadata/`)

One sidecar file per scene, alongside the scene draft.

**Naming:** `{scene_id}_metadata.md` or `{scene_id}_metadata.yaml`

**Purpose:** Per-line dialogue attribution with emotional tone, character state,
and environment notes — for audiobook direction and video production.

See the **Scene Metadata Template** section below.

### The Completeness Tracker

`visual_profiles/_tracker.svg` — auto-regeneratable SVG showing completeness
across all visual profiles. Update when profiles are filled in.

Request regeneration with: *"Regenerate the completeness tracker SVG with these
updated completeness values: [list]"*

---

## HOW TO FILL IN VISUAL PROFILES

### The author input session workflow

1. Open `visual_profiles/_tracker.svg` — see which subjects are least complete
2. Open the relevant visual profile file
3. Read all `[AUTHOR INPUT NEEDED]` fields aloud or in chat
4. Answer them — even rough answers are better than none
5. The Claude session drafts the completed entries and updated image prompts
6. Commit the updated profile to the repo

### What counts as "good enough" for image generation

For a **portrait**, you need:
- Height and build (even approximate)
- Skin tone (can be very brief: "pale northern European" is enough)
- Hair (color and approximate length)
- Eye color
- One distinctive feature
- One sentence about default expression

For a **location establishing shot**, you need:
- Scale (approximate size)
- Construction era / style
- Three dominant colors
- Lighting character (warm/cold/mixed)
- One "what it doesn't look like" note

For a **creature concept**, you need:
- Size relative to a human
- Overall shape / silhouette
- Color (physical space and/or Astral)
- Movement quality
- Whether it's a physical-space or Astral image

---

## THE VISUAL PROFILE TEMPLATE

Use this template when creating a new visual profile from scratch:

```markdown
---
id: visual_profile_{subject_id}
name: "Visual Profile — {Subject Name}"
type: visual_profile
subject_id: {subject_id}
status: minimal | partial | good | complete
completeness: 0
last_updated: {date}
description: >
  One-sentence description of the subject for index.
cross_references:
  - {primary_kb_file}
images:
  - path: images/{directory}/{subject_id}__{type}.png
    type: portrait | concept | map | orb_ref | mood | scene_still | sigil
    section: null
    caption: "{Subject} — {context}"
    prompt_version: 1
    status: pending
    generated_at: null
    model: null
    model_version: null
---

# Visual Profile — {Subject Name}

> **Completeness: 0%** — New file. All fields require author input.

---

## Physical Appearance Anchors

| Attribute | Canonical value | Source | Confidence |
|---|---|---|---|
| [attribute] | [value or AUTHOR INPUT NEEDED] | [source file or —] | ✅ confirmed / ⚠️ partial / ❌ not found |

### What [Subject] Looks Like to a Stranger
[One paragraph from an outside observer's perspective. What registers first?]

### What [Subject] Doesn't Look Like
[Negative space — equally useful for image generation.]

---

## Appearance by Arc

| Arc | Clothing / Gear | Physical condition | Notable changes |
|---|---|---|---|
| Arc 1 | | | |

---

## Astral Appearance
*(For practitioners and creatures — skip for locations and ships)*

- **Color / Will signature:** [AUTHOR INPUT NEEDED]
- **Quality:** [AUTHOR INPUT NEEDED]
- **Size relative to others:** [AUTHOR INPUT NEEDED]

---

## Voice Profile
*(For characters — skip for locations, ships, creatures)*

| Attribute | Description | Source |
|---|---|---|
| Register | [AUTHOR INPUT NEEDED] | |
| Cadence | | |
| Signature phrases / tells | | |
| Emotional expression through voice | | |
| Specific dialogue modes | | |

### Audiobook Direction Notes
[What the director needs to know that isn't in the prose.]

---

## Image Generation Prompts

### {Primary image type}
```
Hard science fiction aesthetic, mid-22nd century {setting} setting, grounded
and realistic, NOT fantasy-stylized. Cinematic lighting. Photorealistic or
highly detailed illustration style. {TYPE-SPECIFIC GUIDANCE}.
{CONTENT FROM FILE}.
--negative fantasy art style, anime, cartoon, painterly brushwork, overly
saturated colors, medieval setting, dragons, swords
```
**Status:** HOLD / READY — [reason]

---

## Open Items for Author

- [ ] [item]
```

---

## SCENE METADATA TEMPLATE

For each scene, create a sidecar metadata file. This serves audiobook, video,
and continuity review simultaneously.

```yaml
# {scene_id}_metadata.yaml
# Sidecar metadata for scene file {scene_id}.md / {scene_id}_draft.md

scene_id: {scene_id}
scene_title: "{Human-readable scene title}"
arc: arc_0N_{slug}
thread: T | A | L | X | P | S
in_universe_date: approximate
duration_in_scene: approximate (e.g., "20 minutes", "3 hours")
last_updated: {date}

# ── ENVIRONMENT ──────────────────────────────────────────────────────────────

location:
  primary: location_{id}
  zone: "{Specific zone within location — The Barn / Habitation Corridor C / etc.}"
  lighting: warm-amber | cold-functional | mixed | exterior-void | astral
  time_of_day: station-morning | station-midday | station-night | cycle-irrelevant
  gravity: 1g | 0.33g | micro | thrust | null
  sound_environment: >
    Brief description of ambient sound — station hum, animal sounds, silence, etc.
  visual_notes: >
    Any visual details specific to this scene that differ from the location baseline.

# ── CHARACTERS PRESENT ───────────────────────────────────────────────────────

characters:
  primary:
    - id: jace_apollo
      entry_state: "tired, post-crossing headache, slightly wry"
      exit_state: "alert, concerned, processing"
      physical_position: "seated at workbench; stands at line 47"
  secondary:
    - id: cerberus
      entry_state: "relaxed, at Jace's feet"
      exit_state: "alert, ears forward"
  background:
    - id: "{unnamed_character_type}"
      notes: "Two other workers visible through viewport"
  off_page_but_relevant:
    - id: kael
      notes: "Referenced in dialogue; not physically present"

# ── DIALOGUE METADATA ────────────────────────────────────────────────────────
# Per-line attribution for audiobook/video production.
# Format: line_number | speaker | emotional_tone | delivery_note | text_excerpt

dialogue:
  - line: 12
    speaker: jace_apollo
    emotional_tone: dry | wry | exhausted
    delivery_note: "The sarcasm is real but so is the concern underneath it"
    text_excerpt: "First eight words of the line for identification..."

  - line: 23
    speaker: sophia_lotte
    emotional_tone: precise | controlled | barely-concealed-excitement
    delivery_note: "She's reporting; she is very not calm"
    text_excerpt: "First eight words..."

  - line: 31
    speaker: jace_apollo
    emotional_tone: processing | quiet
    delivery_note: "Beat before this line — he needed a second"
    text_excerpt: "First eight words..."

# ── EMOTIONAL BEAT ───────────────────────────────────────────────────────────

emotional_beat:
  arc_beat_label: "{Label from arc file emotional arc table}"
  scene_function: setup | development | turn | payoff | transition
  reader_experience: >
    One sentence describing what the reader should feel, not what happens.
  
# ── FORESHADOWING IN THIS SCENE ──────────────────────────────────────────────

foreshadowing_planted:
  - element: "{What is planted}"
    payoff_arc: arc_0N
    payoff_note: "{What it pays off}"

foreshadowing_paid_off:
  - element: "{What from earlier is paid off here}"
    planted_in: "{scene_id or arc where planted}"

# ── PRODUCTION NOTES ─────────────────────────────────────────────────────────

audiobook:
  chapter_break_before: true | false
  pacing_note: >
    Scene pace guidance — fast, slow, building, quiet, etc.
  sound_design_notes: >
    Any non-dialogue audio elements worth flagging: the station hum changes,
    an alarm, an animal sound that is a character moment.

video_ai:
  shot_type_suggestion: establishing | medium | close | sequence
  key_visual_moment: >
    The single frame that best represents this scene. What does it look like?
  character_blocking: >
    Where people are and how they move. Brief.
  environment_reference: >
    Which visual profile image(s) to use as environment reference.

storybot_notes: >
  Anything StoryBot should know when generating prose for this scene that isn't
  in the scene contract. Traps to avoid. Specific details to include.

# ── CONTINUITY FLAGS ─────────────────────────────────────────────────────────

continuity:
  advancement_events: []  # List any skill advancement moments in this scene
  will_orb_drops: []      # List any orb drops with species and absorber
  character_state_changes: []  # Any permanent state changes
  open_decisions_touched: []   # Reference to arc file open decisions engaged here
```

---

## HOW STORYBOT USES THIS SYSTEM

When StoryBot generates prose for a scene, it should:

1. Read the scene contract from the arc file
2. Read the scene's `_metadata.yaml` sidecar
3. Read the relevant Visual Profile files for all primary characters
4. Read the location's Visual Profile

The metadata tells StoryBot:
- What emotional register each character is in (not just their state — their *register*)
- What the environment should feel like in prose (the sensory profile)
- What has been planted that should be visible without being announced
- What is being paid off that needs weight

StoryBot should annotate its generated prose output with:
```yaml
# STORYBOT OUTPUT METADATA
generated_from_scene: {scene_id}
dialogue_lines_generated: N
foreshadowing_planted_per_contract: [list]
foreshadowing_paid_off: [list]
character_emotional_arcs_honored: [list]
flags: [anything that seemed uncertain or that should be reviewed]
```

---

## COMPLETENESS TRACKER — HOW TO UPDATE

The `_tracker.svg` file visualizes completeness across all visual profiles.
To update it, provide this conversation with:

1. The current completeness values for each subject (from the profile files)
2. Which items have been filled in since the last tracker generation
3. Any new subjects added

Request: *"Regenerate the visual profile completeness tracker SVG with these
values: Jace 60%, Kael 55%, Sophia 30%, Jin 45%, Nick 25%, Cerberus 50%,
Fortuna 75%, Falcon 55%. New subjects to add: [list]."*

The tracker SVG shows:
- Completeness bar per subject, color-coded by status
- Which specific field categories are missing (appearance / voice / astral / prompts)
- Image generation readiness flag (HOLD / READY / PARTIAL)

---

## WHAT TO WORK ON IN A NEW SESSION

### If the author has filled in gaps:
1. Search `project_knowledge_search` for `visual_profile` to find all profile files
2. Identify which [AUTHOR INPUT NEEDED] items have been answered
3. Update the relevant profile files with confirmed values
4. Update image generation prompts from HOLD to READY
5. Update completeness ratings
6. Regenerate the tracker SVG

### If you're adding a new subject (new character, location, or creature):
1. Search the KB for all existing description of the subject
2. Create a new visual profile file using the template above
3. Extract all confirmed values; flag everything uncertain
4. Set completeness rating
5. Add to tracker SVG

### If you're adding scene metadata:
1. Identify which scenes have draft prose but no metadata sidecar
2. Create the sidecar using the YAML template above
3. Tag all dialogue lines with speaker and emotional tone
4. Flag any continuity events

### If you're updating for a new arc:
1. Update character visual profiles with arc-specific appearance changes
2. Create location visual profiles for any new locations
3. Create creature visual profiles for any new fauna
4. Check advancement ledger — if a character's capabilities changed, the Astral
   appearance section of their profile may need updating

---

## VOICE PROFILE REFERENCE — EMOTIONAL TONE VOCABULARY

Use consistent vocabulary for emotional tones in dialogue metadata.
This vocabulary maps to audiobook direction and video AI generation.

**Baseline tones (character at rest):**
`dry` | `precise` | `controlled` | `warm` | `wry` | `quiet` | `professional`

**Under pressure:**
`clipped` | `careful` | `terse` | `flat` | `urgent` | `focused` | `suppressed`

**Emotional expression:**
`barely-concealed-{emotion}` | `openly-{emotion}` | `processing` | `landed`

**Jace-specific:** `gallows` | `copy-mode` | `negative-mode` | `unguarded`
**Kael-specific:** `calibrated` | `the-pause` | `composure-intact` | `composure-broken`
**Sophia-specific:** `notebook-mode` | `scientific-shock` | `barely-contained-relief`
**Nick-specific:** `okay-quiet` | `holding-the-network` | `the-README-voice`
**Jin-specific:** `seek-suppressed` | `liberated` | `crew-chief`

---

## CROSS-SYSTEM REFERENCES

| System | File | Purpose |
|---|---|---|
| Image generation agent | `storybot/image_generation_agent_prompt.md` | Agent instructions for generating images from visual profiles |
| Advancement ledger | `magic-systems/advancement_ledger.md` | Tracks skill changes that affect Astral appearance |
| Scene contracts | `arcs/arc_0N_{slug}.md` | Scene-level commitments that metadata should honor |
| Character sheets | `sheets/sheet_{subject}_{arc}_{checkpoint}.md` | Physical condition at specific arc moments |
| Signals guide | `magic-systems/magic_progression_signals_guide.md` | How advancement appears in prose (affects emotional tone) |
