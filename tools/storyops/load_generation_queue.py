"""
Queue loader — reads control/generation-queue.yaml and returns enabled items.

The new queue format references chapter_id and render_profile instead of
raw output_file paths. The runner (artifact_generators.py) dispatches by kind.

Usage:
    from tools.storyops.load_generation_queue import load_queue
    for item in load_queue():
        print(item["id"], item["chapter_id"])

Filters:
    load_queue()                          # all enabled items
    load_queue(kind="chapter_draft")      # by job kind
    load_queue(chapter_id="ch001")        # by chapter
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.storyops.common.config import load_yaml

QUEUE_PATH = Path("control/generation-queue.yaml")


def load_queue(
    kind:       str | None = None,
    chapter_id: str | None = None,
) -> list[dict[str, Any]]:
    """
    Load and return enabled queue items, with optional filtering.

    Args:
        kind:        If set, return only items where item["kind"] == kind
        chapter_id:  If set, return only items for this chapter_id

    Returns:
        List of queue item dicts (enabled=True items only).
    """
    raw   = load_yaml(QUEUE_PATH)
    items = raw.get("queue", [])

    result = []
    for item in items:
        if not item.get("enabled", True):
            continue
        if kind and item.get("kind") != kind:
            continue
        if chapter_id and item.get("chapter_id") != chapter_id:
            continue
        result.append(item)

    return result


def load_all(include_disabled: bool = False) -> list[dict[str, Any]]:
    """Return all items, optionally including disabled ones."""
    raw   = load_yaml(QUEUE_PATH)
    items = raw.get("queue", [])
    if include_disabled:
        return items
    return [i for i in items if i.get("enabled", True)]
