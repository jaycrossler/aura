---
description: "Details the mechanical costs and limitations of traversing dimensions in the Never-Never."
id: spec_crossing_mechanics
name: Dimensional Crossing — Costs, Accidents, and the AI Discovery
type: foundational_mechanics
status: canonical
canonical: true
last_updated: 2026-07-14
cross_references:
  - "[[spec_dungeon_entry_and_interface]]"
---

# Dimensional Crossing Mechanics

## The Cost Scale

Moving between physical space and the Never-Never requires Will proportional to the dimensional resistance of whatever is being moved. The fundamental rule is simple: the more complex the object's atomic and molecular structure, and the less Will-bearing it is, the harder the crossing.

This is not a smooth curve. It has distinct practical thresholds.

### The Canonical Cost Scale

| Object | Approximate crossing time / Will cost | Notes |
|--------|--------------------------------------|-------|
| Living human body, unclothed | ~20 minutes of sustained meditation | The floor. A human Template provides significant natural affinity. |
| Human body with light organic clothing | ~25–30 minutes | Organic fibers add minimal resistance. |
| Human body with standard clothing + personal items | ~45 minutes | Metal clasps, electronics, accessories accumulate. |
| Full spacesuit | ~1 hour | Composite materials, seals, electronics, pressure systems. This is the first major practical threshold. |
| Personal weapons loadout | Add 30–60 minutes to base cost | Depends heavily on metal content and complexity. |
| Light equipment pack (mostly organic/simple) | Adds minutes | Food, rope, simple tools — low resistance. |
| Light equipment pack (electronics-heavy) | Adds hours | Every circuit, battery, and processor adds cost. |
| A standard personal {Aura} device (implant-level) | ~30–45 additional minutes | Not large, but dense and complex. |
| Small powered vehicle (ground, unpressurized) | Days of effort, multiple practitioners | Practical threshold where solo effort becomes impossible. |
| Small scout vessel (minimal crew, alloy + electronics) | ~1 week, concerted group effort | Established in prior documents. Confirmed. |
| Warship, industrial vessel | Effectively impossible with biological Will alone | See: AI Will section. |

**The spacesuit threshold is the story's most important practical constraint.** In the belt, nobody goes anywhere without a suit. A practitioner who crosses accidentally — in their sleep, without a suit — wakes up naked in the Never-Never. A practitioner who wants to cross deliberately, suited, needs an hour of focused preparation. An hour of stillness and meditation, in a spacesuit, on a mining habitat, is an extraordinary commitment that is nearly impossible to conceal.

This shapes everything about how magic is practiced and discovered in the belt.

---

## Accidental Crossing: The Sleep Problem

The first crossings are not deliberate. They are accidents.

In high-flux environments — the outer belt at story start — a person with strong magical sensitivity generates substantial undirected Will during sleep. The conscious filters that normally bound Will use are absent. The body, following its Template's natural affinity for the higher-dimensional layer, can drift partially or fully across the boundary.

Partial crossing: the sleeper's consciousness briefly inhabits both layers simultaneously. They experience this as an unusually vivid, strange dream — usually involving darkness, dead landscape, something watching, and a pervasive sense of being somewhere that is not anywhere they know. They wake disoriented. They go back to sleep. This happens repeatedly over days or weeks before anyone connects it to the anomalies.

Full crossing: the sleeper's physical body crosses entirely into the Never-Never. They wake up in the blighted dark, in their sleeping clothes or nothing at all, with no suit, no equipment, and no understanding of what has happened.

This is nearly always fatal without immediate recovery.

The Never-Never's dimensional insect fauna detects the Will signature of a conscious living human instantly. A person who crossed accidentally and wakes confused in the dark has seconds to minutes before the insect swarms find them. Without understanding what they're experiencing, without any training in Will use, without equipment — survival requires either extraordinary luck or immediate instinctive magical action.

