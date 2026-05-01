---
id: scenes_temporal_map
name: Master Scenes Temporal Map
type: chronology_index
status: working draft (Book 1, early chapters)
last_updated: 2026-04-30
canonical: true
storybot_extrapolation_allowed: true (for unfilled fields)
---

# Master Scenes Temporal Map

This file maps every scene to its position in time, showing absolute dates, time-of-day, durations, gaps between scenes, and character state carry-over. Used by the StoryBot to maintain continuity across the book and extrapolate where data is missing.

**Conventions:**
- All dates use Mars local calendar where applicable; UTC equivalents noted where useful
- **[STORYBOT]** in any field = invitation to extrapolate consistently with established canon
- "TBD" = explicitly unspecified, needs author input
- Times are 24-hour format

---

## Book 1 — Early Chapters

### Scene 01: Jace's Pinta Voyage (Implied, Off-Page)
- **Status:** Reference only — not depicted as a scene
- **Date:** Late 2104 to ~early 2105
- **Duration:** ~4 months in transit
- **Function:** Background context — informs Jace's exhausted state at arrival
- **Gap to next scene:** None (continues directly into arrival)

---

### Scene 02: `event_jace_mars_arrival` (= `event_jace_mars_tour_with_rich`)
- **Date:** Day 1, ~early 2105 [STORYBOT: Anchor as 2105-03-15 unless author specifies]
- **Time start:** 02:00 (Pinta lands)
- **Time end:** ~14:00 (Jace asleep)
- **Duration of scene action:** ~12 hours
- **Estimated text length:** 4,000-6,000 words
- **Spatial range:** Pinta → terminal → observation dome → connected domes → rover → military base → quarters
- **POV:** Jace (tight)
- **Major beats:** Disembark, processing, scanner foreshadowing, meet Rich, walking tour, rover transit, base introduction, lunch, sleep

**Character state at scene start:**
- Jace: Exhausted, anxious-excited, golden-boy confident
- Rich: Fresh, peppy, eager to meet new colleague

**Character state at scene end:**
- Jace: Crashed asleep, knowledge of Mars geography gained, scanner unease forgotten
- Rich: Back to his quarters, fond of Jace, mildly concerned about his naivete

**Time gap to next scene:** ~18-20 hours (Jace sleeps overnight)

**Continuity flags:**
- Scanner foreshadowing — establish but do not resolve
- Sylvester/Mei not yet introduced
- Intel storyline not yet active

---

### Scene 03: `event_jace_gym_arrival`
- **Date:** Day 2, ~early 2105 [STORYBOT: Anchor as 2105-03-16]
- **Time start:** 08:00 (Jace wakes)
- **Time end:** 12:00 (medical appointment begins)
- **Duration of scene action:** ~4 hours
- **Estimated text length:** 2,500-4,000 words
- **Spatial range:** Apartment → corridors → breakfast vendor → gym → apartment → rover → military base
- **POV:** Jace (tight)
- **Major beats:** Wake up, navigation fumbling, breakfast sticker shock, gym workout, HUD game obliviousness, family video messages (failed Artemis send), grooming, base arrival, Sylvester/Mei glimpse

**Character state at scene start:**
- Jace: Rested, fresh, eager
- Rich: At work at base, expecting to formally welcome Jace

**Character state at scene end:**
- Jace: Sharp, well-groomed, anticipatory; aware that Artemis comms are failing; has glimpsed Sylvester and Mei
- Rich: Greeted Jace, expecting normal welcome day

