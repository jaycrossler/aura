---
id: voice_char_nick_lee
character_ref: char_nick_lee
type: character_voice_profile
status: detailed (consolidated from char_nick_lee.md + Ch01-07 dialogue)
last_updated: 2026-08-20
description: "Vocal and speech pattern profile for Nick Lee, formatted for Orpheus TTS audiobook generation. Consolidates the voice notes already embedded in char_nick_lee.md into a dedicated, generator-ready file, and adds new dialogue anchors from Ch05-07."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_nick_lee]]"
  - "[[visual_profile_nick_lee]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Nick Lee

This file consolidates voice information already established in
`char_nick_lee.md` and `visual_profile_nick_lee.md` into the dedicated
`voice_char_*` format used by the audiobook pipeline, and adds dialogue
anchors from the in-person meeting and the {Aura} pitch scene (Ch05-07). No
prior dedicated voice_char file existed for Nick — his voice data lived
inline in the character file.

## Vocal Characteristics

### Audio Profile
- **Voice type:** High-pitched, reads younger than his actual age (28) — a
  known, deliberate story point, not a flaw to correct in casting
- **Accent:** Korean accent, present but a **deliberate performance** — leans
  into it with new people, annoying officials, or when amused; drops it
  entirely in technical mode and with trusted people (especially Jace).
  Underneath the performance is a faint Bay Area (San Francisco) inflection
- **Pitch:** High baseline; flattens and drops slightly in technical mode
- **Speech rate:** Fast by default, often running three topics at once;
  precise and controlled in technical mode
- **Volume:** Moderate-high, animated — matches his constant physical motion
  (finger-typing, gesturing)
- **Resonance:** Light, forward placement — nothing chesty or booming
- **Distinctive features:** Brief micro-pause mid-sentence when one of his
  20-30 background AI agents sends an alert — audible as a half-beat hitch
  before he continues, sometimes on an unrelated word

**Casting note:** A young-reading, high-energy male voice capable of a
noticeable register shift — the performed Korean-accent "customer voice"
should sound audibly different from his flat, fast, accent-dropped technical
voice, and both should be different again from his most relaxed
register (with Jace): still fast, but warmer, looser, genuinely funny rather
than performed.

### Vocal Variations by Emotional State

**Default (friendly/fast):**
- Fast, warm, frequently overlapping topics
- Korean-accent performance present, especially with new people

**Technical mode:**
- Accent drops entirely
- Voice flattens, speeds up further, sounds noticeably more senior/competent
- This is the mode he's proudest of and it shows

**Pushed back on / annoyed:**
- Friendliness doesn't vanish, but the padding does
- Goes precise, not loud — firmness reads as speed and exactness, not volume

**With Jace (truest register):**
- Highest laugh rate of any relationship
- Gamer shorthand, fewer complete sentences, more callback humor
- Accent fully dropped

**The Chapter 23 Astral crossing memory:**
- Makes the games joke, then visibly/audibly changes the subject — a
  performance note: the joke should land a beat too fast, like it's
  covering something, and then the topic should not return

## Speech Patterns

### Verbal Tics and Habits
- Constant micro-narration of his own typing/gesturing, sometimes audible as
  muttered fragments
- The agent-alert micro-pause (see above) — a recognizable tell once a
  listener knows to listen for it
- Rarely finishes a sentence in exactly the shape it started — self-interrupts
  to add a parenthetical, then returns to the point

### Vocabulary Range
- **Technical:** Expert-level, fluent, fast — {Aura} architecture, AI systems,
  belt infrastructure
- **Casual/gamer:** Extensive, especially with Jace — shorthand, in-jokes,
  strategy-game vocabulary
- **Emotional:** Present but usually wrapped in a joke first; the real
  statement often comes right after the punchline, delivered quieter

### Relationship-Specific Speech

**With Jace:** See above — truest, fastest, funniest version of him.
Sample: *"THERE it is."* (delighted, to a successful comeback)

**Pitching {Aura} (Ch05):** Slower and more deliberate than his default —
this is a rehearsed pitch, not off-the-cuff banter, and should sound like it.
Sample: *"That's not what I'm talking about, though... I'm not building
that."* / *"You know that skull cap of yours is running at maybe thirty
percent load doing what you've got on it now?"*

**Relaying rumor/news (Ch05, the missing-girl message):** Faster, slightly
compressed, the register of someone passing along something before they've
fully processed it themselves — not performed, not technical-mode either; a
third, more genuine-but-hurried register.

## Internal Monologue Style
Not a POV character in Ch00-07 — no internal monologue sample available yet.

## Example Dialogue Anchors

- *"Your HUD. What are you actually running on the civilian partition?"*
- *"That's not what I'm talking about, though... I'm not building that."*
- *"You know that skull cap of yours is running at maybe thirty percent
  load doing what you've got on it now? The rest just sits there idle."*
- *(text, rumor)* *"hey — kind of a weird one, don't have real details yet...
  everyone on the boards says she's basically station royalty..."*
- *"Okay. Stand up. I need to see this in person."* (first in-person meeting, Ch07)
- *"He's shorter than on the channel."* (of Cerberus)
- *"THERE it is."*
- *"Arrival assessment: you look terrible, your dog is perfect, you're eating
  the debt soup, and the whole station already loves you for the worst
  possible reasons. Welcome to Fortuna."*
- *"You're gonna like it here. Probably. Statistically."*

## Speech-Affecting Conditions

- **In the chair (server room):** No distinct vocal change, but pacing
  slows very slightly once he's settled and working — the frantic energy has
  somewhere to go
- **Mid-agent-alert:** The characteristic micro-pause; resumes exactly where
  he left off, sometimes finishing an unrelated clause first

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| `default` / fast-friendly | No inline tags needed for most lines |
| genuine delight / "THERE it is" | `<laugh>` acceptable immediately before or replacing part of the line — e.g., `<laugh> THERE it is.` |
| the Chapter 23 crossing deflection | `<chuckle>` on the games joke itself, then a hard cut — no tag on the subject change; the silence/topic-drop should do the work |
| technical mode | No inline tags — the flattened, sped-up delivery is achieved through pacing/register selection, not a vocal tag |
| relaying the rumor (Ch05) | No inline tags — this should read hurried and slightly uncertain, not tagged with a sigh or gasp, since he's explicitly passing along secondhand information he hasn't emotionally processed |

**Casting description for base-voice matching:** A younger-reading, high male
voice with real range between a performed accent register, a flattened fast
technical register, and a warm unguarded register with one specific
relationship (Jace). If the base-voice set doesn't include a naturally
high/young-reading option, prefer one with strong pitch flexibility over one
that's simply high by default, since the accent-drop and technical-mode shift
are load-bearing character beats.

## Revision Notes

- 2026-08-12: Initial dedicated voice_char file. Consolidated from the "Voice"
  section already present in `char_nick_lee.md` (2026-07-14) and
  `visual_profile_nick_lee.md`'s Voice Profile table, and extended with new
  dialogue anchors from `draft_ch05_learning_mode_v2.md` and
  `draft_ch07_arrival_day.md`.