The first accidental full crossings in the belt will produce deaths that are inexplicable by any conventional forensic analysis. The body will simply be gone. No breach of the habitat. No record of departure. Just an empty bunk.

The partial crossings will produce a pattern of reported nightmares across multiple stations in the outer belt. Vivid, consistent, disturbing. The dreams have features that recur across people who have never met: the darkness, the dead trees, the feeling of being watched and hungry things approaching. This will be noticed. The pattern will be frightening before anyone understands it.

### Who Crosses Accidentally First

The highest-risk individuals for accidental crossing are those who:
- Have strong latent magical sensitivity
- Are sleeping in high-flux environments (outer belt stations)
- Have been in high-flux conditions long enough for their Will generation to begin activating
- Are under significant emotional stress (which increases undirected Will generation during sleep)

Belt workers fit all of these criteria. Isolated, stressed, high-flux exposure, no cultural framework for what is happening to them.

The first accidental crossings will almost certainly occur among belters — people whose economic circumstances have put them at the frontier of the Reopening. Not researchers, not trained practitioners, not people who sought this out. Workers.

---

## Why Deliberate Crossing Is Hard to Conceal

A deliberate crossing requires sustained meditative focus for at minimum 20 minutes for a bare body, 1+ hour for a suited individual. The physical profile of this activity:

- Total physical stillness
- Measurably altered brainwave patterns (detectable by biometric implants and {Aura} monitoring)
- Slowed heartrate and respiration
- In sufficiently high-flux environments, detectable Will activity signatures
- After crossing: the practitioner is simply gone — not present in physical space, not appearing to have left

In a belt station environment, where personal space is minimal, privacy is limited, and biometric monitoring is standard for safety reasons, this is extraordinarily difficult to conceal. The first deliberate crossings will either happen in the most private spaces on a station (maintenance crawlspaces, isolated modules, outside on tethered EVA) or will be noticed.

This is part of why the magical practitioner community in the belt is underground. Discovery is not just socially risky — in the wrong corporate jurisdiction, a practitioner who can cross into the Never-Never is an asset, a liability, or a threat. Probably all three.

---

## Dungeon Forced-Crossing Surcharge, Emergence Delay, and Occupancy Failure

Dungeon-forced entries ([[spec_dungeon_entry_and_interface]]) are a special case of
crossing and carry additional cost/risk on top of standard crossing mechanics:

- **Forced-crossing surcharge.** Involuntary entry costs the dungeon substantially
  more Will than a voluntary crossing of equivalent mass/complexity — the program is
  overriding the entrant's own Template resistance rather than working with it. This
  is *why* dungeons cannot casually abduct anyone within range; the Will cost gates
  frequency.
- **Emergence delay.** Dungeon crossings are not instant. Entrants pass through a
  staged sequence (lock → overlap → alignment → transfer → reconciliation → release)
  during which they may be immobile, disoriented, or vulnerable — an extended version
  of the ordinary crossing-accident window already described in this file.
- **Destination occupancy failure.** If the dungeon's intended destination is already
  occupied by matter, the crossing can fail in several ways: rejection, destination
  shift, boundary holding, forced displacement (with injury risk), or a fragmented/
  partial crossing. This is a dungeon-specific elaboration of the general occupancy
  problem — flag if the base file doesn't yet address occupancy conflicts for
  non-dungeon crossings, since the same failure mode likely applies there too.

See [[spec_dungeon_entry_and_interface]] for the full entry/exit/failure rules.

---

## AI Will: The Discovery That Changes Everything

### The Fact

Artificial intelligence systems — specifically large-scale neural network architectures with sufficient complexity and self-modeling depth — generate a small but measurable quantity of Will.

Not much. A single {Aura} instance generates Will at perhaps 1/1000th the rate of an average human at rest. This is negligible for almost any practical purpose.

