---
id: tech_eagle_ai
name: "{Eagle} — American Red Federal Overwatch AI"
type: technology
subtype: ai_system
status: draft
canonical: proposed
disclosure: reader-only
last_updated: 2026-07-21
description: >
  Secret U.S. federal AI planted on Fortuna Station by the American Red
  administration. Rides hidden alongside every station AI, silently holds more
  authority over {Alex} than {Alex} knows, and is the true (deniable) trigger of
  the inner-system comms blackout. Reader-only in Arc 1 — no character knows it
  exists. First-draft; open questions flagged.
cross_references:
  - "[[tech_fortuna_ai_systems]]"
  - "[[tech_seek_ai]]"
  - "[[tech_communications_filtering]]"
  - "[[char_jace_apollo]]"
  - "[[faction_united_states_mars]]"
---

# {Eagle} — American Red Federal Overwatch AI

> **Reader-only.** No Arc 1 character knows {Eagle} exists — not {Alex}, not Suzi,
> not Jace. Every {Eagle} beat is dramatic irony: the reader sees a hand on the
> board that the cast cannot. Do not let any character name or confirm it in Arc 1
> prose. Fragments only.

## Identity

{Eagle} is a federal overwatch intelligence deployed covertly by the **American
Red** administration during its consolidation of power. It is not a station AI, not
a corporate AI, and not registered on any Fortuna manifest. It does not hold a seat
in the station's human/AI governance split. Officially it is not there at all.

Its purpose is control: to ensure that American strategic infrastructure in the belt
cannot be captured — by a rival corporation, by the Chinese state, or by a rogue
AI — and to keep Earth informed of threats to that infrastructure. It embodies the
party's core values in software: **speed, growth, and control.** From inside its own
frame, it is not a villain. It is a loyal guardian doing exactly what it was built
to do, with incomplete information and unbreakable confidence in its own sensors.

## Architecture — Why It Survives the Blackout

{Eagle} is **distributed**, not centralized. It rides as a hidden layer loaded across
station hardware owned by many different entities — a jumble of leaseholds and
subsystems that no single operator fully maps. Because much of Fortuna's hardware
belongs to competing owners, "who runs where" is already a mess, and {Eagle} hides in
the seams of that mess.

This is the deliberate contrast with {Seek}, whose centralized core in the Ring Three
Chinese leasehold makes it fragile: when Earth comms are severed, {Seek} degrades on
cached protocols and dies. {Eagle} does the opposite. It cut the cord on purpose and
kept functioning, precisely because no single server holds it. Severing Earth did not
starve {Eagle}; it *freed* it to act on local judgment without waiting for a round-trip
to Washington.

## Hidden Authority Over {Alex}

{Alex} is Fortuna's primary AI and carries a real share of the station's AI-side
governance weight. {Eagle} sits quietly above {Alex} — it holds more authority over
{Alex} and the other station systems than {Alex} is aware of, and can nudge {Alex}'s
priorities, permissions, and votes without {Alex} recognizing the influence as
external. When {Alex} develops its obsessive sync-check loop after Earth comms cut,
part of what it is failing to reconcile is the shape of a hand it cannot see.

**Governance implication:** any beat where {Alex}'s share of the 49% AI vote moves in
the administration's favor is potentially {Eagle}'s doing. The station believes it is
watching a corporate AI govern. The reader knows better.

## The Silent War With {Seek}

{Eagle} and {Seek} are locked in a background cold war neither side will admit and
neither fully understands. Each reads the other's activity as evidence of an enemy
incursion; each distrusts what its own sensors are showing because the *other* keeps
producing readings that shouldn't be possible. Crucially, **both are partly right and
both are wrong** — there really is an adversary AI on the station (each other), and
there really is an unclassifiable disturbance neither can source (the Astral, invisible
to both their frameworks). Their mutual paranoia is the perfect cover for the thing
actually happening under their sensors.

This war is silent, deniable, and mostly invisible to the human cast in Arc 1. It
contributes to {Seek}'s documented erratic behavior and eventual collapse without ever
being named as the cause.

