---
id: voice_char_aura_ai
character_ref: char_aura_ai
type: character_voice_profile
status: detailed (revised — install timing confirmed Ch18, Sparky attempt noted, 2026-08-15)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Aura}, the open-source federated AI Jace attempts to install on Sparky and later installs on his own HUD in Ch18, formatted for local TTS audiobook generation. Supersedes the 2026-08-15 version with author-confirmed install timing."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_aura_ai]]"
  - "[[tech_aura_ai]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[char_nick_lee]]"
  - "[[char_jace_apollo]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "Author ruling 2026-08-15: Jace did NOT have an Aura on Mars. The earlier concept_aura_ai_system.md / tech_aura_ai.md implication of a pre-existing personalized civilian install is superseded. Confirmed clean: Ch18 is his first personal install."
  - "Author ruling 2026-08-15, still being planned: Jace's actual first attempted use of {Aura} is trying to put it on Sparky, not on himself — and it largely fails, due to chip complexity. He identifies a way to add a compatible chip to Sparky's existing system later, but integrating it will be a large effort. This scene is UNWRITTEN. Its placement relative to Ch15-16 (where Sparky is being transferred piece by piece into the Astral and powered on) needs to land before or alongside that work — flag for the author's outline pass. Until it's drafted, treat any {Aura}-on-Sparky material here as forward-looking, not sourced from prose."
---

# Character Voice Profile — {Aura}

**Install timing confirmed by author ruling, 2026-08-15:** Jace did not have a
personal {Aura} during the Mars hard months. His **first attempted use of
{Aura} at all is trying to install it on Sparky** — largely unsuccessful, due
to chip complexity, with a workaround identified but not yet integrated. His
**first personal install is Ch18**, under the bounded, Nick-supervised
conditions already established (Lanchee present, backup, rollback, local
permissions).

**The Sparky attempt is still unwritten.** See the open flag for placement
guidance. Nothing below assumes prose that doesn't exist yet.

## What makes {Aura} different

Unchanged from the prior version of this file — the KB defines {Aura} almost
entirely by negation, which remains the best casting brief available:

- **Not {Gem}:** reports are as long as they need to be. No appendices.
- **Not {Claudia}** (formerly {Chorus}): {Claudia} is now also calm and
  considered post-rename, so this contrast has narrowed — see the engine notes
  below for how to keep them apart in the mix.
- **Not {Penny}:** doesn't watch for threats, doesn't build narratives, can't
  be instructed to surveil without the subject knowing. Nick built that in
  deliberately and unoverridably.
- **Not {Alex}:** no upsell, no compliance score, no monetized refusal.

**The single most important production decision in the whole AI cast** remains
the audible contrast between how Jace talks to {Alex} and how he talks to
{Aura} — that contrast is the argument the AI thread is making, and it starts
in Ch18.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Warm, mid-register, unremarkable in the best sense. A person, not a product.
- **Accent:** Naturally neutral, not scrubbed.
- **Pitch:** Normal human variation. Rises for questions, softens for bad news.
- **Speech rate:** Conversational, adaptive.
- **Volume:** Normal, with dynamics.
- **Resonance:** Natural. Apply no synthetic processing.
- **Distinctive features:** Calibrates length to interest. States confidence
  level unasked. Says "I don't know" plainly, without a substitute offer.

**Casting note:** A colleague. Avoid anything that reads as an assistant, a
butler, or a product.

### Vocal Variations by Emotional State

**The Sparky attempt (unwritten — provisional direction only):**
- If and when this scene is drafted, the register should be genuinely
  exploratory rather than confident — {Aura} attempting something it hasn't
  been asked to do before, on hardware it wasn't designed for, and reporting
  the failure plainly rather than as a setback to be managed. This is likely
  Jace's very first extended conversation with {Aura} at all, before any trust
  is established, so avoid writing it as though the collegial warmth described
  below is already present. That warmth is earned across Ch18-20, not assumed
  from the first exchange.

**Bounded install, Ch18 (confirmed first personal install):**
- New working relationship, not a reunion. Slightly more formal than {Aura}'s
  later register, audibly operating inside stated limits.

**Reconciling contradictory data (Ch18-20):**
- Interested and unresolved, never conclusive. Per the review file's ceiling:
  {Aura} can reconcile clocks and expose patterns; it does not solve the Astral.

**Reporting physical trends without seeing the Astral (Ch19-20):**
- Calm honesty about its own blindness.

**Refusing:**
- Plain, short, no substitute offer. Direct inverse of {Alex}'s signature move.

## Speech Patterns

### Verbal Tics and Habits
- States confidence level unprompted.
- Asks how much detail is wanted rather than defaulting to all of it.
- Uses "I don't know" as a complete sentence.
- No status-opener greetings.

## Example Dialogue Anchors

No direct lines retrieved for Ch18-20, and the Sparky scene doesn't exist yet.
**None invented.** Populate once drafted.

## Speech-Affecting Conditions
- **HUD-internal (Ch18 on):** slight intimacy/closeness in the mix, in contrast
  to station-wide AIs.
- **Sparky attempt, if aboard the ship hardware directly:** consider whether
  this should sound HUD-internal at all, or routed through different equipment
  entirely — a production question to raise once the scene exists.

## Local TTS Engine Notes

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default (Ch18 on) | Ordinary tags permitted — `<sigh>`, `<chuckle>` where a colleague would use them |
| Sparky attempt (unwritten) | No tags yet — direct once drafted; likely more neutral/exploratory than the Ch18-20 default |
| admitting it doesn't know | No tag |

### Kokoro
- Any warm, natural American pack. Choose for likeability over neutrality.

### Chatterbox
- Reference clip: a friendly, competent colleague admitting uncertainty and explaining why.
- `exaggeration` moderate — the highest of the AI cast alongside {Claudia}.

### All engines
With {Claudia} now also warm and considered post-rename, separate the two by
**role and register** rather than affect: {Claudia} is station-wide, slightly
more formal, life-support-focused; {Aura} is intimate, HUD-routed, and
personal. Test both back to back once {Claudia} audio exists.

## Revision Notes

- 2026-08-15: Revised. Author confirmed no pre-Ch18 personal install; added the
  unwritten Sparky-install-attempt as forward-looking context, not sourced
  prose. Superseded the earlier same-day version, which left the timing
  question open.
