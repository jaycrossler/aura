---
id: tech_sleep_masks
name: "Sleep Mask Scrubbers"
type: technology
status: canonical
canonical: true
last_updated: 2026-07-04
description: >
  Standard-issue sleep respiratory mask technology used across Mars, ships, and
  belt stations. Covers normal operation, emergency-breather capability under
  vacuum and low-density-atmosphere conditions, and the electrolytic tablet
  system. Consolidates and reconciles scattered mask details previously spread
  across spec_crossing_mechanics.md.
cross_references:
  - "[[spec_crossing_mechanics]]"
  - "[[char_jace_apollo]]"
  - "[[char_sophia_lotte]]"
  - "[[char_cerberus]]"
  - "[[char_dog_siren]]"
  - "[[char_helena]]"
---

# Sleep Mask Scrubbers

## Overview

Sleep respiratory masks — universally called "scrubbers" — are standard personal
equipment across the belt, on Mars, and aboard every ship. They are not medical
devices; they are as unremarkable as a seatbelt. Children grow up wearing them.
Every bunk on every station and ship has one, and most people own a personal
mask rather than using shared equipment.

Functionally, a scrubber is a lightweight CPAP-style device: a sealed nose or
mouth mask connected to a small pump/scrubber unit, worn during sleep. Many
models and manufacturers exist — cheap disposable-cartridge versions, mid-range
reusable units, and high-end integrated models that report biometrics to a
personal {Aura} or HUD.

## Primary Purpose — CO2 Management in Low Gravity

In low gravity, exhaled CO2 does not rise and disperse the way it does under
Earth gravity — it pools near a sleeping person's face and is reinhaled. Over a
full night's sleep this produces hypercapnia: disturbed dreams, headache,
confusion, and in poorly-maintained quarters, genuine danger.

The scrubber solves this continuously: it pulls air in, scrubs CO2, and pushes
clean, pressurized atmosphere back to the mask. Under normal operating
conditions — plugged into station or ship atmosphere, functioning normally — a
scrubber can run **for days** without needing to be recharged or swapped. This
is its everyday job, and it is not oxygen-limited in any meaningful way; it is
managing air circulation and CO2 removal, not manufacturing breathable gas from
scratch.

## Secondary Purpose — Emergency Breather

Every scrubber also functions as a short-duration emergency breather if the
surrounding atmosphere fails or is lost — a hull breach, a suit failure, or
(unknown to most users) an accidental Astral crossing.

This mode relies on small electrolytic tablets loaded into the unit. When
normal ambient air is unavailable, the tablet electrolyzes to produce
breathable oxygen directly. Every properly maintained mask should have a fresh
tablet loaded at all times — this is a basic-maintenance expectation, like
checking a smoke detector battery, though not everyone is diligent about it.

**Duration depends on the environment:**

- **True vacuum / complete airless environment** (e.g. a hull breach to open
  space): a single fresh tablet supplies approximately **2–3 hours** of
  breathable oxygen.
- **Low-density existing atmosphere** (e.g. the Never-Never inside or near a
  ship or station, where a small amount of physical-space air has
  quantum-tunneled across the dimensional boundary): the same mask can extend
  usable air to **3–6 hours**, since the mask is supplementing trace ambient
  gas rather than manufacturing all of it from the tablet alone.

This is not a rebreather with unlimited capacity — it is a genuine ticking
clock, and belt culture generally treats "how long is your scrubber good for"
as a practical, unremarkable safety question, not a dramatic one.

## Cross-Species Use

Jace has fitted both Cerberus and Siren with scaled-down sleep masks of the
same basic design. This is not exotic — pet and working-animal respiratory
gear is a normal belt product line, given how many animals live aboard ships
and stations in low gravity.

## Story Notes

- Helena's case (see [[char_helena]]) hinges on mask status at the time of her
  crossing — she was wearing hers, which is why she had hours rather than
  seconds before her death, and why the timeline of her disappearance makes
  sense forensically once the Astral explanation is known.
- Jace's early accidental crossings (see [[spec_crossing_mechanics]]) rely on
  his mask being on and functional without his knowledge of why it matters.
- Sophia can pull an extra jar of tablets into the Astral with her, but only
  with significant effort — bringing inert objects across is hard for her.
  Jace, once he begins deliberately practicing, finds this dramatically
  easier, and eventually rigs multi-tablet sequential-drop canisters for
  extended air, and later still learns to pull full oxygen/nitrogen tanks
  across undetected — see [[spec_crossing_mechanics]] for the progression of
  his Astral basecamp construction.

## Cross-References

- [[spec_crossing_mechanics]] (mask survival window during accidental
  crossings; supersedes/reconciles the earlier 3–6 hour figure, which
  described the low-density-atmosphere case specifically, not vacuum)
- [[char_jace_apollo]]
- [[char_sophia_lotte]]
- [[char_helena]]
- [[char_cerberus]]
- [[char_dog_siren]]

## Revision Notes

- 2026-07-04: New file. Consolidates sleep mask/scrubber mechanics previously
  scattered through spec_crossing_mechanics.md. Establishes CPAP-style
  standard-gear framing, the days-long normal-operation duration, the
  electrolytic tablet emergency-breather mode, and the two duration figures
  (2–3 hrs vacuum / 3–6 hrs low-density Astral air) — reconciling what had
  read as a conflicting single figure in spec_crossing_mechanics.md. Added
  cross-species use (Cerberus, Siren) and forward pointer to Jace's later
  basecamp-construction air-supply progression.

⚠️ FLAG for review-queue: spec_crossing_mechanics.md's existing "Open Questions"
line — "What is the exact scrubber lifetime of the standard belt sleep mask?
(4-8 hours is the working range)" — should be removed/resolved now that this
file exists. Recommend a small patch to spec_crossing_mechanics.md pointing to
tech_sleep_masks.md as the authoritative source, rather than duplicating the
numbers in both places.
