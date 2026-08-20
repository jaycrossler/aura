---

id: open_questions_jin_room_sophia_v1
type: review_queue
status: open
created: 2026-08-19
related: [draft_ch20_borrowed_light, draft_ch21_the_eye_on_three, draft_ch22_quiet_companion, char_jin_luong, char_sophia_lotte, timeline_book01_incursions, outbreak_timeline, location_metis_station, location_adama_station]
last_updated: 2026-08-19
---

# Open Questions — Jin's Room, Sophia Timeline, Adama Cleanup (2026-08-19)

## 1. FIND blocks in the Ch20-22 patches need hand verification

You've been independently editing these chapters, and what I have in context
may lag your actual current files (dialogue differences already visible in
`generated_text/chapters_20-24.txt` vs. what I originally delivered). Every
patch in this package is flagged inline where this matters most — match by
content/beat if the literal FIND text doesn't hit. Worth a careful read-through
before merge rather than a blind find-replace.

## 2. Old `location_metis_station.md` is a stale duplicate — recommend deleting

`location_adama_station.md` already exists as the current canonical file:
fully developed, already framed as a US military (Space Force) shipyard run
by Dr. Eugene Hart, already cross-referenced from `char_sister_artemis.md`,
`char_eugene.md`, and the timeline files. The old `location_metis_station.md`
("The Rock / The Skin / The Throat" naming, no military framing) appears to
predate that rename and was never removed. Recommend deleting it outright
rather than patching it — keeping both risks a future session pulling stale
content from search results, which is exactly what almost happened this
session before I found the Adama file directly.

## 3. Jin's room ties to his existing three-months-of-nest-clearing thread (P-04)

This resolves the earlier flagged conflict from last session cleanly — no
retcon to `char_jin_luong.md`'s "personal, secret" framing was needed, just an
addition. Confirm the addition reads right to you; I kept it consistent with
his already-established three nascent-ability crew members and the Big Strike
gold-vein backstory rather than inventing new personnel.

## 4. Nitrogen atmosphere physics note

Flagging for visibility, not because I think it's wrong: I leaned on Jin's
already-established "[Fire Shaping] sustains flame in low-oxygen and Astral
environments" to justify fire-like signatures persisting in an inert
nitrogen room. If you want the room's fire activity to read as stranger or
more clearly non-mundane at this stage, {Aura}'s dialogue in the Ch22 patch
can be pushed further; I kept it fairly restrained per the "incomplete data,
not conclusions" rule.

## 5. Sophia's five-month timeline ripples outward

I only patched `char_sophia_lotte.md` and added a timeline cross-reference
note. I did not do a full search for every other place "seventeen months" or
a similar figure might appear (e.g., other character files referencing her
tenure, or dialogue in chapters between 15-19 that might state the old
number). Worth a project-wide search for "seventeen months" before treating
this as fully propagated.
