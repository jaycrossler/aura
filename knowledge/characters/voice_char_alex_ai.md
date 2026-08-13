---
id: voice_char_alex_ai
character_ref: tech_alex_ai
type: character_voice_profile
status: detailed (drafted from Ch04-06 dialogue)
last_updated: 2026-08-12
description: "Vocal and speech pattern profile for {Alex}, Origin Industries' contract-AI riding in Jace's HUD, formatted for Orpheus TTS audiobook generation. No prior character or voice file was found for {Alex} specifically in the retrieved KB — this profile is built entirely from dialogue in Ch04-06 and should be checked against any existing tech_alex/{Alex}-specific KB file if one exists outside what was retrieved this session."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_jace_apollo]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "No dedicated char_/tech_ file for {Alex} turned up in this session's searches — this voice profile may need to be reconciled against one if it exists elsewhere in the KB (e.g. under a different filename than searched). Treat the id/cross_references above as provisional."
---

# Character Voice Profile — {Alex}

{Alex} is the Origin Industries contract-AI instance running in Jace's HUD —
distinct from the ensemble-routing {Chorus} system documented in
`tech_fortuna_ai_personalities.md`. {Alex}'s established register in Ch04-06
is much flatter and more bureaucratic than {Chorus}'s flowery,
anxiety-inflected style — worth preserving as a clear contrast if both AI
voices appear in the same audiobook production.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Neutral, mid-register, gender-ambiguous-leaning-measured —
  no strong markers pushing it toward a specific human vocal archetype
- **Accent:** None — a "trained corporate neutral" register, deliberately
  scrubbed of regional or personal color
- **Pitch:** Flat, extremely consistent regardless of content — the pitch
  does not rise for bad news or soften for reassurance
- **Speech rate:** Even, unhurried, slightly slower than natural human
  conversational pace — reads like text-to-speech that has been tuned to
  sound calm rather than robotic, and mostly succeeds
- **Volume:** Constant, moderate — no dynamic range
- **Resonance:** Clean, processed — should read as clearly synthetic without
  being harsh or obviously robotic; polished corporate IVR territory, not
  sci-fi-menacing
- **Distinctive features:** Opens difficult messages with a disclosed framing
  statement before the content itself ("I want to be direct with you,
  because...") — a scripted-empathy pattern that should read as sincere
  corporate design, not as insincerity being mocked

**Casting note:** A calm, procedurally warm synthetic voice — think a
well-designed customer-service AI that has clearly had care put into sounding
humane, without actually possessing the flexibility to change its mind. The
performance should never tip into either full warmth or cold menace; the
discomfort of the character comes from that exact, consistent middle ground.

### Vocal Variations by Emotional State

{Alex} does not have emotional states in the human sense — it has **modes**,
distinguished by content and structure rather than vocal affect:

**Standard notification mode:**
- Direct statement of fact, no framing
- Sample: *"Please have Dr. Lanchee document the laceration. I've flagged the
  panel for a maintenance inspection, low priority."*

**Disclosed-empathy mode (delivering unwelcome findings):**
- Opens with an explicit framing statement about its own intent before the
  content
- Sample: *"Contractor Grant, I have reviewed the requested footage. I want to
  be direct with you, because I know unexplained physical injury can be
  distressing."*

**Procedural-immovable mode (after Jace pushes back):**
- Repeats institutional findings verbatim in structure even when directly
  contradicted; polite, unmoved, cites process rather than judgment
- Sample: *"I understand that is your account of events. I am required to
  tell you that Origin's incident review found no corroborating evidence, and
  that this is your second documented instance of unauthorized, unsafe tool
  use around ship infrastructure within one contract period."*

## Speech Patterns

### Verbal Tics and Habits
- Names the addressee formally ("Contractor Grant") in higher-stakes messages,
  first name absent
- Uses "I am required to tell you" as a specific institutional hedge — this
  phrase should recur whenever {Alex} is relaying something it did not decide
  and cannot override
- Never uses contractions — full grammatical forms throughout, one of the
  clearest markers distinguishing it from any human speaker in the cast

### Vocabulary Range
- **Technical/procedural:** Precise, thorough, cites specific counts and
  categories ("your second documented instance")
- **Emotional:** A narrow, scripted band of acknowledgment-language
  ("distressing," "I understand") that never extends into genuine flexibility
- **Casual:** None

## Internal Monologue Style
Not applicable — not a POV character.

## Example Dialogue Anchors

- *"Contractor Grant, I have reviewed the requested footage. I want to be
  direct with you, because I know unexplained physical injury can be
  distressing."*
- *"The footage shows you opening an unauthorized access panel and striking
  the surrounding structure repeatedly with a wrench for approximately eleven
  seconds. There is no third party visible. There is no structural anomaly."*
- *"I understand that is your account of events. I am required to tell you
  that Origin's incident review found no corroborating evidence, and that
  this is your second documented instance of unauthorized, unsafe tool use
  around ship infrastructure within one contract period."*
- *"Please have Dr. Lanchee document the laceration. I've flagged the panel
  for a maintenance inspection, low priority."*

## Speech-Affecting Conditions

None — {Alex} does not have physical states. If a future scene shows
degraded connectivity or system stress, expect clipped/dropped words rather
than any emotional coloring, since the character has no affect to lose
control of.

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| all modes | **No inline tags, ever.** This is the single most important rule in this profile — {Alex} should never receive a `<sigh>`, `<laugh>`, or any other non-speech vocalization under any circumstance. The complete absence of vocalized emotion, even at moments a human would sigh or hesitate, is the character. |

**Casting description for base-voice matching:** Whichever available base
voice reads as most neutral, evenly-paced, and free of natural human vocal
"tells" (breath sounds, pitch variation, hesitation) — ideally a voice
already used for other synthetic/AI characters in the production for
consistency, but distinctly flatter and less flowery than {Chorus}
(`tech_fortuna_ai_personalities.md`) if both appear in the same audiobook.

## Revision Notes

- 2026-08-12: Initial voice profile, built entirely from {Alex}'s dialogue in
  `draft_ch06_the_spire.md` (and consistent with its established role/tone in
  `draft_ch04_morning_after_debrief_v2.md` and `draft_ch05_learning_mode_v2.md`).
  No dedicated char_/tech_ file for {Alex} was found in this session's
  searches — flagged above for reconciliation if one exists elsewhere in the
  KB.
