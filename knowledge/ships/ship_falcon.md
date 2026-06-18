---
description: "Technical specification and profile for the Falcon, a nuclear-thrust livestock and cargo transport vessel."
id: ship_falcon
name: Falcon
former_names: []
designation: NF-7 (working)
class: one-of-a-kind (Omphalos configuration — spine/spoke/ring architecture)
type: nuclear-thrust livestock and cargo transport
nicknames: ["Barnyard 1", "The Chicken Coop", "The Carousel", "The Merry-Go-Round", "The Donut" (the ring, crew slang), "The Candle" (the spine, crew slang)]

# Origin
builder: Mars-based shipyard (Origin Industries consortium) — heavily modified post-launch
build_location: location_mars_orbit_shipyards
launch_date: ~2075 (working — approximately 30 years before Book 1)
commissioning_date: ~2076
era: early belt expansion era

# Status
status: active
current_owner: Origin Industries / belt consortium
current_location: in transit (Mars to Fortuna Station, Book 1)
fate: ongoing

# Physical Specifications (revised — bicycle-wheel architecture)
architecture: spine / 3 spokes / ring (Omphalos configuration)
ring_radius: 40 meters
ring_diameter: 80 meters
ring_circumference: ~251 meters
ceiling_height: 6 meters
artificial_gravity: 0.3g baseline; Maureen varies it 0.3g–0.4g over the transit
spin_rate: ~2.6 RPM at 0.3g (rises toward ~3.0 RPM when she runs the ring up to ~0.4g)
total_mass_at_departure: up to ~2,000 metric tons
mass_breakdown: >
  Ship and ring structure: ~500 tonnes. Pods and cargo: up to ~500 tonnes. Water and
  argon reserves: ~1,000 tonnes at departure.
age: ~30 years, heavily modified and patched

note_on_scale: >
  The Falcon's ring is deliberately small relative to a comfort-optimized design. At a
  40m radius, the spin rate needed to hold 0.3g (~2.6 RPM, up from an earlier working
  figure of 2.3 RPM at a larger radius) is high enough that crew and any passengers
  feel mild, persistent space-sickness, and high enough that bearing stress and
  plumbing strain are a constant, plausible background threat. This is intentional —
  it is what makes the Book 1 plumbing crisis (Ch. 2) believable. Fortuna Station, by
  contrast, is being built at a 100m radius held at a constant ~1/3 g specifically to
  bring spin rate down and comfort up for long-term residents (see
  location_fortuna_station.md).
variable_spin: >
  Maureen does not hold the ring at a fixed rate. Over the transit she deliberately
  varies spin between ~0.3g and ~0.4g (≈2.6–3.0 RPM). Partly this is operational
  margin-management; partly it is good animal husbandry — varying the apparent gravity
  keeps the livestock from adapting to a single load and teaches them some movement
  variety before they reach a station. It also normalizes the idea, for the reader,
  that spin (and therefore "gravity") is something a captain dials up and down — which
  pays off in the plumbing-crisis de-spin and later on-station.

# Architecture
spine: >
  "The Candle" (crew nickname) — the ship's central shaft, stationary relative to the
  ring's spin. Houses the nuclear electric/thermal drive, reactor, primary fuel and
  water tankage, heat radiators, engineering spaces, main docking ports, and cargo
  handling systems. The spine carries all thrust loads — the ship is pushed through
  space by the spine, with the ring trailing structurally behind it.
spokes: >
  Three large structural spokes connect the spine to the ring. They carry elevators,
  ladders, fluid transfer pipes, power lines, and data networks. Climbing from the ring
  toward the spine feels like climbing "uphill" toward zero gravity.
ring: >
  "The Donut" (crew nickname) — the rotating habitat ring, 40m radius / 80m diameter,
  spinning at ~2.6 RPM to produce 0.3g. The outer wall is "down." The inner wall is
  "up." Walking the ring's ~251m circumference feels like walking a circular
  neighborhood street. Most crew rarely enter the spine except for work assignments.
conical_shield: >
  Large umbrella-like forward debris shield of layered fiber composite, mounted at the
  spine's leading face; deflects space dust and micro-meteorites during transit.

# The Module / Berth System
berth_count: 36 total (18 per side)
module_size: ~13 meters (derived from the historical 40-foot shipping container standard)
module_volume: ~65-70 cubic meters internal; ~35-45 cubic meters practical usable space
module_types: >
  Crew quarters, settler/family housing (powered down this voyage), medical clinics,
  laboratories, machine shops, livestock enclosures, storage, and emergency shelters.
  Modules are standardized and fully interchangeable — the same physical units used
  aboard the Falcon can be unberthed and relocated to Fortuna Station, where they serve
  as emergency shelters or are folded into permanent station structures. See
  [technology/tech_modular_pod_canisters.md] for the full concept.