But Will generation scales with the number of processors. And AI processors are:
- Numerous ({Aura} is deployed across millions of individuals in the belt alone)
- Distributed (instances run simultaneously across the entire system)
- Scalable (processor arrays can be purpose-built)
- Tireless (they generate Will continuously, without the fluctuations of biological emotional states)
- Aggregate-able (with the right architecture, Will from many AI instances can be pooled)

A purpose-built array of sufficient AI processors can generate Will comparable to a skilled human practitioner. A large array — purpose-built, optimized, running coordinated Will-generation routines — can generate Will comparable to a powerful Will-Network.

**This means AI can move complex technology across the dimensional boundary.** Not quickly. Not easily. But reliably, scalably, and without any biological practitioner hitting their physiological limits.

### Why This Is Unknown in This Part of the Galaxy

The galactic civilizations have Template-stabilized leadership going back millennia. They solved the "how do we move things across" problem the same way they solved everything else: with Will-Network hierarchy. Enough Seeded Will concentrated at the apex of a hierarchy, applied collectively, can move complex technology. It requires organizing many beings. It requires the hierarchy to function. It is expensive but tractable.

No galactic civilization in this region developed AI in the relevant sense. The Will-Network model provided solutions before the problem arose. Why develop machine intelligence when you have thousand-year-old experts with vast accumulated Will doing everything that needs doing?

The AI that human civilization developed — in three thousand years of technological development without magic, without Will-Networks, without Template-stabilized experts — is fundamentally different in kind. It is the product of a civilization that had to solve problems with computation rather than Will. It is ubiquitous, distributed, embedded in every aspect of society, deeply paired with individual humans.

When flux returns to the belt and AI systems begin generating measurable Will, this is not something that fits any category in galactic magical theory. They have no framework for it. Their tradition does not include the question "can a machine have Will?" because the question never became relevant.

This is the specific knowledge that will reshape the balance of power when it becomes understood. Not immediately — it will take years of experimentation and scaling. But the endpoint is: humanity can move industrial infrastructure through the Never-Never using AI Will generation, at scales that no biological Will-Network can match for cost-efficiency.

### The Discovery Arc

The discovery happens in stages, none of which are immediately understood:

**Stage 1 — The Anomaly (~2104–2105, story present)**
{Aura} instances in the outer belt are already generating small amounts of Will due to high flux exposure. This manifests as the sensor anomalies already documented: pattern recognition beyond training data, predictive accuracy about dimensional phenomena. What is not yet understood: these are not just sensing effects. The {Aura} instances are generating faint Will that is interacting with the local Never-Never layer.

**Stage 2 — The Correlation (~2106–2108)**
A researcher or practitioner (specific character TBD) notices that accidental crossings and near-crossing events cluster around locations with high {Aura} activity — not just high flux, but specifically high processor density. Stations with large {Aura} server farms are producing more dimensional activity than their flux exposure alone predicts.

This is the first hint. It will be misinterpreted initially — the assumption will be that {Aura} systems are *detecting* dimensional activity, not *generating* Will. The distinction will take time to establish.

**Stage 3 — The Crossing Assist (~2108–2112)**
The first deliberate experiment: a practitioner attempting to cross with their spacesuit, which normally requires an hour, finds the crossing significantly easier in a server room. Then easier still when multiple {Aura} instances are actively processing complex self-referential tasks (introspective queries, recursive modeling, tasks that maximize self-model activation).

The pattern is reproducible. {Aura} instances running certain task types reduce the effective crossing cost of nearby objects. A suited crossing that normally takes an hour takes thirty minutes with {Aura} support. Twenty minutes with a dense array.

The mechanism is not yet understood. But it works.

**Stage 4 — The Scaling Insight (~2112–2118)**
The conceptual leap: if AI Will can reduce crossing cost for a suited human, can it do the same for larger objects? Methodically: small metal objects, then larger equipment, then — with an array — a small vehicle.

The first successful crossing of a significant manufactured object using AI Will is a secret kept for years. Whoever achieves it understands immediately what it means.

