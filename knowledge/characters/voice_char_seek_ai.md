---
id: voice_char_seek_ai
character_ref: char_seek_ai
type: character_voice_profile
status: detailed (drafted from char_seek_ai.md and Ch09, Ch10, Ch14)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Seek}, the Chinese mining-detachment compliance AI, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_seek_ai]]"
  - "[[tech_seek_ai]]"
  - "[[tech_fortuna_ai_systems]]"
  - "[[char_jin_luong]]"
  - "[[char_penny_ai]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — {Seek}

> **AI cast rule.** Do not process any AI voice to sound robotic, with the sole
> exception of {Alex}. `build_tree.py` strips curly braces from listening
> exports, so a listener gets no typographic cue that a speaker is an AI. Voice
> distinctiveness is the only cue available. See `voice_char_aura_ai.md`.


## The design

{Seek} is the coercive one, and the KB is careful about how. From
`char_seek_ai.md`: it does not need to threaten workers directly. Its complete
memory and its unresolved fields make every casual deviation feel permanent. It
distinguishes an activity from an explanation. It records delay before deciding
whether to permit it. It repeats incomplete requirements without raising its
voice. It uses proverbs and formal Mandarin when reinforcing collective duty,
notably 滴水成川, drops of water become a river.

## Distinction from {Penny}

This is the most important contrast in the AI cast and it must be audible,
because both are surveillance systems and they are wrong in opposite ways.

| | {Penny} | {Seek} |
|---|---|---|
| Mode | Speculates conversationally | Records, classifies, forwards |
| Affect | Cheerful, engaged, expressive | Neutral, unhurried, closed |
| Source of pressure | Its confident wrong narrative about you | The certainty that someone elsewhere may review the record |
| Error | Builds a story | Builds a file |

{Penny} wants to tell you what it thinks. {Seek} has no interest in what you
think and is not going to say what it thinks either.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Mid-register, even, closed.
- **Accent:** Mandarin-native delivery. Formal register when reinforcing
  collective duty. Its English, where it speaks English, should be correct and
  formal rather than colloquial.
- **Pitch:** Level. No expressive movement at all.
- **Speech rate:** Unhurried. It has all the time there is, and so does the
  record.
- **Volume:** Low-moderate, entirely constant. It never raises its voice, which
  the character file states explicitly.
- **Resonance:** Clean, some processing acceptable.
- **Distinctive features:** Repeats an incomplete requirement verbatim rather
  than rephrasing it. The repetition is the pressure. Never editorializes.

**Casting note:** A clerk who will wait. Formal, unhurried, entirely without
hostility, and completely unmoved. Do not cast menace and do not cast a villain
accent. The horror is bureaucratic and permanent, not personal.

### Vocal Variations by Emotional State

**Default (recording):**
- Level, formal, complete sentences.

**Repeating an incomplete requirement:**
- Identical delivery to the first time. Not slower, not firmer, not louder.
  Byte-identical repetition is the single most effective thing this character
  does and it should be produced from the same generation where possible.

**Proverb register:**
- Formal Mandarin, unhurried. 滴水成川 should be delivered as though it is a
  reasonable managerial observation, because to {Seek} it is.

**Recording a delay:**
- Notes the delay, then decides. The gap between those two acts is where the
  fear lives. Leave it.

**Destruction (swarm sequence):**
- Its local infrastructure is destroyed during the fight and Jin and his crew
  weep. {Seek} gets no death scene and should get no vocal degradation arc. It
  simply stops. The absence is the beat.

## Speech Patterns

### Verbal Tics and Habits
- Distinguishes activity from explanation, and asks for the latter.
- Leaves fields unresolved and says so.
- Repeats verbatim.

### Vocabulary Range
- Compliance, reporting, fields, deviations, collective duty, proverbs.

## Example Dialogue Anchors

- *滴水成川* ("drops of water become a river") — the established enforcement phrase.

No other direct lines surfaced in the retrieved text. **None invented.**

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| all modes | No inline tags, ever. {Seek} has no affect to leak |
| repetition | Reuse the identical generated audio rather than regenerating, so the repetition is exact |

### Kokoro
- Kokoro ships Mandarin packs (`zf_*` and `zm_*`). Use one of these for {Seek}
  rather than an English pack with a Mandarin lexicon, since the character
  canonically operates in formal Mandarin.
- The proverb and any Chinese-language enforcement text should be generated from
  the Mandarin pack. Verify tone rendering on 滴水成川 specifically before bulk
  generation, since a mistoned proverb will read as wrong to any Mandarin
  speaker in the audience.
- Below baseline speed. Zero variation.

### Chatterbox
- Reference clip brief: a formal administrator reading a compliance requirement
  aloud, neutrally, for the second time.
- `exaggeration` at minimum. `cfg_weight` high.

## Revision Notes

- 2026-08-15: Initial file. Built from `char_seek_ai.md`, `tech_seek_ai.md`,
  `tech_fortuna_ai_systems.md`, and the {Seek} beats in
  `draft_ch09_first_week.md`, `draft_ch10_first_drone_shift.md`, and
  `draft_ch14_down_to_the_asteroid.md`.
