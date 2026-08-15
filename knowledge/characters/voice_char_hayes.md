---
id: voice_char_hayes
character_ref: char_hayes
type: character_voice_profile
status: light (insufficient KB detail for a full profile)
last_updated: 2026-08-15
description: "Light vocal profile for Hayes, formatted for local TTS audiobook generation. Vocal detail is thin but the physical condition is unusually well specified and has direct performance consequences."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_hayes]]"
  - "[[char_jace_apollo]]"
  - "[[char_lanchee]]"
  - "[[char_cerberus]]"
  - "[[location_fortuna_station]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
open_flags:
  - "No accent, age, gender-of-voice, or physical vocal description for Hayes exists in the retrieved KB."
  - "char_hayes.md carries three open decisions of its own, per the _index.md annotation. Those should be resolved before this profile is expanded."
---

# Character Voice Profile — Hayes

> **Light profile.** This character has a speaking role in the drafted chapters
> but the knowledge base does not yet contain enough vocal, physical, or
> dialogue detail to build a full profile without inventing canon. Everything
> below is drawn from what exists. The gaps are listed explicitly rather than
> filled. Expand after the next author pass.

## What the KB establishes

`char_hayes.md` records the status as: *alive (medbay, unconscious, then
recovering; permanently left-handed)*. That is an unusually specific and
unusually useful piece of information for an audiobook, because it means Hayes
has **three distinct vocal states across the book**, and they are not
interchangeable:

1. **Before the injury** (Ch08, Ch09). Baseline. Working register.
2. **Unconscious** (medbay). No lines.
3. **Recovering, permanently left-handed.** A person relearning basic motor
   tasks. Effortful, frustrated, and adjusting.

The third state is the one most likely to be flattened by a generator, and it is
the one that carries the cost of the story. Direct it explicitly.

## Provisional direction

Baseline: ordinary working Fortuna resident, unremarkable, warm enough.
Recovery: slower, more effortful, with real irritation that is aimed at the
hand rather than at whoever is in the room. Do not perform bravery.

## Local TTS Engine Notes

- **Orpheus:** `<groan>` is warranted in the recovery scenes where the prose
  describes physical effort, and nowhere else. No `<sigh>` at the start of
  recovery lines, which would read as self-pity.
- **Kokoro:** generate baseline and recovery as separate passes at different
  speeds, roughly 15 percent apart, rather than trying to get both from one.
- **Chatterbox:** two reference clips, one baseline and one effortful. Switching
  clips is the cleanest way to produce the before-and-after.

## Revision Notes

- 2026-08-15: Initial light profile, created during the Ch00-20 cast and voice audit. Deliberately not padded. See the open flags for what an author pass needs to supply.
