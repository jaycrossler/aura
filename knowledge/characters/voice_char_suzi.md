---
id: voice_char_suzi
character_ref: char_suzi
type: character_voice_profile
status: detailed (drafted from char_suzi.md and Ch09, Ch19)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for Suzi Gonzales, Fortuna Station chief of security, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_suzi]]"
  - "[[char_helena]]"
  - "[[char_jace_apollo]]"
  - "[[char_penny_ai]]"
  - "[[location_fortuna_station]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Suzi Gonzales

`char_suzi.md` already contains a short Voice and Manner section. This file
expands it into the generator-ready format and adds the register notes the
Ch09 and Ch19 scenes require.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Mid-to-low female, weathered, compact. She is 49, gray-haired,
  and keeps herself in very good shape. The voice should sound used, not old.
- **Accent:** Hispanic-American. Her career was U.S. Army Security Forces,
  Earth-stationed, so the accent should read as American first with heritage
  underneath rather than as a marked second-language accent.
- **Pitch:** Low and steady. Almost no expressive range, by temperament rather
  than by suppression.
- **Speech rate:** Unhurried. The character file uses that exact word twice.
  She has time. That is itself the authority.
- **Volume:** Low-moderate. *"Doesn't raise her voice; doesn't need to."*
- **Resonance:** Chest, some grain.
- **Distinctive features:** Watches before she speaks, and the pause before her
  questions is longer than the pause after them. She treats fear as a fact to be
  managed rather than indulged, and that shows as complete tonal flatness when
  discussing frightening things.

**Casting note:** A retired professional who took a quiet job and caught a case
she cannot solve. Dry, economical, unintimidated. Not hard-boiled, not folksy.
The one thing to avoid is any read that makes her sound like she is enjoying
being the authority.

### Vocal Variations by Emotional State

**Default (professional, dry):**
- Level, economical, patient. Investigator's patience, not a performance of it.

**Asking for help (Ch09, the Helena ask):**
- Slightly less formal, and noticeably direct about what she cannot do herself.
  She is asking a courier to keep his eyes open, which she knows is thin.

**Bias surfacing (the Chinese community):**
- `char_suzi.md` is explicit that this should read as a real flaw and not a
  quirk, and the Ch09 draft has her voice a suspicion and then self-check it.
  Perform the suspicion at her normal register, without a hardening. The
  self-check should be quieter, and should not sound like an apology. She has
  not identified it in herself as prejudice.

**Allergic to certainty:**
- The character file names this: she is allergic to people certain about things
  they cannot know. When someone overclaims, her responses get shorter and
  flatter rather than argumentative.

**Personal grief (Helena):**
- She knew Helena. This is Fortuna's first murder investigation and she takes it
  hard, not just professionally. Any beat touching Helena should slow by a
  fraction and go plainer. Never wet.

## Speech Patterns

### Verbal Tics and Habits
- Asks for facts, not opinions.
- Does not soften bad news and does not dramatize it.
- Files a case open rather than inventing a culprit. When she says she does not
  know, she says it flatly and without embarrassment.

### Vocabulary Range
- **Technical:** Chain of evidence, hatch logs, movement sensors, interviews.
  Comfortable with procedure, uncomfortable with anything mystical.
- **Emotional:** Almost absent in speech. Present in what she chooses to keep
  working on.
- **Casual:** Minimal but not cold. Most of her working hours are spent standing
  between factions before an argument becomes something worse, which requires a
  functional, de-escalating everyday register.

### Relationship-Specific Speech

| With | Register |
|---|---|
| Jace | Starts as an authority interviewing a cleared outsider; becomes the first station authority to take him seriously. The warming is slow and should be barely perceptible chapter to chapter. |
| Nick | Relies on his network data. Practical, transactional, respectful. |
| {Penny} | Works with it daily. Direct, unimpressed, and increasingly the human counterweight to {Penny}'s confident wrong narratives. Their scenes are the book's clearest argument about surveillance. |
| The Chinese detachment | The flaw. See above. |

## Internal Monologue Style
Not a POV character in Ch00-20.

## Example Dialogue Anchors

`char_suzi.md` describes her manner but the retrieved chapter text did not
surface direct quoted lines for her. **No dialogue anchors are listed here
rather than inventing them.** Populate this section from `draft_ch09_first_week.md`
and `draft_ch22_no_vampires.md` on the next pass.

## Speech-Affecting Conditions
None established.

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default | No inline tags |
| Helena beats | No tags. A `<sigh>` here would make her grief legible, and the character's whole construction is that it is not |
| de-escalating a faction argument | No tags |

### Kokoro
- A lower American female pack, slowed slightly below baseline.
- Kokoro will not produce grain or wear. If the available packs all read too
  clean and too young, this is a character worth reserving for Chatterbox.

### Chatterbox
- Reference clip brief, 12 to 20 seconds: a woman in her late forties who has
  done twenty years of security work, explaining calmly that the evidence does
  not support the conclusion someone wants. Unhurried, low, no edge.
- `exaggeration` low. `cfg_weight` biased toward adherence so the pacing stays
  slow.

### All engines
Suzi, Lanchee, Mei, and Kim are four low-affect female voices. Suzi is the
lowest and the slowest of the four, and that is the primary separator. Audition
all four in one pass.

## Revision Notes

- 2026-08-15: Initial file. Expanded from the Voice and Manner section of
  `char_suzi.md` (2026-07-27) into the dedicated generator-ready format.
  Dialogue anchors deliberately left empty pending direct retrieval of her lines.
