---
id: review_2026_08_15_cast_and_voice_audit
name: "Ch00-20 Cast Coverage and Voice Profile Audit"
type: developmental_review
book: book01
status: proposal
schema_version: 2
last_updated: 2026-08-15
description: >
  Audit of every named character with a role in drafted Chapters 0 through 20
  against the characters/ folder, covering character-file coverage, voice-file
  coverage, and visual-profile coverage, plus a list of structural problems
  found in the knowledge base during the pass.
cross_references:
  - "[[review_2026-08-14_chapters_00_20_contract_reconciliation]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[VISUAL_PROFILE_SYSTEM_INSTRUCTIONS]]"
  - "[[visual_profile_gaps_2026_08_15]]"
---

# Ch00-20 Cast Coverage and Voice Profile Audit

## Headline finding

**Character-file coverage is essentially complete. Voice-file coverage was not.**

Someone ran a thorough character-file pass on 2026-08-14 that created the AI
character files (`char_alex_ai`, `char_spox_ai`, `char_gem_ai`, `char_chorus_ai`,
`char_penny_ai`, `char_seek_ai`, `char_aura_ai`, `char_misty_ai`) and the newer
Fortuna and Victoria humans (`char_petroski`, `char_sai`, `char_mateo_alvarez`,
`char_brandon_moreau`, `char_nikos_petrou`, `char_saul`). Every named character
found in a Ch00-20 chapter cross-reference list has a `char_` file.

Voice files were a different story. Before this pass there were ten, all created
on 2026-08-12 and all covering the Prologue through Ch07 cast. **Nothing from
Ch08 through Ch20 had a voice profile, including the two largest speaking roles
in the book.**

## Coverage table

| Character | char_ | voice_char_ | visual_profile_ | Note |
|---|---|---|---|---|
| Jace Apollo Grant | stub, contradictory | **added** | yes (60%) | POV. See P0 below |
| Sophia Lotte | yes | **added** | yes | Second largest role |
| Cerberus / Siren | yes | n/a | yes | Non-speaking |
| Nick Lee | yes, corrupted frontmatter | yes | yes | See P1 below |
| Maureen | yes | yes | — | |
| Mei | yes | yes | — | |
| Lanchee | yes | yes | — | |
| Helena | yes | yes | — | Name conflict, see P2 |
| Sai | yes | yes | — | |
| Carlos | yes | yes | — | |
| Artemis Grant | yes | yes | — | |
| Rich Cullivan | yes | yes | — | Non-canonical folder |
| Kim | yes | **added (light-detail)** | no | No physical data at all |
| Suzi Gonzales | yes | **added** | **added (55%)** | |
| Jin Lóng | yes | **added** | yes (88%) | |
| Torres | yes | **added (light)** | no | No first name |
| Hayes | yes | **added (light)** | no | Left-handed detail matters |
| Mira | yes | **added (light)** | no | Highest-value gap |
| Petroski | yes | **added (light)** | no | Only Russian on station |
| Mateo Alvarez | stub | **added (light)** | no | Confirm he speaks |
| Brandon Moreau | yes | **added (light)** | no | |
| Nikos Petrou | yes | **added (light)** | no | |
| Saul | yes | **added (light)** | no | Relationship unretrieved |
| Erin | yes | **added (light)** | no | May be Arc 2 only |
| Kael / Kai | yes | no | yes | Arrives at arc close; deferred |
| Eugene Hart | yes | no | no | Not in Ch00-20 |
| {Alex} | yes | yes | — | |
| {Aura} | yes | **added** | — | |
| {Penny} | yes | **added** | — | |
| {Chorus} | yes | **added** | — | Production blocker, see below |
| {SpoX} | yes | **added** | — | |
| {Gem} | yes | **added** | — | |
| {Seek} | yes | **added** | — | |
| {Misty} | yes | **added** | — | |
| {Falcon} | **missing** | **added (light)** | — | See P3 below |

