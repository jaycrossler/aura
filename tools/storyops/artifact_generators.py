"""
Artifact Generators — top-level dispatcher for the generation queue.

Routes each queue item to the appropriate generator based on `kind`.
This is the main entry point called by the queue runner.

Supported kinds:
  chapter_draft   → full 4-step pipeline (plan → assemble → weave → export)
  status_report   → regenerate report.json and dashboard HTML

Usage (run a single item):
    from tools.storyops.artifact_generators import run_item
    result = run_item(item)

Usage (run the full queue):
    python -m tools.storyops.artifact_generators
"""

from __future__ import annotations

import sys
from typing import Any

from tools.storyops.chapter_generator import generate_chapter
from tools.storyops.status_reporter import generate_report, print_gap_report
from tools.storyops.load_generation_queue import load_queue


# ── Dispatcher ────────────────────────────────────────────────────────────────

def run_item(item: dict[str, Any], force_overwrite: bool = False) -> str | None:
    """
    Route a single queue item to the correct generator.

    Returns:
        Output file path (for chapter_draft), or None (for status_report / skipped).
    """
    kind = item.get("kind", "chapter_draft")

    if kind == "chapter_draft" and force_overwrite:
        item = {**item, "overwrite": True}

    if kind == "chapter_draft":
        return generate_chapter(item)

    elif kind == "status_report":
        report = generate_report()
        print_gap_report(report)
        return None

    else:
        print(f"[artifact_generators] Unknown kind '{kind}' for item '{item.get('id')}' — skipping.")
        return None


# ── Queue runner ──────────────────────────────────────────────────────────────

def run_queue(
    kind:       str | None = None,
    chapter_id: str | None = None,
    include_disabled: bool = False,
    force_overwrite: bool = False,
) -> list[str]:
    """
    Run all enabled items in the queue with optional filters.

    Returns list of output file paths that were generated.
    """
    items = load_queue(kind=kind, chapter_id=chapter_id, include_disabled=include_disabled)
    print(f"[artifact_generators] Running {len(items)} item(s).")

    results = []
    for i, item in enumerate(items):
        print(f"\n[artifact_generators] [{i+1}/{len(items)}] {item['id']}")
        try:
            out = run_item(item, force_overwrite=force_overwrite)
            if out:
                results.append(out)
                print(f"[artifact_generators] ✓ {out}")
            else:
                print(f"[artifact_generators] – skipped / no output")
        except Exception as exc:
            print(f"[artifact_generators] ✗ ERROR on '{item['id']}': {exc}")
            # Continue to next item rather than aborting the run
            continue

    print(f"\n[artifact_generators] Done. {len(results)} artifact(s) generated.")
    return results


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the StoryOps generation queue")
    parser.add_argument("--kind",       default=None, help="Filter by kind (chapter_draft, status_report)")
    parser.add_argument("--chapter",    default=None, help="Filter by chapter_id (e.g. ch001) or 'all'")
    parser.add_argument("--item",       default=None, help="Run a specific item by id")
    parser.add_argument("--include-disabled", action="store_true", help="Include disabled queue items in filtered runs")
    parser.add_argument("--force-overwrite", action="store_true", help="Override queue overwrite=false for chapter_draft jobs")
    args = parser.parse_args()

    if args.item:
        # Run a single named item (regardless of enabled flag)
        from tools.storyops.load_generation_queue import load_all
        all_items = load_all(include_disabled=True)
        matching  = [i for i in all_items if i["id"] == args.item]
        if not matching:
            print(f"Item '{args.item}' not found in queue.")
            sys.exit(1)
        run_item(matching[0], force_overwrite=args.force_overwrite)
    else:
        chapter_filter = None if args.chapter in (None, "all", "ALL") else args.chapter
        include_disabled = chapter_filter is not None
        run_queue(
            kind=args.kind,
            chapter_id=chapter_filter,
            include_disabled=include_disabled,
            force_overwrite=args.force_overwrite,
        )
