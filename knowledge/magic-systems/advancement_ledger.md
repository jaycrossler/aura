---
id: advancement_ledger
name: Character Advancement Ledger
type: kb_system
status: canonical
canonical: true
last_updated: 2026-06-27
description: >
  Machine-legible record of all confirmed skill advancement events across the series.
  One entry per advancement event: character, skill, level transition, trigger, arc,
  and scene reference. Used for continuity checking — if a scene draft shows a
  character using a capability not yet listed here, flag before publishing.
  Supersedes any conflicting level claim in other files (sheets are snapshots;
  this ledger is the authoritative timeline).
cross_references:
  - "[[magic_skills_framework]]"
  - "[[magic_skill_level_scale]]"
  - "[[magic_self_template_skill]]"
  - "[[magic_astral_transfer_skill]]"
  - "[[sheet_jace_arc01_end]]"
  - "[[sheet_sophia_arc01_end]]"
  - "[[sheet_jin_arc01_end]]"
  - "[[sheet_nick_arc01_end]]"
---

# Character Advancement Ledger

## How to Use This File

Each advancement event has:
- `character`: subject ID matching char_ file slug
- `skill`: bracketed skill name (KB notation)
- `from_level`: level before this event (null = not yet possessed)
- `to_level`: level after this event (decimals allowed for sub-level tracking)
- `trigger`: what caused the advancement (orb, practice, teaching, crisis, passive)
- `arc`: arc slug where this occurred
- `scene`: scene reference (thread-based ID if assigned, else descriptive)
- `confirmed`: true = locked canon / false = projected / retcon = supersedes prior entry
- `notes`: optional continuity note

**Continuity check rule:** Before a scene draft shows a character performing a
capability, verify their current level in this ledger. If the required capability
exceeds their confirmed level — flag to review queue, do not silently upgrade.

**L4 ceiling rule:** No Sol human practitioner reaches L4 in any skill within
the first five arcs. L4 represents decade-scale dedication or exceptional innate
affinity (see magic_skill_level_scale.md). Any scene draft showing Sol human L4
capability should be flagged before publication regardless of in-story justification.
This rule supersedes individual orb advancement calculations.

**Retcon rule:** When a retcon is applied, add a new entry with `confirmed: retcon`
and reference the superseded entry in notes. Do not delete old entries.

---

## Ledger

