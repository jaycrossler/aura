---

id: rq_2026-08-20_immutable_sheet_corrections_pending
type: review_queue_log
status: open
created: 2026-08-20
related:
  - "[[sheet_jin_arc01_end]]"
  - "[[sheet_nick_arc01_end]]"
  - "[[char_jin_luong]]"
  - "[[char_yao]]"
  - "[[open_question_nick_crossing_resequence_v1]]"
last_updated: 2026-08-20
---

# Immutable Sheet Corrections Pending — Consolidated (2026-08-20)

Per standing KB rules, files under `sheets/` are never edited after creation.
This logs every currently-known correction against an immutable Arc 1 sheet so
a single authorized regeneration pass can apply all of them together, rather
than editing them piecemeal.

## `sheet_jin_arc01_end.md`

Current text frames Jin's fire abilities as emerging from unspecified,
station-adjacent "covert nest-clearing" and states {Seek} logged eight months
of anomalies without understanding them, blaming "American interference."

**Correction needed:** Reframe origin as the asteroid Tick-Maw encounter; note
that Jin attempted to report it and {Seek} actively suppressed the report;
correct {Seek}'s misattribution language from "American interference" to
"attack or AI-mediated subversion, categorically" (see
`review-queue/2026-08-20_jin_asteroid_ruling.md` for full context).

**Also affected:** the Progression Axis Summary's "Environmental" row ("knows
the mining tunnels cold; no Astral navigation capability yet") may need a
second look now that his crew has been actively hunting Astral fauna across
multiple asteroid claims for an extended period before Arc 1's close — this
reads as more Astral-environmental experience than "no capability yet"
suggests. Flagging, not resolving — author call.

## `sheet_nick_arc01_end.md`

Already tracked in `open_question_nick_crossing_resequence_v1.md` — Nick's
first crossing needs to move from the swarm (90 seconds, in-Astral relay) to
Chapter 23 (19 minutes, aboard the *Victoria*, refuses to cross again).
Cross-referencing here for visibility; no new information this session beyond
confirming the Ch23 placement is final and correct.

## New: Jin's crew — nascent abilities from asteroid hunts

The advancement ledger's continuity-flag table already speculated that "Jin's
three named crew members" (Yáo, Shi Gang, Li Hao) might have nascent L1
skills from suppression-adjacent exposure. With the asteroid-origin canon now
confirmed, this should be resolved more directly: Shi Gang and Li Hao have
been fighting Astral fauna alongside Jin for the same extended period, which
is a much stronger trigger for nascent manifestation than passive {Seek}
suppression pressure alone. **Author call needed:** do Shi Gang and/or Li Hao
have their own nascent abilities, and if so, what are they? Currently
undocumented beyond the existing "possible" flag. See
`magic-systems/advancement_ledger_patch.md` in this package for the interim
flag-row update.

## Recommended process

Batch all three corrections (Jin's sheet, Nick's sheet, and the new
crew-ability question) into one authorized "sheet_sequence: 2" regeneration
pass rather than three separate edits, since they touch overlapping
Arc-1-close continuity.
