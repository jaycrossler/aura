---
id: system_character_sheets
name: Character Progression Sheets — System and Conventions
type: kb_system
status: canonical
canonical: true
last_updated: 2026-06-26
description: >
  System documentation defining conventions, frontmatter schema, and templates
  for character progression sheets — immutable snapshots of character, ship, and
  object state at story checkpoints. Also covers the vault-parallel mechanic and
  build_tree.py integration.
cross_references:
  - magic-systems/magic_skills_framework.md
  - magic-systems/magic_will_orbs.md
  - magic-systems/magic_will_and_templates.md
  - SERIES_BIBLE.md
---

# Character Progression Sheets — System and Conventions

## Purpose

Character sheets track the progression of characters, ships, and Will-significant
objects across the story. They are **immutable snapshot documents** — a frozen
record of state at a specific story checkpoint. Each sheet is a separate file and
is **never edited after creation**. If state changes, create a new sheet.

A character sheet is the KB equivalent of a Template vault snapshot: a preserved
record of someone's state at a moment in time. The sheet system is load-bearing
for resurrection plots — if Kael is resurrected from her vault, the restoration
baseline is `sheet_kael_arc02_death.md`, and that file tells us exactly what she
retains and what she loses.

---

## What Gets a Sheet

- **Characters** — any named character with Skills, Will capacity, or significant
  Template investment
- **Ships** — any named vessel that has been Templated or dimensionally modified
- **Will-significant objects** — any object with an active [Object Template] or
  Rune Writing: Jace's HUD implant, Kael's iron bracer, the rocket buggy,
  dimensional tools and weapons as they develop
- **Familiars** — Cerberus, Kai, and any other Will-bonded animals

---

## File Location and Naming

All sheets live in a **flat** `sheets/` directory at repo root. Do not create
subdirectories — the naming convention provides all needed grouping, and flat
structure makes `project_knowledge_search` retrieval more reliable.

**Naming convention:** `sheet_{subject_id}_{arc_slug}_{checkpoint}.md`

Use the subject's file id (without the `char_` / `ship_` prefix) as `subject_id`.
Use short, stable checkpoint labels — arc/checkpoint slugs are more stable than
dates as the story develops.

**Examples:**

| File | Subject | Moment |
|---|---|---|
| `sheet_jace_arc01_plumbing.md` | Jace | After plumbing crisis — first Will event |
| `sheet_jace_arc01_end.md` | Jace | End of Arc 1 |
| `sheet_jace_arc02_oath.md` | Jace | After oath to Kael at Métis |
| `sheet_kael_arc02_arrival.md` | Kael | Arrival at Fortuna — baseline before teaching |
| `sheet_kael_arc02_death.md` | Kael | Before Bloom attack — vault snapshot |
| `sheet_cerberus_arc01_end.md` | Cerberus | End of Arc 1 — Template noted by Kael |
| `sheet_falcon_arc01_end.md` | Falcon | After Arc 1 modifications |
| `sheet_jace_hud_arc01_plumbing.md` | Jace's HUD | After accidental Templating |
| `sheet_kael_bracer_arc02_arrival.md` | Kael's iron bracer | Arrival baseline |

---

## Required Frontmatter

Every sheet file **must** include this frontmatter exactly. `build_tree.py`
reads these fields to power index display, orphan detection, and sequence
gap warnings.

