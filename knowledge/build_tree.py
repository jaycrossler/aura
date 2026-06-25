#!/usr/bin/env python3
"""
Create knowledge/_index.md

• Walks every file under the working directory
• For *.md files
    – Reads YAML-style front-matter
    – Scans the tail of the file for YYYY-MM-DD dates (e.g. in '## Revision Notes')
    – If the newest date > front-matter last_updated (or it is missing):
        * rewrites/creates last_updated: <newest-date> in the front-matter
    – Collects selected keys and writes them on the same line in the index
"""

from pathlib import Path
import re
import datetime

ROOT = Path(".").resolve()                           # run inside knowledge/
OUTPUT = ROOT.parent / "knowledge/_index.md"         # leave output unchanged
FIELD_ORDER = ["name", "id", "status",
               "last_updated", "type", "description"]

# ---------- regex helpers ----------
FM_KV        = re.compile(r"^(?P<k>[A-Za-z0-9_]+):\s*(?P<v>.+)$")
DATE_IN_LINE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")   # finds ISO dates

def indent(level: int) -> str:
    return "    " * level + "- "

# ---------- metadata extraction ----------
def front_matter(path: Path) -> dict[str, str]:
    """Return YAML-front-matter keys in FIELD_ORDER."""
    meta: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        if fh.readline().strip() != "---":
            return {}
        for line in fh:
            if line.strip() == "---":
                break
            m = FM_KV.match(line.rstrip())
            if m and m["k"] in FIELD_ORDER:
                meta[m["k"]] = m["v"].strip()
    return meta

def latest_revision_date(path: Path) -> datetime.date | None:
    """Scan the file bottom-up; return the newest YYYY-MM-DD date if present."""
    newest: datetime.date | None = None
    for line in reversed(path.read_text(encoding="utf-8").splitlines()):
        m = DATE_IN_LINE.search(line)
        if not m:
            continue
        try:
            d = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if newest is None or d > newest:
            newest = d
            if newest.year < 1900:   # guard weird matches
                newest = None
    return newest

# ---------- front-matter rewriting ----------
def sync_last_updated(path: Path,
                      current_meta: dict[str, str],
                      newest: datetime.date) -> None:
    """Rewrite or add last_updated in the file's front-matter if needed."""
    latest_str = newest.isoformat()
    if current_meta.get("last_updated") == latest_str:
        return                                                # nothing to do

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return                                                # no front-matter

    # split on first two '---'
    parts = text.split("---", 2)
    if len(parts) < 3:
        return
    _, fm_block, rest = parts
    fm_lines = fm_block.splitlines(keepends=True)

    # replace or append
    inserted = False
    for i, ln in enumerate(fm_lines):
        if ln.lstrip().startswith("last_updated:"):
            fm_lines[i] = f"last_updated: {latest_str}\n"
            inserted = True
            break
    if not inserted:
        fm_lines.append(f"last_updated: {latest_str}\n")

    new_content = "---" + "".join(fm_lines) + "---" + rest
    try:
        path.write_text(new_content, encoding="utf-8")
    except PermissionError:
        print(f"⚠️  Could not update {path} (permission denied)")

# ---------- line formatter ----------
def suffix(meta: dict[str, str]) -> str:
    parts = []
    for k in FIELD_ORDER:
        if k in meta:
            label = "updated" if k == "last_updated" else k
            parts.append(f"{label}: {meta[k]}")
    return (" - " + "; ".join(parts)) if parts else ""

# ---------- main ----------
lines = ["# Directory Tree\n"]
for md_path in sorted(ROOT.rglob("*")):
    depth = len(md_path.relative_to(ROOT).parts) - 1
    entry = md_path.name + ("/" if md_path.is_dir() else "")

    if md_path.is_file() and md_path.suffix.lower() == ".md":
        meta = front_matter(md_path)

        rev_date = latest_revision_date(md_path)
        if rev_date:
            sync_last_updated(md_path, meta, rev_date)
            meta["last_updated"] = rev_date.isoformat()

        entry += suffix(meta)

    lines.append(indent(depth) + entry)

OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT} with {len(lines) - 1} entries.")