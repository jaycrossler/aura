# StoryOps Setup

## 1) Local install
1. Clone repo and enter it.
2. Install dependencies:
   - `python -m pip install -r requirements.txt`
3. Smoke run:
   - `python -m tools.storyops.observe`
   - `python -m tools.storyops.lint --profile hard_scifi_novel`
   - `python -m tools.storyops.generate`
   - `python -m tools.storyops.agents`
   - `python -m tools.storyops.publish`

## 2) Run on every GitHub repo change (local machine)
Use `local_runner` from cron / Task Scheduler. It checks remote updates, fast-forwards local branch, and runs observe+lint safely.

### Linux/macOS cron
`*/5 * * * * cd /path/to/repo && /usr/bin/python3 -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --commit false --push false`

### Windows Task Scheduler (PowerShell)
```powershell
cd C:\path\to\repo
python -m tools.storyops.local_runner --repo . --once --profile hard_scifi_novel --commit false --push false
```

## 3) Add or change linters
- Rule implementations: `tools/storyops/lint/rules/...`
- Registry: `tools/storyops/lint/registry.py`
- Rule config + severity: `control/lint-rules.yaml`
- Profile composition: `control/lint-profiles.yaml`

## 4) Local Ollama / cloud AI wiring (optional)
StoryOps MVP is deterministic and does not require LLMs. To add optional LLM calls:

1. Add provider config in `control/project.yaml` (e.g. `llm.provider: ollama|cloud`).
2. Implement provider functions in `tools/storyops/common/llm.py`.
3. For Ollama local:
   - run Ollama service locally
   - call local endpoint from `llm.py` (e.g. `http://localhost:11434`)
4. For cloud APIs:
   - read API key from environment variables
   - keep generation/agent outputs in `generated/` or `proposals/`
   - never auto-edit `/knowledge` or `/manuscript`

Recommended model routing pattern:
- small/local checks → Ollama
- larger synthesis prompts → cloud provider
- always include deterministic fallback path when provider unavailable
