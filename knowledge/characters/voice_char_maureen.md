---
id: voice_char_maureen
character_ref: char_maureen
type: character_voice_profile
status: detailed (drafted from Ch01-07)
last_updated: 2026-08-12
description: "Vocal and speech pattern profile for Captain Maureen, formatted for Orpheus TTS audiobook generation."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_maureen]]"
  - "[[ship_falcon]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Captain Maureen

## Vocal Characteristics

### Audio Profile
- **Voice type:** Alto — low-mid register, weathered, no softness carried in the tone by default
- **Accent:** General American with a flattened, worked-in quality — the accent of someone who has spent decades talking over engine noise and across comm lag, not a regional marker
- **Pitch:** Low-mid, very stable — rarely rises regardless of subject matter
- **Speech rate:** Measured, unhurried, but not slow — she says exactly as many words as the situation requires and stops
- **Volume:** Moderate-low; she has never needed to raise her voice to be obeyed
- **Resonance:** Chest voice, minimal brightness
- **Distinctive features:** Sentences often end on a flat, declarative drop rather than trailing off; she rarely uses contractions when delivering a judgment ("Your seal work held" not "Your seal work's held")

**Casting note:** An older, low-register female voice with almost no vocal fry
and no warmth-signaling upward lilt at sentence ends — the opposite of a
customer-service register. Think a ship captain who has said everything she's
about to say many times before and finds no reason to perform it.

### Vocal Variations by Emotional State

**Default (command mode):**
- Flat affect, complete sentences, no filler words
- Approval and disapproval sound almost identical in pitch — the content
  carries the judgment, not the delivery

**Grudging warmth (rare — Screwdriver, Siren, occasionally Jace):**
- Same flat register, but sentence length shortens further and there's a
  half-beat pause before the line, as if she considered not saying it
- This is Maureen's version of tenderness — do not brighten the pitch to
  signal it; the softening is entirely in content and timing, not tone

**Anger (the departure-burn cargo dispute, Ch01):**
- Volume does not rise; pace slows slightly and consonants get harder
- Longer pauses between clauses — she is choosing not to say the more
  cutting version of the sentence

**Measurement-praise (the closest she comes to a compliment, Ch07):**
- Delivered exactly like a status report: *"Your seal work held. All of it.
  Even the corner anchors you ran hot."* No vocal signal that this is meant
  warmly — the warmth is legible only in the fact that she said it at all

## Speech Patterns

### Verbal Tics and Habits
- States facts, then stops — she does not append qualifiers or soften a
  statement after delivering it
- Almost never asks questions she doesn't need answered; conversational
  small talk is not in her register at all
- Refers to ship problems in exact technical terms, never approximations

### Vocabulary Range
- **Technical:** Precise and fluent — seal tolerances, mass models, manifold
  ratings, delta-v; she uses correct terminology without translating it down
  for a listener
- **Emotional:** Almost nonexistent as direct vocabulary — emotion is
  expressed through what she chooses to say and what she leaves out, not
  through emotional words themselves
- **Casual:** Minimal; even her few lighter moments are dry rather than loose

### Relationship-Specific Speech

**With Jace:** Businesslike throughout, one measurement-compliment as
farewell. Sample: *"Your seal work held. All of it. Even the corner anchors
you ran hot."*

**With crew generally (departure burn, Ch01):** Blunt about frustration —
blames Origin's fixed launch schedule openly rather than softening it for
morale. Sample register: stating the Chinese mining crew's withdrawal and the
resulting filler-cargo decision as a plain grievance, not a rallying speech.

**With animals (off-page confirmed via Siren):** The one place her guard is
known to drop — she secretly feeds Siren treats. No on-page dialogue example
yet; flag for future scenes.

## Internal Monologue Style
Not a POV character in Ch00-07 — no internal monologue sample available yet.

## Example Dialogue Anchors

- *"Your seal work held. All of it. Even the corner anchors you ran hot."* (Ch07, farewell)
- *(paraphrased, departure burn)* a flat, specific account of why the *Falcon* is departing with money-losing filler cargo, blaming Origin's fixed schedule rather than the withdrawn Chinese mining contract itself (Ch01)
- *(implied, Ch04 "tell me not to and I won't" beat)* — her silence itself is the dialogue: Jace explicitly gives her the chance to countermand his risky repair plan, and she says nothing, which the text treats as a deliberate, legible choice rather than an absence

## Speech-Affecting Conditions

- **Near retirement / husband Patrick recovering on Mars:** No on-page
  softening confirmed yet, but her established motivation (getting out, getting
  back to Patrick) is worth keeping in mind for a director — if a later scene
  touches this directly, expect the flat register to crack slightly, briefly,
  and then reassert
- **Over ship comms/announcements:** No distinct processed quality established
  — she speaks to crew directly, not through the majordomo

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| `flat` / `command` (default) | No inline tags — flat, unadorned delivery is the point |
| `grudging warmth` | No inline tags; convey via a beat of silence in the audio direction (pause marker), not a vocalized tag |
| `controlled anger` | No inline tags — do not use `<sigh>` or `<groan>` here; her anger is legible through word choice and pacing alone, never through added vocalization |
| `measurement-praise` | No inline tags — this is the one moment warmth shows, and it should still be under-vocalized, not sweetened |

**Casting description for base-voice matching:** Low-register older female
voice, minimal pitch variation, no upward lilt at clause ends, unhurried but
not slow. Closest fit among common pretrained speaker sets would be whichever
base voice reads as most neutral/authoritative rather than warm or bright —
avoid any speaker whose default includes a smiling or friendly quality, since
Maureen's baseline has neither.

## Revision Notes

- 2026-08-12: Initial voice profile, built from `char_maureen.md` and dialogue
  in `draft_ch01_departure_and_rounds_v2.md`, `draft_ch03_plumbing_crisis_v2.md`,
  and `draft_ch07_arrival_day.md`. No prior voice_char file existed for this
  character.