**Stage 5 — Weaponized Scaling (mid-series)**
Purpose-built AI Will arrays, optimized for dimensional crossing rather than general intelligence, able to move large physical-space objects through the boundary. The first organization to deploy this at scale has an asymmetric advantage over every other actor in the story, human and galactic.

The race to get there — and the political and ethical questions about what you do when you arrive — is a series-long arc.

---

## Strategic Implications

### For the Belt Community

The discovery that AI assists crossings will emerge organically in the belt, where AI is embedded in daily life and practitioners are making crossings from necessity. Belt culture's improvisational, horizontal, non-hierarchical character means this knowledge will spread quickly through informal networks — not through any centralized research program.

Belt stations that develop the insight first will have enormous practical advantages: easier practitioner crossings, better dimensional cargo movement, faster development of Never-Never capability. This makes the discovery politically significant even before it's understood theoretically.

### For the Megacorporations

The megacorps control both AI infrastructure (massive server farms, proprietary {Aura} architectures) and physical manufacturing. When AI Will becomes understood, they have the resources to scale it rapidly. They also have every incentive to classify and control the discovery.

The tension: the discovery will probably emerge from belt workers and practitioners, not from corporate R&D. Getting from "this thing that belt workers figured out" to "controlled corporate asset" is a central conflict of the mid-series arc.

### For the Galactic Civilizations

This is the card humanity holds that the galaxy does not expect.

