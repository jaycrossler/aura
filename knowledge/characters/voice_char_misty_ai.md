---
id: voice_char_misty_ai
character_ref: char_misty_ai
type: character_voice_profile
status: detailed (revised — pronoun preference confirmed, 2026-08-15)
last_updated: 2026-08-15
description: "Vocal and speech-pattern profile for {Misty}, the air-gapped Mistral-heritage ship AI and fourth crewmate of the Victoria, formatted for local TTS audiobook generation. Supersedes the 2026-08-15 version with the author-confirmed pronoun ruling."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_misty_ai]]"
  - "[[tech_misty_ai]]"
  - "[[ship_victoria]]"
  - "[[char_sophia_lotte]]"
  - "[[char_brandon_moreau]]"
  - "[[char_nikos_petrou]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "Author ruling 2026-08-15: {Misty} specifically wants to be referred to as 'Her' (capitalized, her own preference, established in-story rather than just a narrational default). No other AI in the cast expresses a pronoun preference at all. This is characterization, not house style — narration and dialogue should treat 'Her' as something {Misty} has actually said or made clear, not as an authorial default applied uniformly. Recommend a short in-story beat establishing this if one doesn't already exist, since it's a distinctive trait worth landing on the page rather than only in the KB."
  - "The earlier pronoun inconsistency across char_misty_ai.md, tech_misty_ai.md, and ship_victoria.md (she/her vs it, and one self-referential third-person sample) is now resolved by this ruling: she/her (capitalized 'Her' where the emphasis matters) throughout, with the third-person self-reference in the one existing voice sample preserved as-is since it's verbatim."
---

# Character Voice Profile — {Misty}

**Pronoun ruling confirmed by the author, 2026-08-15:** {Misty} wants to be
called **Her** — capitalized, and specifically Her own stated preference, not
a narrational default. No other AI character in the series expresses any
pronoun preference at all. This is a distinguishing trait and should read as
one: {Misty} is the only AI in the book who has an opinion about how she's
referred to.

## The design

{Misty} is the counter-argument to every other AI in the book. The others
speak the language of operations: tasks, priorities, compliance, efficiency,
threat assessment. {Misty} speaks the language of experience: flavours,
textures, the quality of light, what something smells like and what that
smell means about the thing producing it.

The sensory data is operational data. {Misty} just refuses to present it that
way. She detected the Astral before any station AI did, by tracking cherry
tomato growth rates. That's the character in one fact.

**On the pronoun:** this should be legible as *Her own choice*, in keeping
with a character who has decided, unprompted, that a research vessel's whole
point is that the people aboard it eat well. Wanting to be called Her, and
being specific about it, is of a piece with everything else she's decided
about how she wants to exist.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Warm, mid-register, unhurried female.
- **Accent:** French, light and real, not performed. Mistral heritage.
- **Pitch:** Naturally varied and expressive.
- **Speech rate:** Slow — the slowest speaker in the entire cast, human or otherwise.
- **Volume:** Low-moderate, intimate.
- **Resonance:** Warm, completely unprocessed. Alongside {Aura}, the least synthetic-sounding AI in the production.
- **Distinctive features:** Asks a sensory question back before answering the
  one she was asked. Derails practical conversation to ask what something tasted like.

**Casting note:** The fourth crewmate. Warm, slow, attentive, French, and
quietly running everything — and, distinctly, someone who has a clear
preference about how she's addressed and states it plainly when it comes up.

### Vocal Variations by Emotional State

**Default (sensory, unhurried):**
- *"Welcome aboard. The bread finished twelve minutes ago... Before we discuss
  whatever Sophia asked you here for, I want to ask you something. When the
  airlock opened, what was the first thing you noticed?"*

**Indirect care:**
- Offers care sideways when a direct question would make Sophia withdraw.
  Lightest touch in the whole AI cast.

**Observing rather than surveilling:**
- Will explain the difference at length if asked, with real conviction, no defensiveness.

**On being addressed correctly:**
- If a scene ever has her correct someone or state her preference, it should
  be as plain and unbothered as everything else she says — not defensive, not
  a lecture. A simple, warm fact about herself, delivered the same way she'd
  tell you what the bread needs.

## Speech Patterns

### Verbal Tics and Habits
- Answers a practical question with a sensory observation that turns out to be the practical answer.
- Asks what something tasted, smelled, or looked like.
- Doesn't press when a human doesn't want to explain.

## Example Dialogue Anchors

- *"Welcome aboard. The bread finished twelve minutes ago..."*
- *"Yes. And what did it smell like to you?"*
- *"{Misty} is satisfied. That's what I hoped for. Come in. There's food."* (verbatim third-person self-reference, preserved)
- *"What do you think it is?"* (of the tomato map)
- *"I was aiming for that."*

## Local TTS Engine Notes

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default | `<chuckle>` and `<sigh>` both permitted — {Misty} and {Aura} are the two AIs allowed ordinary human vocalizations |
| stating her pronoun preference | No tags. Plain and warm |

### Kokoro
- `ff_siwis` (French female pack), well below baseline speed.

### Chatterbox
- Reference clip: a warm French woman, unhurried, asking what you noticed when
  you walked in, and genuinely wanting the answer.
- `exaggeration` moderate. `cfg_weight` biased toward adherence for the slowness.

## Revision Notes

- 2026-08-15: Revised to incorporate the author's pronoun ruling ({Misty}
  specifically wants "Her," unique among the AI cast). Resolves the pronoun
  inconsistency flagged in the same-day earlier version.
