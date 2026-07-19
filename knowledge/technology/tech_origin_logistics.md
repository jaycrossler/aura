---
id: tech_origin_logistics
name: "Origin Logistics — Interstellar Consumer Fulfillment"
type: technology
status: staged_draft
canonical: false
last_updated: 2026-07-19
description: >
  Technical and cultural spec for Origin Industries' consumer logistics network:
  the Amazon-style ordering experience extended across the solar system via local
  print-on-demand fabrication, delivery tiers, fulfillment contractors, and robot
  fleets. Defines Jace's actual job — the over-qualified delivery man — and the
  quota/metrics system {Alex} enforces against him.
cross_references:
  - "[[faction_origin_industries]]"
  - "[[char_jace_apollo]]"
  - "[[char_maureen]]"
  - "[[concept_resource_scarcity]]"
  - "[[tech_fortuna_ai_personalities]]"
  - "[[arc_01_thread_A_arrival]]"
  - "[[arc_01_thread_T_transit]]"
---

# Origin Logistics — Interstellar Consumer Fulfillment

## The Promise

Anywhere humans live, the catalog follows. Origin Industries — the conglomerate
descended from the Amazon–Blue Origin merger — sells one product above all others:
the feeling that distance doesn't exist. A settler on Fortuna Station opens the
same ordering interface as a customer in Ohio. Sunglasses by tomorrow. A hot meal
in forty minutes. A coffee delivered to a work crew on the asteroid surface, if
you're willing to pay what that actually costs.

Nothing ships from Earth unless it must. The promise is kept by **local
fabrication**: regional print masters, licensed material stock, and a fulfillment
layer of robots and human contractors who turn a catalog entry into a physical
object in hours.

## How an Order Works

1. **Order placed** via HUD, terminal, or AI assistant. Origin's stack ({Alex} at
   the customer-facing layer) quotes a delivery tier and price.
2. **Fulfillment routing.** If the item exists in local inventory, a delivery bot
   or contractor picks it. If not, the print license is pulled and the job is
   queued to the nearest certified fabrication point — an Origin print hall, or a
   private forge enrolled in the fulfillment network (see *The Forge Network*).
3. **Production.** Printed, forged, assembled, or cooked locally. Complex goods
   are hybrid: printed chassis, imported chips, local assembly.
4. **Delivery.** Bots handle standard routes. Humans handle exceptions: sealed
   sections, animals, fragile goods, surface runs, anything too logistically
   heavy for a drone or too slow for the promised window, and anything a bot's
   insurance profile won't cover. The human is the expensive part and priced
   accordingly. For express runs, the contractor pulls on the blue-and-yellow
   Origin courier vest and physically runs — a decorated ex-officer sprinting a
   station ring with someone's dinner is the tier working as designed.

## Delivery Tiers (Fortuna-era examples)

| Tier | Promise | Typical price signal |
|---|---|---|
| Standard | Next resupply cycle (weeks–months) | Near-Earth catalog price |
| Local Print | 24–72 hours | 2–5× catalog |
| Priority | Same day, station-side | 10×+, human courier likely |
| Anywhere | Any reachable location, any time | Quoted per job; the 5,000-token coffee to the asteroid surface is real, occasional, and famous |

Prices in Tokens (1 Token ≈ 1 USD). The tier ladder is the visible face of
[[concept_resource_scarcity]]: raw mass is cheap, processed goods and human time
are not.

## The Forge Network

Origin doesn't own every printer — it enrolls them. Any certified fabrication
space can register as a fulfillment point and collect a **facility fee per job**
routed through it. This is the basis of Maureen's arrangement aboard the
*Falcon*: her forge room is an enrolled node, and Origin pays her a standing
facility rate (~20 Tokens/job) for its use.

**The Maureen Hack (canon):** Maureen orders a cheap stock plate — 1 Token —
every day, routed to her own forge, collecting the 20-Token facility fee on
each. Origin has never noticed and would not care if it did; the paperwork costs
more than the leak. Jace, as the assigned fulfillment contractor, is the one who
has to actually print the plates. He finds this simultaneously insulting and
inspiring. It is one of *many* such grifts — Maureen pulls credits from every
source that will leak them, and the plate hack is merely the one Jace sees
first.

## The Fulfillment Contractor

The human layer has a job title nobody puts on a résumé willingly. A fulfillment
contractor's duties, per the standard Origin belt contract:

