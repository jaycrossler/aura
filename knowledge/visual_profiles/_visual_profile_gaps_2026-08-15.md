---
id: visual_profile_gaps_2026_08_15
name: "Visual Profile Gap Audit — Ch00-20 Speaking Cast"
type: audit
status: open
last_updated: 2026-08-15
description: >
  Audit of which Ch00-20 speaking characters have visual profiles, which have
  enough canonical physical description to build one, and which cannot be
  profiled without author input. Produced alongside the voice-profile batch of
  the same date.
cross_references:
  - "[[VISUAL_PROFILE_SYSTEM_INSTRUCTIONS]]"
  - "[[visual_profile_suzi]]"
  - "[[review_2026-08-15_cast_and_voice_audit]]"
---

# Visual Profile Gap Audit — Ch00-20 Speaking Cast

## Existing visual profiles

| Subject | File | Completeness |
|---|---|---|
| Jace Apollo Grant | visual_profile_jace_apollo | 60 |
| Sophia Lotte | visual_profile_sophia_lotte | (rated in file) |
| Jin Lóng | visual_profile_jin_long | 88 |
| Nick Lee | visual_profile_nick_lee | (rated in file) |
| Kael | visual_profile_kael | 55 |
| Cerberus and Siren | visual_profile_cerberus_and_siren | (rated in file) |
| The Falcon | visual_profile_ship_falcon | (rated in file) |
| Fortuna Station | visual_profile_fortuna_station | (rated in file) |
| Suzi Gonzales | visual_profile_suzi | 55 — **new, this batch** |

Note that `VISUAL_PROFILE_SYSTEM_INSTRUCTIONS.md`'s status table is stale. It
still lists `visual_profiles_sophia_jin_nick_cerberus.md` and
`visual_profiles_locations.md` as combined files, but those have since been split
into the individual files above. The table should be regenerated.

## Buildable now, from existing canon

These characters have enough physical description in their `char_` files to
support a visual profile without inviting new canon. Each is a straightforward
extraction pass.

| Subject | Source detail available |
|---|---|
| Maureen | char_maureen.md |
| Lanchee | char_lanchee.md, plus the Filipino-inflected clinical characterization |
| Helena | char_helena.md, plus the prologue |
| Mei | char_mei.md |
| Petroski | char_petroski.md — the only Russian on the station, retired orbital-structures PhD |
| Hayes | char_hayes.md — including the permanently left-handed detail, which has visual consequences |
| Mira | char_mira.md is 226 lines and canonical; likely has usable detail |
| Eugene Hart | char_eugene.md is 236 lines |

## Not buildable without author input

| Subject | What is missing |
|---|---|
| Kim | Everything physical. Also surname, and whether Kim is given name or surname |
| Torres | Everything physical. Also first name |
| Carlos | Voice profile exists and describes him as older with a low register; physical detail not retrieved |
| Brandon Moreau | Nothing physical established |
| Nikos Petrou | Nothing physical established |
| Mateo Alvarez | Nothing established; file created 2026-08-14 as a stub |
| Saul | Nothing established |
| Erin | Nothing established |

## AI subjects

The AI characters do not need conventional portraits, but several have
canonically described **Astral appearances**, which are genuinely visual and
currently undocumented outside their tech files:

- **{Misty}:** the brightest object aboard the *Victoria*, substantially brighter
  than its reactors. Myriad tiny brownish or murky gold bubbles forming precise
  geometric chains before collapsing. Faint echoes of practiced pathways during
  tasks, slighter and faster than biological thought.
- The other station AIs presumably have comparable signatures. Only {Misty}'s is
  documented.

Recommend a single `visual_profile_ai_astral_signatures.md` covering all nine
AIs, rather than one file each, since the interesting content is comparative.
This would pair with `spec_astral_glow_and_signatures.md`.

## Revision Notes

- 2026-08-15: Initial audit.