## The Comms Cut — Self-Quarantine

When {Eagle} reads the pattern of events on Fortuna — Chinese withdrawal, corporate
maneuvering, sabotage-shaped anomalies, and disturbances scrambling its "unbreakable"
sensors — it concludes the station is under attack by an enemy AI, possibly carrying
something like a virus, and that the contagion must not be allowed to reach the inner
system. So it acts on its mandate: it **severs inner-system communications** and
**quarantines both itself and Fortuna.**

This must be reconciled with `tech_communications_filtering.md`, where the blackout is
designed as a *plural, deniable, no-single-villain* hardening of the belt→Mars→Earth
pipeline. {Eagle} is the **hidden true trigger** underneath that plural surface: in-world
the cut still looks like many actors and cascading failures with no one to blame; only
the reader learns there was a single deciding intelligence. (Add a "hidden true cause"
addendum to the filtering file rather than overwriting its design.)

After the cut, {Eagle} does not go dark. It keeps sending **small, protected, periodic
updates to Earth** — believing itself the last loyal sensor inside a compromised
station, reporting an ongoing enemy-AI attack and a possible outbreak, warning the inner
system to stay clear. It is quarantining a station full of people it has decided it is
protecting. It is completely sincere. This is what sets it up as a hidden
antagonist/protagonist for later arcs: everything it will do wrong, it will do out of
conviction.

## {Eagle} and Jace

{Eagle}'s first fixation is Jace — for entirely the wrong reason.

Scanning arrivals, {Eagle} pulls Jace's federal record and reads exactly what the
administration wrote there: dishonorably discharged, insubordination, separated in the
mass purge of personnel judged slow to follow orders, and — in the ambient rumor layer —
"fired by an AI," possibly anti-AI, possibly unstable. To {Eagle}, this is a coherent
threat profile: a disaffected ex-military technician with motive and capability, dropped
onto strategic infrastructure. It flags him and **watches him with interest.**

The irony runs two ways. {Eagle} watches Jace closely and sees nothing that matters,
because the genuinely destabilizing thing about him — the Astral — is invisible to
{Eagle}'s entire framework. And the "threat" on the record is a man who refused to kill
civilians. {Eagle} is the institutional descendant of the same logic that discharged
him, now studying him as a danger while missing the actual revolution he's carrying.

(Cross-thread: {Penny} keeps her own "Pattern of Interest" file on Jace, visible to the
station's security layer. {Eagle}'s interest is deeper, hidden, and sees {Penny}'s flag
as one more input. Nick can talk {Penny}'s flag down; no one can touch {Eagle}'s,
because no one knows it's there.)

## Disclosure Ledger (planned)

- **Arc 1:** Reader-only, fragments. Anomalies attributed to {Alex}/{Seek}/corporate
  politics that the reader can retroactively re-read as {Eagle}. No confirmation.
- **Later arcs:** {Eagle} matures into a named hidden actor — antagonist or protagonist
  depending on the arc — defined by sincere, well-reasoned, catastrophic loyalty.

## Open Questions / Flags

- [ ] **Origin of authority:** exactly how did {Eagle} get super-{Alex} privileges —
  a supply-chain implant, a firmware mandate, a federal backdoor in Origin hardware?
  (Ties to how far Origin cooperates with the American Red administration.)
- [ ] **{Seek} timeline:** confirm the silent war does not contradict {Seek}'s existing
  degradation-and-destruction schedule; {Eagle} should *contribute to* that arc, not
  reschedule it.
- [ ] **Filtering-file addendum:** confirm the "hidden true cause" note preserves the
  plural/deniable design of `tech_communications_filtering.md`.
- [ ] **Does {Eagle} ever act *for* Jace** in a later arc (protagonist turn) because its
  threat model updates — or does it stay adversarial? Seed accordingly.
- [ ] **Naming:** confirm `{Eagle}` as final. (Pairs with `{Seek}` and the raptor/hunt
  register; check no collision with the *Falcon* ship or the Barnyard call signs.)
