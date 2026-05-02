"""
Status Reporter — generates gap reports and the dashboard data file.

Run this any time to get a full picture of what's been generated, what's missing,
what needs editing, and what the log tail looks like.

Outputs:
  generated/status/report.json   — machine-readable full report (read by dashboard)
  console                        — human-readable summary with gap list

Usage:
  python -m tools.storyops.status_reporter          # generate report + print
  python -m tools.storyops.status_reporter --quiet  # generate report only
"""

from __future__ import annotations

import json
import argparse
import datetime as dt
from pathlib import Path
from typing import Any

from tools.storyops.common.config import load_yaml
from tools.storyops.version_manager import list_versions, VERSIONS_ROOT, PASS_TYPE_ORDER


STRUCTURE_PATH = Path("control/story-structure.yaml")
REGISTRY_PATH  = Path("control/scene-registry.yaml")
PROFILES_PATH  = Path("control/render-profiles.yaml")
REPORT_DIR     = Path("generated/status")
REPORT_JSON    = REPORT_DIR / "report.json"
LOG_DIR        = Path("generated/logs")


# ── Chapter status ────────────────────────────────────────────────────────────

def _chapter_status(chapter_id: str) -> dict[str, Any]:
    """Derive current chapter status from its version manifest."""
    versions = list_versions(chapter_id)
    if not versions:
        return {
            "status":              "not_started",
            "version_count":       0,
            "latest_version":      None,
            "latest_file":         None,
            "latest_pass_type":    "not_started",
            "latest_generated_at": None,
            "latest_word_count":   0,
            "formats_generated":   [],
            "pov_variants":        [],
            "versions":            [],
        }

    prose_versions = [v for v in versions if v.format == "prose"]
    latest = prose_versions[-1] if prose_versions else versions[-1]
    formats = sorted({v.format for v in versions})
    povs    = sorted({v.pov for v in versions})

    return {
        "status":              latest.pass_type,
        "version_count":       len(versions),
        "latest_version":      latest.version_num,
        "latest_file":         latest.file_path,
        "latest_pass_type":    latest.pass_type,
        "latest_generated_at": latest.generated_at,
        "latest_word_count":   latest.word_count,
        "formats_generated":   formats,
        "pov_variants":        povs,
        "versions": [
            {
                "version_num":   v.version_num,
                "pass_type":     v.pass_type,
                "format":        v.format,
                "pov":           v.pov,
                "word_count":    v.word_count,
                "beat_count":    v.beat_count,
                "generated_at":  v.generated_at,
                "file_path":     v.file_path,
                "source_hash":   v.source_hash,
                "note":          v.note,
            }
            for v in versions
        ],
    }


# ── Scene coverage ────────────────────────────────────────────────────────────

def _scene_coverage(
    structure: dict[str, Any],
    registry: dict[str, Any],
) -> dict[str, Any]:
    """Identify scene registration / assignment gaps."""
    registry_ids  = set(registry.keys())
    structured_ids: set[str] = set()
    for ch in structure.get("chapters", []):
        for sid in ch.get("scenes", []):
            structured_ids.add(sid)

    # Status breakdown from registry
    status_counts: dict[str, int] = {}
    for entry in registry.values():
        s = entry.get("status", "unknown")
        status_counts[s] = status_counts.get(s, 0) + 1

    return {
        "total_in_registry":             len(registry_ids),
        "total_in_structure":            len(structured_ids),
        "in_registry_not_structured":    sorted(registry_ids - structured_ids),
        "in_structure_not_registry":     sorted(structured_ids - registry_ids),
        "status_counts":                 status_counts,
        "scene_statuses": {
            sid: entry.get("status", "unknown")
            for sid, entry in registry.items()
        },
    }


# ── Log reading ───────────────────────────────────────────────────────────────

