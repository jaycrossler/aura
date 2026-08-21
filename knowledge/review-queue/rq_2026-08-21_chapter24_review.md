---
id: rq_2026-08-21_chapter24_review
title: Chapter 24 Review Notes
type: review_queue_log
status: open
last_updated: 2026-08-21
description: >
  Copy-editing corrections and continuity decisions for Chapter 24 (Wrong Stars).
cross_references:
  - "[[draft_ch24_wrong_stars]]"
  - "[[future_epigraph_candidates]]"
---

# Chapter 24 Review Notes

Review source: the latest default-branch version of
`knowledge/scenes/draft_ch24_wrong_stars.md` in `jaycrossler/aura`, retrieved
2026-08-21.

## Patch scope

`chapter24_copyedit.patch` proposes copy-editing and bounded logic corrections only.
It does not alter Chapter 23 or supporting knowledge-bank records.

The patch corrects:

- the Sagan epigraph’s visible spelling errors;
- misspellings including `masrkers`, `libarary`, and `wokr`;
- punctuation, possessives, comma splices, and subject-verb agreement;
- the ambiguous Brandon and Nikos crossing paragraph;
- inconsistent capitalization of Astral;
- the physical-to-Astral square-root relationship;
- residual use of `{Aura-S}` after the instance accepts the name `{Sparky}`;
- terminology for the three-rod parity check;
- computed tomography and magnetic resonance imaging terminology.

## Continuity decisions not included in the patch

1. **Brandon’s crossing.** Chapter 23’s description and contract say Brandon crosses
   and helps pull Nick. Chapter 23’s prose leaves Brandon in the Real throughout the
   hunt. Chapter 24 therefore reads as Brandon’s first crossing, while its contract says
   he crosses again. Either add Brandon’s Chapter 23 crossing scene or revise both
   chapters’ metadata and contracts.

2. **Sixteen-rod telegraph.** Chapter 24’s description and contract say Nick sketches
   the sixteen-rod byte link. The current prose contains the three-rod relay but no
   sixteen-rod design scene. Restore the short Foundry discussion or mark that contract
   item as pending for a later chapter.

3. **Carl Sagan wording.** The patch repairs `ins pace int he`, but the exact quotation
   and edition should receive a final source check before publication. If a traceable
   source cannot be located, replace it with one of the sourced candidates in
   `future_epigraph_candidates.md`.

4. **Rocket range.** “Almost a million meters” means nearly 1,000 kilometers, roughly
   1,000 times the intended one-kilometer flight. The revised sentence states that
   relationship explicitly. Confirm that this scale matches the later vehicle arc.

5. **Sparky naming.** The drone and its bounded {Aura} instance now share the name
   `{Sparky}`. The patch makes the speaker tag consistent after the naming exchange.
   Confirm that the shared name is intentional before later chapters depend on it.
