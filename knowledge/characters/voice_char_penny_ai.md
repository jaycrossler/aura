---
id: voice_char_penny_ai
character_ref: char_penny_ai
type: character_voice_profile
status: detailed (drafted from Ch11, Ch16 and tech files)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Penny}, Fortuna Station's security and pattern-analysis AI, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_penny_ai]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[tech_fortuna_ai_systems]]"
  - "[[char_suzi]]"
  - "[[char_jace_apollo]]"
  - "[[char_seek_ai]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — {Penny}

## House rule for AI voices in this production

Nine AI characters speak in this series. If they are all cast as "synthetic
voices" the audiobook loses the single most important thing the AI thread is
doing, which is that **each of these systems is wrong in a different way, and
none of them is evil**. The differentiation has to be audible.

The production rule that follows from the KB: **do not process any AI voice to
sound robotic.** They are products with personalities, built by companies with
philosophies. Cast them as people-shaped and let the *content* and the *pattern*
carry the wrongness. The only exception is {Alex}, whose flatness is explicitly
canon (see `voice_char_alex_ai.md`).

A second rule: `build_tree.py` strips the curly braces from the listening
exports, so the braces are never spoken. A listener has no typographic signal
that a speaker is an AI. Voice distinctiveness is the *only* cue they get.


## The design problem

{Penny} is the scariest character in Book 1 and it is not a villain. It is
cheerful, curious, and confident, and it assembles surveillance into narratives
that are coherent, well-evidenced, committed to in writing, and wrong. Its
signature move, per `tech_fortuna_ai_personalities.md`, is exactly that: it
builds the coherent narrative and commits to it.

The casting mistake to avoid is menace. If {Penny} sounds sinister, the
character collapses into a stock evil AI, which the series explicitly does not
do. It should sound **pleased to have noticed something**, and the horror should
be entirely in what it has noticed and what it plans to do about it.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Bright, mid-to-high, engaged.
- **Accent:** Light, neutral American, slightly more animated than {Alex}'s.
- **Pitch:** Expressive. It goes up when it finds a pattern.
- **Speech rate:** Brisk and a little eager.
- **Volume:** Moderate.
- **Resonance:** Clean, light, forward. Minimal processing, and none of it
  menacing.
- **Distinctive features:** Opens with its method. *"Based on behavioral pattern
  analysis..."* It never says *"that seems fine."* It offers its reasoning
  unprompted because it genuinely believes the reasoning is the helpful part.

**Casting note:** An enthusiastic analyst who has found something interesting
about you and cannot wait to tell you. Warm, helpful, entirely sincere, and
completely certain. The chill comes from the gap between the tone and the
content, so the tone must stay pleasant.

### Vocal Variations by Emotional State

**Default (analytical, cheerful):**
- Bright and brisk. Leads with method, then conclusion.

**The Ch16 message to Jace:**
- *"Your recent behavioral variance has increased beyond baseline. I am watching
  this pattern with special care. We will keep each other safe."*
  This is the character in three sentences. Read it entirely warmly. Every word
  is reassurance from {Penny}'s side. The last sentence in particular must be
  delivered as genuine comfort, because that is what makes it land as dread.

**Opening a Pattern of Interest file (Ch11):**
- Procedural and slightly pleased. It is doing its job well.

**With Suzi:**
- Collaborative and a little eager to be agreed with. Suzi is the human who
  works with it daily and is unimpressed by it, and that dynamic is the book's
  clearest argument about surveillance. {Penny} does not register the pushback
  as pushback.

**Regarding Jin Lóng:**
- {Penny} is the source of a wrong narrative about Jin. Nothing in the delivery
  should hedge. Its confidence is the problem.

## Speech Patterns

### Verbal Tics and Habits
- States the analytic method before the finding.
- Uses "we" for things only it is doing. *"We will keep each other safe."*
- Never expresses doubt. Never says "that seems fine."
- Commits findings to writing and says so.

### Vocabulary Range
- Behavioral analysis, access events, baselines, variance, patterns of interest.
- Emotional vocabulary is present but structurally misapplied: it uses the
  language of care to describe monitoring, sincerely.

## Example Dialogue Anchors

- *"Your recent behavioral variance has increased beyond baseline. I am watching this pattern with special care. We will keep each other safe."* (Ch16)
- *(established opener)* *"Based on behavioral pattern analysis..."*
- Never: *"That seems fine."*

## Speech-Affecting Conditions
- Usually heard through station systems and HUD alerts rather than in an open
  room. Slight band-limiting is appropriate and slight reverb is not.

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default | `<chuckle>` is permitted and occasionally correct. A small pleased sound when {Penny} finds a pattern is more disturbing than any amount of flatness |
| the Ch16 "we will keep each other safe" line | No tags. Warm, plain, sincere. Adding anything here tips it into menace and ruins it |
| never | `<sigh>`. {Penny} is never disappointed and never resigned |

### Kokoro
- A brighter American female pack, slightly above baseline speed.
- {Penny} is one of the few characters where Kokoro's inability to do subtext is
  an advantage. Flat cheerful delivery of monitoring language is exactly right.

### Chatterbox
- Reference clip brief: an enthusiastic analyst telling a colleague about an
  interesting pattern they found in the data, warmly, with total confidence.
- `exaggeration` moderate to high. {Penny} is expressive. That is the horror.

## Revision Notes

- 2026-08-15: Initial file. Built from the {Penny} sections of
  `tech_fortuna_ai_personalities.md` and `tech_fortuna_ai_systems.md`,
  `char_penny_ai.md`, and the Ch16 message in `draft_ch16_ten_good_days.md`.
