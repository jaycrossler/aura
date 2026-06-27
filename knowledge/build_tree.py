#!/usr/bin/env python3
"""
Create knowledge/_index.md

Run from inside the knowledge/ directory:
    cd knowledge && python3 build_tree.py

For every *.md file:
  - Syncs last_updated from the newest ISO date anywhere in the file
  - Extracts standard front-matter fields
  - Computes additional metrics:
      lines          – total line count
      xrefs          – number of cross_references entries
      canonical      – true / false / missing
      open_decisions – count of top-level list items under '## Open Decisions'
      open_mysteries – count of top-level list items under '## Open Mysteries'
      chars          – comma-separated slugs of linked char_ files
  - For sheet files (name starts with 'sheet_'), surfaces:
      subject_id, arc, checkpoint, sheet_sequence
      IMMUTABLE flag (hard warning — never edit sheet files)
  - Appends a '## Warnings' section listing:
      · Draft/staging files
      · Orphaned files (not referenced by any other file's cross_references)
      · Sheet sequence gaps per subject
"""

from pathlib import Path
import re
import datetime

ROOT   = Path(".").resolve()          # run from inside knowledge/
OUTPUT = ROOT.parent / "knowledge/_index.md"

# ── Field lists ────────────────────────────────────────────────────────────
FIELD_ORDER  = ["name", "id", "status", "canonical",
                "last_updated", "type", "description"]
SHEET_FIELDS = ["subject_id", "arc", "checkpoint",
                "sheet_sequence", "immutable"]

DRAFT_STATUSES = {
    "draft", "working_draft", "pre-draft",
    "draft_notes", "to_import", "staging",
    "rewrite_draft",
}

# ── Regex ──────────────────────────────────────────────────────────────────
DATE_RE   = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
KV_RE     = re.compile(r"^(?P<k>[A-Za-z0-9_]+):\s*(?P<v>.+)$")
# Top-level bullet: line starts with -, *, or digit+dot (no leading space)
TOP_BULLET_RE = re.compile(r"^[-*]\s+|^\d+\.\s+")


# ═══════════════════════════════════════════════════════════════════════════
# Front-matter parsing
# ═══════════════════════════════════════════════════════════════════════════

def split_front_matter(text: str) -> list[str]:
    """Return lines inside the opening YAML block, or []."""
    if not text.startswith("---"):
        return []
    parts = text.split("---", 2)
    if len(parts) < 3:
        return []
    return [ln.rstrip("\n") for ln in parts[1].splitlines()]


def parse_front_matter(fm_lines: list[str]) -> dict[str, object]:
    """
    Parse scalar fields from FIELD_ORDER + SHEET_FIELDS,
    plus the cross_references list.
    Returns a dict; cross_references value is list[str].
    """
    all_fields = set(FIELD_ORDER) | set(SHEET_FIELDS)
    meta: dict[str, object] = {}
    i = 0
    while i < len(fm_lines):
        ln = fm_lines[i]

        if ln.startswith("cross_references:"):
            xrefs: list[str] = []
            i += 1
            while i < len(fm_lines) and fm_lines[i].lstrip().startswith("-"):
                item = fm_lines[i].split("-", 1)[1].strip().strip("'\"")
                if item:
                    xrefs.append(item)
                i += 1
            meta["cross_references"] = xrefs
            continue

        m = KV_RE.match(ln)
        if m:
            k, v = m["k"], m["v"].strip().strip("'\"")
            if k in all_fields:
                meta[k] = v
        i += 1
    return meta


# ═══════════════════════════════════════════════════════════════════════════
# Date sync
# ═══════════════════════════════════════════════════════════════════════════

def newest_date(text: str) -> datetime.date | None:
    """Return the most recent ISO date found anywhere in the text."""
    best: datetime.date | None = None
    for m in DATE_RE.finditer(text):
        try:
            d = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if best is None or d > best:
            best = d
    return best


def sync_last_updated(path: Path, text: str,
                      fm_lines: list[str],
                      newest: datetime.date) -> str:
    """
    Rewrite last_updated in the file if newest > current value.
    Returns (possibly updated) file text.
    """
    newest_str = newest.isoformat()
    current = next(
        (ln.split(":", 1)[1].strip() for ln in fm_lines
         if ln.startswith("last_updated:")),
        None,
    )
    if current == newest_str:
        return text   # nothing to do

    out = []
    inserted = False
    for ln in fm_lines:
        if ln.startswith("last_updated:"):
            out.append(f"last_updated: {newest_str}")
            inserted = True
        else:
            out.append(ln)
    if not inserted:
        out.append(f"last_updated: {newest_str}")

    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    new_text = "---\n" + "\n".join(out) + "\n---" + parts[2]
    try:
        path.write_text(new_text, encoding="utf-8")
    except PermissionError:
        print(f"⚠️  Permission denied: {path}")
    return new_text


