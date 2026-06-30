---
id: visual_profile_fortuna_station
name: "Visual Profile — Fortuna Station"
type: visual_profile
subject_id: location_fortuna_station
status: good
completeness: 75
last_updated: 2026-06-28
description: >
  Canonical visual, sensory, and production reference for Fortuna Station.
  Good detail from location files; some zone-specific details need confirmation.
cross_references:
  - locations/location_fortuna_station.md
  - locations/fortuna_station_population_neighborhoods.md
images:
  - path: images/locations/location_fortuna_station__concept.png
    type: concept
    section: null
    caption: "Fortuna Station — exterior establishing shot"
    prompt_version: 1
    status: pending
    generated_at: null
    model: null
    model_version: null
  - path: images/locations/location_fortuna_station__map.svg
    type: map
    section: null
    caption: "Fortuna Station — ring structure diagram"
    prompt_version: 1
    status: needs_svg
    generated_at: null
    model: null
    model_version: null
  - path: images/locations/location_fortuna_station___the_barn__concept.png
    type: concept
    section: the-barn
    caption: "The Barn — Fortuna Station livestock section"
    prompt_version: 1
    status: pending
    generated_at: null
    model: null
    model_version: null
---

# Visual Profile — Fortuna Station

> **Completeness: 75%** — Best-documented location in the KB. Exterior and
> zone character well-established. Specific dimensions and The Barn details
> need author input.

---

## Exterior Appearance

| Attribute | Canonical value | Source |
|---|---|---|
| Structure | Three-ring architecture: Founders Ring, Civic Ring, Expansion Ring | fortuna_station_population_neighborhoods.md |
| Rotation | Constant ~1/3 g (~1.7 RPM) | location_fortuna_station.md |
| Scale | ~350 permanent residents + 50-150 transient; largest belt station | location_fortuna_station.md |
| Era | 2060s–2080s construction; expansion era practical | inference |
| Primary materials | Regolith composite, recycled hull plate, polymer glazing | inferred from "industrial, unfinished" |
| Overall impression | Industrial, practical, busy; temporary-looking fixtures that became permanent | location_fortuna_station.md |
| The asteroid | Embedded in or attached to an asteroid; the rock is visible in establishing shots | inference from "crystal tunnels" |
| [AUTHOR INPUT NEEDED] | Approximate diameter of the rings? Visible docking ports? Antenna arrays? | — |

### Exterior Image Notes
The station should NOT look like a sleek sci-fi station. It should look like
something that was built in stages, added to, patched, and used hard. The
asteroid rock it's attached to should be visible. Docked ships (including
the Falcon, a nuclear-thrust livestock ferry) add to the industrial feel.

---

## Interior Lighting Character

**This is the most important visual element of the interior.**

| Zone type | Lighting | Color temperature | Effect |
|---|---|---|---|
| Lived-in spaces (habitation corridors, common areas, Barn) | Warm artificial; amber-tinted aging LED | 2700-3000K equivalent | Home; accumulated life |
| Working spaces (factory floor, airlocks, smelter adjacent) | Cold blue-white functional | 5000-6000K equivalent | Tool; not a home |
| The Mess | Warm but institutional; the warmth of a diner, not a home | 3200K equivalent | Community space |
| Transition zones | The shift from warm to cold and back is the visual grammar of the station | — | Boundary between home and work |

The warm/cold transition is the station's visual identity. Images should capture it.

---

## Zone Visual Profiles

### The Barn
- Warm; chaotic; the one place on the station with biological texture
- Animal sounds carry further than planned
- Hay dust in recycled air (visible in light shafts)
- Improvised animal management: Jace's domain shows in how it's organized
- [AUTHOR INPUT NEEDED] — what animals? Beyond pigs. Chickens? Goats? All of the above?
- [AUTHOR INPUT NEEDED] — size? Can multiple large animals be loose simultaneously?
- The "Pig Cold War" scene: two pig factions with distinct territories; this is comedy but also real

### The Mess
- Worn furniture, mismatched, assembled from whatever was available
- Where the Jace/Cerberus/Sophia meeting happens (in the Astral layer of it)
- Community space; the place people actually use
- Coffee at 4 Tokens — the economy of the station visible in small things

### Habitation Corridors
- Narrower than working zones; warmer lighting
- People have put things on walls — this is important; accumulated personal effects
- The difference between a corridor anyone walks and a corridor people live in

### Factory Floor / Smelter
- High ceiling; cold lighting; the industrial scale of what the station actually does
- Deep vibration from smelter operations felt through structure during shifts
- [AUTHOR INPUT NEEDED] — what specifically is manufactured? Metal spar production mentioned elsewhere

### Observation Gallery
- Large panoramic viewing; the most important morale space
- Where people gather for arrivals, departures, meteor showers
- [AUTHOR INPUT NEEDED] — which ring? What's the view?

---

## Sensory Profile (for scene writing and audiobook)

| Sense | Description |
|---|---|
| **Visual** | Industrial, unfinished, busy; temporary-looking fixtures that became permanent; warm amber in lived spaces, cold blue-white in working spaces |
| **Sound** | Station hum — slightly lower than the Falcon's, with a rhythmic component from ring rotation; animal sounds from the Barn carry further than planned; smelter operations felt as deep vibration during shifts |
| **Smell** | Recycled air everywhere; the Barn adds organic complexity; the Factory Floor smells of hot metal and cutting fluid |
| **Gravity** | Constant ~1/3 g from rotation; lighter than Mars; people who grew up in full gravity feel it in their knees after long shifts |
| **Temperature** | [AUTHOR INPUT NEEDED] — general station temperature? Cold zones vs. warm zones? |

