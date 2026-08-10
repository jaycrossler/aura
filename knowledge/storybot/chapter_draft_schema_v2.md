---
id: chapter_draft_schema_v2
name: Chapter Draft Schema v2
type: storybot_schema
status: proposed
canonical: false
schema_version: 2
last_updated: 2026-08-10
description: "Proposed interoperable schema for stable beat-to-prose links, contract completion, and open production notes in chapter drafts."
cross_references:
  - "[[draft_ch00_prologue_helena]]"
  - "[[metadata_template_guide]]"
  - "[[progression_review_guide]]"
---

# Chapter Draft Schema v2

## Purpose and status

This schema removes three failure-prone patterns from chapter drafts:

1. Beat links based on mutable line numbers and duplicated prose quotations.
2. Contract state duplicated across a contract, coverage table, and completion checklist.
3. Open decisions duplicated across frontmatter flags, body notes, and inline caveats.

The format is proposed until the StoryBot platform parser, renderer, and linter implement and test it. A draft may opt in with `schema_version: 2`. Legacy drafts remain valid during the transition.

## Normative conventions

The words **must**, **must not**, **should**, and **may** are normative.

### Stable beat anchors

Place one HTML comment immediately before the prose covered by each beat:

```markdown
<!-- beat:{scene_id}.{beat_key} -->
Prose for the beat begins here.
```

- `scene_id` must match the file's `scene_contract` identifier after applying the repository-wide scene-ID normalization rule.
- For the current short-form convention, remove a leading `event_` from `scene_contract`. Example: `event_helena_prologue` becomes `helena_prologue`.
- `beat_key` must be a stable descriptive slug, such as `beat1_morning_rounds`.
- A beat's prose begins after its anchor and ends at the next beat anchor or the thematic break that introduces metadata sections.
- Drafts must not store beat line numbers or quoted copies of prose as links.

Anchor regex:

```regex
<!--\s*beat:([\w.]+)\s*-->
```

The parser should split the body on the anchor regex. Each capture is the fully qualified anchor ID; the following segment is its content. It must split the capture at the final period into `scene_id` and `beat_key`.

### Contract coverage

A schema-v2 draft must contain exactly one level-two Contract coverage section:

```markdown
## Contract coverage (`{scene_contract_id}`)

| Goal Item | Status | Type | Linked Beat |
|---|---|---|---|
| 1 — ... | done | must_accomplish | beat1_morning_rounds |
```

The table has exactly four columns in this order:

| Column | Rule |
|---|---|
| Goal Item | Free text. Preserve the stable contract-item identifier when one exists. |
| Status | One of `done`, `partial`, `open`, `blocked`, or `not_applicable`. |
| Type | One of `must_accomplish` or `must_not_do`. |
| Linked Beat | A `beat_key` declared in this file, or an em dash when no prose span applies. |

The section ends at the next level-two heading or end of file. No cell may contain a literal `|`.

The `Linked Beat` cell intentionally stores only `beat_key`. The anchor stores the qualified `{scene_id}.{beat_key}`. The parser must join them using the file's normalized scene namespace and must report missing or duplicate keys.

Plain-text status tokens are source data. A user interface may map them to icons:

| Token | Suggested display |
|---|---|
| `done` | ✅ |
| `partial` | ⚠️ |
| `open` | ⬜ |
| `blocked` | ⛔ |
| `not_applicable` | ➖ |

The UI must not persist an icon as the status value.

For backward-compatible view models, the parser may derive `must_dos`, `must_nots`, `completed_must_dos`, and `completed_must_nots` by filtering rows on `Type` and `Status == "done"`. The table remains the single source of truth.

### Open Notes

A schema-v2 draft must contain exactly one level-two Open Notes section:

```markdown
## Open Notes

| Note | Status | Resolution |
|---|---|---|
| ... | resolved | One-line decision and source pointer |
| ... | open | |
```

The table has exactly three columns in this order:

| Column | Rule |
|---|---|
| Note | Concise decision, risk, or follow-up item. |
| Status | One of `open`, `resolved`, or `blocked`. |
| Resolution | Blank for an unresolved note, or a concise decision and source pointer. |

The section ends at the next level-two heading or end of file. No cell may contain a literal `|`.

Resolve a note in place by changing its status and filling its resolution. Delete a note only when it duplicates another row or has no continuing historical value. Schema-v2 files must not duplicate these rows in frontmatter `open_flags`, separate production-note lists, or inline caveat tables.

## Parser and renderer requirements

A writer that supports schema v2 must:

1. Parse sections only within their heading boundaries.
2. Require the exact column count and order.
3. Validate status and type enums.
4. Reject literal pipes within cell content.
5. Verify unique anchor IDs.
6. Verify each linked beat exists in the file's normalized scene namespace.
7. Preserve row order and free text.
8. Render the parser's in-memory model back to the same structure.
9. Produce an idempotent parse-render-parse result.

Unknown columns, invalid enum tokens, duplicate headings, duplicate anchors, and broken beat links should produce actionable validation errors. A writer must not silently discard invalid data.

## Migration and compatibility

- Parsers should try schema v2 first when `schema_version: 2`, anchors, and the four-column coverage table are present.
- Parsers should fall back to legacy line-number, quoted-text, two-column coverage, and tracked-completion formats for older drafts.
- Convert drafts opportunistically when next edited. A bulk migration is not required.
- Do not write mixed legacy and v2 tracking structures into the same file.
- `extract_inline_tags()` does not need to parse anchor comments. Beat anchors form a separate convention.

## Platform implementation checklist

The StoryBot platform repository should add:

- A typed schema model shared by parser and renderer.
- New-format-first parsing with legacy fallback.
- Exact-inverse rendering.
- Authoring-time lint rules for enums, column locks, literal pipes, duplicate anchors, namespace mismatches, and unresolved linked beats.
- Fixture tests using `knowledge/scenes/draft_ch00_prologue_helena.md`.
- Round-trip and idempotence tests.
- Tests that edits above an anchor do not change the beat link.
- Tests that rows with `partial`, `blocked`, and `not_applicable` survive round trips.
- A compatibility test proving the existing sidebar arrays remain available.

## Reference draft

`knowledge/scenes/draft_ch00_prologue_helena.md` is the repository fixture and worked example. It demonstrates anchors, a partial contract status, resolved notes retained in place, and open follow-up items.
