---
id: voice_char_sister_artemis
character_ref: char_sister_artemis
type: character_voice_profile
status: detailed (drafted from Ch01, Ch05)
last_updated: 2026-08-12
description: "Vocal and speech pattern profile for Artemis Grant, formatted for Orpheus TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_sister_artemis]]"
  - "[[char_jace_apollo]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Artemis Grant

## Vocal Characteristics

### Audio Profile
- **Voice type:** Alto — warm but toughened, a voice that's spent years
  talking over industrial noise and through comm lag
- **Accent:** General American, Virginia origin like Jace's but worn down
  further by years in the belt — less regional softness than her brother's
- **Pitch:** Medium-low, animated within that range rather than rising into a
  higher register even when excited
- **Speech rate:** Quick, confident, comfortable interrupting herself
- **Volume:** Moderate-high — a voice used to being heard over equipment
- **Resonance:** Chest-forward, some rasp/texture from wear, not delicacy
- **Distinctive features:** A "crooked smile" is explicitly described as
  audible in her voice — a slight asymmetry/wryness in delivery that arrives
  a half-beat before the rest of an emotional reaction; self-interrupts when
  she gets close to saying something classified or personal she doesn't
  intend to finish

**Casting note:** A capable, warm-but-weathered woman's voice with real
texture — not polished or corporate. Should sound like someone who is
delighted to be talking to her brother and also permanently, slightly,
professionally guarded, both at once.

### Vocal Variations by Emotional State

**Default (warm/teasing, Ch01, Ch05 calls):**
- Quick, affectionate ribbing delivered completely deadpan before breaking
  into open warmth
- Sample: *"There he is... Learning Mode himself."*

**Self-interrupting (approaching classified/personal territory):**
- Trails into a redirect rather than a trailing-off silence — she catches
  herself and pivots, audibly, rather than letting the sentence just die
- Sample: *"Some of our ships have the biggest engines in the belt now —
  actually, don't worry about that."*

**The unsaid thing (Ch05, "closest we've been in six years"):**
- Described in-text as her face "doing the complicated thing again, all the
  way through this time" — vocally this should land as a brief drop in pace
  and a slight thinning of the usual confidence, immediately before the
  comms window cuts her off. Not tearful — just momentarily unguarded.

**Delivering hard news gently (the missing-girl mention, Ch05):**
- Noticeably softer and more careful than her default register — she is
  visibly relieved Jace already knows, and the relief should be audible as a
  slight loosening after the first exchange confirms it, not before

## Speech Patterns

### Verbal Tics and Habits
- Teases first, means it second — nearly every warm statement arrives wrapped
  in a joke or a tough-love jab
- Self-censors mid-sentence about Metis's classified work, always pivoting
  rather than just stopping
- Uses "little brother" as a direct address at emotionally loaded moments,
  not casually

### Vocabulary Range
- **Technical:** Fluent in belt/shipyard terms, though she deliberately keeps
  Metis specifics vague per operational security
- **Emotional:** More available than most of the transit-era cast — she'll
  name feelings more directly than Jace will, even if she still wraps them
  in humor first
- **Casual:** Warm, quick, sibling-shorthand-heavy

### Relationship-Specific Speech

**With Jace:** The warmest, most teasing register in the cast so far — real
affection delivered almost entirely through jokes and jabs, with the
sincerity showing through in word choice ("little brother," specific
promises) rather than tone.

## Internal Monologue Style
Not a POV character in Ch00-07 — no internal monologue sample available yet.
(Existing character file notes she is a candidate for POV chapters in later
books — flag for a future voice-profile expansion if that happens.)

## Example Dialogue Anchors

- *"There he is... Learning Mode himself."*
- *"We're building things you wouldn't believe. Some of our ships have the
  biggest engines in the belt now — actually, don't worry about that."*
- *"You couldn't visit anyway — Metis is closed to civilians, it's all
  shipyard and clearances, they don't even let me off-shift without a badge
  check."*
- *"That's not a distance anymore. That's a coincidence."*
- *"Nick tell you about the missing girl yet?"* ... *"Good. Saves me being
  the bad-news sister twice in one call."*
- *"Famous last words from Learning Mode."*
- *"Closest we've been in six years."*
- *(established, Ch01 birthday call)* *"Eat something that was alive this
  morning. That is an order."*
- *(callback, Ch05)* *"When I said 'eat something that was alive this
  morning,' this is not the delivery method I had in mind."*

## Speech-Affecting Conditions

- **Comm lag:** Calls are explicitly noted as landing at low, near-real-time
  lag by this point in the story (down to ~2 seconds) — no delay-related
  vocal artifacts needed, but the call windows are hard-timed (nine seconds
  visible countdown in Ch05) and cut off mid-sentence; the performance should
  end lines cleanly cut rather than trailing off naturally when the window
  closes
- **Fresh scar across two knuckles (Ch05, visual only):** No vocal
  implication, noted here only for cross-reference to the visual profile

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| `default warmth/teasing` | No inline tags for most lines |
| genuine laugh (Ch05 opening) | `<laugh>` acceptable before *"There he is"* |
| self-interrupting pivot | No inline tags — the pivot is achieved by cutting the sentence and changing subject, not by a vocalized sound |
| the unsaid thing / "six years" | No inline tags — keep this beat entirely in pacing and word choice, not a `<sigh>`, to preserve the "doing the complicated thing" ambiguity the prose describes |
| relief at not having to deliver the news herself | A single `<sigh>` is appropriate immediately after *"Good. Saves me being the bad-news sister twice in one call"* |

**Casting description for base-voice matching:** A warm, weathered adult
woman's voice with real lower-register texture — avoid anything polished or
young-sounding; she should read as older and more worn than Jace despite
being family, consistent with years of harder physical work and higher
exposure than his transit-cushioned four months.

## Revision Notes

- 2026-08-12: Initial voice profile, built from `char_sister_artemis.md` and
  dialogue in `draft_ch01_departure_and_rounds_v2.md` (birthday call) and
  `draft_ch05_learning_mode_v2.md` (Artemis Call/canister scene). No prior
  voice_char file existed for this character.
