---
id: magic_skills_framework
name: Skills Framework — [Skill] System, Trees, and Progression
type: magic_system
subtype: progression_mechanics
status: canonical
canonical: true
description: "Reference guide for the magic skills framework, defining the bracketed [Skill] system, skill trees, and Sol human progression."
last_updated: 2026-06-26
cross_references:
  - magic-systems/magic_will_orbs.md
  - magic-systems/magic_will_and_templates.md
  - universe-spec/spec_dimensional_travel_mechanics.md
  - characters/char_jace_apollo.md
  - characters/char_kael.md
  - factions/faction_titans.md
---

# Skills Framework — [Skill] System, Trees, and Progression

## The [Skill] Convention

When Jace and {Aura} begin systematically documenting dimensional abilities, Jace
instructs {Aura} to use square brackets when naming discrete learned capabilities:
`[Long Stepping]`, `[Self Template]`, `[Far Sight]`, and so on.

This convention:
- Visually distinguishes a named, discrete capability from general prose description
- Signals "this is a thing a practitioner can learn and level" as opposed to general Will use
- Allows {Aura} to tag and cross-reference ability observations across sessions
- Emerges in-story as Jace and {Aura} independently derive a taxonomy — they are naming
  things that exist, not inventing a system

**The bracket convention is Jace's in-universe formalization.** Other practitioners
(Kael, Sophia, galactic civilizations) have their own vocabulary for the same
capabilities. Kael's terms will sometimes translate cleanly onto a bracketed skill;
sometimes they won't — her taxonomy carves the space differently. This is intentional:
they arrived at the same underlying physics from different directions.

**Usage in prose:** Magic abilities do not use bracket notation in narration or
character dialogue until the convention is established in-story. After the convention
is established, {Aura}'s logs and Jace's internal monologue may use brackets; other
characters use their own vocabulary.

---

## Foundational Mechanics

### Will as Currency

Skills cost Will to use and Will to advance. Will is generated continuously by all
conscious beings and accumulates over time. It can also be obtained from Will orbs
(see `magic_will_orbs.md`).

- **Using a skill:** costs Will proportional to the skill's power level and the
  magnitude of the effect
- **Advancing a skill:** costs Will to permanently invest in the practitioner's
  Template, unlocking higher capability; this investment is not recoverable but also
  not reversible — once learned, it is structural
- **Skill levels:** tracked as discrete integers (L1–L15+); each level meaningfully
  expands what the skill can do, not just how efficiently

### The Sol Human Baseline

Sol humans at story start have an unusual Will profile (see also `The Kael Observation`
section below):

- **Large accumulated reservoir:** 20–30 years of Will generation with no directed
  outlet. This reservoir is substantial — more raw Will than most young practitioners
  of other species possess at the same age.
- **Heavily invested in mental fortification:** All self-directed Will went inward,
  unconsciously reinforcing cognitive Template layers. Every Sol human starts with
  a passive version of [Mind Wall] already in place.
- **Physically and equipment Template near-zero:** The body Template is maintained
  by baseline biological process but has no active reinforcement. Equipment has no
  Template at all.
- **No skill structure:** Zero formal skills beyond the passive mental fortification.
  The reservoir exists but has never been directed.

This creates an asymmetric starting profile: strong passive mental defense, large
available reserve, no trained offensive or travel capability whatsoever. Kael's
diagnosis of this as "unbalanced" is technically accurate. Her interpretation of it
as primitive is incomplete.

---

## Skill Trees

### Tree 1 — LOCOMOTION
*Moving efficiently through dimensional layers*

**[Long Stepping]**
Convert locomotion into compounding acceleration in the Astral or Hyperspace. Base
speed is physical locomotion (running ≈ 20 kph; vehicle varies up to 500+ kph with
technology). Each travel period, [Long Stepping] converts a percentage of current
speed into additional acceleration that compounds forward.

- L1: 1% conversion — perceptible only over many hours; Jace's starting level
- L5: 20% conversion — meaningful acceleration within a single travel period
- L10: 100% — speed doubles each period; enables multi-light-year travel days
- L15+: 200%+ — Kael's operational range; near-exponential; the half-light-year daily ceiling

*The ceiling is not skill — it is distance limit. No amount of [Long Stepping] lets
you exceed your atomic tension tolerance. You accelerate until you hit your limit,
then stop and reset tau.*