**Time gap to next scene:** ~0 minutes (transitions directly into doctor's appointment)

**Continuity flags:**
- Failed Artemis message — first concrete sign of comms problem
- Sylvester/Mei glimpse — setup for later recruitment
- Jace's obliviousness to flirtation — establishes self-image
- Breakfast prices — foreshadowing financial reality

---

### Scene 04: `event_jace_doctor_appointment`
- **Date:** Day 2, ~early 2105 [STORYBOT: 2105-03-16]
- **Time start:** 12:00 (appointment begins)
- **Time end:** ~13:30 (Rich drops Jace at apartment)
- **Duration of scene action:** ~1.5 hours
- **Estimated text length:** 2,500-4,000 words (pace carefully — emotional climax of Act 1)
- **Spatial range:** Doctor's office → hallway → private room (off-page) → rover → apartment door
- **POV:** Jace (tight)
- **Major beats:** Casual entry, doctor's bad news, information environment activation, diagnosis explanation, Q&A, exit, hallway with Rich and Colonel, off-page private talk, ride home, alone in apartment

**Character state at scene start:**
- Jace: Sharp, confident, anticipatory
- The Doctor: Professional, prepared to deliver bad news
- The Colonel: Formal, in dress uniform, expecting to welcome Jace
- Rich: Cheerful, expecting normal welcome day

**Character state at scene end:**
- Jace: Devastated, in shock, body collapsed, knows about disease, knows discharge is coming
- The Doctor: Off-page after handover
- The Colonel: Withdrew respectfully, will be briefed later
- Rich: Now in friend/protector role, deeply concerned

**Time gap to next scene:** Hours-to-days (Jace alone, processing — likely the next major scene is the bar scene during the hard months, days/weeks later)

**Continuity flags:**
- Bone disease — now canon for all future scenes
- Mars-okay-Earth-no — permanent body constraint
- 30-day vacate clock — runs from this date
- 1M credit debt — implicit, will become explicit as Jace processes
- Genetic implication — sisters need screening
- Rich's role transition — sponsor → friend
- The Colonel's grace — establishes him as honorable

---

### Scene 05: `event_jace_messages_home` (Standalone Reference Scene)
- **Status:** This scene was originally drafted as a separate event, but the gym scene now incorporates it as Beat 6
- **Recommendation:** Either deprecate the standalone file or repurpose it for a *different* messaging beat (e.g., post-discharge messaging home, or pre-departure farewells)
- **[AUTHOR DECISION NEEDED]:** Should `event_jace_messages_home` remain as a separate scene at a different time, or be merged into the gym scene?

---

### Scene 06: `event_jace_bar_rumors` (Recurring)
- **Date:** Multiple instances during the hard months — first instance a week or so post-discharge, then recurring across weeks
- **Time start:** Evening (~19:00-22:00 typical)
- **Duration of scene action:** ~1-2 hours per visit
- **Estimated text length:** Varies — first visit longer (3,000+ words), subsequent shorter (1,500 each)
- **Spatial range:** The Long Burn bar (working name) — same location each time, different people
- **POV:** Jace (tight)
- **Function:** Establish Jace's hard months; plant belt rumors; introduce the Rat as background presence

**Character state at scene start (first visit):**
- Jace: Discharged ~1 week, lost weight, no work yet, financial reality dawning
- Bar regulars: Dock workers, ex-military, contractors

**Character state at scene end (final visit before package run):**
- Jace: Recognizable bar regular, reading the rumor field, beginning to suspect something is genuinely wrong with belt operations
- The Rat: Has noticed Jace, deciding when to engage

**Time gap from doctor scene:** Days-weeks (varies by visit)
**Time gap to next major scene:** Variable

**Continuity flags:**
- Belt rumors should escalate visit-to-visit — sabotage theories, deaths, supply chain failure
- The Rat visible across visits before formal introduction
- Censorship effects becoming felt (news cuts, missing information)

---

### Scene 07: `event_jace_delivers_package` (TBD detail)
- **Date:** Mid hard months, ~2105-04 to 2105-05
- **Function:** First formal contact with the Rat
- **Status:** Not yet detailed — flagged for next worldbuilding session

---

### Scene 08: `event_jace_origin_negotiation`
- **Date:** Late hard months, ~2105-05 to 2105-06
- **Function:** The Origin contract that ships Jace to the belt; the Cerberus moment
- **Status:** Initial draft exists; choreography file pending

---

### Scene 09: `event_intel_deal_with_jace`
- **Date:** Just after Origin negotiation, ~2105-05 to 2105-06
- **Function:** Sylvester recruits Jace as asset; HUD reactivated
- **Status:** Not yet detailed — flagged for next worldbuilding session

---

### Scene 10: `event_falcon_departure`
- **Date:** ~Mid-2105
- **Function:** Boarding and departure
- **Status:** Not yet detailed

---

## Time-Gap Reference Table

| From → To | Gap | Notes |
|-----------|-----|-------|
| Pinta voyage → Mars arrival | None | Scenes flow continuously |
| Mars arrival → Gym | ~18-20 hours | Jace sleeps |
| Gym → Doctor | ~15 minutes | Same day |
| Doctor → Hard months bar | Days-weeks | Off-page processing time |
| Bar visits | Days-weeks each | Recurring |
| Bar → Package delivery | Days | Artemis's request |
| Package → Origin negotiation | Weeks | Crash certification period |
| Origin → Sylvester | Hours-days | Triggered by Origin signing |
| Sylvester → Falcon departure | Days-weeks | Final preparations |
| Departure → Falcon transit | None | Continuous |

---

## Scene Sequencing for Chapter Structure

### Chapter 1 Candidate
- Scene 02: Mars arrival + tour
- Scene 03: Gym (Day 2 morning)
- Scene 04: Doctor's appointment (Day 2 noon)

**Total chapter duration:** ~36 hours
**Total chapter word count:** ~9,000-14,000 words
**Emotional arc:** Hope → Devastation
**Cliffhanger:** Jace's apartment door closing on his old life

### Chapter 2 Candidate
- Scene 06 first visit + montage of hard months
- Scene 07: Package delivery
- Scene 06 second/third visit (escalating rumors)

**Total chapter duration:** ~weeks
**Total chapter word count:** TBD
**Emotional arc:** Devastation → Survival
**Cliffhanger:** Jace's first formal interaction with the Rat — opens the smuggling-network door

### Chapter 3 Candidate
- Scene 08: Origin negotiation
- Scene 09: Sylvester recruitment

**Total chapter duration:** ~days
**Total chapter word count:** TBD
**Emotional arc:** Survival → Reluctant Hope (compromised)
**Cliffhanger:** Jace boarding the *Falcon*

---

## Off-Page Events Affecting Character State

### Between Doctor Scene and First Bar Visit (Days-Weeks)
- Jace processes the discharge over 24 hours, mostly alone
- Calls family — tells them. Dawn cries. Chris is angry at the system. Athena is heartbroken.
- Tries Artemis multiple times — failures continue. Eventually a degraded connection lets through fragments.
- Artemis offers 50,000 credits and the package errand
- Jace stops shaving daily
- Loses 5-7 pounds in the first two weeks (stress, reduced appetite)
- Begins menial labor — cleaning, fixing, errand running
- Daily exercise drops from 2-3 hours to whatever fits between gigs
- His HUD remains deactivated throughout — he has to re-learn unaugmented life
- Begins frequenting the bar for cheap food

### Between Origin Signing and Sylvester Recruitment (Hours)
- Jace returns from the Origin meeting feeling small wins (Cerberus secured, contract signed)
- Sylvester moves quickly — within 24 hours of the Origin signature, he and Mei make contact
- The HUD reactivation is the main hook

### Between Sylvester Recruitment and Falcon Departure (Days-Weeks)
- Final medical clearances
- Crash certification completion
- Cerberus officially added to manifest
- Family farewell calls (more degraded comms with Artemis)
- Jace's HUD reactivated, civilian-contractor mode — relief
- Final shopping for personal belongings (limited mass allowance)
- Quarters cleared
- Boarding day arrives

---

## StoryBot Continuity Rules

When generating prose for any scene, the StoryBot must:

1. **Verify character state matches arrival state** (per scene's "Character state at scene start")
2. **Track knowledge progression** — Jace cannot know things that haven't happened yet, but should remember things that have
3. **Honor time gaps** — don't have characters reference events that haven't occurred or refer to "yesterday" when weeks have passed
4. **Apply emotional carry-over** — the discharge bleeds into all subsequent scenes; Jace cannot suddenly be "back to normal" the next morning
5. **Maintain physical consistency** — Jace's appearance, weight, fitness level evolves; his HUD state (active/inactive/civilian-contractor) changes
6. **Respect relationship state** — when Jace meets Mei "for the first time" formally, it must square with having glimpsed her at the base

When information is missing, the StoryBot may extrapolate consistently — but must flag any extrapolation that could affect canon (new character names, plot events, world rules) for author review.

---

## Cross-References

- See individual scene files in `/scenes/` and `/scenes/choreography/`
- See `/timeline/timeline_master.md` for higher-level chronology
- See `/characters/voice/` for voice profiles
- See `/storybot/metadata_template_guide.md` for full metadata schema

## Revision Notes

- 2026-04-30: Initial detailed temporal map covering Scenes 02-04 (early arrival arc).