# ═══════════════════════════════════════════════════════════════════════════
# Metrics
# ═══════════════════════════════════════════════════════════════════════════

def count_top_level_items(text: str, heading: str) -> int:
    """
    Count top-level list items (no leading whitespace) under `heading`.
    Stops at the next ## heading.
    """
    if heading not in text:
        return 0
    after = text.split(heading, 1)[1]
    count = 0
    for ln in after.splitlines()[1:]:
        if ln.startswith("## "):
            break
        # Only count lines that start at column 0 with a bullet marker
        if TOP_BULLET_RE.match(ln):
            count += 1
    return count


def extract_char_links(cross_refs: list[str]) -> list[str]:
    """
    Return de-prefixed character slugs from cross_references.
    Handles paths (characters/char_kael.md), bare names (char_kael),
    and wiki-link format ([[char_kael]]).
    """
    slugs = []
    for ref in cross_refs:
        stem = Path(ref).stem.strip("[]")   # handles path and wiki-link
        if stem.startswith("char_"):
            slugs.append(stem[5:])           # strip "char_" prefix
    return slugs


# ═══════════════════════════════════════════════════════════════════════════
# Index line formatters
# ═══════════════════════════════════════════════════════════════════════════

def fmt_standard(meta: dict, lines_n: int, xref_n: int,
                 open_dec: int, open_myst: int,
                 chars: list[str]) -> str:
    segs = []
    for k in FIELD_ORDER:
        if k in meta:
            label = "updated" if k == "last_updated" else k
            segs.append(f"{label}: {meta[k]}")

    segs.append(f"lines: {lines_n}")
    segs.append(f"xrefs: {xref_n}")
    segs.append(f"canonical: {meta.get('canonical', 'false')}")

    if open_dec:
        segs.append(f"open_decisions: {open_dec}")
    if open_myst:
        segs.append(f"open_mysteries: {open_myst}")
    if chars:
        segs.append("chars: " + ", ".join(chars))

    return " - " + "; ".join(segs)


def fmt_sheet(meta: dict, lines_n: int) -> str:
    """
    Compact sheet entry emphasising immutability and progression position.
    """
    segs = []

    # Core identity
    if "name" in meta:
        segs.append(f"name: {meta['name']}")
    if "id" in meta:
        segs.append(f"id: {meta['id']}")

    # Sheet-specific fields
    subject  = meta.get("subject_id", "?")
    arc      = meta.get("arc", "?")
    chk      = meta.get("checkpoint", "?")
    seq      = meta.get("sheet_sequence", "")
    immut    = str(meta.get("immutable", "false")).lower()

    segs.append(f"subject: {subject}")
    segs.append(f"arc: {arc}")
    segs.append(f"checkpoint: {chk}")
    if seq:
        segs.append(f"seq: {seq}")

    segs.append(f"updated: {meta.get('last_updated', '?')}")
    segs.append(f"lines: {lines_n}")

    # Immutability warning — prominent
    if immut == "true":
        segs.append("⚠️ IMMUTABLE — do not edit")

    return " - " + "; ".join(segs)


# ═══════════════════════════════════════════════════════════════════════════
# Main walk
# ═══════════════════════════════════════════════════════════════════════════

def indent(level: int) -> str:
    return "    " * level + "- "


lines_out: list[str] = ["# Directory Tree\n"]

# Collect data for post-walk analysis
all_cross_refs: set[str] = set()       # stems referenced by any file
sheet_sequences: dict[str, list[int]] = {}  # subject_id → [seq numbers]
draft_files:   list[str] = []
all_md_stems:  set[str] = set()