*Mythological parallel: Hermes's talaria (winged sandals) — effortless traversal of
any distance. The myth encodes a real capability observed in practitioners of this
tree.*

**[Frame Walking]**
Read and match movement vectors of other objects or reference frames without
vector-merge penalty or collision risk. Prerequisite for cleanly boarding rotating
structures, matching orbital frames, and precision dimensional navigation.

- L1: match slow-moving objects; board non-rotating structures
- L5: match station rotation; board spinning ships at the axis
- L10: match orbital velocities; board moving vehicles at full speed
- L15+: instantaneous frame-matching; no approach phase required

*Mythological parallel: Hermes again — appearing and departing without transition.*

**[Vector Lock]**
Maintain your movement vector against external pressure — resist grabs, forced
merges, grappling. The defensive locomotion skill.

- L1: slow the merge; buy time to disengage
- L5: hold against a single untrained practitioner's grab
- L10: hold against coordinated force from multiple practitioners
- L15+: maintain vector integrity against Will-combat-level pressure

*Parallel: the unmovable quality attributed to certain legendary warriors.*

**[Slip Step]**
Momentarily release physical presence in a dimensional layer to pass through a space
too small or obstructed to navigate normally, then re-anchor on the other side. Short-
range dimensional blink. Expensive at low levels; efficiency improves sharply.

- L1: 1 meter slip; exhausting; recovery time required
- L5: 10 meters; manageable cost; usable in field conditions
- L10: 100 meters; tactical utility; can be chained with recovery
- L15+: kilometer range; near-instantaneous; Kael uses something equivalent routinely

*Parallel: Apollo's sudden appearances. Norse mythology's step-between-worlds.*

---

### Tree 2 — TEMPLATING
*Creating, reading, and maintaining higher-dimensional patterns*

**[Self Template]**
Reinforce your own body's Template to reduce atomic tension accumulation, accelerate
healing, and extend distance limits. The single most important survival skill for any
practitioner who intends to travel.

- L1: 10% reduction in tension accumulation; minor healing acceleration
- L5: distance limit roughly doubled; significant healing boost
- L10: Kael-tier limits; full healing from dimensional stress between travel days
- L15+: Template stabilization against aging; the longevity path

*This is the skill Kael most wants Jace to invest in. Without it, he is fragile in
a way that limits everything else she can teach him.*

**[Object Template]**
Imprint a Template onto a manufactured object, giving it dimensional affinity and
enabling Will-based repair. Objects with Templates survive dimensional travel far
better than unTemplated ones; they can be repaired by reinforcing the Template rather
than by physical replacement of parts.

- L1: simple objects — rope, hand tools, fabric; forged single-material items
- L5: electronics; complex alloy assemblies; Jace's HUD was accidentally L1 here
- L10: full vehicles; complex machines with multiple interdependent systems
- L15+: buildings, stations, large-scale infrastructure; begins approaching pre-Scar
  Titan-wrought construction philosophy

*The atomic weight cost rule applies: gold and platinum Templates cost enormously more
than aluminum or organic Templates. Jace's accidental HUD Templating cost nearly his
entire accumulated reserve precisely because of the precious metals involved.*

**[Template Reading]**
Perceive and interpret the Templates of other beings and objects — their health,
stress, dimensional history, skill structure, and Will distribution. At high levels,
the most powerful intelligence and diagnostic tool available.

- L1: sense gross damage in a Template; know if something is badly hurt
- L5: read emotional state via Template; assess skill level broadly
- L10: read individual skills, Will capacity, dimensional history of an object
- L15+: read deep Template history; perceive stored memories in Echo-rich Templates

*This is the skill behind Kael's diagnosis of Jace's "unbalanced" Template — she
reads the over-reinforced cognitive layers and the untouched physical ones
immediately. Sophia will likely develop this tree before Jace does.*

*Parallel: Apollo's prophecy — not prediction of the future but deep reading of
present Template state, which implies trajectories.*

**[Summoning]**
Maintain a library of Templates in memory or dimensional storage, then spend Will to
bind ambient matter to them — assembling objects or constructs from pattern plus
available material. Not conjuration from nothing: requires both Template knowledge
and accessible matter to bind.

