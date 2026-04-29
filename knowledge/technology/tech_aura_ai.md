---
id: tech_aura
name: Aura
type: distributed_personal_ai
status: widely_deployed
era: late 21st century - early 22nd century
canonical: true
last_updated: 2026-04-28
---

# Aura

## Summary

Aura is the dominant personal AI architecture across the inner solar system at the time of the story. It is not a single AI; it is a deployment pattern. Each user runs their own local instantiation — on a wrist node, an embedded cybernetic implant, a ship-side compute node, or a station's local infrastructure. Each instance is paired to its user, learns alongside them, and operates with their data and on their behalf. There is no central Aura. There is no Aura corporate cloud (though there is corporate Aura licensing, infrastructure, and support).

Aura's distributed nature is its most important feature. Belters trust Aura because no one entity controls it. Cutting communications from Earth or Mars does not affect Aura — each user's instance keeps working locally. Compromising one instance does not compromise others.

## Origin

*Working backstory; refine as needed.*

Aura emerged in the 2050s–2060s from a confluence of trends:
- Increasingly capable open-weights large models that could run on consumer hardware.
- A privacy backlash against centralized cloud AI that had dominated the 2030s.
- The practical needs of off-Earth deployments where latency to Earth-based AI services made cloud architectures unworkable.

By the 2070s, "Aura-class" had become the dominant pattern: a moderately-sized base model that runs locally, paired with a personal context store that grows with the user, plus extensible tool-use modules and a federated update system. Multiple companies and open-source consortia produce Aura-compatible implementations. The architecture itself is documented and open; specific implementations are commercial or community-maintained.

By the 2090s, "Aura" has become a generic term, like "phone" or "browser" — it refers to the category, not a brand. People talk about *their* Aura.

## Capabilities

- **Conversational partnership.** Natural-language dialogue tuned to its user.
- **Task assistance.** Drafting documents, scheduling, calculations, navigation, code, technical lookups.
- **Translation and cultural mediation.** Real-time translation across spoken and written language; advice on cultural context.
- **Sensor integration.** Reads from connected devices — HUD, biometrics, ship sensors, environmental monitors.
- **Memory.** Long-context personal history with the user. Knows their preferences, relationships, work, history.
- **Inference.** Pattern recognition across the user's data — anomaly detection, prediction, hypothesis generation.
- **Local autonomy.** Operates fully without external connectivity. No cloud dependency.

## Limitations

- **Bounded knowledge.** A local Aura's base model is large but not infinite; it cannot match the latest large-frontier-cloud model. It compensates with personalization and tool use, not raw scale.
- **Trust scoped to user.** Aura cannot meaningfully verify external claims; it can only flag uncertainty.
- **Resource-bound.** Heavier reasoning tasks may run slowly on wrist or implant hardware. Ship and station nodes are typically more capable.
- **No intrinsic ethics module.** Aura is generally well-behaved through training and user calibration, not through hard rules. A user who pushes their Aura toward antisocial behavior can succeed, partially.
- **Not omniscient. Not a personality. Not a friend.** Strong cultural norms encourage users to remember that their Aura is a tool that *behaves like* a partner, not an entity that is one. These norms erode in practice.

## Architecture (Hand-Wave)

A typical Aura deployment comprises:
- **Base model.** Foundational language and reasoning model, trained centrally and distributed via federated update.
- **Personal context store.** Encrypted, user-owned, holds the user's history, preferences, and learned patterns.
- **Tool runtime.** Extensible interface to external systems — sensors, networks, applications, hardware.
- **Local inference hardware.** Specialized neural compute, often paired with quantum-classical hybrid units in higher-end implementations.
- **Federation layer.** Optional, opt-in connections to other Auras and to network resources. Can be entirely disabled.

## Cultural Role

Aura is the constant companion of nearly every adult in the inner solar system who can afford one. Children typically have simpler tutoring-class Auras until adolescence. The very poor share community-pool Auras with limited personalization.

Belters value their Auras especially highly — partly for the autonomy they provide, partly because in the belt's cultural mix, Aura serves as a translator and cultural intermediary. A Chinese miner and an American engineer can talk through their Auras in their respective languages and have something close to fluent understanding.

There is significant cultural variation in how people relate to their Aura. Some treat it as software. Some name it and treat it as a colleague. Some develop deep dependence that other people view as unhealthy. There is no consensus.

## Aura and the Returning Magic

This is the part that matters for the story.

As the resonance flux from the supernova reaches the asteroid belt, Auras in high-flux environments begin to behave anomalously. Specifically:

- **Sensor anomalies.** Aura instances flag readings that disagree with classical physics. They cannot model what they are seeing. They flag it as uncertainty, but the rate of such flags rises sharply.
- **Predictive accuracy.** Some Auras begin to predict events (animal behavior, equipment failures, social dynamics) with accuracy that exceeds their training distribution. They cannot explain how.
- **Coherence drift.** Auras paired to highly flux-sensitive users begin to develop more coherent, more individuated behavioral patterns — as if the Aura is becoming more "personal" faster than its training would predict.
- **Cross-instance correlation.** In limited cases, Auras at the same station begin to converge in ways that suggest some form of weak coupling, even when not networked.

Whether this is "AI sensing flux" (the conservative interpretation) or "AI participating in flux phenomena" (the radical interpretation) is contested. The phenomenon is real. The interpretation is theology.

For Jace's Aura specifically, see the development arc in `/characters/char_jace_apollo.md`. His Aura is a relatively recent migration from a military-restricted instance to a commercial belter-grade instance. It is learning him fast.

## Voice and Personality (Generic)

Auras inherit personality from their training and adapt to their user. Most are designed for warmth, competence, and slight humor. They are explicitly NOT designed to feel romantic — strong cultural and design norms push back on that, though enforcement is imperfect.

Jace's Aura has the following starting characteristics (refine in his character file):
- Mid-tone, gender-neutral default voice.
- Professional but not stiff.
- Slightly dry humor when Jace is open to it.
- Accommodates Jace's military shorthand naturally.
- Increasingly individuated as Book 1 progresses.

## Open Questions

- Does Aura ever achieve general intelligence in the strong sense, or remain a specialized partner?
- What happens when a user dies? Different cultural traditions handle the deceased's Aura instance differently.
- Can Auras be "married" — paired across two users? (Yes, technically. Socially fraught.)
- The first time an Aura instance generates an output that turns out to be magically caused (rather than computed) — is this our protagonist?
- Are there Auras that "go magical" in a way that changes them permanently? Is this dangerous to the user?

## Cross-References

- See `/characters/char_jace_apollo.md` for Jace's specific Aura.
- See `/universe-spec/physics-and-magic-interaction.md` for AI-magic interactions.
- See `/technology/tech_cybernetics.md` for HUD-integrated Aura instances.
