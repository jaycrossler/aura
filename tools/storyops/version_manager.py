"""
Version Manager — manages versioned chapter artifacts.

Each chapter can have many versions (v001, v002, ...).
Each version has a pass_type label that tracks where it is in the editing lifecycle.
A manifest JSON per chapter tracks all versions.

Pass type lifecycle:
  raw_draft     → first generated output, untouched
  edit_pass_1   → first human or directed LLM edit
  edit_pass_2   → second edit pass
  revised       → post-structural revision (scene moved, POV changed, etc.)
  polished      → line-level polish / copy edit
  final         → locked

To record a human edit: call bump_pass_type() with the new pass_type and an optional note.
The version file itself is unchanged; the manifest records the upgrade.

File layout:
  generated/drafts/{chapter_id}/v001.md
  generated/drafts/{chapter_id}/v001.meta.json
  generated/drafts/{chapter_id}/v001_audiobook.md        (format variants)
  generated/drafts/{chapter_id}/v002.md
  ...
  generated/versions/{chapter_id}_manifest.json
"""

from __future__ import annotations

import json
import hashlib
import datetime as dt
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

from tools.storyops.common.story_logger import StoryLogger


VERSIONS_ROOT = Path("generated/versions")
DRAFTS_ROOT   = Path("generated/drafts")

# Ordered pass types — higher index = further along
PASS_TYPES = [
    "raw_draft",
    "edit_pass_1",
    "edit_pass_2",
    "revised",
    "polished",
    "final",
]
PASS_TYPE_ORDER = {p: i for i, p in enumerate(PASS_TYPES)}


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class VersionRecord:
    version_num:       int
    chapter_id:        str
    file_path:         str
    meta_path:         str
    generated_at:      str
    queue_item_id:     str
    render_profile_id: str
    pov:               str
    format:            str
    pass_type:         str
    source_hash:       str
    word_count:        int
    beat_count:        int
    note:              str = ""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _hash_sources(source_files: list[str]) -> str:
    """Stable 12-char hash of the sorted source file list."""
    h = hashlib.sha256()
    for f in sorted(source_files):
        h.update(f.encode())
    return h.hexdigest()[:12]


def _manifest_path(chapter_id: str) -> Path:
    return VERSIONS_ROOT / f"{chapter_id}_manifest.json"


def _load_manifest(chapter_id: str) -> dict[str, Any]:
    path = _manifest_path(chapter_id)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"chapter_id": chapter_id, "versions": []}


def _save_manifest(chapter_id: str, manifest: dict[str, Any]) -> None:
    VERSIONS_ROOT.mkdir(parents=True, exist_ok=True)
    _manifest_path(chapter_id).write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _fmt_suffix(fmt: str) -> str:
    """File suffix for non-prose formats."""
    return "" if fmt == "prose" else f"_{fmt}"


# ── Public API ────────────────────────────────────────────────────────────────