- Care and transport of live cargo (animals)
- Local production: print, forge, and assembly jobs against the queue
- Delivery of goods, all tiers, human-exception routes
- Oversight and maintenance of printer and delivery robot fleets
- "Additional tasking as assigned" — the clause that sends a warm body who can
  manage robots wherever Origin needs one: survey runs, cargo transfers, odd jobs

**Metrics.** Every contractor runs against a live scorecard: orders fulfilled per
shift, print-queue throughput, delivery windows hit, customer ratings, exception
rates. {Alex} surfaces the numbers constantly and cheerfully. Status tiers
(Platinum and down) gate pay bonuses, queue priority, and equipment privileges.
Falling behind doesn't get you fired — it gets you *reviewed*, re-tiered, and
assigned worse routes. The pressure is ambient, polite, and total.

## Jace's Position

Jace Grant — former USAF officer, engineering degree, expert drone handler — was
hired in a 72-hour scramble when the contracted Chinese mining team withdrew from
the *Falcon* mission and Origin needed someone who could keep animals alive,
run a print queue, and manage robots. His qualifications got him the interview;
his availability got him the job. His contract is a **five-year** fulfillment
contractor agreement, compensation back-loaded, renewed annually subject to
performance review.

Nobody on Fortuna is going to call him an engineer. He is the delivery guy. He
smiles, nods, hits his windows, and tries to prove he's more than his job code —
to Carlos and Kim, to Maureen, to {Alex}'s scorecard, and mostly to himself.

The access is the compensation the contract never mentions: a fulfillment
contractor goes everywhere, carries a manifest that opens doors, and has
standing reasons to be in the forge at odd hours.

## Story Function

- **Anti-chosen-one architecture.** Jace's plot access is purchased, not fated —
  every corridor he enters, someone paid rush shipping.
- **Mundane antagonist.** {Alex}'s quota pressure runs under the cosmic threat:
  the belt is ending the world and Jace is behind on deliveries.
- **The future of gig angst.** The behind-the-scenes pain of the warehouse and
  the delivery route, extrapolated: schedule compression, metric surveillance,
  smile-and-nod service labor performed by an over-educated workforce.
- **Forge access.** His job legitimizes the bench time that produces Sparky and,
  later, Astral-native equipment.

## Automation and the Agentic Theme

Jace treats every job as a logistics graph. His HUD runs flowcharts — if/then
paths wiring printers, arms, bots, and delivery queues into hands-off pipelines.
On the *Falcon*: a ceiling-mounted ArmBot that opens printer enclosures, cleans
plates, and ferries parts to assembly. On Fortuna: a shared thirty-machine forge
hall he instruments with ArmBots, ScrewBots, and delivery drones.

When it works, automation buys him time — for games, and later for the Astral.
When it fails, it *cascades*: an arm smashes through an enclosure window, a
gripper comes up dripping molten plastic, a mis-sequenced queue floods the
delivery board. On Fortuna the failure surface is other people — a closed door,
a moved equipment rack, a lowered thermostat, and the whole graph falls over.
Fines follow. {Alex}'s scorecard remembers.

This is the series' working critique of agentic systems: delegation is
leverage, brittleness is the price, and the craft is in designing for the
failure you didn't anticipate — checkpoints, fallbacks, humans in the loop.
Nick Lee is the natural voice for the critique; Jace is the case study.

## Open Decisions

- [ ] Exact quota structure and scorecard fields {Alex} displays (want: felt in
  prose, never dumped as a table in-story)
- [ ] Facility-fee rate and plate price sanity-check against token economy spec

## Resolved Decisions

- Maureen Hack: Origin never notices and wouldn't care. One of many grifts.
  (Ruled 2026-07-19.)
- In-prose job title: people say **"delivery guy"** when they acknowledge him at
  all; usually they don't. "Fulfillment contractor" appears only in {Alex}'s
  mouth and in paperwork. (Ruled 2026-07-19.)

## Revision Notes

- 2026-07-19: Initial draft from author session. Defines Origin consumer
  logistics, forge network, Maureen Hack, fulfillment contractor role, and
  Jace's reframe from drone operator to over-qualified delivery man. Contract
  length ruled: five years (supersedes "ten-year" references in
  char_jace_apollo.md — matching edit staged).
- 2026-07-19 (v2): Express-run vest detail; Maureen-many-grifts canon; nickname
  ruling; automation/agentic-theme section added per author session.
