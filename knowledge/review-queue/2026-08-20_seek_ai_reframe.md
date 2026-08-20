---

id: rq_2026-08-20_seek_ai_reframe
type: review_queue_log
status: open
created: 2026-08-20
related:
  - "[[tech_seek_ai]]"
  - "[[char_jin_luong]]"
  - "[[review-queue/2026-08-20_jin_asteroid_ruling]]"
last_updated: 2026-08-20
---

# {Seek} Blindness Reframe — Needs Sync in `tech_seek_ai.md`

`tech_seek_ai.md` was not retrieved during this session, so no direct edit is
staged against it. Flagging so the correction isn't lost.

## What changed

`char_jin_luong.md` (this package) now describes {Seek} as **categorically
blind to magic and to the possibility of aliens** — not merely failing to
understand anomalies, but actively misclassifying them. Its threat model has
exactly two buckets for anything it can't explain: the crew is under attack,
or the crew (or {Seek} itself) has been suborned by a rival AI. This is why it
suppressed Jin's Tick-Maw report rather than escalating it.

The older framing ("blaming the anomalies on American interference") isn't
wrong so much as under-specified — American interference is one instance of
the "attack or subversion" bucket, not the whole model. `tech_seek_ai.md`
should be checked for the same phrasing and broadened to match, so {Seek}'s
behavior reads consistently across its own tech file and Jin's character file.

## Suggested language (for whoever patches the live file)

Replace any variant of "{Seek} blamed the anomalies on American interference"
with something like: "{Seek} has no category for magic or aliens. Anomalies it
cannot classify default to one of two threat models: external attack, or
AI-mediated subversion of its own citizens. It does not fail to notice — it
actively misclassifies."

## Also check

- `char_seek_ai.md`, if it exists separately from `tech_seek_ai.md` — not
  verified this session.
- Any scene files where {Seek} internally narrates or is quoted reasoning
  about anomalies (e.g. drone/relay malfunction scenes) for the same phrasing.
