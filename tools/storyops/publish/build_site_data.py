from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from tools.storyops.common.jsonl import write_json


def _load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def _parse_inventory_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| knowledge/"):
            continue
        parts = [piece.strip() for piece in line.strip("|").split("|")]
        if len(parts) != 3:
            continue
        file_path, word_count_raw, frontmatter = parts
        try:
            word_count = int(word_count_raw)
        except ValueError:
            continue
        category = Path(file_path).parts[1] if len(Path(file_path).parts) > 1 else "root"
        rows.append(
            {
                "file": file_path,
                "category": category,
                "words": word_count,
                "frontmatter": frontmatter.lower() == "yes",
            }
        )
    return rows


def build() -> None:
    story_state = _load_json(Path("generated/status/story_state.json"), {})
    lint_summary = _load_json(Path("generated/lint/lint-summary.json"), {})
    lint_results = _load_json(Path("generated/lint/lint-results.json"), [])
    progress_log_lines = Path("generated/status/progress_log.jsonl").read_text(encoding="utf-8").splitlines() if Path("generated/status/progress_log.jsonl").exists() else []
    inventory_rows = _parse_inventory_rows(Path("generated/reports/knowledge_inventory.md"))

    category_counter = Counter(row["category"] for row in inventory_rows)
    inventory_summary = {
        "total_files": len(inventory_rows),
        "files_with_frontmatter": sum(1 for row in inventory_rows if row["frontmatter"]),
        "files_missing_frontmatter": sum(1 for row in inventory_rows if not row["frontmatter"]),
        "total_words": sum(row["words"] for row in inventory_rows),
        "categories": dict(category_counter),
    }

    lint_by_file: dict[str, int] = {}
    for finding in lint_results:
        lint_file = str(finding.get("file", "unknown")).replace("\\", "/")
        lint_by_file[lint_file] = lint_by_file.get(lint_file, 0) + 1

    dashboard = {
        "story_state": story_state,
        "lint_summary": lint_summary,
        "inventory_summary": inventory_summary,
        "inventory_rows": inventory_rows,
        "lint_findings_count": len(lint_results),
        "lint_by_file": dict(sorted(lint_by_file.items(), key=lambda item: item[1], reverse=True)[:50]),
        "progress_log_entries": len(progress_log_lines),
        "log_paths": {
            "local_runner": "generated/logs/local-runner.log",
            "lint_summary": "generated/lint/lint-summary.md",
            "inventory_report": "generated/reports/knowledge_inventory.md",
        },
    }

    write_json(Path("generated/site-data/dashboard.json"), dashboard)


if __name__ == "__main__":
    build()
