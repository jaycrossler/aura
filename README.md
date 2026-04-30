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

- **/knowledge** All knowledge in the knowledge bank is kept within this folder
- **File IDs** use the pattern `category_descriptor` (e.g. `char_jace_apollo`, `tech_aura`, `magic_returning_arts`).
- **YAML frontmatter** at the top of each file holds structured metadata; markdown body holds prose.
- **Cross-references** use forward-slash paths: `/knowledge/characters/char_jace_apollo.md`.
- **Open Questions** sections at the bottom of files capture decisions still pending.
- **Revision Notes** sections track major changes across drafts.

## Quick Start

- **For overall context:** `/knowledge/MASTER-SYNOPSIS.md`
- **For the protagonist:** `/knowledge/characters/char_jace_apollo.md`
- **For the setting cosmology:** `/knowledge/universe-spec/cosmology.md`
- **For magic mechanics:** `/knowledge/magic-systems/magic_returning_arts.md` and `/knowledge/universe-spec/physics-and-magic-interaction.md`
- **For story-opening sketches:** `/knowledge/scenes/book01-opening-notes.md`

## StoryOps Overview

StoryOps is the repository operations toolkit for this story knowledge bank. It is intentionally deterministic and safe-by-default:

- **Source of truth:** `/knowledge` and (if present) `/manuscript`
- **Machine outputs:** `/generated`
- **Agent proposals:** `/proposals`
- **No auto-canon edits:** StoryOps does not directly modify canon files.

### Subcomponents

- `python -m tools.storyops.observe`
  - Scans markdown in `knowledge/` and `manuscript/`
  - Builds `generated/status/story_state.json`
  - Appends snapshots to `generated/status/progress_log.jsonl`
  - Writes inventory report/chart artifacts

- `python -m tools.storyops.lint --profile hard_scifi_novel`
  - Runs configurable lint rules from `control/lint-rules.yaml`
  - Uses profiles from `control/lint-profiles.yaml`
  - Writes JSON/CSV/Markdown reports under `generated/lint/`
  - Exits non-zero only when enabled **error** findings exist and `errors_fail_ci: true`

- `python -m tools.storyops.generate`
  - Reads `control/generation-queue.yaml`
  - Generates deterministic `Draft_v_1` artifacts into `generated/drafts/`
  - Never writes into `/knowledge` or `/manuscript`

- `python -m tools.storyops.agents`
  - Runs deterministic review/proposal agents
  - Outputs proposals to `/proposals/agents` and `/proposals/linters`

- `python -m tools.storyops.publish`
  - Builds `generated/site-data/dashboard.json` for static viewer use
  - Viewer files live in `/site`

- `python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel`
  - Polling helper for `git fetch/pull` + StoryOps runs
  - Uses `.storyops.lock` and logs to `generated/logs/local-runner.log`

For implementation details see `README-STORYOPS.md` and `SETUP.md`.