```yaml
advancement_events:

  # ─────────────────────────────────────────────
  # JACE APOLLO GRANT
  # ─────────────────────────────────────────────

  - id: jace_mindwall_passive
    character: jace_apollo
    skill: "[Mind Wall]"
    from_level: null
    to_level: 1
    trigger: passive (Sol human baseline — 3000 years unconscious investment)
    arc: pre_story
    scene: n/a — present at story start
    confirmed: true
    notes: >
      Passive structural property of Sol human Template. Not learned; not
      consciously accessible. Appears as architectural solidity in Kael's
      Template Reading.

  - id: jace_hud_object_template
    character: jace_apollo
    skill: "[Object Template]"
    from_level: null
    to_level: 1
    trigger: orb (Dipper-class, Falcon plumbing crisis — accidental absorption)
    arc: arc_01
    scene: T-04 (plumbing crisis)
    confirmed: true
    notes: >
      Accidental. HUD implant (gold/platinum) caused Template stress; absorbed
      Will directed there by Template necessity. Result: unstable L1 Object
      Template on HUD. Not recognized by Jace as a skill event. Kael reads this
      later and finds it unusual.

  - id: jace_astral_transfer_l2
    character: jace_apollo
    skill: "[Astral Transfer]"
    from_level: null
    to_level: 2
    trigger: orb (Dipper-class, Falcon plumbing crisis) + months unconscious practice
    arc: arc_01
    scene: T-04 (plumbing crisis)
    confirmed: true
    notes: >
      Acquired at L2 rather than L1 because Jace had been unconsciously practicing
      (pushing Cerberus partway across in sleep crossings, pulling equipment through)
      for months prior. The Dipper orb crystallized accumulated practice into a named
      skill. Starting at L2 is remarkable; Kael discovers this in Arc 2 testing.

  - id: jace_astral_transfer_l3
    character: jace_apollo
    skill: "[Astral Transfer]"
    from_level: 2
    to_level: 3
    trigger: orb (Scavenging Queen, swarm fight) + months intensive practice since L2
    arc: arc_01
    scene: S-01 (swarm fight, Queen death)
    confirmed: true
    notes: >
      Queen orb absorbed after Sophia kills it. Combined with months of deliberate
      Transfer practice since the plumbing crisis. L3 is expert level; most
      practitioners never reach it. Jace is the first known Sol human at L3 in
      any skill. This is the data point that causes Kael's recalibration in Arc 2.
      He has no combat or protection skills at L3; Kael initially considers Transfer
      a "parlor trick" specialization.

  - id: jace_bloated_maw_orb_capacity
    character: jace_apollo
    skill: "[Astral Transfer]"
    from_level: 2.8
    to_level: 2.8
    trigger: orb (Bloated Tick-Maw — capacity restoration, NOT advancement)
    arc: arc_01
    scene: N-04 (Bloated Maw hunt in {Seek} server area)
    confirmed: true
    notes: >
      NOT a skill advancement event. The Bloated Maw orb is large but its affinity
      (colonial Will / AI-feeding) does not cleanly map to [Astral Transfer]'s
      force-geometry requirements. The Will influx instead restores Template
      capacity — partially clearing the crossing debt accumulation, reducing
      "stupid morning" frequency, allowing slightly heavier transfers without
      the same exhaustion cost.

      Subjective effect: Jace feels recovered for the first time in weeks. This
      is dangerous — the restored energy allows him to continue at an unsustainable
      pace rather than forcing a necessary stop. The crossing debt does not
      disappear; it becomes bearable again.

      Kael reads this Will event during her Arc 2 Template assessment. She
      identifies it as a large orb absorption from an unusual creature she does
      not immediately recognize. When she asks Jace to describe it, his explanation
      reveals: (a) the Bloated Maw existed and was feeding on {Seek} for months,
      (b) he hunted it alone, (c) Sophia did not know.
      Sophia is present during this assessment. This is the first real fracture
      in the Jace-Sophia partnership.

      Progression level unchanged at ~L2.8 pre-event. Queen orb during swarm fight
      pushes to confirmed L3 (see jace_queen_transfer_l3).

      L4 NOTE: No Sol human reaches L4 in any skill for at least 5 arcs. L4 requires
      decade-scale dedicated practice. This ceiling applies universally across
      all Arc 1–5 Sol human practitioners.

  # ─────────────────────────────────────────────
  # SOPHIA LOTTE
  # ─────────────────────────────────────────────

  - id: sophia_mindwall_passive
    character: sophia_lotte
    skill: "[Mind Wall]"
    from_level: null
    to_level: 1
    trigger: passive (Sol human baseline)
    arc: pre_story
    scene: n/a
    confirmed: true
    notes: Kael assesses as "strong and well-developed even by her own tradition's standards."

  - id: sophia_force_application_l1
    character: sophia_lotte
    skill: "[Force Application]"
    from_level: null
    to_level: 1
    trigger: practice (solo month at Fortuna, experimental)
    arc: arc_01
    scene: pre-Jace-arrival solo period
    confirmed: true
    notes: >
      Developed through solo experimentation applying physics intuition to Will direction.
      L1 at first Tick-Maw encounter.

  - id: sophia_force_application_l2
    character: sophia_lotte
    skill: "[Force Application]"
    from_level: 1
    to_level: 2
    trigger: orb (Tick-Maw nest creature) + continued practice
    arc: arc_01
    scene: X-02b (Tick-Maw sweep) and subsequent practice
    confirmed: retcon
    notes: >
      RETCON 2026-06-27: Previously logged as L3 at Arc 1 end (Queen orb solidifying
      borderline L2→L3). Revised per series balance decision: all non-Jace practitioners
      end Arc 1 at L2 maximum. Sophia ends Arc 1 at solid L2 [Force Application].
      The Queen orb (from S-01) still occurs but advances her to confident L2, not L3.
      Arc 2 is where Sophia reaches L3 through continued training and a second orb event.
      Supersedes the L3 entry in sheet_sophia_arc01_end.md — that sheet requires a
      patch to correct to L2.

  - id: sophia_astral_transfer_l1
    character: sophia_lotte
    skill: "[Astral Transfer]"
    from_level: null
    to_level: 1
    trigger: practice (self-developed through necessity)
    arc: arc_01
    scene: solo period
    confirmed: true
    notes: Functional for personal kit only. Gap with Jace's L3 visible to Kael on assessment.

  - id: sophia_far_sight_l1
    character: sophia_lotte
    skill: "[Far Sight]"
    from_level: null
    to_level: 1
    trigger: practice (systematic documentation work)
    arc: arc_01
    scene: solo period
    confirmed: true
    notes: Seventeen notebooks of observational data are the practice log.

  - id: sophia_far_sight_l2
    character: sophia_lotte
    skill: "[Far Sight]"
    from_level: 1
    to_level: 2
    trigger: practice (continued documentation; Jace collaboration)
    arc: arc_01
    scene: mid-arc practice period
    confirmed: true
    notes: >
      Arc 1 end level. Sophia's observational orientation means this skill
      develops alongside Force Application rather than after it.

  - id: sophia_dimensional_sight_l1
    character: sophia_lotte
    skill: "[Dimensional Sight]"
    from_level: null
    to_level: 1
    trigger: practice (developed as safer alternative to full crossing)
    arc: arc_01
    scene: solo period
    confirmed: true
    notes: Brief duration; lower cost than crossing; useful for detection.

  # ─────────────────────────────────────────────
  # JIN LÓNG
  # ─────────────────────────────────────────────

  - id: jin_mindwall_passive
    character: jin_luong
    skill: "[Mind Wall]"
    from_level: null
    to_level: 1
    trigger: passive (Sol human baseline; possibly reinforced by {Seek} suppression pressure)
    arc: pre_story
    scene: n/a
    confirmed: true
    notes: >
      {Seek}'s sustained suppression attempts over months may have incidentally
      strengthened Jin's passive Mental Fortification. Kael will note this as
      anomalously thick for a practitioner who never trained it.

  - id: jin_fire_shaping_l1
    character: jin_luong
    skill: "[Fire Shaping]"
    from_level: null
    to_level: 1
    trigger: crisis (nest-clearing under {Seek} suppression — manifested under extreme duress)
    arc: arc_01
    scene: P-04 (Jin's quiet war — early)
    confirmed: true
    notes: >
      Manifested without knowledge of magic existing. Jin had no framework for
      what was happening. He used it because it worked. He told no one.

  - id: jin_fire_shaping_l2
    character: jin_luong
    skill: "[Fire Shaping]"
    from_level: 1
    to_level: 2
    trigger: practice (3 months of nest-clearing operations)
    arc: arc_01
    scene: P-04 period (accumulated)
    confirmed: true
    notes: >
      Reached through intensive field use under life-or-death conditions, with no
      training, no knowledge of the skill system, and active suppression from {Seek}.
      L2 is functional and reliable but not yet expert. No orb absorption
      contributed — all practice-based.

  - id: jin_thermal_shell_l1
    character: jin_luong
    skill: "[Thermal Shell]"
    from_level: null
    to_level: 1
    trigger: passive (self-protection reflex during sustained fire use)
    arc: arc_01
    scene: P-04 period (accumulated)
    confirmed: true
    notes: >
      Jin developed passive thermal protection as a byproduct of [Fire Shaping]
      practice — the fire-aligned Will bled into self-protection. Not consciously
      deployed; Kael will identify it as a passive L1 on Template Reading in Arc 2.

  # ─────────────────────────────────────────────
  # NICK LEE
  # ─────────────────────────────────────────────

  - id: nick_mindwall_passive
    character: nick_lee
    skill: "[Mind Wall]"
    from_level: null
    to_level: 1
    trigger: passive (Sol human baseline)
    arc: pre_story
    scene: n/a
    confirmed: true
    notes: >
      His calm under pressure during the swarm fight suggests his passive
      Mental Fortification is strong. Assessment pending Kael's Template Reading.

  - id: nick_information_flow_nascent
    character: nick_lee
    skill: "[Information Flow]"
    from_level: null
    to_level: 0.5
    trigger: practice (emerging through {Aura} Will-detection work; briefly demonstrated
              in swarm fight Astral relay)
    arc: arc_01
    scene: S-01 (swarm fight — Nick's 90-second crossing)
    confirmed: true
    notes: >
      Nascent and unrecognized. L0.5 notation indicates skill is present but not
      yet named, documented, or consciously accessible. Nick attributes the relay
      accuracy to better signal processing. Kael will attribute it to something else.
      Full L1 achieved when Nick names and tests the skill in Arc 2.

  # ─────────────────────────────────────────────
  # KAEL (reference — not advancing during Arc 1)
  # ─────────────────────────────────────────────

  - id: kael_skills_at_arc2_arrival
    character: kael
    skill: "[multiple — see notes]"
    from_level: n/a
    to_level: n/a
    trigger: reference snapshot only — not an advancement event
    arc: arc_01
    scene: S-03 (Kael arrives)
    confirmed: true
    notes: >
      Kael arrives at Fortuna with established skills. Reference levels per
      magic_skill_level_scale.md: [Long Step] L4, [Occlusion] L3, [Force Shell] L4,
      [Self Template] L3, [Far Sight] L3, [Psychic Anchor] L3, [Mind Wall] L3
      (active/directional), [Template Reading] L2, [Frame Walking] L2,
      [Force Application] L2, [Object Template] L2, [Astral Transfer] L2.
      She has not advanced any skill during the arc; she arrived at these levels
      through 300 years of Woven service.

  # ─────────────────────────────────────────────
  # PROJECTED — Arc 2 (unconfirmed; draft guidance only)
  # ─────────────────────────────────────────────

  - id: proj_jace_self_template_l1
    character: jace_apollo
    skill: "[Self Template]"
    from_level: null
    to_level: 1
    trigger: teaching (Kael; mandatory first instruction)
    arc: arc_02
    scene: TBD — Arc 2 teaching sequence
    confirmed: false
    notes: >
      Kael's first teaching priority. Jace resists (finds it boring); eventually
      clicks during or after a crisis. L1 is the minimum viable practitioner
      baseline. See magic_self_template_skill.md for teaching sequence.

  - id: proj_jin_thermal_shell_l2
    character: jin_luong
    skill: "[Thermal Shell]"
    from_level: 1
    to_level: 2
    trigger: teaching (Kael) + practice
    arc: arc_02
    scene: TBD
    confirmed: false
    notes: >
      Kael prioritizes this because Jin is returning to dangerous environments.
      Thermal Shell L2 is consciously deployable and meaningfully extends
      survivable operating range in cold Astral conditions.

  - id: proj_nick_information_flow_l1
    character: nick_lee
    skill: "[Information Flow]"
    from_level: 0.5
    to_level: 1
    trigger: testing (self-directed; named to {Aura} before named to anyone else)
    arc: arc_02
    scene: TBD — Nick's naming moment
    confirmed: false
    notes: >
      The advancement is the naming. Nick runs reproducible tests, confirms the
      relay accuracy is not signal processing, logs it with {Aura}. Does not
      immediately disclose to Jace. Very Nick.

  - id: proj_sophia_template_reading_l1
    character: sophia_lotte
    skill: "[Template Reading]"
    from_level: null
    to_level: 1
    trigger: practice (self-directed, documentation instinct) + possible Kael teaching
    arc: arc_02_arc_03
    scene: TBD
    confirmed: false
    notes: >
      Creates tension with Kael (who has strong feelings about who should have
      Template Reading capability). Sophia develops it because she needs to
      understand what she's observing. The conflict between her need to know and
      Kael's instinct to restrict is a relationship beat.

  - id: proj_sophia_force_application_l3
    character: sophia_lotte
    skill: "[Force Application]"
    from_level: 2
    to_level: 3
    trigger: orb (Arc 2 event TBD) + continued training
    arc: arc_02
    scene: TBD
    confirmed: false
    notes: >
      Arc 2 advancement. With Kael's training and a second significant orb event,
      Sophia reaches the expert ceiling in her primary skill. This is what makes
      her genuinely dangerous to Kael-class opponents by Arc 3.
```

---

## Continuity Flags

The following items require attention before prose drafts are written:

| Flag | Description | Priority |
|---|---|---|
| `RETCON` | sheet_sophia_arc01_end.md states [Force Application] L3 — must be patched to L2 | HIGH |
| `OPEN` | Queen orb absorption by Sophia: revised to advance her to L2 (not L3); confirm this is consistent with the swarm fight scene contract in arc_01 | HIGH |
| `OPEN` | Jin's three named crew members with abilities: if they manifested under {Seek} suppression, they may have nascent L1 skills not yet logged | MEDIUM |
| `OPEN` | Jace's [Object Template] on HUD: currently L1 unstable; does Arc 2 Kael teaching help him stabilize it? Not yet in ledger | MEDIUM |
| `OPEN` | Cerberus familiar bond: not yet logged as a skill entry; Kael will read it in Arc 2; needs a ledger entry once formalized | LOW |

---

## Revision Notes
- 2026-06-27: New file. All Arc 1 confirmed events logged. Sophia Force Application
  retcon applied (L3→L2 at Arc 1 end). Arc 2 projections drafted. Continuity flag
  table populated.