Twenty-two new voice files in this batch, plus one new visual profile and one
visual-profile gap audit.

## Structural problems found

Ordered by severity. None of these were resolved; they are surfaced for a ruling.

### P0. `char_jace_apollo.md` is a nine-line contradictory stub

Already Priority 0 in `review_2026-08-14_chapters_00_20_contract_reconciliation.md`
and still open. The file describes Jace as the *Falcon*'s pilot and captain. He
is an Origin courier contractor riding as a passenger, and Maureen is the
captain. Every drafted chapter contradicts the file.

This blocked the new `voice_char_jace_apollo.md`, which had to be built from the
chapter drafts and arc files instead. **This is the single highest-value fix in
the knowledge base.** The POV character of a twenty-one chapter book has nine
lines of character documentation, and one of them is wrong.

### P1. `char_nick_lee.md` has corrupted YAML frontmatter

The `_index.md` entry for this file reads:

> `type: Rotates between types and spices; description: A very nice ergonomic
> chair with built-in back massager, armrest keyboards,`

Body content has leaked into the frontmatter block, almost certainly an unclosed
quote or a stray `---`. `build_tree.py` is parsing chair upholstery as a file
type. The file also shows `xrefs: 1` where it should have many, which means the
`cross_references` block is inside the damaged region and Nick is effectively
disconnected from the graph. **This is a parser-visible bug, not a style issue.**

### P2. Helena's surname is asserted in one file and TBD in another

`char_helena.md` carries `name: Helena [surname TBD]`. `voice_char_helena.md`,
created 2026-08-12, refers to her throughout as **Helena Reyes**.

Either the surname was ruled and the character file was never updated, or the
voice file invented it. Do not resolve by picking one. **Author ruling needed.**

### P3. `{Falcon}` is a canonical braces-named AI with no character file

Author ruling 13 in `rq_2026-07-15_book1_first_pass.md` established {Falcon} as
the *Falcon*'s majordomo AI, and `CLAUDE_PROJECT_INSTRUCTIONS.md` now lists it
in the canonical braces set alongside the other eight. Every other braces-named
AI has a `char_*_ai.md` file. {Falcon} has only `tech_falcon_majordomo.md`.

Recommend creating `characters/char_falcon_ai.md` to match the pattern. The same
review item also lists an unconfirmed pending patch to `ship_falcon` and to any
KB references to an unnamed majordomo.

### P4. `voice_char_jace_apollo` was a broken cross-reference

`storybot_orpheus_voice_tag_reference.md` cross-references `[[voice_char_jace_apollo]]`
and describes it as an earlier file using freeform bracket tags. No such file
existed in the repo. Either it was deleted without updating the reference, or it
was never committed. The new file in this batch resolves the broken link, but if
an earlier version exists outside the repo it should be diffed against the new one.

### P5. `voice_char_alex_ai.md` points at a file that does not exist

Its frontmatter reads `character_ref: tech_alex_ai`. The actual file is
`characters/char_alex_ai.md`, created two days after the voice file. The voice
file's own `open_flags` block predicted exactly this and asked for reconciliation.
A one-line fix, staged in `patches/EDITS.md`.

### P6. `normalize_cross_references.py` is scanning `to_merge/`

The 2026-08-14 report contains entries for paths like
`to_merge\aura_chapter_text_export_2026-08-14\repo\knowledge\scenes\draft_ch18_quiet_companion.md`.
The script's `SKIP_DIR_PREFIXES` is `("templates", ".git", "review-queue")` and
does not include `to_merge`. The result is that every staged import is scanned
twice, once in place and once in staging, inflating the reports and creating
phantom duplicate filenames that a future dedupe pass could act on wrongly.

`CLAUDE_PROJECT_INSTRUCTIONS.md` already says `.gitignore` should contain
`to_merge/`, so the intent is clearly to exclude it. Add `to_merge` and
`cleanup_reports` to `SKIP_DIR_PREFIXES`.

### P7. Eight near-identical cross-reference reports in `cleanup_reports/`