design_philosophy: >
  Heavily compartmentalized and over-engineered for survival. Airlocks sit at every
  module and corridor boundary, not just at major hull breach points. The ship assumes
  things will eventually go wrong locally, and is built so that "locally" stays local.

# Livestock Pod Mapping (Book 1 Voyage)
container_to_pen_mapping: >
  The 10 livestock enclosures established for Book 1 map onto 5 standard module
  berths. Each 13m container is split into two ~6m pens divided by a shared central
  access corridor; the two pens draw life support and environmental control through
  that shared corridor. This keeps the existing 10-enclosure manifest intact while
  fitting cleanly into the new berth architecture. See
  [livestock/falcon_animal_manifest_book1.md] for the full pen-by-pen breakdown and
  proposed pairings.

# Fluid Shielding and Dampening System
tank_zones: >
  Approximately 36 primary AI-managed fluid tank zones lining the ring — roughly one
  shadowing each module berth — plus additional connector tanks at the spoke
  junctions. (Revised down from an earlier working figure of 25 individual tanks,
  which belonged to a larger, since-abandoned ring size.)
tank_description: >
  The ~1,000 tonnes of water and argon carried at departure is a single combined mass
  budget that does double duty. The water is continuously recirculated through the
  tank zones by a localized AI, providing both dynamic ballast (counteracting crew
  movement, livestock activity, and cargo handling) and the primary radiation shield —
  it is not meaningfully "spent" in normal operation. The argon is the propellant for
  the nuclear-electric cruise engines, and is genuinely consumed. On a typical 4-month
  transit, normal operation draws down roughly 800 tonnes (80%) between propulsion use,
  life support draw, and ordinary leakage; the remaining ~200 tonnes (20%) is reserve
  margin held for emergencies or course changes.
ai_management: >
  The fluid management AI pumps continuously, routing liquid mass around the ring to
  counteract any shift in the ship's center of balance — crew movement, livestock
  activity, cargo access, even a running dog. It maintains spin stability within tight
  tolerances, but the Falcon's smaller, faster-spinning ring leaves a thinner margin
  for error than a larger, slower design would.
radiation_shielding: >
  The outer liquid layer is the primary cosmic radiation shield, absorbing solar flares
  and deep-space radiation before it reaches biological payload.
sound_profile: >
  The pumping system is constant and audible throughout the ship. Liquid surging
  through pipes, pressure valves cycling, the deep resonant thrum of mass in motion.
  New crew find it disorienting. Veterans stop hearing it. It becomes part of the
  ship's voice — and its absence, if the system ever stopped, would be immediately
  alarming.
known_quirks: >
  30 years of add-on plumbing, patches, and improvised fixes make the fluid system a
  maintenance nightmare. Leak events are common — small ones freeze into ice geysers
  on the exterior hull. Drone swarms patch continuously. A major failure is always
  theoretically imminent. The Falcon's tighter ring radius and higher spin rate mean
  this risk runs hotter than it would on a larger, gentler design. This comes to a
  head in the Book 1 near-disaster event (Ch. 2).

# Camera and Communications System
cameras: >
  The Falcon has cameras throughout — corridors, machine shop, crew areas, and all ten
  animal enclosures. Originally installed for animal welfare monitoring and remote
  engineering oversight (Saul uses them from Mars to review Jace's work). In practice
  they serve a broader function.
pig_cam: >
  The livestock enclosure feeds — particularly the pig-cam — have become popular
  viewing for Fortuna Station and beyond. The gilts' antics (panel investigations,
  social hierarchies, scrub brush performances) have developed followings. Nick Lee at
  Fortuna references pig-cam events casually in conversation with Jace, as if
  commenting on a shared TV show.
comms_context: >
  The camera and comms system illustrates how connected the solar system has become.
  Lanchee consults on Fortuna medical cases daily. Saul reviews Jace's repairs from
  Mars. Nick and Jace play games with a shrinking time lag. The ship is isolated in
  space but not in communication. The coming comms blackout will cost something real.

# Cargo
cargo_system: >
  General and habitat cargo now travels in the standardized 36-berth module system
  (see above) rather than as loose exterior pods. The maintenance drone swarm retains
  its own small dedicated supply caches (see Drone Swarm, below) for repair materials,
  which is a distinct and much smaller-scale system.
