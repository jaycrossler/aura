# README-STORYOPS

Full technical documentation for the StoryOps generation, review, and publishing pipeline for **The Aura Chronicles** knowledge bank.

---

## Table of contents

1. [Architecture overview](#1-architecture-overview)
2. [Safety model](#2-safety-model)
3. [Module reference](#3-module-reference)
4. [The generation pipeline (StoryBot)](#4-the-generation-pipeline-storybot)
5. [Knowledge base structure](#5-knowledge-base-structure)
6. [Control files](#6-control-files)
7. [Render profiles and variants](#7-render-profiles-and-variants)
8. [Versioning and pass types](#8-versioning-and-pass-types)
9. [Logging and diagnostics](#9-logging-and-diagnostics)
10. [LLM provider setup](#10-llm-provider-setup)
11. [Command reference](#11-command-reference)
12. [CI / GitHub Actions / Scheduler](#12-ci--github-actions--scheduler)
13. [Extending StoryOps](#13-extending-storyops)
14. [VS Code debug setup](#14-vs-code-debug-setup)
15. [Current status](#15-current-status)
16. [Roadmap](#16-roadmap)
17. [Next tasks — prioritized](#17-next-tasks--prioritized)

---

## 1. Architecture overview

StoryOps has four major systems:

```
┌─────────────────────────────────────────────────────────────────┐
│  1. KNOWLEDGE BASE                                              │
│  knowledge/{characters,locations,scenes,technology,factions...} │
│  Hierarchical Markdown. Ground truth. LLM must not contradict.  │
└────────────────────────┬────────────────────────────────────────┘
                         │ RAG assembly (scene_assembler.py)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. STORYBOT — Generation Pipeline                              │
│  Plan → Assemble → Weave → Export → Version                    │
│  tools/storyops/   (Python, LLM-powered)                        │
└────────────────────────┬────────────────────────────────────────┘
                         │ generated/drafts/, generated/versions/
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. OBSERVE / LINT / AGENTS                                     │
│  Continuity checking, KB cross-reference, voice linting,        │
│  agent proposals — never auto-edits canon                       │
└────────────────────────┬────────────────────────────────────────┘
                         │ generated/status/report.json
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. SITE / PUBLISH                                              │
│  Dashboard, reader view, knowledge explorer, feedback capture   │
│  generated/dashboard/index.html + site/                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Safety model

| Zone | Path | Who edits |
|------|------|-----------|
| **canon** | `/knowledge`, `/manuscript` | Human only — never auto-modified |
| **generated** | `/generated` | Machine output — not canon |
| **proposed** | `/proposals` | Agent suggestions — requires author approval to promote |
| **control** | `/control` | Human-authored config read by all tools |

StoryOps does **not** auto-edit `/knowledge` or `/manuscript`. Ever.

The generation pipeline writes to `/generated/drafts/` only. The importer routes files into `/knowledge/` but only on explicit author invocation. Agent proposals go to `/proposals/` and require explicit promotion to canon.

---

## 3. Module reference

### `tools.storyops.observe`
Scans `/knowledge` and `/manuscript`. Builds `generated/status/story_state.json`. Appends to `generated/status/progress_log.jsonl`. Writes inventory chart artifacts.

```bash
python -m tools.storyops.observe
```

### `tools.storyops.lint`
Runs configurable lint rules against knowledge and generated files. Reads from `control/lint-rules.yaml` and `control/lint-profiles.yaml`. Writes JSON/CSV/Markdown reports to `generated/lint/`. Exits non-zero only when enabled **error** findings exist and `errors_fail_ci: true`.

```bash
python -m tools.storyops.lint --profile hard_scifi_novel
python -m tools.storyops.lint --path knowledge/scenes/book01-opening-notes.md
```

### `tools.storyops.artifact_generators`
Reads `control/generation-queue.yaml`. Runs the four-step StoryBot pipeline. Writes versioned artifacts to `generated/drafts/`. Emits step-by-step progress to stdout and `generated/logs/story-generator.log`. Never writes into `/knowledge` or `/manuscript`.

```bash
python -m tools.storyops.artifact_generators --chapter ch001
python -m tools.storyops.artifact_generators --item gen_book01_ch004_horror
python -m tools.storyops.artifact_generators
```

### `tools.storyops.agents`
Runs deterministic review and proposal agents. Outputs to `/proposals/agents` and `/proposals/linters`. Does not modify canon.

```bash
python -m tools.storyops.agents --agent-id master_continuity
```

Current agent IDs: `master_continuity`. Planned: `voice_editor`, `tone_reviewer`, `character_emulator_{id}`.

### `tools.storyops.status_reporter`
Gap analysis across all chapter manifests and scene registry. Writes `generated/status/report.json`. Prints human-readable gap report. Dashboard reads this file.

```bash
python -m tools.storyops.status_reporter
python -m tools.storyops.status_reporter --quiet
```

### `tools.storyops.publish`
Builds `generated/site-data/dashboard.json` for static viewer. Viewer files in `/site`.

```bash
python -m tools.storyops.publish
```

### `tools.storyops.local_runner`
Polling helper: `git fetch/pull` + StoryOps run. Uses `.storyops.lock`. Logs to `generated/logs/local-runner.log`. Mirrors subprocess output to stdout. Generation is **off by default** — add `--run-generate true`.

```bash
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel
python -m tools.storyops.local_runner --repo . --interval-seconds 300 --profile hard_scifi_novel
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --run-generate true
```

### `tools.storyops.importer`
Imports knowledge markdown from `.zip`, directory, or single `.md`. Supports concatenated docs with multiple frontmatter blocks. Routes into `/knowledge/*/` using frontmatter `type`/`id`. Merges by replacing when incoming content is same length or longer. Writes `generated/reports/import-report.json`. Deletes source on success.

```bash
python -m tools.storyops.importer <source>
```

---

## 4. The generation pipeline (StoryBot)

### Step 1 — Chapter Planner (`chapter_planner.py`)

**Input:** chapter definition + scene registry + render profile → **Output:** `ChapterOutline`

One LLM call. Produces:
- `emotional_arc_summary` — the shape of the chapter in one paragraph
- `opening_image` / `closing_image` — concrete sensory moments (not abstract)
- `beats[]` — one `BeatPlan` per scene: `valence` (-1.0…+1.0), `tension` (0.0…1.0), `emotional_start`/`end`, `key_dialogue_hooks`, `pov_notes`
- `continuity_anchors` — things from prior chapters to reference
- `continuity_setup` — seeds planted here for future payoff

### Step 2 — Scene Assembler (`scene_assembler.py`)

**Input:** `ChapterOutline` + scene registry → **Output:** `AssembledChapter`

No LLM call. For each beat: loads source file from `knowledge/scenes/`, runs keyword-token RAG across all `knowledge/` subdirectories, returns up to 10 ranked knowledge snippets per scene.

To upgrade RAG: replace `_rag_search()` with embedding similarity. `ScenePacket` interface unchanged.

### Step 3 — Chapter Weaver (`chapter_weaver.py`)

**Input:** `AssembledChapter` + render profile + optional POV override → **Output:** `WovenChapter`

One LLM call. Produces:
- `chapter_markdown` — full prose
- `beats[]` — `dialogue[]` with `speaker`, `line`, `emotion`, `action`, `subtext`, `ssml_hints`; `sensory_palette` (sight/sound/smell/touch/taste); `continuity_flags`; `missing_knowledge`

**The beat metadata is the key downstream asset** — feeds audiobook voice casting, GN scripts, animation storyboards.

### Step 4 — Artifact Exporter (`artifact_exporter.py`)

| Format | LLM call? | Output |
|--------|-----------|--------|
| `prose` | No | Clean markdown |
| `audiobook` | Yes | SSML-annotated script with speaker cast |
| `graphic_novel` | Yes | Page-by-panel script |
| `animation_storyboard` | Yes | Shot-by-shot with camera + music cues |

---

## 5. Knowledge base structure

```
knowledge/
├── MASTER-SYNOPSIS.md
├── universe-spec/                        # Immutable core rules
├── scenes/
│   ├── event_*.md                        # Scene narrative summaries
│   ├── choreography/choreo_event_*.md    # Detailed scene blocking
│   └── sensory/sensory_event_*.md        # Scene sensory primers
├── characters/
│   ├── char_*.md                         # Character bibles
│   ├── voice/voice_char_*.md             # Voice profiles ← CRITICAL for LLM
│   └── states/states_char_*.md           # State templates
├── locations/
│   ├── location_*.md                     # Layout and atmosphere
│   └── sensory/sensory_location_*.md     # Sensory primers ← CRITICAL for LLM
├── factions/                             # Organizations and agendas
├── factions-relationships/               # Cross-faction maps
├── technology/                           # Tech specs
├── ships/                                # Named vessels
├── magic-systems/                        # Rules and practitioners
├── timeline/
│   ├── timeline_master.md
│   └── scenes_temporal_map.md
└── review-queue/                         # Pending author decisions
```

**File ID convention:** `category_descriptor` — e.g. `char_jace_apollo`, `location_terminus`, `faction_origin_industries`. Lowercase, underscores.

**KB authoring rules:**
- Every character file needs a `voice/voice_char_*.md` companion (rhythm, register, sample lines, what they never say)
- Every location file should have a `sensory/sensory_location_*.md` companion
- Keep files 400–800 words — multiple focused files rank better in RAG
- Mark extrapolable content `[STORYBOT]`, required author decisions `TBD`, conflicts `[AUTHOR DECISION NEEDED]`

---

## 6. Control files

See inline schema comments in the YAML files themselves. Key points:

- **Scene IDs are stable slugs** — never use position numbers. Moving a scene between chapters edits `story-structure.yaml` only.
- **Order lives only in `story-structure.yaml`** — the registry is a dictionary of identities.
- **Render profiles are additive** — the same scene produces different renders without touching source files.

---

## 7. Render profiles and variants

| ID | Format | Tone |
|----|--------|------|
| `standard` | prose | Hard sci-fi intimate third person |
| `horror_variant` | prose | Amplify body horror in the science |
| `kids_variant` | prose | Middle-grade, wonder-forward |
| `nsfw` | prose | Adult — more latitude in gym/bar/medical |
| `audiobook_standard` | audiobook | SSML + speaker cast |
| `audiobook_action` | audiobook | Short sentences during action |
| `graphic_novel` | graphic_novel | Panel-by-panel script |
| `animation_storyboard` | animation | Shot-by-shot + music cues |

---

## 8. Versioning and pass types

`raw_draft → edit_pass_1 → edit_pass_2 → revised → polished → final`

Record a human edit (updates manifest, does not create a new file):
```python
from tools.storyops.version_manager import bump_pass_type
bump_pass_type("ch001", 1, "edit_pass_1", "Slowed the rover approach.")
```

---

## 9. Logging and diagnostics

Per job: `generated/logs/{job_id}.log` (human) + `generated/logs/{job_id}.jsonl` (structured JSONL).

Semantic event types: `llm_call`, `llm_response`, `scene_assembled`, `continuity_flag`, `missing_knowledge`, `version_saved`, `pipeline_complete`, `pipeline_error`.

---

## 10. LLM provider setup

```bash
STORYOPS_LLM_PROVIDER=openai    # openai | claude | ollama | mock
STORYOPS_LLM_MODEL=gpt-4o       # gpt-4o | gpt-4o-mini | claude-opus-4-6 | llama3.1:8b
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
OLLAMA_BASE_URL=http://127.0.0.1:11434
```

`gpt-4o` for prose (Step 3). `gpt-4o-mini` for planning (Step 1) at 10× lower cost. `claude-opus-4-6` for strong voice consistency.

---

## 11. Command reference

```bash
# Observe / lint
python -m tools.storyops.observe
python -m tools.storyops.lint --profile hard_scifi_novel
python -m tools.storyops.status_reporter

# Generation
python -m tools.storyops.artifact_generators --chapter ch001
python -m tools.storyops.artifact_generators --item gen_book01_ch004_horror
- **[AUTHOR DECISION NEEDED]:** Should `event_jace_messages_home` remain as a separate scene at a different time, or be merged into the gym scene?
# Agents / publish
python -m tools.storyops.agents --agent-id master_continuity
python -m tools.storyops.publish

# Import
python -m tools.storyops.importer <source>

# Local runner
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --run-generate true
```

---

## 12. CI / GitHub Actions / Scheduler

### GitHub Actions (`.github/workflows/`)

| Workflow | Trigger | Runs |
|----------|---------|------|
| `observe-knowledge.yml` | push to `knowledge/` | `observe` |
| `story-lint.yml` | push, PR | `lint --profile hard_scifi_novel` |
| `generate-content.yml` | manual dispatch | `artifact_generators` |
| `run-agents.yml` | scheduled / manual | `agents` |
| `build-viewer.yml` | push to `generated/` | `publish` |

### Cron (Linux/Mac)
```
*/5 * * * * cd /path/to/repo && python3 -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --run-generate true
```

### Windows PowerShell
```powershell
cd C:\path\to\repo
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --run-generate true
```

---

## 13. Extending StoryOps

- **New lint rule:** add under `tools/storyops/lint/rules/`, register in `registry.py`, configure in `control/lint-rules.yaml`
- **New render profile:** add to `control/render-profiles.yaml` — no code changes
- **New knowledge directory:** add to `KNOWLEDGE_ROOTS` in `scene_assembler.py`
- **Upgrade RAG:** replace `_rag_search()` in `scene_assembler.py`
- **New agent:** add to `tools/storyops/agents/`, register in dispatcher

---

## 14. VS Code debug setup

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run queue (ch001)",
      "type": "debugpy", "request": "launch",
      "module": "tools.storyops.artifact_generators",
      "args": ["--chapter", "ch001"],
      "cwd": "${workspaceFolder}", "justMyCode": false,
      "env": { "PYTHONPATH": "${workspaceFolder}" }
    },
    {
      "name": "Run single item",
      "type": "debugpy", "request": "launch",
      "module": "tools.storyops.artifact_generators",
      "args": ["--item", "gen_book01_ch001_standard_v1"],
      "cwd": "${workspaceFolder}", "justMyCode": false,
      "env": { "PYTHONPATH": "${workspaceFolder}" }
    },
    {
      "name": "Status reporter",
      "type": "debugpy", "request": "launch",
      "module": "tools.storyops.status_reporter",
      "cwd": "${workspaceFolder}", "justMyCode": false,
      "env": { "PYTHONPATH": "${workspaceFolder}" }
    },
    {
      "name": "Lint",
      "type": "debugpy", "request": "launch",
      "module": "tools.storyops.lint",
      "args": ["--profile", "hard_scifi_novel"],
      "cwd": "${workspaceFolder}", "justMyCode": false,
      "env": { "PYTHONPATH": "${workspaceFolder}" }
    }
  ]
}
```

---

## 15. Current status

### Pipeline
- ✅ Four-step pipeline (plan → assemble → weave → export)
- ✅ All four format exporters (prose, audiobook, GN, animation)
- ✅ POV override support
- ✅ Versioning with manifest and `bump_pass_type()`
- ✅ Dual structured logging (.log + .jsonl)
- ✅ Gap analysis and status reporter
- ✅ Mission control dashboard (amber/void-black, auto-refreshes)
- ✅ OpenAI SDK with fence-stripping, clear parse errors

### Knowledge base (book01)
- ✅ 22 scenes in scene-registry.yaml; 8 chapters in story-structure.yaml
- ✅ `location_terminus.md` — city overview, Terminus settlement
- ✅ `location_the_long_burn_bar.md` — sensory palette, atmosphere
- ✅ `location_mars_livestock_farm.md` — Cerberus scene setting
- ⚠️ Character bibles partially written — voiceprints missing
- ❌ `faction_origin_industries.md` — needed before ch007
- ❌ `voice_char_mei.md` — needed before Mei POV variants
- ❌ `MASTER-SYNOPSIS.md` — needs full authorial pass

### Site
- ✅ Dashboard: status grid, gaps, scene coverage, job log, log tail
- ❌ Public reader view
- ❌ Knowledge base explorer (D3 graph)
- ❌ Feedback capture UI

---

## 16. Roadmap

### Phase 1 — Stabilize (current)
Clean generation on ch001–ch004. Fill critical KB gaps. Establish editing workflow.

### Phase 2 — Site
- **Reader view** — latest prose, version selector, pass-type indicator
- **Knowledge explorer** — D3 force-directed graph. Nodes: characters, locations, scenes, chapters, factions. Missing nodes = hollow circles. Click → side panel with file preview.
- **Feedback capture** — inline passage flagging. Flags in `generated/feedback/{chapter_id}.json`. Resolved when fixed + timestamped.
- **Diff view** — side-by-side version comparison

### Phase 3 — Linting and Review
- KB cross-checker, voice consistency linter, timeline validator
- Continuity flag resolver (surface `.meta.json` flags in UI)
- Readability and dialogue density metrics per chapter/profile

### Phase 4 — Agent Architecture
- **Editor agent** — sentence-level proposals, structured diff
- **Tone agent** — emotional register vs. intended arc
- **Continuity agent** — KB cross-check, inconsistency list (no fixes)
- **Character emulator agents** — one per named character. POV generation and "what if" exploration.
- **Scene opponent agent** — simulate exchanges for negotiation and confrontation scenes
- **Orchestrator** — routes author requests, coordinates agents, returns structured results

### Phase 5 — Extra Tools
- Chapter/scene reorderer UI (writes `story-structure.yaml` directly)
- KB editor UI (form-based, validates required fields)
- Translation pipeline (render profile + language instruction)
- Glossary extractor (proper nouns across all chapters)
- Cover art prompt generator (sensory palette → stable diffusion prompts)

---

## 17. Next tasks — prioritized

### 🔴 Critical KB gaps (block next generation runs)

**1. `knowledge/factions/faction_origin_industries.md`** — needed before ch007. Corporate ethos, pricing contempt, rep/boss dynamic, "most expensive dog" setup.

**2. `knowledge/characters/voice/voice_char_mei.md`** — needed before any Mei POV variant. Minimal words, precise, no emoting, pauses before answers.

**3. `knowledge/timeline/scenes_temporal_map.md`** — cross-reference every scene ID to canonical date/time. Prevents planner from missequencing or creating knowledge-before-event errors.

### 🟡 Site: Knowledge explorer

**4. `site/knowledge-explorer.html`** — D3 force-directed graph reading `site/kb-graph.json` (pre-generated by Python from YAML + `knowledge/` scan). Missing nodes = hollow circles. Click = side panel. Best tool for orienting new contributors and future AI sessions.

### 🟢 Feedback layer

**5. Inline feedback in reader view** — highlight passage → flag dialog → `generated/feedback/{chapter_id}.json`. Status reporter includes flags in `report.json`. Mark resolved when addressed.

---

*Update this document when architecture changes. The version in the repo is always current.*
