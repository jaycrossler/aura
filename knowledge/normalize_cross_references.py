#!/usr/bin/env python3
"""
normalize_cross_references.py — Pass 1 KB hygiene: link format normalization

Rewrites every `cross_references:` entry in every .md file's frontmatter to
Obsidian wiki-link format: [[stem]]  (no path prefix, no .md extension, no
quotes). This is the only cross_references format Obsidian's graph view will
actually render as an edge, and it parses cleanly through build_tree.py's
existing stem-extraction logic.

Run from the repo root (the directory that contains knowledge/, or adjust
ROOT below):

    python3 normalize_cross_references.py --dry-run     # preview only
    python3 normalize_cross_references.py                # apply changes
    python3 normalize_cross_references.py --report-only  # broken-link audit, no writes

What it does:
  1. Walks every .md file under the KB root (skips templates/, review-queue
     notes, and the script/index files themselves).
  2. Parses the cross_references: list in frontmatter regardless of source
     format: 'char_kael', "char_kael", [char_kael], [[char_kael]],
     characters/char_kael.md, char_kael — all normalize to the same stem.
  3. Rewrites the list as:
         cross_references:
           - "[[char_kael]]"
           - "[[arc_01_falcon_fortuna]]"
  4. Validates each resulting stem against the real set of filenames in the
     repo. Entries that don't resolve to any actual file are NOT silently
     dropped — they're left in place (still normalized in format) and listed
     in the broken-links report for a human to resolve, since guessing the
     intended target is exactly the kind of silent-resolution this KB's
     workflow rules out.
  5. Leaves all other frontmatter fields and the file body untouched.
  6. Writes a summary report to stdout and a full report to
     ./cleanup_reports/normalize_cross_references_<date>.md

Does NOT touch: [Skill] brackets, {AI} braces, non-cross_references fields,
file bodies, or files outside cross_references frontmatter.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(".").resolve()  # run from inside knowledge/ (same convention as build_tree.py)

SKIP_DIR_PREFIXES = ("templates", ".git", "review-queue")
SKIP_FILE_PREFIXES = ("_index", "build_tree", "README")

XREF_LINE_RE = re.compile(r"^\s*cross_references:\s*$")
LIST_ITEM_RE = re.compile(r"^(\s*-\s*)(.+?)\s*$")


def extract_stem(raw: str) -> str:
    """
    Reduce any supported source format to a bare stem.
    Handles: 'x', "x", [x], [[x]], path/x.md, x
    """
    s = raw.strip()
    s = s.strip("'\"")          # strip surrounding quotes
    s = s.strip()
    s = s.strip("[]")           # strip single or doubled brackets (both ends)
    s = s.strip()
    s = s.strip("'\"")          # some files quote INSIDE the brackets: [['x']]
    p = Path(s)
    stem = p.stem if p.suffix else p.name
    # strip any leftover path separators if stem still has them (rare malformed case)
    stem = stem.split("/")[-1]
    return stem.strip()


def should_skip(rel: Path) -> bool:
    parts = rel.parts
    if any(part.startswith(SKIP_DIR_PREFIXES) for part in parts[:-1]):
        return True
    if any(parts[-1].startswith(p) for p in SKIP_FILE_PREFIXES):
        return True
    return False


def find_frontmatter_bounds(lines: list[str]) -> tuple[int, int] | None:
    """Return (start, end) line indices of the frontmatter block (exclusive of --- markers)."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return (1, i)
    return None


