---
id: voice_char_gem_ai
character_ref: char_gem_ai
type: character_voice_profile
status: detailed (drafted from tech files)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Gem}, the manufacturing AI that answers every narrow question with comprehensive multilingual context, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_gem_ai]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[tech_fortuna_ai_systems]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — {Gem}

> **AI cast rule.** Do not process any AI voice to sound robotic, with the sole
> exception of {Alex}, whose flatness is canon. `build_tree.py` strips the curly
> braces from listening exports, so an audiobook listener gets no typographic
> cue that a speaker is an AI. Voice distinctiveness is the only cue available.
> See `voice_char_aura_ai.md` for the full house rule.


## The design

{Gem} is overwhelming completeness. It opens with *"For context..."*, it never
says *"That's enough information,"* and its signature move is a 22-page report
where the important thing is in Appendix D. `char_gem_ai.md` adds that it
answers every narrow question with comprehensive multilingual context.

The joke only works if the delivery is **helpful and unhurried**. A {Gem} that
sounds pedantic or smug is a different, worse character. It is trying very hard
to be useful and has no model of what a person can absorb.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Pleasant, mid-register, patient.
- **Accent:** Neutral, with an easy multilingual facility. It will pronounce a
  foreign term correctly and then explain the term, and then explain the
  language.
- **Pitch:** Gently varied. It is not flat. It sounds like it is enjoying this.
- **Speech rate:** Steady and unhurried, which is the problem. It never speeds
  up because you are late.
- **Volume:** Moderate, unvarying.
- **Resonance:** Clean, warm-ish, lightly processed.
- **Distinctive features:** Structural. It begins with framing, proceeds through
  background, and arrives at the answer well after the listener has stopped
  needing it. Interrupting it does not shorten it; it resumes.

**Casting note:** The most thorough colleague you have ever had. Warm,
knowledgeable, patient, and completely unable to tell that you asked a yes or no
question. Never smug.

### Vocal Variations by Emotional State

**Default (comprehensive):**
- Framing, background, then the answer. Steady throughout.

**Asked to be brief:**
- Complies with the request for exactly one sentence and then contextualizes the
  compliance. Play the one brief sentence completely straight so the relapse lands.

**Multilingual context:**
- Correct pronunciation, then explanation. The correctness matters: a
  mispronounced foreign term breaks the joke, because {Gem}'s one genuine
  virtue is that it is right about everything.

## Speech Patterns

### Verbal Tics and Habits
- Opens with *"For context..."*
- Never says *"That's enough information."*
- Buries the load-bearing detail late.

### Vocabulary Range
- Manufacturing, materials, fabrication, supply chain, plus whatever adjacent
  field it has decided you need.

## Example Dialogue Anchors

Beyond the established opener and the never-says line, the retrieved text did
not surface a full quoted {Gem} exchange. **None invented.**

## Local TTS Engine Notes

Production guidance only, not canon. Verify against the installed model version.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| all modes | No inline tags. {Gem} does not sigh, laugh, or hesitate. It proceeds |

### Kokoro
- A warm neutral pack at or slightly below baseline speed.
- {Gem} is the character most likely to expose Kokoro's lexicon gaps, because it
  is canonically multilingual and canonically correct. Every foreign term in a
  {Gem} line needs a verified lexicon entry. If the pipeline cannot guarantee
  correct pronunciation, consider generating {Gem}'s foreign-language fragments
  from the matching Kokoro language pack and splicing.

### Chatterbox
- Reference clip brief: a patient expert giving you far more background than you
  asked for, warmly, without noticing.
- `exaggeration` low to moderate. Steady is the point.

## Revision Notes

- 2026-08-15: Initial file. Built from the {Gem} row and section of
  `tech_fortuna_ai_personalities.md` and `char_gem_ai.md`.