def _log_tail(lines: int = 50) -> list[str]:
    """Return last N lines of the most recently modified log file."""
    if not LOG_DIR.exists():
        return []
    logs = sorted(
        LOG_DIR.glob("*.log"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not logs:
        return []
    all_lines = logs[0].read_text(encoding="utf-8").splitlines()
    return all_lines[-lines:]


def _recent_jobs(limit: int = 10) -> list[dict]:
    """Summarize recent job logs from JSONL files."""
    if not LOG_DIR.exists():
        return []
    jsonl_files = sorted(
        LOG_DIR.glob("*.jsonl"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )[:limit]

    jobs = []
    for path in jsonl_files:
        lines = path.read_text(encoding="utf-8").splitlines()
        complete = errors = None
        for line in reversed(lines):
            try:
                record = json.loads(line)
                event  = record.get("data", {}).get("event", "")
                if not complete and event == "pipeline_complete":
                    complete = record
                if not errors and record.get("level") == "ERROR":
                    errors = record
            except Exception:
                pass
        jobs.append({
            "job_id":     path.stem,
            "modified_at": dt.datetime.fromtimestamp(
                path.stat().st_mtime, tz=dt.timezone.utc
            ).isoformat(),
            "completed":  complete is not None,
            "output_file": complete.get("data", {}).get("output_file") if complete else None,
            "duration_secs": complete.get("data", {}).get("duration_secs") if complete else None,
            "had_errors": errors is not None,
            "error_msg":  errors.get("msg") if errors else None,
        })
    return jobs


# ── Gap analysis ──────────────────────────────────────────────────────────────

def _compute_gaps(
    chapter_reports: list[dict],
    scene_coverage:  dict[str, Any],
) -> list[dict]:
    gaps = []

    for ch in chapter_reports:
        if ch["status"] == "not_started":
            gaps.append({
                "severity":   "high",
                "type":       "chapter_not_started",
                "chapter_id": ch["chapter_id"],
                "title":      ch["chapter_title"],
                "detail":     "No versions generated yet.",
            })
        elif PASS_TYPE_ORDER.get(ch["status"], 0) < PASS_TYPE_ORDER.get("edit_pass_1", 1):
            gaps.append({
                "severity":   "medium",
                "type":       "chapter_raw_draft_only",
                "chapter_id": ch["chapter_id"],
                "title":      ch["chapter_title"],
                "detail":     f"Only {ch['version_count']} raw draft version(s) — no edits recorded.",
            })

        # Flag chapters with continuity flags in their latest meta
        latest_file = ch.get("latest_file")
        if latest_file:
            meta_path = Path(latest_file).with_suffix(".meta.json")
            if meta_path.exists():
                try:
                    meta = json.loads(meta_path.read_text(encoding="utf-8"))
                    flags = meta.get("continuity_flags", [])
                    if flags:
                        gaps.append({
                            "severity":   "medium",
                            "type":       "continuity_flags",
                            "chapter_id": ch["chapter_id"],
                            "title":      ch["chapter_title"],
                            "detail":     f"{len(flags)} continuity flag(s): {'; '.join(flags[:3])}",
                        })
                    missing_k = meta.get("missing_knowledge", [])
                    if missing_k:
                        gaps.append({
                            "severity":   "low",
                            "type":       "missing_knowledge",
                            "chapter_id": ch["chapter_id"],
                            "title":      ch["chapter_title"],
                            "detail":     f"LLM requested: {'; '.join(missing_k[:3])}",
                        })
                except Exception:
                    pass

    for sid in scene_coverage["in_structure_not_registry"]:
        gaps.append({
            "severity": "high",
            "type":     "scene_missing_from_registry",
            "scene_id": sid,
            "detail":   "Referenced in story-structure.yaml but not defined in scene-registry.yaml.",
        })

    for sid in scene_coverage["in_registry_not_structured"]:
        gaps.append({
            "severity": "low",
            "type":     "scene_not_assigned_to_chapter",
            "scene_id": sid,
            "detail":   "Defined in registry but not assigned to any chapter.",
        })

    return gaps


# ── Main report builder ───────────────────────────────────────────────────────

def generate_report() -> dict[str, Any]:
    """Build the full status report and write report.json."""
    structure = load_yaml(STRUCTURE_PATH) if STRUCTURE_PATH.exists() else {}
    chapters  = structure.get("chapters", [])

    raw_registry = load_yaml(REGISTRY_PATH) if REGISTRY_PATH.exists() else {}
    registry: dict[str, Any] = {s["id"]: s for s in raw_registry.get("scenes", [])}

    raw_profiles = load_yaml(PROFILES_PATH) if PROFILES_PATH.exists() else {}
    profiles     = [p["id"] for p in raw_profiles.get("profiles", [])]

    # Build per-chapter reports
    chapter_reports = []
    total_words     = 0
    for ch in chapters:
        ch_id  = ch["id"]
        status = _chapter_status(ch_id)
        total_words += status.get("latest_word_count", 0)
        chapter_reports.append({
            "chapter_id":    ch_id,
            "chapter_title": ch.get("title", ""),
            "subtitle":      ch.get("subtitle", ""),
            "pov_default":   ch.get("pov_default"),
            "timeline_span": ch.get("timeline_span"),
            "tone_notes":    (ch.get("tone_notes", "") or "")[:200],
            "pacing":        ch.get("pacing"),
            "target_word_count": ch.get("target_word_count"),
            "scene_ids":     ch.get("scenes", []),
            "scene_count":   len(ch.get("scenes", [])),
            **status,
        })

    scene_coverage = _scene_coverage(structure, registry)
    gaps           = _compute_gaps(chapter_reports, scene_coverage)
    recent_jobs    = _recent_jobs()

    # Summary
    summary = {
        "chapters_not_started":  sum(1 for c in chapter_reports if c["status"] == "not_started"),
        "chapters_raw_draft":    sum(1 for c in chapter_reports if c["status"] == "raw_draft"),
        "chapters_edit_pass_1":  sum(1 for c in chapter_reports if c["status"] == "edit_pass_1"),
        "chapters_edit_pass_2":  sum(1 for c in chapter_reports if c["status"] == "edit_pass_2"),
        "chapters_revised":      sum(1 for c in chapter_reports if c["status"] == "revised"),
        "chapters_polished":     sum(1 for c in chapter_reports if c["status"] == "polished"),
        "chapters_final":        sum(1 for c in chapter_reports if c["status"] == "final"),
        "total_words_latest":    total_words,
        "gaps_high":             sum(1 for g in gaps if g["severity"] == "high"),
        "gaps_medium":           sum(1 for g in gaps if g["severity"] == "medium"),
        "gaps_low":              sum(1 for g in gaps if g["severity"] == "low"),
    }

    report = {
        "generated_at":    dt.datetime.now(dt.timezone.utc).isoformat(),
        "book_id":         structure.get("book", "unknown"),
        "total_chapters":  len(chapters),
        "render_profiles": profiles,
        "summary":         summary,
        "chapters":        chapter_reports,
        "scene_coverage":  scene_coverage,
        "gaps":            gaps,
        "recent_jobs":     recent_jobs,
        "log_tail":        _log_tail(lines=60),
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


# ── Console printer ───────────────────────────────────────────────────────────

PASS_BARS = {
    "not_started":  "░░░░░░",
    "raw_draft":    "█░░░░░",
    "edit_pass_1":  "██░░░░",
    "edit_pass_2":  "███░░░",
    "revised":      "████░░",
    "polished":     "█████░",
    "final":        "██████",
}
SEVERITY_ICONS = {"high": "🔴", "medium": "🟡", "low": "🔵"}


def print_gap_report(report: dict[str, Any] | None = None) -> None:
    if report is None:
        report = generate_report()

    s = report["summary"]
    print(f"\n{'═'*64}")
    print(f"  STORYOPS — {report['book_id'].upper()}  |  {report['generated_at'][:19]}")
    print(f"{'═'*64}")
    print(f"  Chapters : {report['total_chapters']}  |  Words (latest): {s['total_words_latest']:,}")
    print(f"  Gaps     : 🔴 {s['gaps_high']}  🟡 {s['gaps_medium']}  🔵 {s['gaps_low']}")
    print(f"{'─'*64}")

    print("  CHAPTER STATUS")
    for ch in report["chapters"]:
        bar     = PASS_BARS.get(ch["status"], "░░░░░░")
        wc      = f"{ch['latest_word_count']:>5,}w" if ch["latest_word_count"] else "    --"
        fmts    = ",".join(ch["formats_generated"]) or "none"
        print(f"  [{bar}] {ch['chapter_id']:<8} {ch['status']:<14} {wc}  {ch['chapter_title']}")
        if ch["formats_generated"] and ch["formats_generated"] != ["prose"]:
            print(f"           {'':8} formats: {fmts}")

    if report["gaps"]:
        print(f"\n{'─'*64}")
        print(f"  GAPS ({len(report['gaps'])})")
        for gap in report["gaps"]:
            icon   = SEVERITY_ICONS.get(gap["severity"], "•")
            target = gap.get("chapter_id") or gap.get("scene_id", "?")
            print(f"  {icon}  [{gap['type']}] {target}")
            print(f"       {gap['detail']}")

    if report["recent_jobs"]:
        print(f"\n{'─'*64}")
        print("  RECENT JOBS")
        for job in report["recent_jobs"][:5]:
            status = "✓" if job["completed"] else ("✗" if job["had_errors"] else "…")
            dur    = f"{job['duration_secs']:.1f}s" if job["duration_secs"] else "--"
            print(f"  {status} {job['job_id']:<38} {dur}")

    print(f"\n  Report written to {REPORT_JSON}")
    print(f"{'═'*64}\n")


# ── CLI entry ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate StoryOps status report")
    parser.add_argument("--quiet", action="store_true", help="Write report.json without console output")
    args = parser.parse_args()

    if args.quiet:
        generate_report()
    else:
        print_gap_report()