```yaml
---
id: sheet_{subject_id}_{arc}_{checkpoint}
name: "{Subject Name} — {Checkpoint Label}"
type: character_sheet
subject: {Human-readable name, e.g. "Jace Grant"}
subject_id: {File stem without prefix, e.g. "jace_apollo"}
subject_type: character | ship | object | familiar
checkpoint: {One-line description, e.g. "After plumbing crisis and Will orb absorption"}
arc: arc_01
sheet_sequence: 1
immutable: true
is_vault_snapshot: false
last_updated: {date this sheet was created — set once, never changed}
description: "{Subject} at {checkpoint} — {one sentence of context}"
cross_references:
  - characters/char_{subject_id}.md
  - arcs/arc_{arc_slug}.md
---
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | ✓ | `sheet_{subject_id}_{arc}_{checkpoint}` |
| `name` | ✓ | Human-readable; shown in index |
| `type` | ✓ | Always `character_sheet` |
| `subject` | ✓ | Display name of the subject |
| `subject_id` | ✓ | Matches the character/ship/object file id without prefix |
| `subject_type` | ✓ | `character`, `ship`, `object`, or `familiar` |
| `checkpoint` | ✓ | One-line description of the story moment |
| `arc` | ✓ | Arc slug, e.g. `arc_01` |
| `sheet_sequence` | ✓ | Integer ordinal within this subject's sheet history; starts at 1 |
| `immutable` | ✓ | Always `true` — `build_tree.py` surfaces this as a warning |
| `is_vault_snapshot` | ✓ | `true` only if this sheet corresponds to an in-story Template vault storage event |
| `last_updated` | ✓ | Set to the creation date; **never change after creation** |
| `description` | ✓ | One sentence for the index |
| `cross_references` | ✓ | At minimum: the subject's main file and the arc file |

### `sheet_sequence` rules

- Assign `1` to the first sheet created for a subject, `2` to the next, and so on.
- Sequences are **per subject**, not global. Jace can be at seq 5 while Kael is at seq 2.
- `build_tree.py` detects gaps (e.g. if seq 3 is missing for a subject) and emits
  a warning in `_index.md`. Fix gaps by creating missing sheets or renumbering.
- Never reuse a sequence number. If a sheet is deleted, leave the gap and note it
  in the `## Warnings` section of `_index.md`.

---

## Sheet Body Template

```markdown
# {Subject Name} — {Checkpoint Label}

## Story Context
*Required. One paragraph: what just happened, why this is a meaningful snapshot,
and what state the subject was in immediately before this moment. This is the
"why does this sheet exist" section.*

## Will Profile
- **Current reserve:** low / moderate / high / depleted / not applicable
- **Generation rate:** baseline / enhanced / diminished — and why
- **Reservoir discipline:** untrained / developing / trained / expert

## Active Skills
*List every known [Skill] with current level. Include passive/unconscious skills
(e.g. Sol human [Mind Wall]). Omit skills that have not yet been demonstrated or
taught — those belong in the next sheet.*

| Skill | Level | How acquired | What it can do at this level |
|---|---|---|---|
| [Mind Wall] | passive | All Sol humans; cognitive Template hardening | Resists Will-based social compulsion; not yet conscious |
| [Object Template] | L1 (accidental, unstable) | Will orb absorption during plumbing crisis | HUD implant only; expensive to maintain |

## Templated Items
*List all objects this subject has active Templates on.*

| Item | Template level | Stability | Notes |
|---|---|---|---|
| HUD implant | L1 | Unstable | Gold/platinum content; high maintenance cost |

## Physical Condition
Current injuries, healing status, dimensional stress accumulated, any body
Template modifications from this arc.

## Will Links
*Any active Will Seeding relationships, familiar bonds, or Astral anchors.*

| Link type | Partner | Strength | Notes |
|---|---|---|---|
| Familiar bond | Cerberus | Developing | Not yet named; Kael will read it in Arc 2 |

## Progression Axis Summary
*Quick summary of where this character stands on each of the four progression axes
at this checkpoint. Use: none / minimal / developing / established / strong.*

| Axis | Level | Notes |
|---|---|---|
| Personal Template | minimal | One accidental L1 skill; no deliberate training |
| Toolchain | developing | Survival suits built; multi-camera rig; early drone mods |
| Social | developing | Sophia partnership; Nick alliance; Maureen cautious trust |
| Environmental | developing | Fortuna corridors learned; Astral station interior mapped |

## Open Notes
*Flags, unresolved questions, and foreshadowing relevant to this subject's
progression. Things a later sheet should address.*

- [ ] HUD crossing anomaly unresolved — gold/platinum crossing with organic integration
- [ ] Will-depletion illness after orb absorption — cause not yet understood
```

---

## Checkpoint Triggers

Create a new sheet when any of the following occur:

1. **First skill acquisition** — first confirmed use or teaching of any named [Skill]
2. **End of arc** — standard checkpoint for all active characters with sheets
3. **Template event** — new [Object Template] created or destroyed; vault snapshot
   taken in-story (create the sheet at the same moment the in-story vault is made)
4. **Significant Will event** — major depletion, surge, or reservoir change
   (Jace post-plumbing; Kael after carrying Jace to Métis)
5. **Death** — create the death sheet *before* the death scene is written; this is
   the vault baseline; note `is_vault_snapshot: true` if the character has a vault
6. **Resurrection** — create a new sheet immediately after, noting what was lost
   relative to the vault snapshot
7. **Familiar bond events** — creation, deepening, or severance of Will bonds
8. **Major axis advancement** — if any progression axis jumps a full tier
   (e.g. Social goes from minimal → established in a single arc event)

