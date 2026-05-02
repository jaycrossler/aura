# StoryOps — Current literature focus: The Aura Chronicles

A working repository for a hard sci-fi novel series set in the late 21st and early 22nd centuries, in a solar system on the cusp of magical transformation.

**Book 01** (*Fortuna*, working title) follows Jace Grant — a decorated U.S. military drone operator who arrives on Mars certain of his future, receives a career-ending medical diagnosis on Day 2, spends four months in quiet collapse, acquires a dog named Cerberus, and departs on the Falcon as a civilian contractor with a secret intelligence arrangement.

---

## Repository structure

```
/knowledge/                    — Ground truth: all canon lives here
  MASTER-SYNOPSIS.md           — The big picture; start here
  universe-spec/               — Immutable core rules (physics, cosmology, magic laws)
  characters/                  — One file per character (char_*.md)
    voice/                     — Voice profiles (voice_char_*.md)
    states/                    — Emotional/physical state templates
  factions/                    — Political, corporate, and cultural organizations
  factions-relationships/      — Cross-faction relationship maps
  locations/                   — Planets, stations, cities, significant places (location_*.md)
    sensory/                   — Location sensory primers (sensory_location_*.md)
  timeline/                    — Chronology of events + scene temporal map
  magic-systems/               — Magic rules, schools, practitioners
  technology/                  — Tech specs and infrastructure
  ships/                       — Specific named vessels
  scenes/                      — Scene drafts, author notes, choreography (event_*.md)
    choreography/              — Detailed scene blocking (choreo_event_*.md)
    sensory/                   — Scene sensory primers (sensory_event_*.md)
  templates/                   — Reusable templates for new files
  review-queue/                — Items flagged for later author attention

/control/                      — StoryOps configuration (human-edited)
  scene-registry.yaml          — All scenes: stable IDs, source files, tags, status
  story-structure.yaml         — Chapters: scene assignment, order, POV, tone, pacing
  render-profiles.yaml         — Generation profiles: voice, format, tone variant
  generation-queue.yaml        — Jobs queue: chapter + profile combinations
  lint-rules.yaml              — Lint rule configuration
  lint-profiles.yaml           — Lint profile definitions

/tools/storyops/               — Generation and review pipeline (Python)
/generated/                    — All machine output (not canon)
  drafts/                      — Versioned chapter files
  status/                      — report.json (read by dashboard)
  dashboard/                   — index.html (mission control)
  logs/                        — Per-job .log and .jsonl files
/proposals/                    — Agent suggestions (not canon; require author promotion)
/site/                         — Published site (reader view, KB explorer, feedback)
```

---

## Working conventions

- **`/knowledge` is canon.** Nothing writes here except the author (or the importer on explicit invocation).
- **File IDs** use `category_descriptor` (e.g. `char_jace_apollo`, `location_terminus`, `faction_origin_industries`). Lowercase, underscores.
- **YAML frontmatter** at the top of every knowledge file holds structured metadata; markdown body holds prose.
- **Cross-references** use forward-slash paths: `/knowledge/characters/char_jace_apollo.md`.
- **Open Questions** sections at the bottom of files capture pending author decisions.
- **Revision Notes** sections track major changes across drafts.
- **`[STORYBOT]`** marks details the generation system can extrapolate. **`TBD`** marks required author decisions. **`[AUTHOR DECISION NEEDED]`** marks conflicts.

---

## Quick start (reading)

- **Overall context:** `/knowledge/MASTER-SYNOPSIS.md`
- **Protagonist:** `/knowledge/characters/char_jace_apollo.md`
- **Setting cosmology:** `/knowledge/universe-spec/cosmology.md`
- **Magic mechanics:** `/knowledge/magic-systems/magic_returning_arts.md`
- **Book 01 opening:** `/knowledge/scenes/book01-opening-notes.md`
- **Mars world-building:** `/knowledge/locations/location_terminus.md`

---

## Quick start (generation)

```bash
pip install openai requests pyyaml python-frontmatter

export STORYOPS_LLM_PROVIDER=openai
export STORYOPS_LLM_MODEL=gpt-4o
export OPENAI_API_KEY=sk-...

# Generate chapter 1
python -m tools.storyops.artifact_generators --chapter ch001

# Run gap analysis and open dashboard
python -m tools.storyops.status_reporter
open generated/dashboard/index.html
```

---

## StoryOps overview

StoryOps is the repository operations toolkit. It is **deterministic and safe-by-default**:

| System | What it does |
|--------|-------------|
| `observe` | Scans knowledge and manuscript; builds state snapshots |
| `lint` | Runs configurable rules; CI-safe; never modifies files |
| `generate` (StoryBot) | Four-step pipeline: plan → assemble → weave → export |
| `agents` | Review and proposal agents; outputs to `/proposals/` only |
| `status_reporter` | Gap analysis; writes `report.json`; powers dashboard |
| `publish` | Builds static site data |
| `local_runner` | Git poll + pipeline runner |
| `importer` | Routes KB markdown into `/knowledge/` on explicit invocation |

For full technical documentation: **`README-STORYOPS.md`**
For AI session context: **`CONTEXT.md`**

---

## Current chapter status (book 01)

| Chapter | Title | Arc | Status |
|---------|-------|-----|--------|
| ch001 | Descent | arrival | `raw_draft` |
| ch002 | The Facility | arrival | `not_started` |
| ch003 | First Night | arrival | `not_started` |
| ch004 | The Appointment | collapse | `not_started` |
| ch005 | Hard Months — Falling | hard-months | `not_started` |
| ch006 | Hard Months — Rising | hard-months | `not_started` |
| ch007 | The Deals | the-deals | `not_started` |
| ch008 | Departure | departure | `not_started` |