- L1: simple geometric forms; basic structural shapes
- L5: functional tools and simple machines; recognizable objects
- L10: complex machines; multi-component assemblies; working mechanisms
- L15+: living constructs; bound organisms shaped to Template; the pre-Scar Golem
  tradition; Hephaestus's automata

*The matter must come from somewhere. At low levels, practitioners carry feedstock.
At high levels, the local environment provides. In the Astral, the dimensional
substrate itself can be shaped.*

**[Rune Writing]**
Encode Will instructions into physical substrates — carved, written, printed, or
etched. A rune holds a simplified Template or Will-program that activates under
specified conditions, operating without the practitioner's ongoing attention.

- L1: single-condition triggers; "release when struck" or "seal when unpowered"
- L5: conditional logic; "permit entry if Template matches stored pattern"
- L10: autonomous Will-programs; self-maintaining seals; the Metis Station shield
  that Kael teaches Jace is L8–L10 equivalent
- L15+: self-modifying rune systems; runes that learn and adapt

*This is the foundational technology behind pre-Scar dimensional infrastructure:
roads, waystations, Template Vaults. All were maintained by Rune Writing at
civilizational scale. The Scribes in `magic_technological_adaptation.md` are doing
L1 Rune Writing without knowing it — mechanical firing mechanisms etched with
functional geometry are runes that work in low-flux environments.*

*Parallel: Norse runic magic; Egyptian hieroglyphic sealing; Hermetic binding.*

**[Ward Setting]** *(sub-skill of Rune Writing)*
Create a dimensional barrier around a physical space that blocks Astral access from
outside and can be keyed to specific Templates — allowing named individuals through
while excluding all others. The practical defensive application of Rune Writing for
space protection.

- L1: basic barrier; blocks low-level fauna; no keying
- L5: blocks Tier 2–3 fauna; can be keyed to a small number of Templates
- L8: the Metis Station scene — Kael sets a ward keyed to each survivor's Template,
  demonstrating to Jace what organized dimensional defense looks like
- L10: active wards that respond to intrusion attempts; can expel rather than merely
  block; alert the setter when triggered
- L15+: layered ward systems; nested permissions; the kind of infrastructure that
  pre-Scar stations ran as baseline

*The Metis Station ward scene is Jace's first lesson in [Ward Setting]. He watches
Kael do it, asks how it works, and her answer — showing him the rune structure — is
his introduction to [Rune Writing] as the underlying skill.*

---

### Tree 3 — FORCE SHAPING
*Manipulating kinetic energy, pressure, and momentum*

**[Will Strike]**
Project Will as directed kinetic force — a pressure wave, not a grip. Does not
require physical contact. Scales from a candle-deflecting breath to structural damage.

- L1: candle-flame force; deflect small objects; light push
- L5: stagger a person; break loose objects free; force a door
- L10: structural damage to equipment; break welds; collapse frames
- L15+: stop bullets via vector collapse on incoming projectile; tactical demolition

*Parallel: Zeus's thunderbolt — pure projected force, not lightning specifically.
The mythology encodes the observation of practitioners doing this at high levels.*

**[Force Shell]**
Maintain a pressure differential around yourself or an object — a force field that
holds against physical force, debris, and dimensional pressure. Very expensive to
sustain; the cost scales with the force being resisted.

- L1: deflect small debris; slow a thrown rock
- L5: hold against strong physical impact; partial pressure seal
- L10: hold atmosphere against hard vacuum for short durations; the air bubble
  that Kael extends around Jace during Hyperspace transit is L10+
- L15+: functional armor against Will-combat-level attacks; Kael's layered shells

*Parallel: Achilles's near-invulnerability; the divine aegis; shields in every
tradition that cannot be broken by ordinary weapons.*

**[Vector Collapse]**
Force-merge a target's movement vector with a chosen reference frame — stopping it
in place relative to that frame. The offensive/control application of the tau
mechanics. 

- L1: slow a thrown object; reduce a running person to a walk
- L5: stop a person's directed movement; freeze small vehicles
- L10: halt a larger vehicle; freeze multiple targets simultaneously
- L15+: the full stop — drop anything moving into absolute stillness; the technique
  behind "stopping bullets" is actually L15 [Vector Collapse], not [Will Strike]