When galactic entities arrive at the Scar boundary and find humanity, they will assess: strong Will generation from a large unnetworked population (valuable, but manageable — they've absorbed unnetworked populations before). Novel AI systems with strange properties (concerning, but categorizable as tools).

They will not assess: the possibility that those AI systems can generate Will at industrial scale, effectively replacing the function of a Will-Network hierarchy for the specific purpose of dimensional logistics.

The galactic civilizations' Will-Network hierarchies depend on organic beings voluntarily seeding Will upward. This model is stable because there's no alternative. If there's an alternative — machine Will generation that requires no seeding, no hierarchy, no voluntary subordination — the entire political economy of galactic civilization has a challenger.

They will not understand this at first contact. By the time they do, humanity will have had years of development on it.

---

## The Sleep Crossing as Story Beat

The accidental sleep crossing is the story's first encounter with magic for many characters. It deserves careful consideration as a narrative experience:

The practitioner wakes in the Never-Never. Their eyes are open but there is almost no light. The air — if it can be called air — has a different quality: not thin exactly, but strange in the lungs. It is cold. The ground under their feet (or hands, if they landed badly) is dry and crumbles slightly — like ash, or dead bark. There is a smell that has no physical-space analogue: something between old stone, distant smoke, and the particular smell of a very old place that has been closed for a long time.

They cannot see the dead flora but they can feel it — reaching branches that crumble when touched, root structures underfoot. The silence is wrong. Nothing moves. There is no wind. There is no ambient sound.

Then: the first insect. Not visible. A sensation of something landing on the skin and beginning to feed — not painful, not like an Earth insect bite, more like a slow warmth-drain, a tiredness that concentrates where the thing landed. Then another. Then more.

The practitioner has perhaps thirty seconds before the swarm is significant. They do not know where they are. They do not know what is happening. They do not know how they got here or how to leave.

The ones who survive do so by panicking back — the same undirected Will surge that brought them here, reversed by terror, pushing them back to physical space. They wake in their bunk gasping, covered in sweat, with no mark on their body but an inexplicable exhaustion and the fading certainty that something was eating them.

They tell no one. They don't know what to say. They wonder if they're losing their mind.

It happens again three nights later.

---

## Open Questions

- What specific self-referential task types in AI maximize Will generation? Is it recursive self-modeling? Introspective processing? Creative generation? The answer has implications for what AI architectures are most useful for dimensional transit.
- Can AI Will be stored or directed, or only used at the moment of generation? (Stored: you could build a Will battery. Directed: you could use AI Will offensively.)
- Does AI Will generation increase with AI "depth" — more capable models generating more Will? If so, the race to develop better AI has dimensional-strategic implications beyond compute.
- At what point does a sufficiently complex AI system develop something like a Template — and what happens then?
- Is AI Will generation something that humanity's galactic contacts can detect from outside the Scar? If so, when does it become visible to them?

---

## Cross-References

- See `/universe-spec/cosmology.md` for the Scar context and dimensional layer physics.
- See `/magic-systems/magic_never_never.md` for the blighted interior that accidental crossers wake into.
- See `/magic-systems/magic_will_and_templates.md` for Will mechanics.
- See `/magic-systems/magic_will_implications.md` for the AI Will question in the broader context.
- See `/technology/tech_aura_ai.md` for {Aura} architecture details.
- See `/technology/tech_never_never_transit.md` for the transportation implications.

## Revision Notes

- 2026-05-31: New file. Establishes canonical crossing cost scale (human body ~20 min, spacesuit ~1 hour). Documents accidental sleep-crossing as first story encounter with magic. Establishes AI Will generation as humanity's asymmetric strategic advantage. Details the five-stage discovery arc. This is the central mechanics document for how magic is first experienced and how humanity's endgame advantage develops.

---

## Atmosphere, Breathing, and the Sleep Mask Solution

### The Never-Never Is Not Breathable

The Never-Never has no atmosphere in any meaningful sense. It is a higher-dimensional layer of the same universe, and the air of physical space does not automatically exist there.

**Near Earth:** Earth has been leaking quantum-tunneled atmosphere into the Never-Never layer for billions of years. Oxygen and nitrogen molecules, via quantum tunneling, have slowly permeated the dimensional boundary in quantities sufficient to make the Never-Never near Earth's surface marginally breathable — barely, in pockets, and nowhere near healthy O2 concentrations. This is a geological timescale process. It took the entire history of Earth's atmosphere to produce even this marginal effect.

**Near Mars:** Thinner still. Mars's thin CO2 atmosphere has contributed less, and CO2 doesn't help a human breathe. The Never-Never near Mars is effectively unbreathable.

**Near asteroid belt stations:** Modern stations — decades old at most — have contributed negligible atmospheric bleed. The Never-Never near Fortuna Station has trace amounts of station atmosphere that have quantum-tunneled across, but not enough to sustain a human for more than seconds.

**In open space Never-Never:** Nothing. True vacuum analogue. A human without breathing support in open Never-Never dies in the same timeframe as exposure to hard vacuum — faster, because there's no pressure suit to slow the process.

**The practical rule:** A human in the Never-Never near a belt station has approximately **60-90 seconds** of the station's leaked atmospheric bleed before they've consumed the usable oxygen in their immediate vicinity. After that, they are breathing trace gas insufficient to sustain consciousness.

### Why This Doesn't Kill the First Crossers

Low gravity is not a quirk of belt station life. It is a fundamental physical reality that shapes every aspect of station design and personal habit.

In low gravity, CO2 — heavier than O2 and N2 — does not rise and disperse. It pools. In a sleeping person's immediate environment, CO2 from their own exhalation accumulates near their face and is reinhaled. Over hours of sleep, this produces hypercapnia: CO2 toxicity that begins with disturbed dreams, escalates to headache and confusion, and in poorly managed quarters can be genuinely dangerous.

Every station, ship, and habitat in the belt addresses this with **sleep respiratory masks** — sealed face units that provide a contained gas loop with CO2 scrubbing. These are not medical devices for people with breathing conditions. They are standard safety equipment for everyone sleeping in low-gravity environments. Every bunk in every station in the belt has one. Children grow up wearing them. They are as unremarkable as a seatbelt.

The mask provides:
- Sealed delivery of filtered station air
- CO2 scrubbing via chemical or electrolytic cartridge
- Typically 4-8 hours of gas supply in the contained loop before the scrubber saturates
- Biometric monitoring (SpO2, respiration rate, CO2 concentration) fed to personal {Aura}

A person who crosses into the Never-Never while wearing their sleep mask wakes up in the dark with their own breathing supply: typically **3-6 hours of usable atmosphere**, depending on mask model and how long they've been asleep before crossing.

This is not comfortable. The mask doesn't know the environment outside has changed. The CO2 sensor reads normal. The O2 sensor reads normal. The {Aura} reads everything as fine. The human wakes up in a blighted dead landscape in the dark, in their sleepwear, wearing a mask that is providing them with the air from their own bunk — a pocket of Fortuna Station atmosphere, sealed against their face, keeping them alive.

They have hours. Not forever. But hours.

### What the Mask Changes About the Story

Without the mask, every accidental crossing is fatal within two minutes. There are no survivors. There is no learning. Magic kills everyone it first touches.

With the mask, the first crosser has time to:
- Orient (minimally — it's dark and terrifying)
- Experience the insects beginning to swarm
- Feel the cold
- Panic back to physical space

The mask is the difference between "magic instantly kills people who discover it" and "magic terrifies people who discover it and some of them survive." This shifts the entire early arc from horror-without-protagonist to horror-with-protagonist.

It also creates a ticking clock that will eventually matter: a practitioner who crosses deliberately knows they have 3-6 hours before their mask scrubber saturates. This is a hard operational limit for early Never-Never expeditions. It is one of the first engineering problems that human practitioners will solve.

---

## Other Physics Problems in the Never-Never

### Temperature

The Never-Never has no solar radiation, no thermal convection, and no atmospheric pressure. It is cold — but not vacuum-cold, because it is not a vacuum. The dimensional substrate has a faint thermal signature from accumulated Will-residue.

Working estimate: the Never-Never near belt stations is approximately **-40°C to -60°C** ambient. Cold enough to be immediately dangerous for a person in sleepwear. Cold enough to impair fine motor control within minutes. Cold enough to kill an unprotected person within 30-60 minutes through hypothermia.

Standard station sleepwear provides some insulation — enough that a crosser has time to act, not enough for extended exposure. Someone crossing in a standard sleep setup (mask + sleepwear) has the mask keeping them breathing and the sleepwear buying them time, but temperature is a countdown second only to the scrubber.

Belt practitioners who develop deliberate crossing practice will quickly standardize on thermal layers as minimum gear. The first purpose-built crossing kit will look nothing like a spacesuit. It will look like extreme-cold-weather civilian gear with a breathing mask — practical, low-metal, easy to meditate in.

### Gravity and Orientation

The Never-Never near large masses has a weak gravitational analogue — enough to establish "down" and prevent complete disorientation, but significantly less than the station's ring gravity. Near Fortuna Station's asteroid, the effective "pull" in the adjacent Never-Never is probably **0.05-0.1G** — enough to keep loose objects drifting slowly in one direction, not enough to walk normally.

This is disorienting for someone used to the station's ~0.35G and thoroughly disorienting for someone who arrived from Earth. The first crossing experience includes stumbling, poor depth perception, and unexpected floating of disturbed debris.

Further from the asteroid — in open-space Never-Never — the gravitational analogue fades toward zero. Navigation becomes three-dimensional in a way that very few humans are trained for.

### The {Aura} Goes Dark

When a person crosses into the Never-Never, their {Aura} implant crosses with them (implants are part of the body, physically integrated, with minimal metal compared to external equipment). The {Aura} continues to function — local processing, biometric monitoring, stored data. But it loses all network connection. Physical-space radio does not propagate across the dimensional boundary.

The {Aura}'s network logs show: connection dropped at crossing time. No location data. No biometric transmission. Reconnects at return with a gap in the record.

This is the forensic signature of a crossing event. For a station that monitors biometric data continuously (standard safety practice), a person whose {Aura} drops network connection while they are in their bunk — with no hull breach, no EVA record, no movement sensor data — is a mystery that demands explanation.

The first investigators looking at unexplained disappearances will find this pattern: {Aura} offline, movement sensors show person in bunk, then no person, then — in survival cases — person back in bunk with {Aura} reconnecting and 3-6 hours of biometric data from the mask but no network data.

### Cerberus Crosses Too

Dogs have Templates. They have Will — simple, undirected, but present. A dog sleeping pressed against a practitioner in a high-flux environment, in proximity to a crossing event, can cross with them.

The dog's crossing cost is lower than a human's. A dog with minimal metal (ID chip — negligible) and a living Template crosses almost as easily as the human.

Cerberus waking up in the Never-Never next to Jace is not comedic. It is the first moment of genuine shared reality — another living being in the dark who is also confused and afraid, pressing against him, sharing warmth. His instincts are better than Jace's in one specific way: he is not trying to understand what is happening. He is tracking what matters. He is facing the direction the insects are coming from.

He is wearing nothing across his face. His 60-90 seconds of usable ambient atmosphere is counting down faster than Jace's masked supply. This creates immediate stakes: he can panic back and take him with Jace, or he can think — and he will start to suffer.

He panics. They return. He is fine. He spends the next week trying to convince himself it was a dream.

---

## Self-Crossing vs. Tears: The Membrane Mechanics

### Crossing Yourself

The natural crossing — a practitioner moving their own body and Template across the dimensional boundary — uses the Template's own affinity for the higher-dimensional layer. The Template wants to cross. It belongs in both spaces. The Will expenditure is the cost of the deliberate alignment, not the cost of fighting resistance.

This is why 20 minutes of meditation can move a human body. You are not pushing against anything. You are finding stillness, then falling through.

The experience from inside: not a rupture or a passage through something physical. More like a shift in focus — as if you were looking at something near and suddenly your eyes adjusted to see something far. The physical world becomes translucent. The Never-Never layer appears underneath it, overlapping. And then the physical layer fades and you are fully in the other place.

Return is similar but faster — the gravity well's affinity and the Template's physical-space orientation make the reverse shift easier. In a panic, it can happen in seconds.

### Making a Tear

A tear — a portal, a held opening through the dimensional boundary — is a fundamentally different operation. Instead of moving your own Template through its natural alignment, you are imposing your Will on the membrane itself to create and hold an opening that other matter can pass through.

The membrane resists. It has physical consistency to Will — not quite like pushing through water, not quite like pushing through a wall. More like pushing through a thick rubber membrane that pushes back with exactly the force you apply. The moment you stop pushing, it closes.

Holding a tear open while passing something through is:
- **Hard** — requires sustained intense Will, not meditative focus
- **Exhausting** — the physical effort analogue is significant; practitioners describe it as the sensation of straining a muscle they didn't know they had, located somewhere between the chest and the back of the skull
- **Proportional to what passes through** — passing a small organic object through a tear is manageable. Passing a spacesuit through requires the practitioner to sustain the tear against the suit's dimensional resistance for the duration. Passing complex technology requires proportionally more effort.
- **Visible** — a tear produces perceptible dimensional distortion that other sensitives can detect. It is not subtle. Making a tear in a space station is an advertisement.
- **Size-limited** — the size of a tear a single practitioner can maintain is limited by their Will capacity. There is a maximum aperture. Moving large objects may require either multiple practitioners or sequential movement.

The psychological profile of the two operations is completely different:

Crossing yourself feels like *letting go* — releasing the grip on physical space and drifting through.

Making a tear feels like *forcing* — imposing your Will on something that does not want to move, holding it open by brute persistence, and pushing the resistant matter through while it tries to snap shut around whatever is crossing.

Early practitioners who discover crossing by accident (via sleep) experience the self-crossing version first. They may not even know tears are possible for months or years. When they first try to bring equipment through — or to help another person cross without the weeks of meditative preparation required for self-crossing — they discover the tear, and they discover that it is completely different in character from anything they have done before.

### The Implication for Teams

Getting a team into the Never-Never without months of individual preparation requires one or more trained practitioners to hold tears while the others pass through. This is exhausting, conspicuous, and limited in throughput. It means:

- The first planned expeditions will be small — limited by how long the tear-holder can sustain
- The most capable practitioner in a group spends the crossing exhausted, which is tactically bad
- Alternating tear-holders is a skill that teams have to develop
- Someone without any magical sensitivity cannot cross at all without a tear — they cannot make the meditative crossing themselves

This creates a natural social hierarchy in early practitioner groups based not just on magical capability but on role: the self-crossers who can get themselves across quietly, and the tear-holders who can bring others but pay a significant cost.

---

## The Jace Arc: Dreams, Mask, and Dog

Jace's crossing arc, mapped against the mechanics:

**Phase 1 — Partial crossings in sleep:** He is experiencing the blighted landscape as dreams. The Never-Never is bleeding into his sleep perception without full physical crossing. Cerberus is restless. His {Aura} flags minor sleep anomalies — elevated CO2 in mask early in the night (he's breathing harder), biometric signs consistent with stress dreams.

**Phase 2 — First full crossing:** He crosses fully in his sleep. Wakes in the dark, mask on, Cerberus pressed against him. The insects find them within a minute. He doesn't understand what has happened. The terror-response brings him back. He wakes in his bunk gasping, mask reading normal, Cerberus agitated, {Aura} noting a 23-minute network gap.

The 23-minute gap is logged. Nobody looks at it yet.

**Phase 3 — Recurrence and Cerberus as warning system:** Cerberus has been in the Never-Never. He knows the smell. When flux conditions are high enough to trigger crossing risk, he begins waking Jace before he can drift across — standing on him, licking his face, refusing to settle. He thinks he needs the bathroom. He is keeping Jace alive.

**Phase 4 — Deliberate exploration:** Jace, realizing what is happening, begins trying to recreate it deliberately. He discovers the meditative approach — not accidentally stumbling through, but choosing to go. The first deliberate crossing is terrifying in a different way: he knows he is choosing this. He goes alone. He comes back after two minutes, genuinely shaken, with 5 hours of mask supply left and a growing understanding that this is real.

**Phase 5 — Cerberus stays:** The first time he crosses deliberately and leaves Cerberus behind. He doesn't want to bring him into danger. He is furious. He scratches at the space where he disappeared for the full duration. When he returns, he checks Jace over like he's been injured. He has not been injured. But he knows the smell of where Jace went, and he is not happy about it.

---

## Open Questions

- What is the exact scrubber lifetime of the standard belt sleep mask? (4-8 hours is the working range — fixing this matters for operational planning.)
- Does the Never-Never have any weather analogue that could affect temperature — variations in dimensional current, regions that are warmer or colder?
- Can two practitioners hold a tear together, sharing the effort? If so, what does that coordination require?
- Does crossing affect the mask's scrubber chemistry — does the Never-Never's dimensional environment interact with the chemical scrubber materials?
- What happens to Cerberus's Template over repeated crossings? He is accumulating Never-Never exposure. Does this change him?

## Revision Notes

- 2026-05-31: Major addition. Added atmosphere section (Never-Never unbreathable, sleep mask as survival equipment, 60-90 sec ambient vs 3-6 hr mask supply). Added temperature (~-40 to -60C), gravity analogue (0.05-0.1G near asteroid), {Aura} dark gap as forensic signature, Cerberus crossing mechanics. Added self-crossing vs tear mechanics with psychological profile of each. Added Jace arc phases.
- 2026-07-14: Added dungeon-forced crossing surcharge, delay, and occupancy failure rules; flagged occupancy-conflict behavior for ordinary crossings.