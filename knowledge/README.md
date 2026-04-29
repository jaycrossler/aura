# Story Bible — The Aura Chronicles

A working repository for a hard sci-fi novel/series set in the late 21st and early 22nd centuries, in a solar system on the cusp of magical transformation.

## Repository Structure

```
/knowledge/MASTER-SYNOPSIS.md         — The big picture; start here
/knowledge/universe-spec/             — Immutable core rules (physics, cosmology, magic laws)
/knowledge/characters/                — One file per character
/knowledge/factions/                  — Political, corporate, and cultural organizations
/knowledge/locations/                 — Planets, stations, cities, significant places
/knowledge/timeline/                  — Chronology of events
/knowledge/magic-systems/             — Magic rules, schools, practitioners
/knowledge/technology/                — Tech specs and infrastructure
/knowledge/ships/                     — Specific named vessels (one file per ship)
/knowledge/scenes/                    — Scene drafts and notes by novel and chapter
/knowledge/templates/                 — Reusable templates for new files
/knowledge/review-queue/              — Items flagged for later attention (currently empty)
```

## Working Conventions

- **File IDs** use the pattern `category_descriptor` (e.g. `char_jace_apollo`, `tech_aura`, `magic_returning_arts`).
- **YAML frontmatter** at the top of each file holds structured metadata; markdown body holds prose.
- **Cross-references** use forward-slash paths: `/characters/char_jace_apollo.md`.
- **Open Questions** sections at the bottom of files capture decisions still pending.
- **Revision Notes** sections track major changes across drafts.

## Quick Start

- **For overall context:** `/MASTER-SYNOPSIS.md`
- **For the protagonist:** `/characters/char_jace_apollo.md`
- **For the setting cosmology:** `/universe-spec/cosmology.md`
- **For magic mechanics:** `/magic-systems/magic_returning_arts.md` and `/universe-spec/physics-and-magic-interaction.md`
- **For story-opening sketches:** `/scenes/book01-opening-notes.md`