**[Pressure Reading]**
Sense pressure differentials, structural stress, and force vectors passively. The
engineering sensing skill. Jace would naturally develop this — it is how an engineer
*sees* when the layer provides the information.

- L1: sense gross structural failure risk; feel a crack before it propagates
- L5: read load distribution across a structure; identify stress concentrations
- L10: map stresses across a ship hull in real time; predict failure points
- L15+: sense force vectors at distance; read incoming attacks before contact

---

### Tree 4 — THERMAL
*Moving heat and managing combustion*

**[Heat Draw]**
Pull thermal energy from a target and redirect it. Conservation applies — heat must
go somewhere. The practitioner chooses where.

- L1: cool a small object; slow a reaction
- L5: freeze a pipe; create localized cold; extract heat from a confined space
- L10: localized cold zones; significant thermal extraction at range
- L15+: heat extraction from living targets (dangerous, ethically complex)

**[Fire Shaping]**
Direct, sustain, and sculpt combustion. Requires fuel and ignition source at low
levels; at high levels, Will itself provides both. The Bloom's primary vulnerability
— they hate fire, and this is exploitable.

- L1: sustain a flame in low-oxygen; prevent a fire from going out
- L5: direct flame direction and intensity; shape a burn
- L10: complex flame geometries; sustained without conventional fuel
- L15+: plasma-temperature working; fire as a tool with precision and distance

*Jin Lóng's primary skill tree. The emerging fire-users in the belt are independently
discovering what every fire-deity tradition encoded: [Fire Shaping] at high levels
is not a campfire trick. It is a weapon and a tool of extraordinary power.*

*Parallel: Prometheus (fire given to humanity); Hephaestus (fire as craft); Agni;
Surtr; every fire-deity tradition across human mythology.*

**[Thermal Shell]**
Maintain a temperature envelope around yourself or an object. The survival skill for
deep Astral cold (-20°C near Fortuna) and Hyperspace's worse thermal conditions.

- L1: slow heat loss; extend survivable time in cold
- L5: maintain comfortable body temperature in Astral cold indefinitely
- L10: function in extreme thermal environments (active stellar approach zones)
- L15+: extend thermal protection to others; Kael's air bubble has a [Thermal Shell]
  component keeping Jace from freezing during Hyperspace transit

---

### Tree 5 — PERCEPTION
*Sensing beyond normal range in physical and dimensional space*

**[Far Sight]**
Extend sensory awareness through the dimensional layer. Since the Astral sees at
dist², Far Sight resolves physical-space objects at ranges proportional to the
layer's compression.

- L1: sense living minds in the immediate dimensional vicinity
- L5: read physical-space objects at kilometer range via Astral projection
- L10: telescope-grade resolution across the belt; identify ships by hull configuration
- L15+: real-time awareness across an entire station; Odin's ravens as a metaphor
  for distributed sensory network at this level

*At L10+, this becomes humanity's most powerful prospecting and intelligence tool.
A practitioner in the belt Astral can survey physical-space asteroid compositions
faster than any physical instrument array.*

*Parallel: Odin's ravens Huginn and Muninn; Apollo's oracular sight; Indra's
thousand eyes; the all-seeing quality of sky deities in every tradition.*

**[Dimensional Sight]**
Perceive the dimensional layers without physically entering them. Safer than full
entry; less information; no exposure to fauna or poisoning.

- L1: sense the presence of the Astral; feel dimensional activity nearby
- L5: observe Astral events from physical space; see fauna without being visible
- L10: read Astral terrain topology without crossing; navigate by sight from outside
- L15+: perceive Hyperspace from the Astral without entering; the layer above as
  visible terrain

**[Echo Sense]**
Read the dimensional residue of past events from objects and locations. History is
encoded in the Never-Never substrate; this skill reads it.

- L1: sense emotional residue; know a place has been traumatic
- L5: reconstruct recent events from a location; see the last 24–48 hours
- L10: read deep history; access the collapse-layer residue of the Scar
- L15+: commune with coherent Echoes; receive intentional transmissions from stored
  Template fragments

*Parallel: psychometry traditions; the Cassandra archetype (involuntary L5–L8 with no
control skills to manage it — what she experienced was not madness but uncontrolled
[Echo Sense] activating near the high-history terrain of Troy).*

---

### Tree 6 — MENTAL FORTIFICATION
*The uniquely Sol human defensive tree*

