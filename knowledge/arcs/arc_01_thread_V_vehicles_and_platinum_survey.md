---
id: arc_01_thread_V_vehicles_and_platinum_survey
name: "Arc 1 — Thread V: Vehicles and the Platinum Survey"
type: arc_thread
part_of: arc_01_falcon_and_fortuna
status: draft — scaffold only, not yet broken into individual scene contracts
canonical: true
last_updated: 2026-08-20
description: >
  New thread. The team builds a distance-capable rocket and outfits Sparky
  (already carrying his {Aura-S} chip from Chapter 24) to explore asteroids
  from the Astral side, discovers a large platinum deposit, and launders the
  discovery as a conventional survey "find" to help the station's finances.
  Testing explosions in the Astral during this work draw both Kael's and the
  Scavenging Queen's attention, seeding the swarm attack. Sets up vehicle
  capability the team will lean on again in Arc 2.
cross_references:
  - "[[arc_01_thread_X_astral]]"
  - "[[arc_01_thread_K_kael_covert_arrival]]"
  - "[[arc_01_thread_S_swarm]]"
  - "[[arc_02_woven_and_unbound]]"
  - "[[char_jace_apollo]]"
  - "[[char_sophia_lotte]]"
  - "[[char_brandon_moreau]]"
  - "[[char_nick_lee]]"
  - "[[spec_astral_lightspeed_addendum]]"
  - "[[draft_ch24_wrong_stars]]"
  - "[[draft_ch26_the_sweep]]"
---

# Thread V — Vehicles and the Platinum Survey

## Status note

This is a scaffold, not a finished set of scene contracts. It captures the
shape and sequencing the author described; individual scenes (V-01, V-02, etc.)
should be broken out and given full Must-Accomplish/Must-NOT lists once
chapter placement is decided, following the pattern used in the other Thread
files.

## Placement

After Chapter 26 ("The Sweep") and before the swarm battle (Thread S) — this
thread is the direct cause of the swarm's arrival, so it needs to resolve
before S-01 begins. Overlaps with the tail end of Thread K (Kael's covert
departure/return window).

## Physics grounding

This thread is now mechanically justified by the Astral light-speed ruling
(see `universe-spec/spec_astral_lightspeed_addendum.md`): motion through the
Astral covers physical-space distance at a compressed (dist²) rate, which is
*why* Astral-side exploration is meaningfully faster than physical-space
travel, not just a convenient escalation.

## Sequence

### V-01 — The Rocket

**Summary:** The team builds a rocket capable of covering real distance,
building on Jace's engineering background and the crossing-mechanics work
already established. Purpose (initially): give them a physical-space vehicle
that can keep pace with what they're learning is possible on the Astral side,
and give Sparky's eventual asteroid runs a physical-space anchor/recovery
point.

**Open questions:**
- Scale and crew of the rocket — one-person scout craft, or something Brandon/
  Nikos/Nick can also use?
- Does this reuse/repurpose existing station hardware, or is it built from
  scratch? Ties into Origin Industries contract logistics if the latter.

### V-02 — Sparky's Asteroid Runs

**Summary:** With his {Aura-S} chip operational (installed Chapter 24) and the
distance-transform model from X-05a/X-10 available, Sparky is sent exploring
asteroids from the Astral side — covering ground physically inaccessible to
him at that speed, scanning for resources.

**Open questions:**
- Does Jace or Sophia need to accompany Sparky into the Astral for these runs,
  or can he operate autonomously for a bounded window? This has real stakes
  given the established crossing-cost and exhaustion rules.
- How many runs before the platinum find — one lucky strike, or an escalating
  search?

### V-03 — The Find

**Summary:** Sparky locates a large platinum deposit. Given the established
materials canon (Group 11 metals as Astral-perception blockers/traversal
barriers), a platinum-bearing asteroid may itself interact interestingly with
Astral sight or crossing cost — worth checking against
`universe-spec/spec_materials` before drafting, if the author wants that
texture included.

### V-04 — The Cover Story

**Summary:** The team reports the platinum as a conventional survey find —
laundering an Astral-side discovery into something the station's institutional
structures (Origin, Kim's drone-ops survey pipeline, station finance) can
process without anyone needing to explain how it was actually found.

**Open questions:**
- Who else needs to be brought in to make the cover story hold up — does Kim
  need to be looped in at some level, or does this stay inside the existing
  small team (Jace, Sophia, Brandon, Nikos, Nick)?
- What does this do for Fortuna's finances concretely, and does it change
  station politics (e.g., China's declining 30-year investment, mentioned in
  Jin's file) in a way worth tracking?

### V-05 — The Explosions

**Summary:** Testing (rocket engine work, Sparky's Astral-side operations, or
both) produces large explosions in the Astral. This is the attention-drawing
event: both Kael (already in the system, per Thread K) and the Scavenging
Queen register it as the brightest/most significant Will-expenditure event
they've seen from this station, triggering Kael's return and the swarm's
approach.

**Must accomplish:**
1. The explosions should read as a natural consequence of ambitious,
   under-supervised experimentation — not a mistake played for blame, but a
   real cost of moving this fast.
2. This is the direct causal link into Thread S (the swarm) and Kael's return
   (K-08, not yet written — Kael's re-arrival belongs procedurally to Thread S
   as the lead-in to S-01, since her return is "only in the final part of the
   last battle" per author instruction).

## Cross-thread dependencies

- Requires Thread K's K-06 (Kael's departure) to have already happened, so her
  return in Thread S reads as a response to V-05's explosions specifically.
- Requires the physics addendum merged or at least referenced, so the
  Astral-speed justification for asteroid exploration is on record.
- Feeds Arc 2's stated vehicle needs directly — flag for
  `arc_02_woven_and_unbound.md` to cross-reference this thread once V-01
  through V-05 are fully scened.

## Revision Notes

- 2026-08-20: New thread, scaffold only. Captures author's rocket/Sparky-
  platinum/cover-story/explosion-trigger outline. Individual scene contracts
  (V-01 through V-05) still need Must-Accomplish/Must-NOT lists and exact
  chapter placement before this is draft-ready.
