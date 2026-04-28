# Story Bible — The Aura Chronicles

A working repository for a hard sci-fi novel/series set in the late 21st and early 22nd centuries, in a solar system on the cusp of magical transformation.

## Repository Structure

```
/MASTER-SYNOPSIS.md         — The big picture; start here
/universe-spec/             — Immutable core rules (physics, cosmology, magic laws)
/characters/                — One file per character
/factions/                  — Political, corporate, and cultural organizations
/locations/                 — Planets, stations, cities, significant places
/timeline/                  — Chronology of events
/magic-systems/             — Magic rules, schools, practitioners
/technology/                — Tech specs and infrastructure
/ships/                     — Specific named vessels (one file per ship)
/scenes/                    — Scene drafts and notes by novel and chapter
/templates/                 — Reusable templates for new files
/review-queue/              — Items flagged for later attention (currently empty)
```

## Working Conventions

- **File IDs** use the pattern `category_descriptor` (e.g. `char_marcus_hale`, `tech_aura`, `magic_returning_arts`).
- **YAML frontmatter** at the top of each file holds structured metadata; markdown body holds prose.
- **Cross-references** use forward-slash paths: `/characters/char_marcus_hale.md`.
- **Open Questions** sections at the bottom of files capture decisions still pending.
- **Revision Notes** sections track major changes across drafts.

## Quick Start

- **For overall context:** `/MASTER-SYNOPSIS.md`
- **For the protagonist:** `/characters/char_marcus_hale.md`
- **For the setting cosmology:** `/universe-spec/cosmology.md`
- **For magic mechanics:** `/magic-systems/magic_returning_arts.md` and `/universe-spec/physics-and-magic-interaction.md`
- **For story-opening sketches:** `/scenes/book01-opening-notes.md`