def save_version(
    chapter_id:        str,
    content:           str,
    meta:              dict[str, Any],
    queue_item_id:     str,
    render_profile_id: str,
    pov:               str,
    fmt:               str,
    source_files:      list[str],
    word_count:        int,
    beat_count:        int,
    log:               StoryLogger,
    pass_type:         str = "raw_draft",
    note:              str = "",
) -> VersionRecord:
    """
    Save a versioned chapter artifact and update the chapter manifest.

    Returns the VersionRecord for the saved version.
    """
    manifest    = _load_manifest(chapter_id)
    existing    = manifest.get("versions", [])

    # Count versions of THIS format to get the version number
    fmt_versions = [v for v in existing if v.get("format") == fmt]
    version_num  = len(fmt_versions) + 1

    # Output paths
    output_dir = DRAFTS_ROOT / chapter_id
    output_dir.mkdir(parents=True, exist_ok=True)

    suffix    = _fmt_suffix(fmt)
    file_path = output_dir / f"v{version_num:03d}{suffix}.md"
    meta_path = output_dir / f"v{version_num:03d}{suffix}.meta.json"

    now         = dt.datetime.now(dt.timezone.utc).isoformat()
    source_hash = _hash_sources(source_files)

    # Write content with YAML frontmatter
    frontmatter_lines = [
        "---",
        f"id: {chapter_id}",
        f"version: {version_num}",
        f"pass_type: {pass_type}",
        f"pov: {pov}",
        f"format: {fmt}",
        f"render_profile: {render_profile_id}",
        f"generated_at: '{now}'",
        f"source_hash: {source_hash}",
        f"word_count: {word_count}",
        f"beat_count: {beat_count}",
        "---",
        "",
    ]
    file_path.write_text("\n".join(frontmatter_lines) + content + "\n", encoding="utf-8")

    # Write metadata sidecar
    meta_out = {
        **meta,
        "version_num":  version_num,
        "generated_at": now,
        "source_hash":  source_hash,
        "pass_type":    pass_type,
    }
    meta_path.write_text(json.dumps(meta_out, indent=2), encoding="utf-8")

    record = VersionRecord(
        version_num       = version_num,
        chapter_id        = chapter_id,
        file_path         = str(file_path),
        meta_path         = str(meta_path),
        generated_at      = now,
        queue_item_id     = queue_item_id,
        render_profile_id = render_profile_id,
        pov               = pov,
        format            = fmt,
        pass_type         = pass_type,
        source_hash       = source_hash,
        word_count        = word_count,
        beat_count        = beat_count,
        note              = note,
    )

    existing.append(asdict(record))
    manifest["versions"]          = existing
    manifest["latest_version"]    = version_num
    manifest["latest_file"]       = str(file_path)
    manifest["latest_pass_type"]  = pass_type
    manifest["latest_word_count"] = word_count
    _save_manifest(chapter_id, manifest)

    log.version_saved(version_num, str(file_path), pass_type, word_count)
    return record


def get_latest(chapter_id: str, fmt: str = "prose") -> VersionRecord | None:
    """Get the most recent version record for this chapter/format."""
    manifest = _load_manifest(chapter_id)
    versions = [v for v in manifest.get("versions", []) if v.get("format") == fmt]
    if not versions:
        return None
    return VersionRecord(**versions[-1])


def list_versions(chapter_id: str) -> list[VersionRecord]:
    """Return all version records for this chapter across all formats."""
    manifest = _load_manifest(chapter_id)
    return [VersionRecord(**v) for v in manifest.get("versions", [])]


def bump_pass_type(
    chapter_id:    str,
    version_num:   int,
    new_pass_type: str,
    note:          str = "",
) -> None:
    """
    Record that a version has been worked on (human edit, LLM revision, etc.).
    Updates the manifest only — does not create a new file.

    Call this after manually editing a generated file:
        bump_pass_type("ch004", 1, "edit_pass_1", "Slowed down the corridor walk.")
    """
    if new_pass_type not in PASS_TYPES:
        raise ValueError(f"Unknown pass_type '{new_pass_type}'. Valid: {PASS_TYPES}")

    manifest = _load_manifest(chapter_id)
    updated  = False
    for v in manifest.get("versions", []):
        if v["version_num"] == version_num:
            v["pass_type"] = new_pass_type
            if note:
                v["note"] = note
            updated = True
            break

    if not updated:
        raise ValueError(f"Version {version_num} not found for chapter '{chapter_id}'")

    # Update manifest summary if this is the latest version
    latest_versions = manifest.get("versions", [])
    if latest_versions and latest_versions[-1]["version_num"] == version_num:
        manifest["latest_pass_type"] = new_pass_type

    _save_manifest(chapter_id, manifest)


def get_latest_prose_file(chapter_id: str) -> str | None:
    """Convenience: return the file path of the latest prose version, or None."""
    rec = get_latest(chapter_id, fmt="prose")
    return rec.file_path if rec else None
