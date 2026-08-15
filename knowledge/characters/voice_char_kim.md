---
id: voice_char_kim
character_ref: char_kim
type: character_voice_profile
status: detailed (revised — author-ruled name and ethnicity, 2026-08-15)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for Kim Jones-Hyatt, Fortuna Station drone operations manager, formatted for local TTS audiobook generation. Supersedes the 2026-08-15 light profile now that her surname and background are ruled."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_kim]]"
  - "[[char_carlos]]"
  - "[[char_jace_apollo]]"
  - "[[location_fortuna_station]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "Author ruling 2026-08-15: full name is Kim Jones-Hyatt, and she is an African American woman. char_kim.md still reads 'Kim [surname TBD]' and needs updating to match. Staged in patches/EDITS.md."
---

# Character Voice Profile — Kim Jones-Hyatt

Full name and background ruled by the author on 2026-08-15: **Kim
Jones-Hyatt**, African American. This supersedes the earlier light profile,
which had no name or physical data at all. `char_kim.md` itself still needs
the same update — see the open flag.

The character direction from `review_2026-08-14_chapters_00_20_contract_reconciliation.md`
still governs everything below: **do not reduce her to someone who blocks
Jace's clever ideas.** She is better than him at the actual job and
responsible for the people inside the system.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Mid-range female, unhurried, grounded.
- **Accent:** General American. Regional specifics not yet ruled; a light
  Mid-Atlantic or Southern-inflected American register is a reasonable
  production default until further specified, since it's common in Origin's
  American-heavy management pipeline, but this is not canon.
- **Pitch:** Level. She does not rise at the end of questions, which is part of
  why her questions land as pressure rather than curiosity.
- **Speech rate:** Slow to moderate, with real comfort in silence. Ch16 has her
  stand behind Jace "for long enough to become a weather condition" before
  saying anything — the pauses are the performance.
- **Volume:** Low to moderate. She never needs volume.
- **Resonance:** Natural, grounded.
- **Distinctive features:** Short questions in sequence, each one landing
  before the next. She is running an audit, not an argument.

**Casting note:** A competent Black woman in middle management who is
completely unimpressed and completely fair. Dry, patient, authoritative
because she is right, not because she is loud. Avoid any read that leans on
stereotype for either warmth or sternness — she is precise, not performed.

### Vocal Variations by Emotional State

**Default (managerial, dry):**
- Short questions, level delivery, generous pauses.

**Unimpressed (her signature mode, Ch16):**
- *"Who authorized this?" / "Who reviewed it?" / "That is not the answer I
  wanted."* Each flatter than the last. No rise in volume, no sarcasm. The
  flatness is the pressure.

**Correcting without punishing:**
- She checks the work, finds it acceptable, and still imposes a trial —
  because that is what a responsible manager does. The performance should make
  both halves legible.

**Dry humor:**
- *"Do not sound so pleased with yourself."* Deadpan, already walking away.

## Speech Patterns

### Verbal Tics and Habits
- Question, pause, question. Doesn't fill her own silences.
- States a decision as a fact, not an offer. *"Two-day trial."*
- Doesn't explain her reasoning unless asked directly.

### Vocabulary Range
- **Technical:** Fluent and operational — queues, exception patterns, route
  logs, escalation paths, permissions. She taught Jace the exception patterns
  he later encodes without her authorization; worth preserving in performance
  that she is the source of his competence, not the obstacle to it.
- **Emotional:** Not on the page in Ch00-20.
- **Casual:** Minimal.

### Relationship-Specific Speech

**With Jace:** Professional, increasingly wary. From Ch16 she's the person he
cannot charm; after the Ch18 automation-failure repair beat, she's the person
he owes. Her register shouldn't change much across that arc — his should.

**With Carlos:** Not yet on the page. Both are Fortuna operations.

## Internal Monologue Style
Not a POV character. No sample available.

## Example Dialogue Anchors

- *"Who authorized this?"*
- *"Who reviewed it?"*
- *"That is not the answer I wanted."*
- *"Two-day trial. You watch every run."*
- *"Do not sound so pleased with yourself."*

## Speech-Affecting Conditions
None established on the page.

## Local TTS Engine Notes

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| all modes | No inline tags. Her entire effect is flat delivery plus silence |

### Kokoro
- An American female pack. Audition for flatness and groundedness over
  brightness.
- Her characterization depends on pause length, which Kokoro won't produce on
  its own — insert explicit 700-1200ms silence between her question lines at
  the segmentation stage.

### Chatterbox
- Reference clip brief: a grounded Black American woman in her thirties or
  forties, calmly asking a direct-report a question she already knows the
  answer to. Level, unhurried, no edge.
- `exaggeration` low.

## Revision Notes

- 2026-08-15: Revised following author ruling on name (Kim Jones-Hyatt) and
  background (African American). Supersedes the same-day light profile.
  Dialogue anchors unchanged from `draft_ch16_ten_good_days.md`.
