---
id: storybot_metadata_template_guide
name: StoryBot Metadata Template Guide
type: system_documentation
status: working draft
last_updated: 2026-04-30
---

# StoryBot Metadata Template Guide

This document defines the metadata structures the StoryBot uses to procedurally generate book chapters, audiobook narration, illustrations, and other multimedia outputs from the knowledge base. It also serves as a reference for what to capture as new scenes and characters are developed.

---

## Core Concept

The StoryBot reads a chapter outline (sequence of scenes) and pulls from multiple metadata layers to generate consistent, rich prose. The output is **dual-format**:

1. **Prose text** — the readable chapter
2. **JSON sidecar** — structured metadata describing every dialogue line, character state, location detail, and sensory cue, for downstream rendering (audiobook with character voices, AI-generated illustrations, video clips, etc.)

When new knowledge is added or existing knowledge changes, affected chapters can be regenerated automatically.

---

## File Type Architecture

### Existing File Types (already in use)
- `/characters/char_*.md` — Character bios
- `/locations/location_*.md` — Locations
- `/factions/faction_*.md` — Factions
- `/scenes/event_*.md` — Scene narrative summaries (high-level)
- `/technology/tech_*.md` — Tech specifications
- `/timeline/timeline_master.md` — Master chronology
- `/universe-spec/concept_*.md` — World-rule concepts

### New File Types (introduced this session)
- `/characters/voice/voice_char_*.md` — Voice profiles
- `/characters/states/states_char_*.md` — Emotional/physical state templates
- `/scenes/choreography/choreo_event_*.md` — Detailed scene blocking and choreography
- `/scenes/sensory/sensory_event_*.md` — Scene-specific sensory primers (optional, for high-detail scenes)
- `/locations/sensory/sensory_location_*.md` — Location-specific sensory primers
- `/timeline/scenes_temporal_map.md` — Master scene-to-time mapping
- `/storybot/*` — System documentation and templates

### Recommended Future File Types
- `/chapters/chapter_*.md` — Chapter-level outlines mapping multiple scenes
- `/chapters/chapter_*.json` — Generated chapter sidecar metadata
- `/scenes/dialogue/dialogue_event_*.md` — Pre-written or anchor dialogue snippets
- `/storybot/style_guide.md` — Author voice and writing style guide
- `/storybot/regeneration_log.md` — Track which chapters need regeneration when knowledge changes

---

## Required Metadata for Each File Type

### Character File (`char_*.md`)
Already established; should include:
- Identity (id, name, aliases, species, gender, pronouns, dates, birthplace)
- Status (alive/dead, first/last appearance, POV)
- Affiliations (factions, loyalties)
- Relationships (family, allies, rivals, romantic)
- Capabilities (magic, skills, languages)
- Physical (appearance, distinguishing features)
- Story function (archetypes, arc, themes)
- Cross-references

### Character Voice Profile (`voice_char_*.md`)
- Audio profile (voice type, accent, pitch, rate, volume, resonance)
- Vocal variations by emotional state
- Speech patterns (verbal tics, fillers, sentence structure)
- Vocabulary range (technical, casual, emotional, intimate)
- Relationship-specific speech
- Internal monologue style (for POV characters)
- Example dialogue anchors
- Speech-affecting conditions (suit, HUD on/off, drinking, tired)
- Audio generation tags
- Visual/body language markers
- Knowledge state tracking

### Character State Template (`states_char_*.md`)
*Captures how a character physically/emotionally manifests different states*
- Confident state (face, body, voice, breathing)
- Nervous state
- Angry/frustrated state
- Sad/devastated state
- Excited/joyful state
- Tired state
- Other character-specific states
- Triggers for each state
- Recovery patterns

### Scene Narrative File (`event_*.md`)
Already established; high-level scene summary

