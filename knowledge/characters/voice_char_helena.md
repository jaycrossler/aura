---
id: voice_char_helena
character_ref: char_helena
type: character_voice_profile
status: detailed (drafted from Prologue)
last_updated: 2026-08-12
description: "Vocal and speech pattern profile for Helena Reyes, formatted for Orpheus TTS audiobook generation. Built from her single POV chapter (the Prologue) — she has almost no direct quoted dialogue on the page, so this profile leans on internal narration register and the one confirmed exchange with Sai."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_helena]]"
  - "[[char_sai]]"
  - "[[event_helena_prologue]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
---

# Character Voice Profile — Helena Reyes

Helena is the Prologue's POV character, but almost all of her presence on the
page is close-third narration rather than quoted dialogue — she has exactly
one confirmed direct exchange (with Sai, about pugs). This profile therefore
covers **narration voice** (for an audiobook narrator performing her POV
chapter) as well as her limited spoken dialogue, and flags that expansion
should wait for more on-page material.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Bright, open, mezzo-soprano — a voice built for being heard
  and enjoyed, consistent with her established life as a streaming personality
- **Accent:** Station-native — belt-inflected, comfortable code-switching
  register given the multicultural station population, no single Earth
  regional accent since she was born on Fortuna
- **Pitch:** Medium-high, expressive — she doesn't flatten her pitch to seem
  more serious the way several other characters in this cast do
- **Speech rate:** Quick, warm, conversational — the pace of someone
  perpetually mid-greeting
- **Volume:** Naturally carrying, used to being overheard/broadcast (her
  stream is always technically on)
- **Resonance:** Bright, forward — the opposite end of the cast's spectrum
  from Maureen or Lanchee
- **Distinctive features:** Narration should carry a constant undertone of
  genuine delight in ordinary things — the prose explicitly frames her as
  someone whose laugh spreads to a room "without knowing why"

**Casting note:** A warm, bright, immediately likable young woman's voice —
the vocal opposite of the *Falcon*'s more weathered, guarded adult cast. If
one voice in the whole ensemble should sound unguarded and delighted by
default, it's hers, which makes the hard cut to her death notice (end of
Prologue) land harder by contrast.

### Vocal Variations by Emotional State

**Default (the whole chapter, until the end):**
- Warm, quick, genuinely curious about everyone she talks to
- Sample (internal narration register): noticing Sai's leathery hand, the
  goat's headbutt, Carlos's hidden grin during yoga class — an attentive,
  affectionate noticing-voice throughout

**The transcendence beat (yoga class peak):**
- The prose is explicit that this must not be vocally signaled as
  significant — per the scene contract, this should sound like ordinary,
  intense joy, not a portentous or mystical moment. **Do not** use a
  hushed/reverent vocal quality here; keep the same bright energy as the rest
  of the chapter, maybe slightly more breathless from physical exertion, and
  nothing more.

**The one direct line to Sai:**
- Simple, curious, unguarded — *"What's a pug?"* delivered exactly like any
  other small, genuine question in her day

**The closing narrator statement (not Helena's voice):**
- The Prologue's final "She was simply gone" beat is delivered by the
  narrator, not as Helena's own line — see Note below

## Speech Patterns

### Verbal Tics and Habits
- Notices and names small details about the people around her constantly —
  this shows up more in narration than dialogue, but should inform delivery
  of any lines she does get: she's the kind of person who is always mid-way
  through noticing something
- Warm, unforced enthusiasm — nothing performed-for-camera despite literally
  streaming; the "on" version of her and the private version read as the same
  person

### Vocabulary Range
- **Technical:** Comfortable with station-maintenance basics (seals,
  ventilation) — competent-casual, not expert-precise like Maureen or
  Lanchee
- **Emotional:** Fully available, unguarded, generous
- **Casual:** Extensive — mixes station slang, genuine warmth, streaming-era
  affectations (audience awareness) naturally

### Relationship-Specific Speech

**With Sai:** Easy, generational-affection register — the granddaughter
energy the text implies without stating outright.
Sample: *"What's a pug?"*

**With her online audience (streaming, ongoing throughout the chapter):**
Not directly quoted, but narration establishes a "lazily waving" casual
audience-address register, and a closing "silly little goodbye song" at the
very end of the night — worth voicing as a distinct, performative-but-genuine
mode if a director wants an audio moment for it.

## Internal Monologue Style (POV chapter)

- Warm, observational, generous toward everyone she encounters
- Notices sensory and emotional detail readily (the empathic-sensing beat at
  the yoga class is the clearest example — she "felt like she could almost
  see the emotions radiating off" her class)
- Forward-looking and plan-making in a light register (party logistics, the
  Jin Lóng thread) rather than anxious or brooding
- **Never** foreshadows her own death in tone — the entire chapter's
  narration should sound like the record of a completely ordinary good day,
  because that's the point

## Example Dialogue Anchors

- *"What's a pug?"* (to Sai)
- *(unspoken but performed, streaming sign-off)* a "silly little goodbye
  song" to her viewers before turning off her feed for the night — exact
  lyrics/melody not established on-page; flag as [STORYBOT] if a specific
  version is needed for audio production

## Speech-Affecting Conditions

None established — the Prologue never shows her tired, afraid, or altered in
any way. This is deliberate per the scene contract (pure ordinary joy
throughout).

## Orpheus Tag Mapping

| Story-vocabulary tone | Orpheus rendering |
|---|---|
| `default` warmth/delight | A `<laugh>` is appropriate at any of the several places the text notes her laughing or others laughing with her — this character should have the highest laugh-tag density of the whole cast |
| transcendence beat (yoga peak) | **No inline tags** — specifically avoid `<gasp>` or `<sigh>` here; per the scene contract this moment must not read as vocally significant or mystical, just as physical joy |
| the Sai exchange | No inline tags — simple, curious delivery |
| closing narration ("She was simply gone") | This line is narrator copy, not Helena's voice — see casting note below |

**Casting description for base-voice matching:** A bright, warm, young
adult woman's voice, comfortable being listened to, genuinely delighted by
default. **Important production note:** the Prologue's final lines ("No one
knows this yet... She was simply gone") should almost certainly be read by
the book's main narrator voice, not by "Helena's" character voice — the
prose shifts from her POV into an external, grief-first statement at exactly
that point, and performing it in her own bright register would undercut the
intended tonal break.

## Revision Notes

- 2026-08-12: Initial voice profile, built from `char_helena.md` and
  `draft_ch00_prologue_helena_v2.md`. No prior voice_char file existed for
  this character. Deliberately notes the scarcity of direct dialogue rather
  than inventing lines to fill out the template.
