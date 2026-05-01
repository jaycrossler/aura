# StoryOps MVP

StoryOps is a deterministic, local-first operations toolkit for **The Aura Chronicles** knowledge bank.

## What it does
- Observe repository story state and output status snapshots
- Run configurable linting rules and CI-safe checks
- Generate controlled Draft_v_1 content from queue items
- Produce agent proposal documents (never canon edits)
- Build static dashboard data for simple site viewing
- Poll remote Git changes and run StoryOps locally

## Safety model
- **canon**: `/knowledge`, `/manuscript` (human-approved only)
- **generated**: `/generated` (machine output; not canon)
- **proposed**: `/proposals` (agent suggestions only)

StoryOps does **not** auto-edit `/knowledge` or `/manuscript`.

## Commands
- `python -m tools.storyops.observe`
- `python -m tools.storyops.lint --profile hard_scifi_novel`
- `python -m tools.storyops.lint --path knowledge/scenes/book01-opening-notes.md`
- `python -m tools.storyops.generate --queue-id gen_book01_ch001_storybot_v2`
- `python -m tools.storyops.agents --agent-id master_continuity`
- `python -m tools.storyops.publish`
- `python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel`
- `python -m tools.storyops.local_runner --repo . --interval-seconds 300 --profile hard_scifi_novel`

## Validation expectations
Run modules independently:
1. observe
2. lint
3. generate
4. agents
5. publish
6. local_runner

Lint exits non-zero only when enabled error findings exist and `errors_fail_ci: true` in `control/lint-rules.yaml`.

## Cron / Scheduler
`*/5 * * * * cd /path/to/repo && /usr/bin/python3 -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --commit false --push false`

```powershell
cd C:\path\to\repo
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --commit false --push false
```

## GitHub Actions
See `.github/workflows/`:
- `observe-knowledge.yml`
- `story-lint.yml`
- `generate-content.yml`
- `run-agents.yml`
- `build-viewer.yml`

## Extending StoryOps
- New rule: add module under `tools/storyops/lint/rules/`, register in `registry.py`, configure in `control/lint-rules.yaml`
- New lint profile: edit `control/lint-profiles.yaml`
- New generation queue item: edit `control/generation-queue.yaml`
- Storybot chapter generation supports `mock` (default), `ollama`, `openai`, and `claude` via `tools/storyops/common/llm.py`.
- Generated chapter metadata is emitted next to each chapter as `*.meta.json` with dialogue/action/emotion beats for downstream audio/video pipelines.
- Configure with env vars: `STORYOPS_LLM_PROVIDER`, `STORYOPS_LLM_MODEL`, plus provider key (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) as needed.

## Knowledge Importer

- `python -m tools.storyops.importer <source>`
  - Imports knowledge markdown from a `.zip`, directory, or single markdown file
  - Supports concatenated markdown docs containing multiple frontmatter blocks
  - Routes files into `/knowledge/*` subfolders using frontmatter `type`/`id`
  - Merges by replacing existing files when incoming content is same or longer
  - Writes `generated/reports/import-report.json` and deletes source on success
