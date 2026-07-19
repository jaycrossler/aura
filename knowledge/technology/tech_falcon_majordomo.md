---
id: tech_falcon_majordomo
name: "Falcon Majordomo — Ship Automation System"
type: technology
status: staged_draft
canonical: false
last_updated: 2026-07-19
description: >
  The Falcon's non-AI automation and annunciator system. Handles alarms, status
  announcements, environmental scheduling, and access control. Explicitly not an
  AI — no curly braces in prose. Exists because Maureen refuses to run a ship AI.
cross_references:
  - "[[ship_falcon]]"
  - "[[char_maureen]]"
  - "[[tech_fortuna_ai_personalities]]"
---

# The Falcon Majordomo

## What It Is

A dumb-adjacent automation stack: rule-based scheduling, threshold alarms,
canned announcements, door and access-rights management. No model, no
personality, no learning, no conversation. It executes its tables and reads its
lines.

**Typographic rule:** The majordomo is *not* an AI and therefore never takes
curly braces. In prose it is "the majordomo" — lowercase, unadorned. The absence
of braces is itself information: on this ship, the thing that talks to you is
just a speaker.

## Why It Exists

Maureen refuses to run a ship AI. She tolerates contractors' personal AIs when
contracts require them — {Seek} loaded for Chinese runs, {Gem} for AlphaCorp
runs, {Alex} riding along in Origin crews' HUDs — and she resents every one of
them. Her ship answers to tables she wrote herself. The majordomo is that
refusal, made of relays.

## The Voice

No personality was installed. Nonetheless, the majordomo delivers every line —
docking clearances, oxygen advisories, emergency alarms — with the flat cadence
of something that has been interrupted mid-task for the ten-thousandth time.
Crew and passengers universally describe it as *exhausted* and *annoyed*.
Maureen insists this is latency and worn speaker drivers. Nobody believes her.
Nobody can prove her wrong.

Running gag guidance: the humor comes from deadpan delivery against urgent
content ("ANOMALOUS MASS DISTRIBUTION," delivered like a sigh), and from the
crew's insistence on anthropomorphizing a thing that is demonstrably a lookup
table. Do not let it become secretly sentient. It is a speaker.

## Capabilities and Limits

- Alarms and annunciations (environmental, structural, docking, livestock)
- Scheduling: lighting cycles, feed timers, filtration, thermal management
- Access rights: door permissions and system-role grants from a static rights
  table (see the ch05 "engineering administrator" beat — the table's role
  bundling is naive, which is how Jace's fabrication rights silently confer
  ship-wide engineering admin)
- Cannot converse, infer, or improvise; unrecognized situations produce the
  nearest canned message, sometimes absurdly mismatched

## Revision Notes

- 2026-07-19: Created from author session. Replaces the unregistered "{Falcon}"
  AI references in draft_ch04 (edit staged). No-braces ruling confirmed by
  author.
