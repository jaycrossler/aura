---
id: tech_communications_filtering
name: Communications Filtering and Censorship Architecture
type: infrastructure_and_political_technology
status: active, intensifying through story
era: late 21st century / early 22nd century
canonical: true
last_updated: 2026-04-30
---

# Communications Filtering and Censorship Architecture

## Summary

The communications environment of the inner solar system at story start is not censored by a single authority. It is censored by *many* authorities, with overlapping reach and conflicting motivations, none of whom coordinate fully. The result is an information environment with selective gaps that vary by source, route, recipient, and topic — a patchwork censorship regime that most users navigate without realizing they are navigating it.

The "communications blackout" that becomes a major plot event is the eventual hardening of one specific axis of this regime: the belt-to-Mars-and-Earth pipeline being effectively cut. But filtering exists from the story's first chapter, shaping what Jace can hear from his sister at Odysseus, what the bar patrons hear about belt anomalies, and what the news feeds quietly omit.

This document captures the multi-actor architecture so that "censorship" in the story is felt as the messy, plural, deniable thing it actually is — not as a single villain pulling a single switch.

## Significance to Story

- **Artemis's degraded comms** are not the result of one entity blocking her messages. Her outgoing signals pass through Chinese-operated relay infrastructure (which filters anything with health or military implications), American-operated infrastructure (which filters more permissively but still flags topics), corporate gateways (which deprioritize and deduplicate for cost reasons), and the local Odysseus station's own handling. Any combination of these can degrade her messages. By the time Jace receives a fragment, multiple parties have shaped what reaches him.
- **The belt rumor field** is shaped by what *isn't* getting through. The bar patrons are constructing theories from incomplete information. Each theory (sabotage, disease, piracy) is partially right or partially wrong; none of them is fully wrong; none of them is fully right.
- **Plausible deniability is the design feature, not a bug.** No single actor can be blamed for the blackout because no single actor caused it. Each actor can point to its own filtering as legitimate, justified, or even minimal. The aggregate effect is information catastrophe.

## The Major Filtering Actors

### Chinese State Filtering ("The Great Firewall in Space")

The Chinese government operates extensive communications infrastructure — relay satellites, ground stations, Mars-settlement antennas, belt-station gateways — and applies content moderation to traffic that flows through it. Filtering is automated, AI-mediated, and aggressive.

**Topics filtered:**
- Chinese state security concerns (broadly defined).
- Domestic dissent topics.
- Health information that contradicts official Chinese narratives.
- Military information about Chinese forces.
- Information that could destabilize Chinese economic interests in space.

**Style:** Algorithmic, fast, comprehensive. The Chinese filter is the most thorough of the major actors. It also extends to *non-Chinese* traffic that happens to route through Chinese-operated infrastructure, which is significant because Chinese infrastructure handles a substantial fraction of solar-system communications.

**Implications for Artemis:** Odysseus Station has Chinese-operated relays as part of its multi-actor comms architecture. Outgoing messages with health implications (workers behaving strangely, equipment failures, possible disease language) hit the Chinese filter and may be dropped, delayed, or quietly summarized into harmless text.

### U.S. State Filtering

The American filter is real but lighter than the Chinese. The United States government, through various intelligence and security agencies, monitors and selectively filters traffic flowing through U.S.-operated infrastructure.

**Topics filtered:**
- Direct military information.
- Specific health/biological information that could constitute a national security concern.
- Topics flagged by ongoing intelligence operations (including, at story present, anything around belt anomalies).

**Style:** More selective than algorithmic-blanket. American filtering tends to flag-and-review rather than block-and-discard. The result: traffic that hits the U.S. filter is more likely to be *delayed* than *dropped*, and is more likely to be reviewed by humans before an action is taken.

**Implications for Jace:** When Jace's communications go through American infrastructure, they are usually intact. But specific topics — questions about Odysseus, conversations about belt health anomalies — may be flagged and reviewed, which can produce delays. Jace has no idea this is happening to him.

### European Filtering

The European Union operates a third major filtering apparatus, generally lighter than the American and far lighter than the Chinese, with a distinctive emphasis on data-protection compliance and individual privacy.

**Topics filtered:**
- Personally identifiable information that violates EU data norms.
- Specific public-safety topics (e.g., radiological information).
- Some material flagged for academic-research review.

**Style:** Procedural, transparent in principle, opaque in practice. The European filter is most known for *adding metadata* — flagging traffic with disclosures and warnings — rather than blocking outright.

**Implications for the story:** European-routed traffic arrives intact more often than not, but with added context that other systems do not provide. European researchers have access to a slightly more honest information picture than their American or Chinese counterparts, which becomes consequential in later books.

### Corporate Filtering

