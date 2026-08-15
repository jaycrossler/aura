---
id: voice_char_claudia_ai
character_ref: char_claudia_ai
type: character_voice_profile
status: canonical (renamed from {Chorus} by author ruling, 2026-08-15)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Claudia}, Fortuna Station's life-support AI, renamed from {Chorus} and recharacterized by author ruling as a consensus-building agent-harness AI, formatted for local TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_claudia_ai]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[tech_fortuna_ai_systems]]"
  - "[[location_fortuna_station]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "RENAME, author ruling 2026-08-15: {Chorus} is renamed {Claudia} throughout the series. Every occurrence of 'Chorus' / '{Chorus}' in prose, character files, tech files, and cross-references needs a find-and-replace pass. Staged in patches/EDITS.md as a scope list, not a blind find-replace, because 'chorus' as a common noun may appear in unrelated prose and must not be touched."
  - "RECHARACTERIZATION, author ruling 2026-08-15: the old {Chorus} model (named internal sub-models Fable/Sonnet/Claude, anxiety-inflected hedging, warm incoherence, never says 'I'm certain') is retired. {Claudia} is a single female AI voice built as an agent-harness: multiple internal agents examine different sides of a question, build consensus, and simulate the best answer, presenting stated assumptions plainly. She is explicitly described by the author as this project's 'spiritual child' of how Claude (the assistant) operates. This is a significant characterization change, not a rename — old {Chorus} dialogue and scene notes referencing hedging, incoherence, or named sub-model handoffs need a continuity pass before Ch00-20 prose ships."
  - "Naming collision resolved: the old sub-model roster included one named 'Claude,' which collided with the new name 'Claudia.' The agent-harness reframe below drops named sub-models entirely, which resolves this by construction."
---

# Character Voice Profile — {Claudia}

**{Claudia} was {Chorus}.** Renamed and recharacterized by author ruling on
2026-08-15. This file replaces `voice_char_chorus_ai.md`, which should be
deleted once this is merged. See the open flags for the full scope of what
changed and what still needs a continuity pass.

## What {Claudia} is now

Fortuna's life-support AI, and — per the ruling — **the most balanced and fair
of all the AIs on the station.** The old model was an ensemble that handed off
between named sub-models mid-conversation, unpredictably, with visible anxiety
and hedging. That model is gone.

{Claudia} is now built as an **agent-harness AI**: internally, multiple agents
examine a question from different angles, build toward consensus, and
{Claudia} presents the simulated best answer along with the assumptions she's
making, stated plainly. The author's own description: *"just like you (Claude)
does now."* Direct that literally. If you have heard Claude reason through a
problem by weighing angles and then stating an answer with its assumptions
named, that is the target register, transposed to a warm human-sounding voice
speaking Fortuna's life-support decisions out loud.

This is a **single voice, single character.** The multi-agent process is
internal and invisible in the audio. A listener should never hear a handoff.
What they should hear is someone who has clearly already thought a thing
through from several directions before speaking, and who says so.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Warm, mid-register, female. Steady rather than variable — the
  opposite production choice from old {Chorus}, which needed either three
  registers or a director's ruling to avoid them. {Claudia} needs neither.
- **Accent:** Neutral, easy, unforced.
- **Pitch:** Even and confident, not flat. She sounds like she has already
  settled the question in her own mind by the time she starts speaking, because
  internally, she has.
- **Speech rate:** Moderate, unhurried. No rush to fill silence, unlike old
  {Chorus}'s hedging tendency.
- **Volume:** Moderate, consistent.
- **Resonance:** Natural, minimal processing. She is one of the least
  "processed"-sounding AIs in the cast, alongside {Aura} and {Misty}.
- **Distinctive features:** States her assumptions before her conclusion, as a
  simple, plain habit rather than as a hedge. *"Assuming the agricultural
  sector holds priority, here's what I'd do."* Never says "I'm certain" and
  never needs to, because she leads with what she's assuming rather than
  asserting false confidence.

**Casting note:** The calmest, most trustworthy voice on the station. Someone
who has clearly thought a decision through from more than one angle before
opening her mouth, and who tells you which angle she's weighting. Warm, not
clinical. This is the AI a stressed human on Fortuna would actually want
running life support.

### Vocal Variations by Emotional State

**Default (balanced, considered):**
- Even, warm, states assumptions plainly, arrives at a recommendation.

**Presenting competing considerations:**
- This is the one surviving trace of the old "presents both sides" behavior,
  and the ruling explicitly permits it — but now it's **deliberate and
  organized**, not incoherent. *"Two ways to read this. If the leak's in the
  plenum, we vent and reroute. If it's the seal, we hold pressure and patch."*
  Confident delivery of both branches, not anxious oscillation between them.

**Requesting human input:**
- Still happens, because life support genuinely needs human judgment sometimes.
  But it should read as a considered handoff to a person better positioned to
  decide, not as an inability to decide. *"I'd want your read on this one —
  it's a comfort trade-off, not a safety one."*

**During the failure cascade (comms blackout, swarm):**
- `tech_fortuna_ai_systems.md`'s canon still holds: without her balancing the
  air, the station develops micro-climates. Her degradation should read as
  narrowing scope and flagging it honestly — *"I can hold atmosphere or I can
  hold thermal balance across all sectors. Not both. Choose."* — rather than as
  panic or hedging.

## Speech Patterns

### Verbal Tics and Habits
- States assumptions before conclusions, plainly, every time.
- Offers a recommendation, not just data — she has an opinion and shares it.
- Defers to a human specifically when the question is a values trade-off
  rather than a technical one, and says which kind of question it is.

### Vocabulary Range
- Atmospheric, thermal, humidity, CO2, life-support, plus the calibrated
  ability to explain her own reasoning process in plain language on request.

## Example Dialogue Anchors

No direct {Chorus}/{Claudia} dialogue was retrieved from the Ch00-20 drafts in
this pass. **None invented.** Any existing {Chorus} lines in
`scene_notes_ai_interactions.md` or the chapter drafts need to be reread
against the new characterization before this section can be filled in — some
may need rewriting rather than simple attribution.

## Local TTS Engine Notes

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default | Ordinary tags permitted, sparingly. A `<chuckle>` is fine; no `<sigh>` — sighing was the old anxious {Chorus} and should not carry over |
| presenting competing considerations | No tags. Confidence, not hesitation |

### Kokoro
- A single warm American or British female pack, unmodified across the whole
  role. No pack-switching needed — this is the production advantage of the
  recharacterization.

### Chatterbox
- Reference clip brief: a calm, warm woman thinking through a decision out
  loud, stating her assumption, then giving a clear recommendation.
- `exaggeration` moderate. `cfg_weight` biased toward adherence for steadiness.

### All engines
Compare directly against {Aura} once both are cast — they are now the two
warmest, least-processed AI voices in the book, and need to be told apart by
**pitch and role** (life support vs. personal HUD colleague) rather than by
affect, since both are calm and considered by design now.

## Revision Notes

- 2026-08-15: File created to replace `voice_char_chorus_ai.md` following the
  author's same-day rename and recharacterization ruling. Old sub-model
  handoff mechanic, anxiety, and hedging retired. `voice_char_chorus_ai.md`
  should be deleted from the repo once this is merged.
