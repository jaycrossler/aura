#!/usr/bin/env python3
"""
Create filetree.md:
- Shows every folder / file in the current directory
- For *.md files, adds selected front-matter fields on the same line
"""

from pathlib import Path
import re

ROOT   = Path(".").resolve()
OUTPUT = ROOT.parent / "knowledge/_index.md"
FIELD_ORDER = ["name", "id", "status", "last_updated", "type", "description"]

# -------- helpers --------
def indent(level: int) -> str:
    return "    " * level + "- "

fm_key_val = re.compile(r"^(?P<k>[A-Za-z0-9_]+):\s*(?P<v>.+)$")

def front_matter(path: Path) -> dict[str, str]:
    """
    Return a dict of desired keys from the file's front matter.
    Does not rely on PyYAML; stops when the second '---' is reached.
    """
    meta: dict[str, str] = {}
    try:
        with path.open(encoding="utf-8") as fh:
            if fh.readline().strip() != "---":
                return {}
            for line in fh:
                line = line.rstrip()
                if line.strip() == "---":          # end of front matter
                    break
                if not line or line.lstrip().startswith("#"):
                    continue                      # skip blanks / comments
                m = fm_key_val.match(line)
                if m and m["k"] in FIELD_ORDER:
                    meta[m["k"]] = m["v"].strip()
    except Exception:
        pass
    return meta

def suffix(meta: dict[str, str]) -> str:
    """
    Assemble the semicolon-separated field list in the requested order.
    last_updated is shown with the label 'updated'.
    """
    parts = []
    for k in FIELD_ORDER:
        if k in meta:
            label = "updated" if k == "last_updated" else k
            parts.append(f"{label}: {meta[k]}")
    return " - " + "; ".join(parts) if parts else ""

# -------- main routine --------
lines = ["# Directory Tree\n"]
for path in sorted(ROOT.rglob("*")):
    depth = len(path.relative_to(ROOT).parts) - 1
    entry = path.name + ("/" if path.is_dir() else "")
    if path.is_file() and path.suffix.lower() == ".md":
        entry += suffix(front_matter(path))
    lines.append(indent(depth) + entry)

OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT} with {len(lines)-1} entries.")