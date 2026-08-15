---
id: voice_char_jin_luong
character_ref: char_jin_luong
type: character_voice_profile
status: detailed (consolidated from char and visual profiles)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for Jin Lóng, head mining supervisor of Fortuna's Chinese detachment, formatted for local TTS audiobook generation. Consolidates the Voice fields already in char_jin_luong.md and the Voice Profile table in visual_profile_jin_long.md."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_jin_luong]]"
  - "[[visual_profile_jin_long]]"
  - "[[char_seek_ai]]"
  - "[[char_mei]]"
  - "[[sheet_jin_arc01_end]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Jin Lóng

Jin's voice data already existed in two places: the `# Voice` block in
`char_jin_luong.md` and the Voice Profile table plus Audiobook Direction Notes
in `visual_profile_jin_long.md`. This file consolidates both without changing
any of it, and adds the production detail the local engines need.

Jin is the series' false villain. Everything about the vocal design serves the
reveal: he sounds contained and dangerous, and he is neither.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Mid-to-low male, compact and dense, matching the physicality.
  Mid-forties, reads younger because of fitness.
- **Accent:** Canonically **surprisingly clear, with no accent that reads as
  non-native**. Clean and precise. Mandarin is his native language and English
  is functional, but the English should not be performed as effortful. This is a
  deliberate authorial choice and should not be softened toward a stereotype.
- **Pitch:** Low, level, very little movement.
- **Speech rate:** Measured. He says less than he means, and the gap is audible.
- **Volume:** Low. **When angry he gets quieter, not louder.** The character file
  is explicit: the danger is in the reduction.
- **Resonance:** Chest, contained.
- **Distinctive features:** He does not fill silence. When Jin stops talking,
  the silence is load-bearing and the mix should let it run.

**Casting note:** Contained, watchful, precise. The scar across the corner of
his mouth makes his neutral face read as smirking or angry, and the voice should
work against that rather than with it. He is neither. Do not cast menace.

### Vocal Variations by Emotional State

**Default (contained):**
- Level, clean, economical.

**Under {Seek} (all of Arc 1 before the swarm):**
- Further constrained. Every word weighted against surveillance. The direction
  note in the visual profile is the important one: **leave room for the reader
  to sense something is wrong with the paranoia, not the man.** He is suppressed,
  not sinister. Practically, this means slightly shorter phrases, slightly
  longer gaps, and no editorial colour.

**Angry:**
- Quieter and more precise, never louder.

**With his crew:**
- The warmth is real and it is the foundation of the character. They call him
  their Dragon privately. He would do anything for them. This register is not
  loud either, but the temperature is completely different.

**With Mei:**
- Unfailingly polite and never inviting. He is waiting to see what she actually
  is. Politeness with a closed door behind it.

**Liberation (Ch-swarm, {Seek} destroyed):**
- The canonical direction: **the liberation breath and tear carry no speech.**
  The moment is physical. Do not generate a vocalization for it; if the
  production wants a sound there, it should be recorded or spliced, not tagged.

**Post-liberation:**
- Same voice, same register, different temperature. The ceiling is gone. The
  shift should be audible without changing his vocal register, which is a
  genuinely difficult direction and is best achieved with pacing and breath
  rather than with pitch.

## Speech Patterns

### Verbal Tics and Habits
- Says less than he means, consistently.
- Reads a room before speaking; the first line in any scene arrives after a beat.
- Under {Seek}, avoids anything that could be logged as an explanation rather
  than an activity, which is {Seek}'s own distinction.

### Vocabulary Range
- **Technical:** Expert mining operations, crew management, thermal work.
- **Mandarin:** Native. {Seek}'s enforcement phrase 滴水成川 ("drops of water
  become a river") belongs to the AI, not to him, but he has lived inside it for
  years. Any Mandarin in his own mouth should be unhurried and unperformed.
- **Emotional:** Nearly absent in words. Entirely present in action.

## Internal Monologue Style
Not a POV character in Arc 1.

## Example Dialogue Anchors

The retrieved chapter text did not surface direct quoted lines for Jin in
Ch00-20. **None are invented here.** Populate from `draft_ch09_first_week.md`
and the swarm sequence on the next pass.

## Speech-Affecting Conditions
- **Mining environment:** Lower-ceiling corridors, heavy conduit. Close, dry
  acoustic rather than reverberant.
- **Suit and comms during the swarm:** Standard band-limiting.

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default and under {Seek} | No inline tags, ever. Suppression is the character and any vocalization breaks it |
| angry | No tags. Quieter and more precise |
| liberation moment | No tags. Canonically no speech. Do not attempt to generate the weeping |
| with his crew | No tags |

### Kokoro
- Kokoro ships Mandarin packs (`zm_*`) and American male packs. Jin's canon says
  his **English has no non-native accent**, so use an American male pack for his
  English and reserve a Mandarin pack only for actual Mandarin lines.
- Slow below baseline and insert deliberate pre-line pauses. His pauses are
  characterization.

### Chatterbox
- Reference clip brief: a man in his mid-forties, physically capable, speaking
  quietly and precisely to someone he does not fully trust, in a room he assumes
  is monitored.
- `exaggeration` very low. This is the lowest-expressivity setting in the human
  cast alongside Mei.
- Consider a **second reference clip** for post-liberation: same voice, warmer
  room, no monitoring. Switching clips is the most reliable way to produce the
  "same register, different temperature" direction.

## Revision Notes

- 2026-08-15: Initial dedicated voice_char file. Consolidated verbatim from the
  `# Voice` block in `char_jin_luong.md` (2026-06-30) and the Voice Profile table
  plus Audiobook Direction Notes in `visual_profile_jin_long.md`. No canon
  changed. Dialogue anchors left empty pending retrieval.