**Do not** create sheets for every chapter. The system is for meaningful state
changes, not continuous logging. When in doubt, wait until the arc ends.

---

## Immutability Rule

**Never edit a sheet after creation.** This is the single most important rule.

If you discover an error in a sheet after creation:
1. Create a corrected sheet with the same checkpoint label and append `_v2`
   to the filename only
2. Add a note to the original sheet's `## Open Notes`: `[SUPERSEDED by sheet_X_v2]`
3. Update `_index.md` manually or re-run `build_tree.py`

The reason immutability matters: sheets are used to answer "what did this character
know/have at this exact moment?" for continuity checking, resurrection mechanics,
and retroactive foreshadowing review. An edited sheet breaks that function entirely.

---

## The Vault Parallel

The sheet system mirrors the in-universe Template vault mechanic deliberately.

| In-universe | KB |
|---|---|
| Practitioner stores a vault copy | Author creates a sheet |
| Vault records state at storage moment | Sheet records state at creation moment |
| Resurrection restores to vault baseline | Continuity check uses sheet as baseline |
| Vault cannot be updated without a new storage event | Sheet cannot be edited — new checkpoint = new sheet |
| Lost vault = lost resurrection option | Deleted sheet = lost continuity anchor |

When a character stores a vault in-story, create the sheet at the same session.
Set `is_vault_snapshot: true`. This is the file a resurrection plot depends on.

---

## build_tree.py Integration

`build_tree.py` treats sheet files differently from all other markdown files:

- **Detection:** any file whose name begins with `sheet_`
- **Index display:** shows `subject`, `arc`, `checkpoint`, `seq`, and an
  `⚠️ IMMUTABLE` warning instead of the standard field set
- **Sequence gap detection:** after the main walk, checks that each subject's
  sheet_sequence values form a contiguous sequence starting at 1; gaps are
  reported in the `## Warnings` section of `_index.md`
- **Orphan detection:** sheets are included in orphan checking; a sheet with no
  references from other files is flagged (this usually means the subject's main
  character file hasn't been updated to reference the sheet)

The character's main file (`char_jace_apollo.md`) should reference its sheets
in `cross_references`. This is what prevents sheets from appearing as orphans.
Add a `sheets:` section to each character file listing the sheet ids in order.

---

## Initial Sheets to Create

Priority order — create these before starting prose drafts for Arc 2:

| File | Subject | Checkpoint | Vault? | Seq |
|---|---|---|---|---|
| `sheet_jace_arc01_plumbing.md` | Jace | After plumbing crisis — first Will event | no | 1 |
| `sheet_jace_arc01_end.md` | Jace | End of Arc 1 | no | 2 |
| `sheet_cerberus_arc01_end.md` | Cerberus | End of Arc 1 — Template noted by Kael | no | 1 |
| `sheet_jace_hud_arc01_plumbing.md` | Jace's HUD | After accidental Templating | no | 1 |
| `sheet_kael_arc02_arrival.md` | Kael | Arrival at Fortuna — baseline before teaching | no | 1 |
| `sheet_kael_arc02_death.md` | Kael | Immediately before Bloom attack | **yes** | 2 |
| `sheet_kael_bracer_arc02_arrival.md` | Kael's iron bracer | Arrival baseline | no | 1 |
| `sheet_jace_arc02_oath.md` | Jace | After oath to Kael at Métis | no | 3 |
| `sheet_kai_arc02_arrival.md` | Kai | Arrival baseline — Crystal Dragon at Fortuna | no | 1 |

---

## Retcon Note (2026-06-26)

The original version of this document listed "Kael's hoverboard" as an example
Will-significant object. This is now incorrect — Kai is Kael's mount, not a
hoverboard. The relevant object sheet for Kael's equipment is `sheet_kael_bracer`
(the iron bracer with the air-bubble enchantment). See `characters/char_kael.md`
and `characters/char_kai.md`.

---

## Revision Notes

- 2026-06-25: Initial draft. Character sheet system established.
- 2026-06-26: Major revision. Added required frontmatter schema with full field
  reference. Added `sheet_sequence`, `immutable`, `is_vault_snapshot`,
  `subject_type` fields. Added `build_tree.py` integration section. Added
  immutability rule with error-correction procedure. Updated vault-parallel
  table. Updated initial sheets list (bracer replaces hoverboard; Kai added).
  Added progression axis summary section to body template. Retcon note added.
