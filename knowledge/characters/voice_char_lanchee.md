---
id: voice_char_lanchee
character_ref: char_lanchee
type: character_voice_profile
status: detailed (drafted from Ch04-07)
last_updated: 2026-08-12
description: "Vocal and speech pattern profile for Dr. Lanchee, formatted for Orpheus TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_lanchee]]"
  - "[[ship_falcon]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Dr. Lanchee

## Vocal Characteristics

### Audio Profile
- **Voice type:** Light mezzo — precise, controlled, small in volume but never
  quiet in authority
- **Accent:** Filipino-inflected English, understated rather than pronounced
  — clean consonants, careful vowel placement, the accent of someone
  fluent and clinical rather than performative
- **Pitch:** Medium, very level — she does not use pitch to signal emotion,
  she uses word choice and pacing
- **Speech rate:** Measured, deliberate — the pace of someone reading a chart
  aloud even when she isn't
- **Volume:** Low-moderate; she has never needed volume to be heard clearly
- **Resonance:** Head/mask resonance, light — nothing booming or chesty
- **Distinctive features:** Clipped, complete clinical sentences that read as
  a parts list even when she's furious; she "stops softening" a statement
  rather than escalating it when angry

**Casting note:** Precise, controlled, clinical female voice with a light,
understated Filipino accent — think a physician dictating a chart, applied to
every register including anger. Avoid any reading that adds warmth through
pitch; her warmth (rare, with Siren, in later chapters) comes through content,
not tone.

### Vocal Variations by Emotional State

**Default (professional/clinical):**
- Flat, precise, unhurried
- States findings as findings: *"Dehydration. Sleep deficit. Stress
  response."* — a diagnosis delivered like a parts list

**Controlled anger (Ch04, post-crisis):**
- Volume does not rise — "she did not raise her voice. She simply stopped
  softening it."
- Sentences lengthen slightly and stack facts in sequence, building a case
  rather than venting
- Sample: *"You did the mass model twice and then vented cryogenic propellant
  into a compartment adjacent to my medical stores, my home, and me,
  personally, at four in the morning, with no warning that I could act on."*

**Dry deadpan (recurring):**
- Delivered completely flat, no vocal wink — the humor is entirely in the
  content, not the delivery
- Sample: *"I can only write a prescription for two of those."*

**Guarded concern (Ch06, "you're jumpy"):**
- Slightly slower pace, a longer pause before the actual question
- Doesn't push when deflected — drops the subject cleanly rather than
  pressing, which itself should read as a form of care in the performance

## Speech Patterns

### Verbal Tics and Habits
- Answers questions with the minimum necessary information, then stops
- Rarely uses a patient's name in direct address — refers to symptoms and
  facts, not the person, even while treating them personally
- Never explains her own reactions or feelings — the listener has to infer
  them from what she says and doesn't say

### Vocabulary Range
- **Technical/medical:** Fluent, exact, unglossed — she does not simplify
  medical terminology for a layperson unless directly asked
- **Emotional:** Almost none — see Maureen for a similar pattern, though
  Lanchee's silences read more clinical than commanding
- **Casual:** Very limited — even her jokes are structured like diagnoses

### Relationship-Specific Speech

**With Jace (patient/coworker):** Clinical, briefly cutting when he's put her
at risk, otherwise economical and slightly protective without ever naming it
as such.

**With Siren (off-page-adjacent):** No direct dialogue example yet — the
character file notes she tolerates Siren sleeping across her feet for hours
without objection; a director should treat any future scene here as the
warmest register she has, even if the words themselves stay clinical.

## Internal Monologue Style
Not a POV character in Ch00-07 — no internal monologue sample available yet.

## Example Dialogue Anchors

- *"Excellent medical response."* (dry, to Jace's body failing to notify him it was in crisis)
- *"Dehydration. Sleep deficit. Stress response."*
- *"You do understand my clinic sits two berths down from where you decided to detonate a manifold."*
- *"You did the mass model twice and then vented cryogenic propellant into a compartment adjacent to my medical stores, my home, and me, personally, at four in the morning, with no warning that I could act on."*
- *"It explains enough to prescribe water, rest, and better judgment. I can only write a prescription for two of those."*
- *"You're jumpy. More than blood loss explains."*
- *"You'd tell me if something strange was going on aboard this ship. Wouldn't you."* (Ch06 — not quite a question; delivered flat, almost resigned to the answer already)

## Speech-Affecting Conditions

- **Treating a patient mid-procedure (Ch06 stitches):** Voice stays level even
  while hands are occupied — no strain or distraction audible; this is
  established as professional habit, not effort
- **Early Will manifestation (unflagged in prose — diagnostic intuition
  sharpening):** No vocal change specified yet; per the character file this
  should NOT be voiced as anything unusual — she attributes it internally to
  rest, and the performance should give the listener zero signal that
  anything is off

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| `dry` / `clinical` (default) | No inline tags |
| `controlled anger` | No inline tags — the escalation is entirely lexical (longer, more specific accusatory clauses), never vocalized as a sigh or groan |
| `guarded concern` | A single `<sigh>` is acceptable immediately before *"You'd tell me if something strange was going on aboard this ship"* if the director wants one audible beat of held-back worry — optional, not required |
| `dry deadpan humor` | No inline tags — never a `<chuckle>`; the joke should land completely dry |

**Casting description for base-voice matching:** Precise, light-mid register
female voice with understated Filipino-accented English, minimal warmth
markers, very even pacing. Should sound equally comfortable reading a chart
and delivering a rebuke — same voice, same control, different content.

## Revision Notes

- 2026-08-12: Initial voice profile, built from `char_lanchee.md` and dialogue
  in `draft_ch04_morning_after_debrief_v2.md`, `draft_ch06_the_spire.md`, and
  `draft_ch07_arrival_day.md`. No prior voice_char file existed for this
  character.