**Background:** Sol humans have been generating Will for 3,000 years with nowhere to
put it. It went inward. Every Sol human unconsciously fortifies their cognitive
Template — the mental/emotional layers become dense, over-reinforced, almost
architectural in their solidity. The physical-body Template and equipment are
comparatively undefended.

To a trained [Template Reading] practitioner (like Kael), this reads as grotesque
imbalance. The cognitive layers are fortress-thick; the physical layers are
papery. Jace looks, from the Astral, like a heavily armored brain in an unprotected
body.

To a Will-Network civilization whose social structure depends on Resonance-mediated
compliance and Will Seeding, Sol humans are accidentally nearly impossible to
mentally coerce. This advantage is invisible until it is tested.

**[Mind Wall]**
Active resistance to Resonance intrusion, Template-to-Template attacks, and Memory
Leech attachment. Sol humans have a passive version of this from birth. Training
makes it active, directional, and consciously deployable.

- L1: passive (all Sol humans have this from birth); sense Resonance attempts
- L5: resist L5-equivalent directed Resonance; awareness of Template-reading attempts
- L10: actively expel an attaching Memory Leech; block high-level Resonance
- L15+: complete Template opacity; cannot be read, influenced, or attached to without
  consent regardless of attacker's skill level

*Parallel: iron and salt in folklore as protection against glamour and possession.
Every tradition that encodes "certain people cannot be enchanted" is documenting
high [Mind Wall] individuals. The resistance was always real.*

**[Will Reservoir]**
Store excess Will as a compressed internal reserve rather than radiating it
passively. The trained version of what Sol humans do naturally — but trained means
it can be compressed much further, deployed faster, and refilled more efficiently.

- L1: hold 10% more than natural baseline
- L5: hold double natural reserve; efficient compression
- L10: hold a week's generation in reserve; deploy instantly under pressure
- L15+: hold a month's generation; the "gem-like" quality of Kael's reserves seen
  in the Astral — her Will batteries are this skill at L12+

*Sol humans start with unorganized L1–L2 equivalent of this from their lifetime of
accumulation. The reservoir exists; training compresses and disciplines it.*

**[Psychic Anchor]**
Lock your identity and memory against Template stress, Echo absorption, and identity
drift. The skill that prevents the Scar's poisoning from fragmenting who you are.
Also the counter to [Summoning]-level constructs that attempt to overwrite identity.

- L1: resist casual Echo attachment; maintain self in light Scar exposure
- L5: maintain identity coherence through days in the Scar interior
- L10: operate in high-Echo environments without fragmentation; Scar corridor travel
- L15+: withstand direct Template-to-Template identity attacks; the final line

*Parallel: Odysseus tied to the mast — anchored against the Sirens' Template pull.
The rope was not metaphor. He had high [Psychic Anchor] and the mast was his physical
anchor; the song was a [Resonance Broadcast] attack and he survived it.*

**[Resonance Broadcast]**
Project your mental Template outward as a pressure wave — area suppression that
other practitioners experience as physical wrongness, dread, and the sense that they
should not be here. The offensive expression of the overdeveloped Sol human
cognitive Template.

- L1: vague discomfort in nearby sensitives
- L5: genuine fear response in unshielded practitioners; animals flee
- L10: Template-shock to unshielded practitioners; the battlefield aura of legendary
  warriors
- L15+: area suppression; every conscious being in range experiences it simultaneously

*Parallel: the divine terror (Greek: deimos/phobos) that demigods project in battle.
The Homeric heroes who caused armies to break just by being present were doing this
at L10–L12. The Berserker war-shout is L5–L8 with no theoretical framework behind it.*

**[Occlusion]**
Conceal your Template from observation — hiding your Will distribution, skill
structure, reserve levels, and emotional state from [Template Reading] attempts.
The practitioner default for any trained galactic individual in public.

- L1: blur surface emotional state; dim the glow slightly
- L5: hide active skill use; appear unTrained to casual observation
- L10: full Template concealment; appear as an untrained primitive to even skilled
  readers; Kael runs this at L10+ as baseline, always
- L15+: active misdirection; project a false Template to mislead readers

*Kael drops her [Occlusion] for Jace after the oath at Metis — one of the few times
he sees her without it. The demonstration (see Scene A-19 in arc_02) is a trust signal
that she would not extend to almost anyone.*