Roughly 11,300 lines across eight files dated 2026-07-26 through 2026-08-14,
each a near-superset of the last. They dominate semantic search results for any
character-name query, which measurably degraded retrieval during this audit.

Recommend keeping only the most recent and archiving or deleting the rest. If
the history matters, move them outside the semantically indexed tree.

### P8. Possible duplicate chapter numbers

`build_tree.py` raises `ValueError` on duplicate chapter numbers, so if these
files coexist the exporter is currently broken:

| Number | Files seen across reports |
|---|---|
| Ch05 | `draft_ch05_morning_after_debrief.md`, `draft_ch05_learning_mode.md` |
| Ch06 | `draft_ch06_learning_mode.md`, `draft_ch06_the_spire.md` |
| Ch07 | `draft_ch07_artemis_call_canister.md`, `draft_ch07_arrival_day.md` |
| Ch08 | `draft_ch08_arrival_day.md`, `draft_ch08_settling_in.md` |

The older names appear in reports up to 2026-07-31 and the newer ones from
2026-08-12 onward, which is consistent with a renumbering pass having happened.
**However**, several current files still cross-reference the old stems, for
example `draft_ch06_the_spire.md` references `[[draft_ch05_learning_mode]]`,
and the Ch05 file itself is now `draft_ch05_learning_mode.md`, so that one
resolves. Others may not.

**Verification item, not a confirmed fault.** Run `python normalize_cross_references.py --report-only`
and check the broken-references section, then run `python build_tree.py` and
confirm it does not raise.

### P9. `char_pytest_candidate_regression.md` is test debris

A character file named "Pytest Candidate Regression" with an empty description
and the body text *"Added from the chapter editor's new-entity suggestions,
flesh out this profile."* This is an automated tool having extracted a phrase
from a log or a comment and created a character from it. Delete.

### P10. Every voice file is orphaned

All ten pre-existing `voice_char_*.md` files appear in the `_index.md` orphan
list, because voice files link **to** their character file but no character file
links **back**. The new files in this batch have the same problem by
construction.

The fix is a one-line addition to each `char_` file's `cross_references`.
Staged in `patches/EDITS.md`.

### P11. `VISUAL_PROFILE_SYSTEM_INSTRUCTIONS.md` status table is stale

It lists `visual_profiles_sophia_jin_nick_cerberus.md` and
`visual_profiles_locations.md` as combined files at 25 to 75 percent. Those were
split into individual files some time ago. The table should be regenerated, along
with `visual_profiles/_tracker.svg`.

## Production blocker: {Chorus}

Not a knowledge-base fault, but it will stop the audiobook. {Chorus} hands off
between named internal models mid-conversation, and each opens differently. There
are three ways to render that in audio and they produce very different listening
experiences. It cannot be fixed in post. See `voice_char_chorus_ai.md` for the
options and a recommendation. **Needs a director or author ruling before any
{Chorus} audio is generated.**

## Open questions for the author

1. Sophia's accent: German-primary with French colour, or French-primary with
   German precision? The character file and the Ch13 prose disagree.
2. Helena's surname. Reyes or still TBD?
3. Kim's surname, and whether Kim is a given name or a surname.
4. Torres's first name.
5. {Chorus} handoff rendering, per the blocker above.
6. {Aura} install timing. Did Jace have a personalized {Aura} on Mars, or is
   Ch18 genuinely the first? Carried over unresolved from the 2026-08-14 review.
7. {Misty}'s pronouns. she/her throughout, or the current mix?
8. {Falcon}'s personality. The light profile proposes "old ship software" as a
   contrast with {Alex}. Approve, reject, or replace.
9. Do Mateo Alvarez and Erin speak in Book 1 at all? If not, their voice files
   should be deleted rather than expanded.

## Revision Notes

- 2026-08-15: Initial audit, produced alongside a batch of twenty-two new voice
  profiles, one new visual profile, and a visual-profile gap audit.