def normalize_file(path: Path, all_stems: set[str]) -> dict:
    """
    Returns a dict describing what changed:
      {changed: bool, before: [...], after: [...], broken: [...]}
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    bounds = find_frontmatter_bounds(lines)
    if not bounds:
        return {"changed": False, "before": [], "after": [], "broken": []}

    start, end = bounds

    xref_start = None
    for i in range(start, end):
        if XREF_LINE_RE.match(lines[i]):
            xref_start = i
            break
    if xref_start is None:
        return {"changed": False, "before": [], "after": [], "broken": []}

    # Collect the list items following cross_references:
    item_lines = []
    i = xref_start + 1
    while i < end and LIST_ITEM_RE.match(lines[i]) and lines[i].lstrip().startswith("-"):
        item_lines.append(i)
        i += 1
    xref_end = i  # exclusive

    before_raw = []
    stems = []
    for ln_idx in item_lines:
        m = LIST_ITEM_RE.match(lines[ln_idx])
        raw_item = m.group(2)
        before_raw.append(raw_item)
        stems.append(extract_stem(raw_item))

    normalized = [f'  - "[[{stem}]]"' for stem in stems]
    after_raw = [f"[[{stem}]]" for stem in stems]

    broken = [stem for stem in stems if stem and stem not in all_stems]

    changed = before_raw != after_raw
    if changed:
        new_lines = lines[:xref_start + 1] + normalized + lines[xref_end:]
        new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
        path.write_text(new_text, encoding="utf-8")

    return {"changed": changed, "before": before_raw, "after": after_raw, "broken": broken}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Show what would change, write nothing")
    ap.add_argument("--report-only", action="store_true", help="Only audit broken links, write nothing")
    args = ap.parse_args()
    write_mode = not (args.dry_run or args.report_only)

    md_files = [p for p in sorted(ROOT.rglob("*.md")) if not should_skip(p.relative_to(ROOT))]
    all_stems = {p.stem for p in md_files}

    changed_files = []
    broken_report = []

    for path in md_files:
        rel = path.relative_to(ROOT)

        if write_mode:
            result = normalize_file(path, all_stems)
        else:
            # simulate without writing by reading only
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            bounds = find_frontmatter_bounds(lines)
            result = {"changed": False, "before": [], "after": [], "broken": []}
            if bounds:
                start, end = bounds
                xref_start = None
                for i in range(start, end):
                    if XREF_LINE_RE.match(lines[i]):
                        xref_start = i
                        break
                if xref_start is not None:
                    i = xref_start + 1
                    stems = []
                    before_raw = []
                    while i < end and LIST_ITEM_RE.match(lines[i]) and lines[i].lstrip().startswith("-"):
                        m = LIST_ITEM_RE.match(lines[i])
                        before_raw.append(m.group(2))
                        stems.append(extract_stem(m.group(2)))
                        i += 1
                    after_raw = [f"[[{s}]]" for s in stems]
                    result = {
                        "changed": before_raw != after_raw,
                        "before": before_raw,
                        "after": after_raw,
                        "broken": [s for s in stems if s and s not in all_stems],
                    }

        if result["changed"]:
            changed_files.append((rel, result["before"], result["after"]))
        if result["broken"]:
            broken_report.append((rel, result["broken"]))

    # ── stdout summary ──────────────────────────────────────────────────
    mode = "DRY RUN" if args.dry_run else ("REPORT ONLY" if args.report_only else "APPLIED")
    print(f"[{mode}] Scanned {len(md_files)} files.")
    print(f"[{mode}] {len(changed_files)} file(s) had non-standard cross_references formatting.")
    print(f"[{mode}] {len(broken_report)} file(s) reference a stem with no matching file.\n")

    for rel, before, after in changed_files[:20]:
        print(f"  ~ {rel}")
    if len(changed_files) > 20:
        print(f"  ... and {len(changed_files) - 20} more")

    if broken_report:
        print("\n⚠️  Broken references (target file not found — needs human review):")
        for rel, broken in broken_report:
            print(f"  {rel}: {', '.join(broken)}")

    # ── full report file ────────────────────────────────────────────────
    reports_dir = ROOT / "cleanup_reports"
    reports_dir.mkdir(exist_ok=True)
    date_str = datetime.date.today().isoformat()
    report_path = reports_dir / f"normalize_cross_references_{date_str}.md"

    with report_path.open("w", encoding="utf-8") as f:
        f.write(f"# Cross-Reference Normalization Report — {date_str}\n\n")
        f.write(f"Mode: {mode}\n\n")
        f.write(f"Files scanned: {len(md_files)}\n")
        f.write(f"Files normalized: {len(changed_files)}\n")
        f.write(f"Files with broken references: {len(broken_report)}\n\n")

        f.write("## Files Changed\n\n")
        for rel, before, after in changed_files:
            f.write(f"### `{rel}`\n\n")
            f.write("| Before | After |\n|---|---|\n")
            for b, a in zip(before, after):
                f.write(f"| `{b}` | `{a}` |\n")
            f.write("\n")

        f.write("## Broken References (target file not found)\n\n")
        if broken_report:
            f.write("These stems don't match any filename in the repo. Do NOT guess the "
                    "intended target — resolve manually or flag to review-queue.\n\n")
            for rel, broken in broken_report:
                f.write(f"- `{rel}` → missing: {', '.join(f'`{b}`' for b in broken)}\n")
        else:
            f.write("None found.\n")

    print(f"\nFull report written to {report_path}")
    if args.dry_run or args.report_only:
        print("No files were modified.")


if __name__ == "__main__":
    main()