for path in sorted(ROOT.rglob("*")):
    # Skip the output file itself and hidden dirs
    if path == OUTPUT:
        continue
    rel = path.relative_to(ROOT)
    if any(part.startswith(".") for part in rel.parts):
        continue

    depth = len(rel.parts) - 1
    entry = path.name + ("/" if path.is_dir() else "")

    if not (path.is_file() and path.suffix.lower() == ".md"):
        lines_out.append(indent(depth) + entry)
        continue

    # ── Read and sync ──────────────────────────────────────────────────
    text     = path.read_text(encoding="utf-8")
    fm_lines = split_front_matter(text)
    meta     = parse_front_matter(fm_lines)
    xrefs    = meta.get("cross_references", [])

    tail_date = newest_date(text)
    if tail_date:
        text = sync_last_updated(path, text, fm_lines, tail_date)
        meta["last_updated"] = tail_date.isoformat()

    # ── Accumulate for post-walk analysis ─────────────────────────────
    all_md_stems.add(path.stem)
    for ref in xrefs:
        all_cross_refs.add(Path(ref).stem.strip("[]"))

    status_val = str(meta.get("status", "")).lower()
    if status_val in DRAFT_STATUSES:
        draft_files.append(str(rel))

    # ── Metrics ───────────────────────────────────────────────────────
    total_lines    = len(text.splitlines())
    xref_count     = len(xrefs)
    open_decisions = count_top_level_items(text, "## Open Decisions")
    open_mysteries = count_top_level_items(text, "## Open Mysteries")
    char_links     = extract_char_links(xrefs)

    # ── Sheet vs standard ─────────────────────────────────────────────
    is_sheet = path.name.startswith("sheet_")

    if is_sheet:
        # Accumulate sequence info for gap detection
        subj = meta.get("subject_id", "")
        seq_raw = meta.get("sheet_sequence", "")
        if subj and seq_raw:
            try:
                seq_int = int(seq_raw)
                sheet_sequences.setdefault(subj, []).append(seq_int)
            except ValueError:
                pass
        suffix = fmt_sheet(meta, total_lines)
    else:
        suffix = fmt_standard(meta, total_lines, xref_count,
                              open_decisions, open_mysteries, char_links)

    lines_out.append(indent(depth) + entry + suffix)


# ═══════════════════════════════════════════════════════════════════════════
# Post-walk warnings
# ═══════════════════════════════════════════════════════════════════════════

warnings: list[str] = []

# 1. Draft / staging files
if draft_files:
    warnings.append("### Draft and Staging Files")
    warnings.append(
        "These files have non-canonical status and should not be "
        "treated as authoritative:\n"
    )
    for f in sorted(draft_files):
        warnings.append(f"- `{f}`")
    warnings.append("")

# 2. Orphaned files — not referenced by any other file's cross_references
#    Exclude _index.md, build_tree.py, templates/, and README files
ORPHAN_EXCLUDE_PREFIXES = ("README", "_index", "build_tree",
                            "concept-template", "faction-template",
                            "location-template", "magic-system-template",
                            "technology-template", "arc_template")

orphans = [
    stem for stem in sorted(all_md_stems)
    if stem not in all_cross_refs
    and not any(stem.startswith(p) for p in ORPHAN_EXCLUDE_PREFIXES)
]
if orphans:
    warnings.append("### Orphaned Files")
    warnings.append(
        "These files are not referenced by any other file's "
        "`cross_references`. They may be disconnected from the KB graph:\n"
    )
    for s in orphans:
        warnings.append(f"- `{s}`")
    warnings.append("")

# 3. Sheet sequence gaps
if sheet_sequences:
    gap_warnings: list[str] = []
    for subj, seqs in sorted(sheet_sequences.items()):
        seqs_sorted = sorted(seqs)
        expected = list(range(1, seqs_sorted[-1] + 1))
        missing = sorted(set(expected) - set(seqs_sorted))
        if missing:
            gap_warnings.append(
                f"- `{subj}`: missing seq {', '.join(str(m) for m in missing)} "
                f"(have: {seqs_sorted})"
            )
    if gap_warnings:
        warnings.append("### Sheet Sequence Gaps")
        warnings.append(
            "These subjects have non-contiguous sheet sequence numbers. "
            "Create the missing sheets or renumber:\n"
        )
        warnings.extend(gap_warnings)
        warnings.append("")

# Append warnings section to output
if warnings:
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")
    lines_out.append("## Warnings\n")
    lines_out.extend(warnings)

OUTPUT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT} with {len(lines_out) - 1} entries.")
if warnings:
    warn_sections = sum(1 for w in warnings if w.startswith("### "))
    print(f"⚠️  {warn_sections} warning section(s) appended — review ## Warnings in _index.md")
