---
id: storybot_orpheus_voice_tag_reference
name: "Orpheus TTS — Voice Tag Reference for Audiobook Generation"
type: system_documentation
status: working draft
last_updated: 2026-08-12
description: "Reference note explaining how this KB's voice_char_*.md files map the story's existing emotional-tone vocabulary onto Orpheus TTS's actual supported syntax, so the audiobook pipeline gets a consistent, generator-ready format across all character voice profiles."
cross_references:
  - "[[voice_char_jace_apollo]]"
  - "[[VISUAL_PROFILE_SYSTEM_INSTRUCTIONS]]"
---

# Orpheus TTS — Voice Tag Reference

This note exists because the voice profiles drafted this session (Maureen,
Lanchee, Nick, Artemis, Carlos, Mei, {Alex}, Helena, Sai) are formatted for
direct use with **Orpheus TTS** (Canopy Labs' open-weights emotive
speech model), which has a narrower, more specific tag vocabulary than the
freeform `[bracket]` tags in the earlier `voice_char_jace_apollo.md`. Rather
than silently changing that file's format, this note documents the mapping so
both styles coexist and a StoryBot pass can normalize later if wanted.

## Orpheus's actual supported syntax

Orpheus does **not** take arbitrary emotion brackets in the prompt text. It
takes two separate things:

1. **A voice identity** — selected via a base/reference voice (Orpheus ships
   several pretrained speakers, e.g. `tara`, `leah`, `jess`, `leo`, `dan`,
   `mia`, `zac`, `zoe`; custom character voices are typically produced by
   picking the closest base speaker and steering it with a written voice
   description, or by fine-tuning/cloning against reference audio if the
   pipeline supports it). **This KB does not canonically assign a specific
   Orpheus base speaker per character** — that's a production decision for
   whoever runs the pipeline. Each profile below instead gives a **casting
   description** (register, pacing, texture) so a human or a matching step
   can pick the closest available base voice.
2. **Inline non-speech tags**, placed directly in the text to be spoken, which
   Orpheus renders as actual vocalized sound rather than described emotion.
   The supported tags are:

   `<laugh>` `<chuckle>` `<sigh>` `<cough>` `<sniffle>` `<groan>` `<yawn>` `<gasp>`

   These go inline, e.g.: `"You couldn't visit anyway <sigh> Adama is closed
   to civilians."` Only use a tag where the character would actually make
   that sound — don't insert one just to mark an emotional beat that has no
   associated vocalization.

## How these profiles use that

Each `voice_char_*.md` file below keeps this KB's existing descriptive
emotional-tone vocabulary (matching `VISUAL_PROFILE_SYSTEM_INSTRUCTIONS.md`'s
tone list: `dry`, `precise`, `clipped`, `barely-concealed-{emotion}`, etc.) for
**prose/dialogue-metadata tagging** — this is what a human director or a
non-Orpheus pipeline would use, and it's what scene metadata sidecars already
reference. Then, separately, each file adds an **"Orpheus tag mapping"**
section translating that vocabulary into the actual `<tag>` syntax Orpheus
will accept, plus a **casting description** paragraph for base-voice
selection.

## Revision Notes

- 2026-08-12: Initial note, written alongside this session's batch of new
  voice profiles for the Prologue–Ch07 speaking cast.