*Sol humans have no equivalent skill. They have been broadcasting their full Template
to any dimensional observer who cared to look since the first practitioner entered
the Astral. This is partly why Kael found them so readable — and partly why she
found them so interesting.*

---

## The Kael Observation — What She Sees and What She Misses

When Kael reads Jace's Template after the oath:

**What she sees:**
- Cognitive/mental layers: dense, over-reinforced, almost architectural. The passive
  [Mind Wall] equivalent is already structural — it is not a skill he learned, it is
  a physical property of his Template. Like finding bone where you expected muscle.
- Physical-body layers: thin, patchy, unmaintained. A practitioner who has done no
  [Self Template] work. Vulnerable in ways that read as careless.
- Will reserves: large but unorganized. The lifetime accumulation is there, but it is
  not compressed or structured — it pools and leaks rather than sitting in tight gems.
- Skill structure: zero formal skills beyond the passive mental fortification. The
  potential is visible; the discipline is not.
- Equipment: the HUD has an unexpected Template on it. She notes this. She doesn't
  comment yet.

**What she misses:**
The cognitive density is not a failure of discipline. It is three thousand years of
compression into the most complex neural architecture in the local Scar region. The
Will that went into mental fortification was not wasted — it was invested, just into
a different thing than galactic tradition values. The overdeveloped cognitive Template
makes Sol humans nearly impossible to Resonance-control, nearly impossible to Will-
Seed involuntarily, and nearly impossible to fully read at depth.

The thing Kael calls broken is the thing that will eventually make Jace — and Sol
humanity broadly — unpredictable in ways no galactic civilization's models account for.

**What she says:**
"Why are you all so broken? You are savages. Why is your Template so unbalanced?"

She is not being cruel. She is reading what she sees accurately within her framework.
The framework does not have a category for what Sol humans actually are.

---

## Sol Humans in the Astral — Visual Reference

When Jace and Kael observe other Sol humans from the Astral (Scene A-19, post-oath
at Metis), the visual contrast is striking:

**Sol humans in physical space, seen from the Astral:**
The physical body is almost ghostly — translucent, barely there. What blazes is the
cognitive layer: dense rainbow webs wrapped tight around the brain and nervous system,
kaleidoscope patches of color that shift with thought, emotion bleeding visible in
real time. The Will isn't directed anywhere — it generates constantly and radiates
outward in uncontrolled streams, pooling around the feet, dripping off the hands,
hazing the air around them. Every thought, every emotion, every passing idea is
visible as color and light. Messy. Overwhelming. Beautiful in the way of a wildfire.

**Kael seen from the Astral (with [Occlusion] dropped):**
Shining. Organized. Deliberate.
- Bones and deep structural tissue: Templated and reinforced — bright skeletal
  architecture, her physical body built not just inhabited
- Layered will-netting around her body in tight geometric shells — dimensional
  armor, functional and precise
- Floating faceted gems of Will: her reserves, compressed and contained, waiting.
  Not leaking. Not pooling. Ready.
- The umbilical to Kai: a deep cord of light running from her core outward —
  thick, load-bearing, two-way. It is not a leash; it is closer to a second spine.
- Her cognitive layer: present, controlled, thin compared to Sol humans. Her
  thoughts don't bleed. She thinks with a scalpel. Where Sol humans are wildfire,
  she is a forge.

**What Kael reads as civilization:**
Her Will is knife-sharp, organized, efficient. Sol humans' is chaotic, leaking,
haphazard. To her, the contrast is between a disciplined practitioner and a crowd
of untrained children who happen to glow very brightly.

**What the scene actually shows:**
The Sol humans' cognitive complexity — the depth and richness of those kaleidoscope
patterns — is something Kael genuinely doesn't have. Her cognitive Template is
trained and efficient and has been for three centuries. It is not that complex.
She redistributed her Will into physical Templates, equipment, and her bond with
Kai decades ago. She is more powerful. She may not be more capable of becoming
something genuinely new.

---

## Revision Notes

- 2026-06-25: New file. Full skill tree framework across six trees. [Skill] bracket
  convention established. Sol human baseline profile. Kael observation and visual
  contrast scene documented. Mythological parallels mapped to physics-first skill
  descriptions. Titans noted as convergent path in Templating/Locomotion trees.