---

## Image Generation Prompts

### Exterior Establishing Shot
```
Hard science fiction aesthetic, mid-22nd century asteroid belt setting, grounded
and realistic, NOT fantasy-stylized. Cinematic lighting. Photorealistic or highly
detailed illustration style. Exterior establishing shot of Fortuna Station —
a three-ring rotating industrial station attached to or embedded in an asteroid.
2060s-2080s construction era: practical, functional, built in stages, visibly
patched and expanded. Not sleek. Not clean. Industrial. Docked ships visible
including a large livestock ferry. The asteroid rock is part of the composition.
Deep space background. The station is lit from within — warm amber light bleeding
from habitation sections, colder functional light from working areas.
--negative fantasy, anime, Death Star sleekness, smooth white surfaces,
overly futuristic, sterile
```

### The Barn Interior
```
[HOLD pending animal manifest confirmation]
Hard science fiction aesthetic. Interior of a working livestock section aboard a
rotating asteroid station. Mid-22nd century. Warm amber lighting. Biological
texture — hay dust visible in light shafts, animal pens improvised from
available materials, working equipment. Not clean. Very much alive. [ANIMAL LIST].
The organization reflects the specific logic of someone who knows animals and
manages this space alone.
```

---

## Open Items for Author

- [ ] Ring diameters / approximate station size
- [ ] Animal manifest for the Barn (what specifically does Jace manage?)
- [ ] The Pig Cold War — how many pigs, what territories, what is the comedic detail?
- [ ] Station temperature norms
- [ ] Observation Gallery location and view angle
- [ ] What is manufactured on the factory floor (metal spars confirmed — what else?)
- [ ] Exterior: antenna arrays, docking port count, any distinctive external features?

---
---
id: visual_profile_ship_falcon
name: "Visual Profile — The Falcon"
type: visual_profile
subject_id: ship_falcon
status: partial
completeness: 55
last_updated: 2026-06-28
description: >
  Canonical visual and sensory reference for the Falcon, nuclear-thrust livestock
  and cargo transport. Decent technical detail from ship file; interior zones need work.
cross_references:
  - ships/ship_falcon.md
images:
  - path: images/ships/ship_falcon__concept.png
    type: concept
    section: null
    caption: "The Falcon — exterior transit shot, asteroid belt"
    prompt_version: 1
    status: pending
    generated_at: null
    model: null
    model_version: null
---

# Visual Profile — The Falcon

> **Completeness: 55%** — Technical profile established in ship file; visual
> character and interior zones need specific details for image generation.

---

## Exterior Appearance

| Attribute | Canonical value | Source |
|---|---|---|
| Propulsion | Nuclear thrust | ship_falcon.md |
| Primary function | Livestock and cargo transport | ship_falcon.md |
| Class | Livestock-Primary Ferry (Omphalos configuration) | ship_livestock_ferry_class.md |
| Size | [AUTHOR INPUT NEEDED] — approximate dimensions? |  |
| Visual character | [AUTHOR INPUT NEEDED] — working vessel; not sleek |  |
| Distinctive features | [AUTHOR INPUT NEEDED] — what makes the Falcon recognizable vs. other ships? |  |
| Sound | Station hum slightly higher-pitched than Fortuna's | location_fortuna_station.md |

### What the Falcon Should Feel Like
A working livestock ferry is a very specific kind of ship. It smells. It has the
plumbing complexity that comes from managing living animals in zero-to-low gravity.
It is not the vessel anyone would choose for a luxury crossing. It is also a home
for the people who work it.

---

## Interior Zones

| Zone | Visual character | Notes |
|---|---|---|
| Livestock bays | [AUTHOR INPUT NEEDED] | This is Jace's domain; the site of the plumbing crisis |
| Bridge / Operations | [AUTHOR INPUT NEEDED] | Maureen's space |
| Crew quarters | Cramped; functional; personal effects accumulated | inference |
| The plumbing crisis site | Pipes, conduit, dark; the first dimensional breach in Jace's story | arc_01.md |
| [AUTHOR INPUT NEEDED] | Are there other notable spaces? Common area? Engine section accessible? | — |

---

## Sensory Profile

| Sense | Description | Source |
|---|---|---|
| Sound | Slightly higher hum than Fortuna; the specific sound of a nuclear-thrust vessel in transit | location_fortuna_station.md |
| Smell | Animal; the specific smell of a livestock vessel; Jace is used to it, new passengers are not | inference |
| Gravity | Varies — thrust gravity during burns; microgravity during coast phases | inference |
| Temperature | [AUTHOR INPUT NEEDED] |  |

---

## Open Items for Author

- [ ] Falcon dimensions (rough scale)
- [ ] What makes the Falcon visually distinctive from other ships?
- [ ] Interior layout — can you describe the route from livestock bays to anywhere else?
- [ ] The plumbing crisis location specifically — what does that section look like?
- [ ] Bridge/operations visual character
- [ ] Any notable exterior markings, color, wear patterns?
