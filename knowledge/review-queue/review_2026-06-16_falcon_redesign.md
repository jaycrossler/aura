---
id: review_queue_2026-06-16_falcon_redesign
type: review_queue_item
status: open
created: 2026-06-16
---

# Review Queue — Falcon Redesign Follow-ups

## 1. Chapters 1-2 terminology pass (flagged, not yet done)
`scenes/book01-ch01-morning-round.md` and the Ch. 2 plumbing-crisis draft were written
using the old architecture: "314 tanks," 100m diameter, 2.3 RPM references. These need
a pass to match the revised ship_falcon.md (40m ring radius, ~36 tank zones, ~2.6 RPM).
Not committed in this round — staged for a future session.

## 2. Pre-existing gravity inconsistency (newly discovered, not introduced by this round)
`scenes/book01-transit-vignettes.md` states the *Falcon*'s cylinder "spins to ~0.4g,"
which conflicts with the 0.3g established everywhere else (ship_falcon.md and prior
drafts). This predates the current redesign — flagging it now since it was noticed
during the architecture rewrite, but leaving it untouched until you want to address it.

## 3. Fortuna Station design — explicitly deferred
Per discussion, Fortuna Station's full redesign (100m ring radius, ~1.8 RPM, ~100
containers per wheel, total station mass still TBD/placeholder, asteroid-surface vs.
ring-side manufacturing split) is intentionally NOT included in this commit. To be
worked through in a dedicated session.

## 4. Tank zone count is approximate
ship_falcon.md sets ~36 fluid tank zones (one per berth) as a clean, working number
rather than a precisely engineered figure. Fine for now; flag if the plumbing crisis
chapter needs a more exact number for a specific failure description.

## 5. Animal pen pairings (Container Mapping) are a first draft
`livestock/falcon_animal_manifest_book1.md`'s 5-container pairing logic (sheep+goats,
pigs+cattle, ducks+geese, chickens+turkeys, rabbits+dog) is proposed, not confirmed.
Worth a quick gut-check against any blocking or scene needs already drafted.