dynamic_balancing: manifest AI handles symmetrical loading/unloading of berths at waypoints

# Crew (Book 1 Voyage)
captain: char_maureen (grumpy, near retirement, wants out)
engineer: char_saul (NOT aboard — on Mars recovering from cancer surgery; monitors remotely)
animal_handler_1: char_mei (undercover; listed as animal tender)
animal_handler_2: char_jace_apollo (junior; split duties — animals and drone repair)
ship_doctor: char_lanchee (demure, rarely seen; consults Fortuna medical cases remotely; lives and works out of her own canister module — see char_lanchee.md)
total_human_crew: 4 aboard (Maureen, Mei, Jace, Lanchee)
remote_crew: char_saul (Mars; time-delayed oversight via ship cameras)
automated_crew: ~30 maintenance drones (exterior hull repair swarm)
personal_drones: Thing One, Thing Two (Jace's HUD-controlled personal drones)
fabrication_drone_in_progress: Sparky (Jace's custom survey drone, under construction)
settlers_this_voyage: none (all life support allocated to livestock)
settler_cabins: present but powered down this voyage

# Livestock (Book 1 Voyage)
total_animals: 54 female breeding stock + 2 dogs (Cerberus male, Siren female)
enclosures: 10, mapped onto 5 module berths (see livestock/falcon_animal_manifest_book1.md)
notable_animals: >
  Siren follows Maureen everywhere; Maureen secretly feeds her treats. Siren also
  spends hours in Lanchee's canister, asleep across her feet.

# Drone Swarm
exterior_drones: hundreds of repair robots crawling hull continuously
drone_tasks: welding micro-fractures, injecting sealants, reinforcing hull sections
maintenance_supply_pods: small dedicated 6m³ supply caches for repair materials (distinct from the 13m module/berth system)

# Ship AI / Systems
majordomo: ship-side AI managing integrated systems
known_conflict: >
  Maureen has not integrated Jace's personal drones with the ship's majordomo —
  citing certification protocols. Jace manages Thing One and Thing Two manually
  through his HUD. Low-grade ongoing friction.
aura_integration: ship Aura instance, federated with crew Auras

# Narrative Role
role_in_narrative: primary confined setting for Book 1 transit chapters
symbolic_meaning: the ark; the second-chance vessel; jury-rigged and imperfect but irreplaceable
uniqueness: >
  The Falcon is one-of-a-kind. She is the only vessel currently capable of moving
  large quantities of animals and food to belt stations. Newer Omphalos-class designs
  are in development but not yet operational. Every belt station depends on her.

# Cross-references
related_factions: [faction_belter_stations, faction_megacorps, faction_origin_industries]
related_characters: [char_jace_apollo, char_mei, char_maureen, char_saul, char_lanchee, char_cerberus, char_siren]
related_locations: [location_mars_orbit, location_fortuna_station]
related_events: [book1_plumbing_crisis, book1_jace_transit_chapters]
related_technology: [technology/tech_modular_pod_canisters.md]

# Revision Notes
- 2026-06-16: Major architecture rewrite. Replaced single-rotating-cylinder
  description with spine/3-spoke/ring (bicycle wheel) architecture. Ring resized to
  40m radius / 80m diameter (down from 100m diameter). Spin rate updated to ~2.6 RPM.
  Total mass revised to ~2,000t (down from 10,000+t) with explicit breakdown. Fluid
  tank count revised from 314 to ~36 zones. Exterior "hundreds of 6m³ cargo pods"
  system retired in favor of the 36-berth modular system. "Donut" and "Candle" retained
  as crew nicknames only. Pending: Chapters 1-2 still use the old 314-tank language and
  need a terminology pass to match.
---

# Falcon ("Barnyard 1" / "The Merry-Go-Round")

## Summary

The *Falcon* is a 30-year-old, one-of-a-kind nuclear livestock transport running the
Mars-to-Fortuna-Station corridor. She is not glamorous. She is a spine, three spokes,
and an 80-meter ring held together by drone swarms, improvised plumbing, and
institutional stubbornness. She smells like animals. Her fluid shielding system is a
plumbing disaster waiting to happen. Her captain wants to retire. Her maintenance logs
read like a confession.

She is also the only ship in the solar system that can move hundreds of animals and
tons of food to the asteroid belt. Every station in the belt depends on her. This makes
her, improbably, one of the most important vessels in human space.

## Architecture

The *Falcon* uses an Omphalos configuration — what engineers describe formally as a
spine/spoke/ring vessel, and what every spacer just calls "a bicycle wheel wrapped
around a nuclear tugboat." A stationary central spine (crew nickname: the Candle)
houses propulsion, reactor, and sensitive equipment. Three structural spokes carry
power, data, and fluid lines out to a rotating 80-meter ring (crew nickname: the
Donut), which spins at ~2.6 RPM to provide 0.3g. The outer wall of the ring is "down."
The inner wall is "up." A large conical fiber shield deflects debris at the spine's
forward face.

Running the ring's inner circumference is about 251 meters.

The ring is small enough, and spins fast enough, that the Coriolis effect is
noticeable — crew and any passengers get mild, intermittent space-sickness, especially
early in a voyage or after time in the zero-g spine. It is also small enough, and
spins fast enough, that bearing stress and plumbing strain are a real and constant
background risk. Everyone aboard understands, at some level, that the ship is running
closer to her margins than a newer design would.

## The Module Berths

The ring carries 36 standardized berths (18 per side), each sized to accept a ~13-meter
modular unit. These modules are interchangeable — crew quarters, clinics, machine
shops, livestock enclosures, storage, whatever the voyage needs — and the same
physical units can be pulled and relocated to Fortuna Station, where they double as
emergency shelters or get folded into the station's growing permanent structure. See
[technology/tech_modular_pod_canisters.md] for the full concept, including how this
plays out for individual characters like Lanchee.

For Book 1's livestock voyage, the 10 established animal enclosures are mapped onto 5
of these berths — each container split into two ~6m pens sharing a central access
corridor and life support. See [livestock/falcon_animal_manifest_book1.md].

The whole ship leans heavily over-engineered for survival: airlocks sit at nearly every
compartment boundary, not just at hull breach points. Nothing failing locally is
allowed to stay local for long.

## The Fluid System

The ring is lined with roughly 36 AI-managed fluid tank zones — one per berth, plus a
few connector tanks at the spoke junctions — carrying a combined ~1,000 tonnes of
water and argon at departure. The water handles dynamic ballast and radiation
shielding and is mostly recirculated rather than spent; the argon is genuinely consumed
as propellant for the cruise engines. A typical 4-month transit burns through about 80%
of that combined mass, leaving 20% in reserve for emergencies or rerouting.

Every mass shift aboard — a crew member running the ring, a pig leaning on a panel, a
module being accessed — is counteracted by liquid moving somewhere else in the hull.

It is loud. The pumping never stops. The pipes groan and surge. Pressure valves cycle
with a rhythmic thunk that new crew notice and veterans have stopped hearing. The
sound is the ship's heartbeat. If it ever stopped, everyone would wake up immediately.

After 30 years of repairs and improvisations, the plumbing is held together by
attitude — and held to a tighter tolerance than it would be on a larger, slower-spinning
design. A major failure is always theoretically imminent. In Book 1, it happens.

## The Camera System

Cameras cover everything — corridors, compartments, the machine shop, all ten
livestock enclosures. Originally installed for animal welfare monitoring and remote
engineering oversight. In practice they are the ship's eyes for anyone who cares to
look.

Saul watches Jace's maintenance work from Mars, voice notes arriving minutes after the
fact. Lanchee's Fortuna patients are as familiar to her as if she'd already met them.
Nick Lee on Fortuna follows the pig-cam like a nature documentary and references the
gilts' latest activities in casual conversation. The ship is 200 million kilometers
from anywhere and completely connected.

The comms blackout, when it comes, will cut all of this at once.

## Crew Dynamics (Book 1)

Four humans on an 80-meter ring with fifty-four animals and two dogs.

Maureen commands. Wants to retire. Blames Jace for everything she can. Feeds Siren
treats in private.

Mei tends animals and says very little. Progress measured in words per day.

Lanchee tends her patients remotely from her own canister-clinic and is rarely seen
outside it. Siren has decided it's the second-best place on the ship.

Jace does the work. His engineer is on Mars sending voice notes. His captain won't
integrate his drones. His crewmates are a study in productive silence. The animals, at
least, are never boring.

## The Machine Shop Arrangement

Jace performs maintenance beyond his job description in exchange for Maureen's tacit
permission to use the fabrication room and printer. The arrangement is never formally
negotiated. Saul is watching the repairs from Mars and leaving approving notes. Maureen
reads them every evening and says nothing.

## Open Questions

- Whether the *Falcon*'s return voyage involves anything significant
- Specific timeline of anomaly events during transit
- Whether Maureen formally acknowledges Jace's contributions at Fortuna
- Whether the comms blackout has a specific triggering event or gradual onset
- Exact spoke-junction tank capacity vs. per-berth tank capacity (currently approximate)
