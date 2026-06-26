---
id: system_character_sheets
name: Character Progression Sheets — System and Conventions
type: kb_system
status: canonical
canonical: true
description: "System documentation defining conventions and templates for character progression sheets (snapshots of states at story checkpoints)."
last_updated: 2026-06-26
cross_references:
  - magic-systems/magic_skills_framework.md
  - magic-systems/magic_will_orbs.md
  - magic-systems/magic_will_and_templates.md
---

# Character Progression Sheets — System and Conventions

## Purpose

Character sheets track the progression of characters, ships, and Will-significant
objects across the story. They are snapshot documents — a record of state at a
specific story checkpoint — not continuously updated files. Each sheet is a
separate file, never edited after creation.

A character sheet is, in-universe, the equivalent of a Template vault snapshot:
a preserved record of someone's state at a moment in time. If a character is
resurrected from a vault, the last sheet before the vault copy was made is the
restoration baseline.

---

## What Gets a Sheet

- **Characters:** any named character with Skills, Will capacity, or significant
  Template investment
- **Ships:** any named vessel that has been Templated or dimensionally modified
- **Will-significant objects:** any object with an [Object Template] or active
  Rune Writing (Jace's HUD, Kael's hoverboard, the rocket buggy, dimensional
  tools and weapons as they develop)
- **Familiars:** Cerberus, Kai, and any other Will-bonded animals

---

## File Location and Naming

Sheets live in a flat `sheets/` directory at repo root.

Naming convention: `sheet_{subject_id}_{arc_slug}_{checkpoint}.md`

Examples:
- `sheet_jace_arc01_plumbing.md` — Jace after the Falcon plumbing crisis (first Will event)
- `sheet_jace_arc01_end.md` — Jace at end of Arc 1
- `sheet_jace_arc02_oath.md` — Jace after swearing to Kael at Metis
- `sheet_kael_arc02_death.md` — Kael's state immediately before death (vault snapshot)
- `sheet_cerberus_arc01_end.md` — Cerberus at end of Arc 1
- `sheet_falcon_arc01_end.md` — the ship Falcon after Arc 1 modifications
- `sheet_jace_hud_arc01_plumbing.md` — the HUD implant after accidental Templating

Sheets sort chronologically by arc then checkpoint label. Use short, descriptive
checkpoint names. Avoid dates — arc/checkpoint slugs are more stable as the story
develops.

---

## Sheet Template

```markdown
---
id: sheet_{subject_id}_{arc}_{checkpoint}
subject: {Character/Ship/Object name}
subject_id: {matching character/ship/object file id}
checkpoint: {one-line description of the story moment}
arc: {arc_slug}
approximate_chapter: {optional — chapter reference if known}
last_updated: {date created — never modified after}
---

# {Subject Name} — {Checkpoint Label}

## Story Context
One paragraph: what just happened, why this is a meaningful snapshot.

## Will Profile
- **Current reserve:** {rough estimate — low/moderate/high/depleted}
- **Generation rate:** {baseline/enhanced/diminished and why}
- **Reservoir discipline:** {untrained/developing/trained/expert}

## Active Skills
List each known [Skill] with current level and brief note on how it was acquired
or what it can do at this level.

| Skill | Level | Notes |
|---|---|---|
| [Mind Wall] | passive | All Sol humans; not consciously controlled yet |
| [Object Template] | L1 (accidental) | HUD implant only; result of Will orb absorption |

## Templated Items
List all objects the subject has active Templates on, with notes on quality and
maintenance cost.

| Item | Template quality | Notes |
|---|---|---|
| HUD implant | L1 (accidental, unstable) | Gold/platinum components; expensive to maintain |

## Physical Condition
Current injuries, healing status, dimensional stress accumulated.

## Active Will Links
Any Will Seeding relationships, familiar bonds, or active anchors to other characters.

## Open Notes
Flags, unresolved questions, foreshadowing relevant to this character's progression.
```

---

## Checkpoint Triggers

Create a new sheet when:

1. **Major skill acquisition** — first time a character uses or learns a named [Skill]
2. **End of an arc** — standard checkpoint for all active characters
3. **Template event** — significant new Templating, a Template destroyed, a vault
   snapshot taken (in-story and in KB simultaneously)
4. **Will depletion or surge** — significant change in reserve state (Jace post-
   plumbing; Kael after carrying Jace to Metis)
5. **Death or resurrection** — the sheet just before death is the vault baseline;
   create a new sheet immediately after resurrection noting what was lost
6. **Familiar bond events** — creation, strengthening, or severance of Will bonds

Do **not** edit existing sheets. Create a new one. The history must be preserved.

---

## The Vault Parallel

The character sheet system mirrors the in-universe Template vault mechanic
deliberately. A practitioner who stores a Template vault copy is freezing their
state; the sheet created at that moment is the KB record of what was stored.

If Kael is resurrected from her vault (a future-arc possibility), the restoration
baseline is `sheet_kael_arc02_death.md` — she would lose everything she learned
after that copy was made. The sheet tells us exactly what she retains and what
she loses, without having to reconstruct it from narrative.

This also means the sheet system is load-bearing for resurrection plots. Maintain
it carefully.

---

## Initial Sheets to Create

The following sheets should be created to establish the baseline:

| Sheet file | Subject | Checkpoint |
|---|---|---|
| `sheet_jace_arc01_plumbing.md` | Jace | After plumbing crisis and Will orb absorption — first Will event |
| `sheet_jace_arc01_end.md` | Jace | End of Arc 1 — Fortuna departure |
| `sheet_cerberus_arc01_end.md` | Cerberus | End of Arc 1 — Template complexity noted by Kael |
| `sheet_kael_arc02_arrival.md` | Kael | On arrival at Fortuna — her baseline before teaching Jace |
| `sheet_kael_arc02_death.md` | Kael | Immediately before Bloom attack — vault snapshot |
| `sheet_jace_arc02_oath.md` | Jace | After oath to Kael at Metis — first formal apprenticeship |
| `sheet_jace_hud_arc01_plumbing.md` | Jace's HUD | After accidental Templating |

---

## Revision Notes

- 2026-06-25: New file. Character sheet system established. Naming convention,
  template, checkpoint triggers, and initial sheet list documented.
