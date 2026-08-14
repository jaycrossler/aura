#!/usr/bin/env python3
"""
Create knowledge/_index.md and audiobook-ready chapter text exports.

Run from inside the knowledge/ directory:
    cd knowledge && python3 build_tree.py

Optional modes:
    python3 build_tree.py --index-only
    python3 build_tree.py --chapter-text-only
    python3 build_tree.py --chunk-size 5

Chapter text exports are written to scenes/chapter_text/:
  - chapter_NN.txt contains one chapter with frontmatter, Markdown, braces,
    contract coverage, and open notes removed.
  - chapters_NN-NN.txt combines consecutive chapter-number windows. The
    default five-chapter windows are 00-04, 05-09, 10-14, and so on.
  - Blank lines provide light paragraph, scene, and chapter pauses for TTS.

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

import argparse
import re
import datetime
from pathlib import Path

ROOT   = Path(".").resolve()          # run from inside knowledge/
OUTPUT = ROOT.parent / "knowledge/_index.md"
SCENES_ROOT = ROOT / "scenes"
CHAPTER_TEXT_ROOT = SCENES_ROOT / "chapter_text"

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
CHAPTER_SOURCE_RE = re.compile(r"^draft_ch(?P<number>\d{2,})_.+\.md$")
MANAGED_CHAPTER_TEXT_RE = re.compile(
    r"^(?:chapter_\d{2,}|chapters_\d{2,}-\d{2,})\.txt$"
)
CONTRACT_HEADING_RE = re.compile(
    r"^##\s+Contract coverage\b.*$", re.IGNORECASE | re.MULTILINE
)
MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
WIKI_LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
HTML_TAG_RE = re.compile(r"<[^>]+>")
INLINE_CODE_RE = re.compile(r"`([^`]*)`")
SIMPLE_BRACKET_RE = re.compile(r"\[([^\[\]]+)\]")
EMPHASIS_RE = re.compile(r"(?<!\w)(?:\*{1,3}|_{1,3})|(?:\*{1,3}|_{1,3})(?!\w)")


# ═══════════════════════════════════════════════════════════════════════════
# Audiobook chapter-text export
# ═══════════════════════════════════════════════════════════════════════════

def remove_front_matter(text: str) -> str:
    """Return Markdown after an opening YAML frontmatter block."""
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    return parts[2] if len(parts) == 3 else text


def clean_inline_markdown(text: str) -> str:
    """Remove lightweight Markdown and story tags while retaining spoken text."""
    text = WIKI_LINK_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = MARKDOWN_LINK_RE.sub(lambda m: m.group(1), text)
    text = INLINE_CODE_RE.sub(lambda m: m.group(1), text)
    text = HTML_TAG_RE.sub("", text)
    text = text.replace("{", "").replace("}", "")
    text = SIMPLE_BRACKET_RE.sub(lambda m: m.group(1), text)
    text = EMPHASIS_RE.sub("", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def chapter_markdown_to_text(markdown: str) -> str:
    """Convert one chapter draft to lightly formatted, TTS-friendly text."""
    body = remove_front_matter(markdown)
    contract = CONTRACT_HEADING_RE.search(body)
    if contract:
        body = body[:contract.start()]

    sections: list[list[str]] = [[]]
    in_fence = False

    for raw_line in body.splitlines():
        line = raw_line.rstrip()

        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            cleaned = clean_inline_markdown(line)
            if cleaned:
                sections[-1].append(cleaned)
            continue

        if re.fullmatch(r"\s*(?:##|---|\*\s*\*\s*\*)\s*", line):
            if any(part.strip() for part in sections[-1]):
                sections.append([])
            continue

        heading = re.match(r"^#{1,6}\s+(.*)$", line)
        if heading:
            cleaned = clean_inline_markdown(heading.group(1))
            if cleaned:
                sections[-1].append(cleaned)
                sections[-1].append("")
            continue

        line = re.sub(r"^\s*>\s?", "", line)
        line = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", line)

        # Tables are editorial material in current chapter drafts. Contract
        # tables have already been truncated; ignore any remaining table rows.
        if line.strip().startswith("|") and line.strip().endswith("|"):
            continue

        cleaned = clean_inline_markdown(line)
        sections[-1].append(cleaned)

    rendered_sections: list[str] = []
    for section in sections:
        text = "\n".join(section)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if text:
            rendered_sections.append(text)

    # Three empty lines between scenes give common TTS tools a longer pause
    # without introducing SSML or generator-specific pause tags.
    return "\n\n\n\n".join(rendered_sections).strip() + "\n"


def discover_chapter_sources(scenes_root: Path) -> list[tuple[int, Path]]:
    """Find canonical chapter drafts by filename and reject duplicate numbers."""
    chapters: dict[int, Path] = {}
    for path in sorted(scenes_root.glob("draft_ch[0-9][0-9]_*.md")):
        match = CHAPTER_SOURCE_RE.match(path.name)
        if not match:
            continue
        number = int(match.group("number"))
        if number in chapters:
            raise ValueError(
                f"Duplicate chapter {number}: {chapters[number].name}, {path.name}"
            )
        chapters[number] = path
    return sorted(chapters.items())


def write_if_changed(path: Path, text: str) -> None:
    """Write generated text only when its content changed."""
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def generate_chapter_texts(
    scenes_root: Path = SCENES_ROOT,
    output_root: Path = CHAPTER_TEXT_ROOT,
    chunk_size: int = 5,
) -> tuple[int, int]:
    """Generate individual and chunked audiobook text files."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")

    sources = discover_chapter_sources(scenes_root)
    output_root.mkdir(parents=True, exist_ok=True)

    chapter_text: dict[int, str] = {}
    expected_outputs: set[Path] = set()

    for number, source in sources:
        text = chapter_markdown_to_text(source.read_text(encoding="utf-8"))
        chapter_text[number] = text
        output_path = output_root / f"chapter_{number:02d}.txt"
        write_if_changed(output_path, text)
        expected_outputs.add(output_path)

    chunk_count = 0
    buckets: dict[int, list[int]] = {}
    for number in chapter_text:
        start = (number // chunk_size) * chunk_size
        buckets.setdefault(start, []).append(number)

    for start, numbers in sorted(buckets.items()):
        end = start + chunk_size - 1
        combined = "\n\n\n\n\n".join(
            chapter_text[number].rstrip() for number in sorted(numbers)
        ) + "\n"
        output_path = output_root / f"chapters_{start:02d}-{end:02d}.txt"
        write_if_changed(output_path, combined)
        expected_outputs.add(output_path)
        chunk_count += 1

    # Remove only files owned by this generator. Preserve any hand-authored
    # notes or other text files placed in chapter_text/.
    for path in output_root.glob("*.txt"):
        if MANAGED_CHAPTER_TEXT_RE.match(path.name) and path not in expected_outputs:
            path.unlink()

    return len(chapter_text), chunk_count


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


parser = argparse.ArgumentParser(
    description="Rebuild the knowledge index and audiobook chapter text."
)
mode = parser.add_mutually_exclusive_group()
mode.add_argument(
    "--index-only",
    action="store_true",
    help="rebuild _index.md without regenerating chapter text",
)
mode.add_argument(
    "--chapter-text-only",
    action="store_true",
    help="regenerate chapter text without rebuilding _index.md",
)
parser.add_argument(
    "--chunk-size",
    type=int,
    default=5,
    help="chapters per combined text file (default: 5)",
)
args = parser.parse_args()

if not args.index_only:
    chapter_count, chunk_count = generate_chapter_texts(chunk_size=args.chunk_size)
    print(
        f"Wrote audiobook text for {chapter_count} chapter(s) "
        f"and {chunk_count} chunk(s) to {CHAPTER_TEXT_ROOT}."
    )

if args.chapter_text_only:
    raise SystemExit(0)


lines_out: list[str] = ["# Directory Tree\n"]

# Collect data for post-walk analysis
all_cross_refs: set[str] = set()       # stems referenced by any file
sheet_sequences: dict[str, list[int]] = {}  # subject_id → [seq numbers]
draft_files:   list[str] = []
all_md_stems:  set[str] = set()
non_canonical_stems: set[str] = set()

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

    is_canonical = str(meta.get("canonical", "true")).lower() != "false"
    if not is_canonical:
        non_canonical_stems.add(path.stem)

    status_val = str(meta.get("status", "")).lower()
    if is_canonical and (status_val in DRAFT_STATUSES):
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
        "These files were marked as draft or have non-canonical status and should not be "
        "treated as finalized:\n"
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
    and stem not in non_canonical_stems
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
    print(f"WARNING: {warn_sections} warning section(s) appended — review ## Warnings in _index.md")