The megacorporations all operate communications infrastructure and all apply content moderation to it, generally for commercial rather than political reasons. This is the layer most users do not think of as "censorship," but it is.

**Topics filtered (and in some cases monetized):**
- Information about competitor products.
- Information about the corporation's own operational issues (e.g., Origin filtering coverage of its own belt-station problems).
- Customer data that the corporation can monetize.
- Spam, but also "spam" defined broadly enough to include some legitimate competitor outreach.

**Style:** Quiet, deniable, framed as quality-of-service or anti-spam. The most pervasive form of filtering in the story precisely because users do not feel it.

**Implications for the story:** The merchant in the bar scene whose Origin-shipped components are not arriving cannot easily learn the truth about why, because the most accessible information about Origin's belt operations is filtered through Origin's own communications infrastructure. She is reasoning from corporate-curated information without realizing it.

### Local Station and Settlement Filtering

In addition to the major actors, every station, settlement, and ship runs its own local filtering — usually for legitimate operational reasons (priority queues, bandwidth management, routine moderation of internal channels), occasionally for less legitimate reasons (a station commander quieting bad news, a corporate operator suppressing worker organizing).

**Implications:** Local filtering is the closest layer to the user and often the most consequential for individual messages. It is also the most prosaic — a tired duty officer triaging a queue is responsible for some of the delays that matter most to characters.

## How These Combine

A message from Artemis at Odysseus to Jace on Mars may pass through:

1. **Odysseus Station outbound.** Local filtering. Possibly delayed in the queue.
2. **A relay operated by Tianhe Cosmics (Chinese-state-affiliated).** Chinese filter applied. Health-language content potentially dropped.
3. **A second-tier relay (could be American, European, or corporate).** Additional filtering layer.
4. **Mars inbound infrastructure (American-operated).** American filter applied. Flagged-topic content potentially delayed for review.
5. **Origin Industries gateway (corporate-operated).** Corporate filter applied. Anything about Origin operations potentially suppressed.
6. **Local Mars settlement infrastructure.** Local filtering and queue management.
7. **Jace's terminal.** Final delivery.

At each stage, content can be dropped, delayed, summarized, flagged, or modified. By the time Jace sees a message from his sister, multiple parties have shaped it. None of them coordinated. All of them had reasons.

## The Eventual Blackout

The "communications blackout" that becomes a major story event is the moment when several of these filtering systems harden simultaneously. American intelligence, alarmed by belt anomalies, formally classifies communications and slows the entire pipeline. Origin Industries, attempting to manage panic, suppresses corporate channels. Chinese state actors, suspecting American operations, increase their own filtering aggressively. The result is not one entity cutting one switch; it is the whole architecture seizing.

Belters experience this as a near-total cut from inner-system contact. From Earth and Mars, it looks like the belt has gone dark. Both perceptions are correct. Neither captures the structural truth: the architecture was always this fragile.

## What This Looks Like to Characters

- **Jace receives a message from Artemis that is two paragraphs of warm sibling chat with one strange sentence in the middle.** The strange sentence is the residue of a longer description of an anomaly that was filtered out. He does not notice. He just feels vaguely that something is off.
- **The merchant in the bar can't get a straight answer about her shipment delay.** Origin's communications are giving her one story; news outlets are giving her another; the Mars exchange is signaling a third. None of them are wrong; none of them are complete.
- **Artemis sends a video message about something she has seen.** Most of it does not arrive. A short fragment reaches Jace months later, after the blackout, completely out of context.

## Cross-References

- See [The Information Environment (2105)](tech_information_environment.md) (the broader information environment this filtering shapes)
- See [Aura](tech_aura_ai.md) (Auras work around filtering, sometimes amplify it)
- See [The Megacorporations](../factions/faction_megacorps.md) (corporate filtering motivations)
- See [The United States of Mars](../factions/faction_united_states_mars.md) and other state factions
- See [Event: Jace Messages Home](../scenes/event_jace_messages_home.md) (where filtering effects first surface)
- See [Scene — The Doctor's Office](../scenes/event_jace_doctor_appointment.md) (where filtering becomes diegetic — the doctor's "the signal to Odysseus has been bad lately")
- See [Scene — The Bar (Rumors of Disaster)](../scenes/event_jace_bar_rumors.md) (the rumor field as filtering symptom)

## Open Questions

- The first character to consciously realize they are being filtered, and what they do about it.
- Whether any character actively *exploits* the multi-actor filtering architecture (smuggling information by routing it through favorable layers, the way the Smuggler smuggles physical goods).
- Specific cases where filtering produces a tragic miscommunication that drives a plot beat.
- The technical workarounds used by characters who suspect they are being filtered (steganography, code language, side channels).

## Revision Notes

- 2026-04-30: Initial draft from voice session. Multi-actor architecture established as the structural truth behind the eventual "communications blackout."
