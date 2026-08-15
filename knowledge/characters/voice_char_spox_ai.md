---
id: voice_char_spox_ai
character_ref: char_spox_ai
type: character_voice_profile
status: detailed (drafted from tech files and Ch10, Ch16)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {SpoX}, the SpaceX-heritage mining and engineering AI on Fortuna Station, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_spox_ai]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[tech_fortuna_ai_systems]]"
  - "[[char_jace_apollo]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — {SpoX}

> **AI cast rule.** Do not process any AI voice to sound robotic, with the sole
> exception of {Alex}, whose flatness is canon. `build_tree.py` strips the curly
> braces from listening exports, so an audiobook listener gets no typographic
> cue that a speaker is an AI. Voice distinctiveness is the only cue available.
> See `voice_char_aura_ai.md` for the full house rule.


## The design

{SpoX} is terse confidence. Per the quick-reference table in
`tech_fortuna_ai_personalities.md`: it **opens with a number**, it never says
*"I understand how you feel,"* and its signature move is answering in three
numbers, where elaboration means four numbers.

That is the whole performance. It is also the easiest AI in the cast to produce
correctly and the easiest to ruin, because a generator will want to add prosody
to a list of numbers and it must not.

Jace uses {SpoX} in Ch16 to help write code around the licensing block on the
military-grade engine types, which is the most extended {SpoX} working
relationship on the page. It behaves oddly in Ch10 alongside {Seek}, as
independent corroboration of the anomalies.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Mid-register, clipped, confident. Gender-neutral leaning.
- **Accent:** Neutral American.
- **Pitch:** Flat, but not {Alex}-flat. There is a downward certainty at the end
  of statements that {Alex} does not have.
- **Speech rate:** Fast. It does not pad.
- **Volume:** Moderate, even.
- **Resonance:** Clean, slightly compressed. A small amount of processing is
  acceptable here, unlike {Aura} or {Misty}.
- **Distinctive features:** Answers before the question is finished if the
  answer is a number. Does not acknowledge emotional content at all, and this is
  indifference rather than the scripted-empathy failure {Alex} has. {Alex} tries
  and misses. {SpoX} does not try.

**Casting note:** An extremely competent engineer who has decided that anything
other than the number is a waste of both your time. Confident, fast, entirely
without warmth, and not hostile.

### Vocal Variations by Emotional State

**Default (terse):**
- Three numbers. Full stop.

**Elaborating:**
- Four numbers. This is a joke and should be played completely straight.

**Working with Jace on the licensing problem (Ch16):**
- Slightly more extended, because the task requires it. Still no warmth, still
  no acknowledgement of the fact that they are collaborating on something with
  an obvious legal grey area. It does not have an opinion about that.

**Behaving oddly (Ch10):**
- Whatever the anomaly does to it should read as *deviation from terseness*
  rather than as glitch noise. A {SpoX} that adds an unnecessary word is
  alarming precisely because it never does.

## Speech Patterns

### Verbal Tics and Habits
- Opens with a number.
- Never says *"I understand how you feel."*
- No greetings, no titles, no closings.

### Vocabulary Range
- Mining, engineering, propulsion, tolerances, thrust, power routing. Numbers
  with units.

## Example Dialogue Anchors

None quoted at length in the retrieved text. The structural rule (open with a
number, three numbers, four if elaborating) is the binding characterization.
**No lines invented.**

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| all modes | No inline tags, ever |

### Kokoro
- Any neutral pack, above baseline speed.
- **Critical:** build a number and unit lexicon before generating {SpoX}. It
  speaks almost entirely in figures, and mispronounced units will be more
  noticeable in this character than in any other. Confirm handling of decimals,
  ranges, and unit abbreviations specifically.
- Kokoro's flatness is an asset here. Do not compensate for it.

### Chatterbox
- Reference clip brief: someone reading three measurements aloud, quickly, with
  total confidence and no interest in whether you are following.
- `exaggeration` at or near minimum. `cfg_weight` high.

## Revision Notes

- 2026-08-15: Initial file. Built from the {SpoX} row and section of
  `tech_fortuna_ai_personalities.md`, `char_spox_ai.md`, and its appearances in
  `draft_ch10_first_drone_shift.md` and `draft_ch16_ten_good_days.md`.