### Scene Choreography File (`choreo_event_*.md`) — NEW
- Temporal anchors (date, times, durations)
- Setting layout (spatial map, multiple spaces if applicable)
- Sensory primer (visual, auditory, olfactory, tactile, atmosphere)
- Characters present (primary, secondary, background, mentioned)
- Beat-by-beat choreography (numbered beats with action, character states)
- Character emotional/physical state tracking (entry, exit)
- Dialogue style markers
- Camera/POV notes
- What this scene plants for later
- StoryBot extrapolation notes (what's invented vs. canonical)
- Cross-references

### Location Sensory Primer (`sensory_location_*.md`) — NEW
*Per-location sensory baseline*
- Visual palette (colors, lighting, signature views)
- Auditory baseline (constant sounds, occasional sounds, voices)
- Olfactory profile (dominant smells, secondary smells)
- Tactile environment (gravity, temperature, surfaces)
- Population texture (who's typically there, what they're doing)
- Time-of-day variations
- Seasonal/situational variations

### Temporal Map (`scenes_temporal_map.md`) — NEW
- Scene index with absolute dates/times
- Time-gap reference table
- Scene sequencing for chapter structure
- Off-page events affecting character state
- Continuity rules

### Chapter Outline (`chapter_NN.md`) — RECOMMENDED FUTURE
- Chapter title
- Scenes included (in order)
- Total duration (in-universe time)
- Emotional arc
- POV characters
- Estimated word count
- Cliffhanger or resolution
- Dependencies (what must be true from prior chapters)

---

## Character State JSON Schema (for sidecar metadata)

Each scene in JSON sidecar should track character state at fine granularity. Example schema:

```json
{
  "scene_id": "event_jace_doctor_appointment",
  "scene_metadata": {
    "date": "2105-03-16",
    "time_start": "12:00",
    "time_end": "13:30",
    "location": "mars_air_force_detachment_medical_office",
    "weather": "n/a (interior)",
    "lighting": "clinical, warm white"
  },
  "characters_present": [
    {
      "id": "char_jace_apollo",
      "role": "POV",
      "physical_state": {
        "wearing": "Air Force dress blue uniform, polished shoes",
        "physical_condition": "fresh, well-groomed, well-rested",
        "weight_estimate": "180 lbs (Earth-baseline, recently arrived)",
        "fitness_level": "peak military",
        "visible_features": "blond hair styled, clean-shaven, HUD implant visible (active)",
        "gravity_environment": "0.38g Mars",
        "hud_state": "active, military-grade"
      },
      "emotional_state": {
        "entry": "confident, anticipatory",
        "exit": "devastated, in shock",
        "arc_within_scene": ["confident", "puzzled", "shocked", "horrified", "bargaining", "despair", "numb"]
      },
      "knowledge_state": {
        "knows_at_entry": [
          "He has been assigned to drone command at Mars Air Force Detachment",
          "He has a 1M credit education debt (paid down by 10% so far)",
          "He has a HUD implant with confidential military upgrades",
          "His sponsor is Lt. Rich Cullivan",
          "Mars geography (broad)",
          "He has glimpsed two intel personnel (Mei and Sylvester)",
          "Comms to Artemis at Odysseus are failing"
        ],
        "learns_during_scene": [
          "He has a degenerative bone disease, no known cure",
          "Returning to Earth will accelerate the disease",
          "He cannot serve in the active military",
          "He has 30 days to vacate base housing",
          "Civilian transition options exist on Mars",
          "His sisters should be screened genetically"
        ]
      }
    },
    {
      "id": "char_doctor_mars_medical",
      "role": "supporting",
      "physical_state": {
        "wearing": "medical uniform, name badge",
        "physical_condition": "professional, composed",
        "visible_features": "[STORYBOT — extrapolate]"
      },
      "emotional_state": {
        "entry": "professional, prepared for difficult conversation",
        "exit": "sympathetic, mildly drained from delivering hard news"
      }
    }
  ],
  "dialogue_lines": [
    {
      "line_id": "line_001",
      "speaker": "char_doctor_mars_medical",
      "text": "Lieutenant Grant. I'm Dr. [Name]. Please, have a seat.",
      "audio_tags": ["professional", "calm"],
      "facial_expression": "polite, slight smile",
      "body_language": "standing, hand extended for handshake",
      "subtext": "Assessing Jace's emotional readiness"
    },
    {
      "line_id": "line_002",
      "speaker": "char_jace_apollo",
      "text": "Thank you, Doctor.",
      "audio_tags": ["confident", "formal"],
      "facial_expression": "polite, mildly curious",
      "body_language": "standing, returns handshake firmly",
      "subtext": "Treating this as routine"
    }
  ],
  "spatial_blocking": {
    "starting_positions": {
      "char_jace_apollo": "doorway",
      "char_doctor_mars_medical": "behind desk, standing"
    },
    "movement_beats": [
      "Jace enters, walks to visitor chair, sits",
      "Doctor sits at desk after handshake",
      "Doctor activates wall displays via gesture",
      "Information visualizations fill the room",
      "Jace remains seated throughout, body progressively collapsing"
    ]
  },
  "sensory_overlay": {
    "visual": "Initially calm office. Activates into immersive 3D data environment with skeletal models, medical journal text, comparison scans floating in air.",
    "auditory": "Quiet office sounds → soft whoosh of activation → AI voice supplementing doctor's explanations",
    "olfactory": "Antiseptic, plant on desk, doctor's coffee",
    "tactile": "Chair becomes uncomfortable as Jace's body tenses, hands grip armrests"
  },
  "cinematography_hints": {
    "opening_shot": "Medium two-shot of Jace and doctor",
    "key_moments": [
      "Wide shot when room activates with information",
      "Tight on Jace's face as 'bad news' lands",
      "Closer and closer on Jace as he asks questions",
      "Wide shot for hallway scene with Rich and Colonel"
    ],
    "closing_shot": "Apartment door closing on Jace from outside"
  },
  "extrapolation_allowed": [
    "Doctor's full name and personality details",
    "Specific medical disease name",
    "Specific medical journal references",
    "Background medical staff",
    "Specific private room location"
  ],
  "extrapolation_forbidden": [
    "Changing the diagnosis",
    "Adding new plot events",
    "Resolving the Mars-vs-Earth implication",
    "New character introductions"
  ]
}
```

---

## Question Categories for Worldbuilding Sessions

When developing new scenes/characters/locations with the author, ask questions in these categories. **Maximum 4 questions per turn** to avoid overwhelming the author in voice mode.

### Temporal Questions
- When does this happen? (date, time of day)
- How long does it take?
- What's the gap from the previous scene?
- What happens off-page between scenes?
- Is this a one-time event or recurring?

### Spatial Questions
- Where does this take place? (specific location and sub-locations)
- How big is the space?
- What's the physical layout?
- What can characters see / not see?
- What are the entry/exit points?
- What's the lighting?

### Character Presence Questions
- Who is in the scene?
- Who speaks vs. who's background?
- Are there mentioned-but-not-present characters?
- What's the population density?
- Who's wearing what?

### Sensory Questions
- What does it look like? (visual palette, lighting, key visual elements)
- What does it sound like? (constant sounds, occasional sounds, voices)
- What does it smell like? (especially distinctive)
- What does it feel like? (gravity, temperature, surfaces)
- What's the atmosphere/mood?

### Character State Questions
- What's the POV character's emotional state at scene start?
- How does it change during the scene?
- What's their physical state?
- What do they know? What do they not know?
- What relationships are active?

### Dialogue Questions
- Who speaks first?
- What's the tone of the conversation?
- Are there any specific lines that must land?
- What's not said but implied?
- How formal vs. informal?

### Plot Function Questions
- What does this scene plant for later?
- What does it pay off from earlier?
- What changes by scene end?
- Is there a turning point?
- What does the reader need to feel?

### Voice/Personality Questions
- How does each character speak in this scene specifically?
- Any verbal tics or characteristic phrases?
- Body language during dialogue?
- Subtext (what they don't say)?

### Continuity Questions
- Is this consistent with character state from the prior scene?
- Does this contradict any established canon?
- Are there any timeline issues?

### Extrapolation Questions
- Where can the StoryBot invent details?
- What must NOT be invented?
- What should be flagged for clarification?

---

## How to Ask Questions in Worldbuilding Sessions

### Best Practices

1. **Limit to 4 questions per turn** — author is often hands-free or voice-input
2. **Mix categories** — don't ask only spatial or only emotional; balance
3. **Sequence logically** — start with high-level (when/where) before drilling into details (specific dialogue, specific sensory)
4. **Acknowledge what you have** — recap quickly so author knows what you've already captured
5. **Flag your assumptions** — if you're guessing, say so, and ask if it's right
6. **Offer extrapolation as fallback** — when author doesn't know, offer "[STORYBOT can extrapolate this]" as an option

### Question Templates

**For new scenes:**
1. "When does this happen, and how long does it last?"
2. "Where does it take place, and what's the spatial layout?"
3. "Who's in it, and what's the emotional state of the POV character?"
4. "What's the key beat that must land?"

**For new characters:**
1. "What's their role in the story arc?"
2. "What do they look like and how do they speak?"
3. "What's their relationship to existing characters?"
4. "What do they know that the protagonist doesn't?"

**For new locations:**
1. "What's the function — what happens there?"
2. "Visual palette and lighting?"
3. "Sounds and smells?"
4. "Who's typically there, and what's the population texture?"

**For revising/expanding existing scenes:**
1. "What's missing from the current draft?"
2. "Are there sensory or emotional details we should expand?"
3. "Is the character state at entry/exit correct?"
4. "What's the dialogue rhythm we want?"

---

## Workflow for Generating a Chapter

The StoryBot's chapter generation workflow:

1. **Read chapter outline** (`/chapters/chapter_NN.md`)
2. **Identify scenes** to be included
3. **For each scene:**
   - Load scene narrative file
   - Load scene choreography file (if exists)
   - Load voice profiles for each speaking character
   - Load location sensory primers
   - Load temporal context from `scenes_temporal_map.md`
   - Load character knowledge state at scene entry
4. **Generate prose** for each scene, applying:
   - Character voice consistent with profiles
   - Sensory details consistent with primers
   - Dialogue consistent with relationship dynamics
   - Body language consistent with emotional states
5. **Generate JSON sidecar** with:
   - Per-line dialogue metadata
   - Character state at each beat
   - Spatial blocking
   - Cinematography hints
6. **Validate continuity:**
   - Cross-check character knowledge state
   - Verify temporal consistency
   - Confirm no canon contradictions
7. **Output:** Markdown chapter + JSON sidecar
8. **Log dependencies:** What knowledge files were used (for regeneration tracking)

When a knowledge file changes, the StoryBot can identify which chapters depend on it and flag those for regeneration.

---

## Areas Where StoryBot Can Always Extrapolate

Unless explicitly forbidden in a specific file, the StoryBot can invent:

- Background NPCs and their dialogue (unnamed pedestrians, vendors, soldiers)
- Specific small details (food prices, vendor names, shop layouts)
- Sensory specifics consistent with established palettes
- Character clothing variations consistent with their style
- Specific HUD app names, game titles, media references
- Brand names for products
- Specific patterns in maintenance damage, weathering
- Mars-local slang, idioms, common phrases
- Specific exercises, equipment, food items
- Casual conversation between background characters
- Physical descriptions of unimportant locations consistent with palette

## Areas Where StoryBot Must Flag for Author

- Major plot events not in timeline
- New named characters
- Resolutions to ambiguities (the bone disease, comms blackout, magic emergence)
- Changes to canonical traits
- Cross-faction politics shifts
- Magic system rules
- Technology capabilities not yet specified

---

## Example Session Flow (Worldbuilding Conversation)

**Author:** "Let's add a scene where Jace meets the Rat for the first time."

**StoryBot:** (Acknowledges, asks 4 questions)
1. "When does this happen — early in the hard months or after Artemis sends the package errand?"
2. "Where do they meet — at the bar, at the launch facility, or somewhere else?"
3. "What's the tone of the meeting — businesslike, warmly conspiratorial, or tense?"
4. "Does Jace know who the Rat is going in, or does it become clear during the meeting?"

**Author:** (Answers via voice)

**StoryBot:** (Acknowledges, asks 4 more questions about specifics)
1. "Spatial layout — where exactly does the meeting happen, and what does it look like?"
2. "Sensory environment — what's distinctive about this place at the time of day they meet?"
3. "How does the Rat speak — pace, accent, mannerisms?"
4. "What does Jace do/say that establishes his character in this scene?"

**Author:** (Answers)

**StoryBot:** (Once enough detail captured, generates choreography file with [STORYBOT] flags for what to extrapolate)

---

## Cross-References

- See `/storybot/` directory for system documentation
- See `/scenes/choreography/` for example choreography files
- See `/characters/voice/` for example voice profiles
- See `/timeline/scenes_temporal_map.md` for example temporal mapping

## Revision Notes

- 2026-04-30: Initial draft from voice session.
