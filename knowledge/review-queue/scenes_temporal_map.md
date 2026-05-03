---
id: scenes_temporal_map
name: Master Scenes Temporal Map
type: chronology_index
status: working draft (Book 1, early chapters)
last_updated: 2026-05-02
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
- **Chapter assignments** are working candidates — final chapter structure is the author's call

---

## Book 1 — Chapter / Scene Map

| Chapter | Scene ID | Title | Day | Status |
|---|---|---|---|---|
| (pre) | scene_01_pinta_voyage | Pinta voyage (off-page) | Late 2104 → early 2105 | reference only |
| **Ch01** | scene_02a_jace_shuttle_descent | Shuttle descent and pickup | Day 1 ~02:00 | pre-draft |
| **Ch01** | scene_02b_jace_rover_tour | Rover tour through U.S. settlement (incl. WiFi excitement, Coffee Tree Dome, Bird Dome, Pangu reference) | Day 1 ~02:30–11:00 | pre-draft |
| **Ch01** | scene_02c_jace_drone_center_tour | Drone control center tour | Day 1 ~16:00 | draft |
| **Ch01** | scene_02d_jace_commander_welcome | Base commander welcome | Day 1 ~17:30 | sketch |
| **Ch02** | scene_03_jace_gym_arrival_with_messages | Gym session + multitasking messaging home (Jelly/Jinx mentioned, Artemis sends fail) | Day 2 ~08:00–12:00 | pre-draft |
| **Ch02** | scene_04_jace_doctor_appointment | Doctor's appointment / discharge | Day 2 ~12:00–13:30 | pre-draft |
| **Ch03** | scene_06a_jace_bar_rumors_first | First bar visit (~1 week post-discharge) | ~early 2105-04 | pre-draft |
| **Ch03** | scene_06b_rich_comms_favor | Rich's comms favor for Jace | ~early-mid 2105-04 | sketch |
| **Ch03** | scene_06c_jace_bar_rumors_recurring | Bar visits 2–3 (escalating rumors) | ~mid 2105-04 → early 2105-05 | pre-draft |
| **Ch03–Ch04** | scene_06e_jace_dog_breeder_visits | Dog breeder visits (recurring across hard months) | ~weeks 2–12 post-discharge | draft |
| **Ch04** | scene_07_jace_delivers_package | First package delivery to the Rat | ~mid 2105-05 | TBD detail |
| **Ch04** | scene_06d_jace_bar_rumors_final | Bar visit 4 (formal Rat introduction) | ~late 2105-05 | pre-draft |
| **Ch04** | scene_06f_jace_horse_farm_offer | Parents offer to sell the farm; Jace refuses; commits to Origin | Late hard months, days before Origin meeting | draft |
| **Ch05** | scene_08_jace_origin_negotiation | Origin Industries contract; Cerberus secured | ~late 2105-05 → early 2105-06 | initial draft |
| **Ch05** | scene_09_intel_deal_with_jace | Sylvester recruits Jace; HUD reactivated | Hours-days post-Origin | TBD detail |
| **Ch06** | scene_10_falcon_departure | Boarding and departure | ~mid 2105 | TBD detail |

**Deprecated:**
- ~~`event_jace_messages_home`~~ — merged into `scene_03_jace_gym_arrival_with_messages`. File should be deleted or repurposed.

---

## Detailed Scene Records

### Scene 01: Jace's Pinta Voyage (Implied, Off-Page)
- **Status:** Reference only — not depicted as a scene
- **Date:** Late 2104 to ~early 2105
- **Duration:** ~4 months in transit
- **Function:** Background context — informs Jace's exhausted state at arrival; sets up his data-hunger (carrier comms on the Pinta were brutally low-bandwidth)
- **Gap to next scene:** None (continues directly into arrival)

---

### Scene 02 — Day 1 Arrival (Chapter 01)

The arrival day is structured as four linked sub-scenes that together form the bulk of Chapter 01. Spatial flow: Pinta → terminal → observation dome → connected domes (including Coffee Tree Dome and Bird Dome) → rover → military base → drone center → command office → quarters.

#### Scene 02a: `event_jace_shuttle_descent`
- **Chapter:** Ch01
- **Date:** Day 1, ~early 2105 [STORYBOT: Anchor as 2105-03-15 unless author specifies]
- **Time:** ~02:00 (Pinta lands)
- **Function:** Arrival, first breath of Mars air, first meeting with Rich (who is carrying his coffee canister)
- **Source:** `knowledge/scenes/event_jace_mars_tour_with_rich.md` (opening beats)

#### Scene 02b: `event_jace_rover_tour`
- **Chapter:** Ch01
- **Date:** Day 1
- **Time:** ~02:30 → ~11:00 (terminal processing, walking tour, rover ride to base)
- **Major beats:**
  - Disembark, processing, scanner foreshadowing, meet Rich
  - **WiFi-excitement dialogue and download-queue exchange** ("the WiFi here is incredible... I have like three hundred friends back home waiting for me to come online" / Rich's hint about belt comms being different)
  - Walking tour through dome cluster including:
    - **Coffee Tree Dome** (Rich's favorite — different temperature/pressure, Mars coffee cultivation, Rich's coffee sourcing)
    - **Bird Dome** (100-credit entry, higher pressure, fake lake, geese with goslings, Mars Goose Cam phenomenon)
  - HUD/fiscal-naïveté conversation between Jace and Rich (with entertainment + blush sub-beat)
  - Pangu/Pengu reference dropped in passing (oily-clothed Chinese workers transferring through)
  - Rover transit to base
  - Lunch
- **Source:** `knowledge/scenes/event_jace_mars_tour_with_rich.md`

#### Scene 02c: `event_jace_drone_center_tour`
- **Chapter:** Ch01
- **Date:** Day 1
- **Time:** ~16:00 (after lunch, after settling)
- **Function:** Six drone operators, fleet scope reveal (~400 drones, ~900 robots), HUD+command reveal, Mei + Sylvester glimpse through secure-area window, **"almost a thousand American drones / half corporate" line** plants corporate Mars presence
- **Source:** `knowledge/scenes/event_jace_drone_center_tour.md`

#### Scene 02d: `event_jace_commander_welcome`
- **Chapter:** Ch01
- **Date:** Day 1
- **Time:** ~17:30
- **Function:** Brief, warm meeting with Space Force Colonel; belt anomalies mentioned as background concern; Jace files it under "not my problem yet"
- **Source:** TBD (sketched in `control/scene-registry.yaml`)

**Combined Day 1 Character State at end:**
- Jace: Crashed asleep, knowledge of Mars geography gained, scanner unease forgotten, drone operation scope absorbed, Mei/Sylvester glimpsed but unreflected, slightly aware that corporations are everywhere on Mars, delighted by the WiFi
- Rich: Back to his quarters, fond of Jace, mildly concerned about his naïveté, aware Jace has the medical checkup coming, refilled coffee canister

**Combined Day 1 Continuity Flags:**
- Scanner foreshadowing — establish but do not resolve
- Sylvester/Mei glimpsed but not formally introduced
- Belt anomalies mentioned in passing (Colonel; also Rich's "crazy busy lately with all the problems")
- Service rivalry undercurrent established (Space Force command, Air Force operational)
- Jace's HUD enthusiasm and fiscal naïveté both established
- Pangu/Pengu reference planted
- Corporate-presence-on-Mars planted via the 1000-drones line
- Mars Goose Cam planted as cultural touchstone
- Coffee canister established as Rich's iconic mannerism
- Jace's data-hunger after Pinta voyage established (load-bearing irony for comms-degradation arc)

**Time gap to next scene:** ~14–16 hours (Jace sleeps overnight)

---

### Scene 03: `event_jace_gym_arrival_with_messages` (Chapter 02)

> **MERGED SCENE — was previously two scenes (gym + messages_home).** Per author session 2026-05-02, the family-messaging beat is now fully integrated into the gym scene as parallel multitasking with Jace's HUD game.

- **Chapter:** Ch02
- **Date:** Day 2, ~early 2105 [STORYBOT: Anchor as 2105-03-16]
- **Time start:** 08:00 (Jace wakes)
- **Time end:** 12:00 (medical appointment begins)
- **Duration of scene action:** ~4 hours
- **Estimated text length:** 3,000–4,500 words
- **Spatial range:** Apartment → corridors → breakfast vendor → gym → apartment → rover → military base
- **POV:** Jace (tight)
- **Major beats:** Wake up, navigation fumbling, breakfast sticker shock, gym arrival, **multitasking sequence (HUD game + family messages including asks about Jelly the family dog and Jinx the family horse + repeatedly failed Artemis sends while running on treadmill)**, two girls flirtation that Jace doesn't notice (because he is multitasking through it), grooming, base arrival, Sylvester/Mei glimpse, hand-off to medical

**The Multitasking Beat:**

While Jace runs on the treadmill, his HUD is doing three things at once:
1. Running the combat sim / strategy game he loves
2. Recording video messages home (Dawn, Chris, Athena), each of which includes an ask about Jelly (the family dog) or Jinx (the family horse) — small recurring Earth anchors
3. Attempting to send a message to Artemis at Odysseus Station — repeatedly, with each attempt failing

His face appears, to anyone looking, to be staring forward in concentration. He is, in fact, oblivious to the room around him. Two young women on adjacent treadmills smile at him, one of them speaks toward him at one point — he doesn't notice. He is too deep in the game-and-messaging stack. The reader sees what Jace doesn't.

**Replies arrive later** (off-page, possibly that evening or next morning before he meets Rich): Jelly is fine, sleeping in the barn; Jinx is fine, slow on cold mornings but cantering well in the afternoon. Chris attaches a short clip of Jinx in the south pasture. Jace watches it twice. These small confirmations are load-bearing for the horse farm offer scene later in the arc.

**Character state at scene start:**
- Jace: Rested, fresh, eager
- Rich: At work at base, expecting to formally welcome Jace (canister already refilled)

**Character state at scene end:**
- Jace: Sharp, well-groomed, anticipatory; aware that Artemis comms are failing (though writing it off as latency); has glimpsed Sylvester and Mei; warm reassurances about Jelly and Jinx anchoring him to home
- Rich: Greeted Jace, expecting normal welcome day

**Time gap to next scene:** ~0 minutes (transitions directly into doctor's appointment)

**Continuity flags:**
- Failed Artemis message — first concrete sign of comms problem
- Sylvester/Mei glimpse — setup for later recruitment
- Jace's obliviousness to flirtation — establishes self-image AND social-avoidance pattern
- Breakfast prices — foreshadowing financial reality
- Multitasking-as-avoidance — character pattern that recurs
- Jelly and Jinx as established anchors — load-bearing for Scene 06f

---

### Scene 04: `event_jace_doctor_appointment` (Chapter 02)
- **Chapter:** Ch02
- **Date:** Day 2, ~early 2105 [STORYBOT: 2105-03-16]
- **Time start:** 12:00 (appointment begins)
- **Time end:** ~13:30 (Rich drops Jace at apartment)
- **Duration of scene action:** ~1.5 hours
- **Estimated text length:** 2,500–4,000 words (pace carefully — emotional climax of Act 1)
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

**Time gap to next scene:** Hours-to-days off-page processing → days/weeks before the first bar visit

**Continuity flags:**
- Bone disease — now canon for all future scenes
- Mars-okay-Earth-no — permanent body constraint
- 30-day vacate clock — runs from this date
- 1M credit debt — implicit, will become explicit as Jace processes
- Genetic implication — sisters need screening
- Rich's role transition — sponsor → friend
- The Colonel's grace — establishes him as honorable

---

### Scene 05: ~~`event_jace_messages_home`~~ — DEPRECATED

**Status:** Merged into Scene 03. The file `event_jace_messages_home.md` should be deleted from the repo (or repurposed for a *different* messaging beat — e.g., post-discharge messaging home, or pre-departure farewells from the *Falcon*).

**Author decision needed:** Delete the file outright, or rename and repurpose for a later messaging beat?

---

### Scene 06: `event_jace_bar_rumors` (Chapters 03–04)

This is a recurring scene rather than a single scene. Each visit is a discrete sub-scene with its own chapter assignment.

| Sub-scene | Chapter | Anchor | Function |
|---|---|---|---|
| 06a — First visit | Ch03 | ~1 week post-discharge | Establishing scene; rumors are still rumors; the Rat visible across the room but not engaged |
| 06b — *(Rich's comms favor — see scene_06b_rich_comms_favor below — falls between 06a and 06c chronologically)* | Ch03 | early-mid hard months | — |
| 06c — Second/third visits | Ch03 | mid hard months | Rumors escalate — Odysseus comms officially classified intermittent; the merchant's shop has closed |
| 06d — Fourth visit | Ch04 | post-package | Formal Rat introduction; working relationship begins |

- **Time start (each):** Evening (~19:00–22:00 typical)
- **Duration of scene action:** ~1–2 hours per visit
- **Estimated text length:** Varies — first visit longer (3,000+ words), subsequent shorter (1,500 each)
- **Spatial range:** The Long Burn bar (working name) — same location each time, different people
- **POV:** Jace (tight)
- **Function:** Establish Jace's hard months; plant belt rumors; introduce the Rat as background presence

**Continuity flags:**
- Belt rumors should escalate visit-to-visit — sabotage theories, deaths, supply chain failure
- The Rat visible across visits before formal introduction
- Censorship effects becoming felt (news cuts, missing information)
- Jace's weight loss visible across visits — the rice-and-cheap-food economy in physical evidence

---

### Scene 06b: `event_rich_comms_favor` (Chapter 03)
- **Chapter:** Ch03
- **Date:** Hard months — TBD specific date, post-discharge, post-medical, between bar visits 06a and 06c
- **Function:** Rich uses his base IT/comms access to do Jace one significant favor (specific favor mechanism TBD — see scene file)
- **Source:** `knowledge/scenes/event_rich_comms_favor.md`
- **Continuity flags:** This is the scene that pays off Rich's IT/comms role and his compassion-with-limits character note. Specific favor option (1–4 in scene file) needs author selection.

---

### Scene 06e: `event_jace_dog_breeder_visits` (Chapters 03–04, recurring)
- **Chapter:** Ch03 → Ch04 (recurring across the hard months, weeks 2 through ~12 post-discharge)
- **Date:** Across the hard months
- **Time start (each):** Variable — daytime, between gigs
- **Duration of scene action:** ~1–3 hours per visit
- **Estimated text length:** Varies — first visit longer (2,000+ words), subsequent shorter (500–1,500 each); composite use across multiple chapters
- **Spatial range:** Mars dog breeder facility (sub-section of U.S. settlement agricultural division) → walk back through dome corridors
- **POV:** Jace (tight)
- **Function:** Establish Jace as a dog person before the Origin negotiation; foreshadow Cerberus; show Jace's depression and lonliness as he keeps coming back to the place that doesn't charge him; seed the puppy-naming moment

**Recurring visit structure:**
| Visit | Anchor | Beat |
|---|---|---|
| Visit 1 | ~week 2 post-discharge | Discovery; mother is pregnant; handler's friendly tolerance |
| Visit 2 | ~week 3 | Mother gives birth; Jace sees the litter for the first time |
| Visit 3 | ~weeks 4–6 | Regular visits; puppies grow; Jace begins favoring the boy |
| Visit 4 | ~weeks 6–8 | Handler reveals: mother and one female to Fortuna; boy puppy to be sold separately on Mars at a price beyond Jace's reach |
| Visit 5 | ~weeks 8–10 | Bond deepens; Jace doesn't say anything to anyone |
| Visit 6 | Just before Origin | Quiet final visit. **The naming of the puppy as Cerberus** happens on the walk home from this or the previous visit. |

**Source:** `knowledge/scenes/event_jace_dog_breeder_visits.md`

**Continuity flags:**
- Cerberus's family lives at this facility; mother and sister ship to Fortuna ahead of him
- Jace's pre-negotiation attachment makes the Origin "ask" inevitable rather than impulsive
- The handler — TBD as recurring or one-arc figure

---

### Scene 07: `event_jace_delivers_package` (Chapter 04)
- **Chapter:** Ch04
- **Date:** Mid hard months, ~2105-04 to 2105-05
- **Function:** First formal contact with the Rat at the launch facility
- **Status:** Not yet detailed — flagged for next worldbuilding session

---

### Scene 06f: `event_jace_horse_farm_offer` (Chapter 04)
- **Chapter:** Ch04
- **Date:** Late hard months, post-package run, days before the Origin negotiation
- **Time start:** Evening Mars-time (afternoon Virginia-time)
- **Duration of scene action:** ~30–45 minutes (single video call)
- **Estimated text length:** 2,500–3,500 words
- **Spatial range:** Jace's small post-discharge apartment in Terminus → video call with Dawn and Chris in their Virginia farm kitchen
- **POV:** Jace (tight)
- **Function:** **The motivational hinge that drives Jace toward the Origin contract.** Parents offer to sell the Virginia horse farm to clear his million-credit debt. Jace refuses. The refusal sharpens him — for the first time in weeks, his officer's posture comes back. He commits to the Origin asteroid contract during the call.

**Major beats:**
- The call comes (two-person frame, unusual)
- Soft open (rice, gigs, Rich)
- The offer (Dawn does most of the talking; Chris is silent and devastated)
- Jace's refusal (sharp, immediate, with *Jinx* and *farm* and *Athena would come home to* landing as specific words)
- The plan forms (Jace tells them about the Origin opportunity — he has just decided)
- The signoff (Dawn cries, Chris doesn't quite, Jace asks about Jelly and Jinx)

**Character state at scene start:**
- Jace: Hollowed, drifting, considering Origin abstractly without commitment
- Dawn: Resolved to make the offer
- Chris: Resolved (would have done it), devastated quietly

**Character state at scene end:**
- Jace: Committed. Knows he is taking the Origin contract.
- Dawn: Crying, relieved he refused
- Chris: Proud (silent)

**Source:** `knowledge/scenes/event_jace_horse_farm_offer.md`

**Continuity flags:**
- Jace's refusal of the parental sacrifice IS the driver for the Origin contract
- The bone disease's cruel layer (Jace preserving a place he will never see again) is in the reader's awareness without being said
- Jelly and Jinx as anchors paid off here
- The farm is preserved in canon — future references to the farm remain accurate

---

### Scene 06d: `event_jace_bar_rumors_final` (Chapter 04)
- **Chapter:** Ch04
- **Date:** Late hard months, post-package, before Origin meeting (or interleaved with 06f horse farm offer — author's call on ordering)
- **Function:** Formal Rat introduction at the bar; working relationship begins
- **Status:** Pre-draft; see Scene 06 sub-scene table above

---

### Scene 08: `event_jace_origin_negotiation` (Chapter 05)
- **Chapter:** Ch05
- **Date:** Late hard months, ~2105-05 to 2105-06
- **Function:** The Origin contract that ships Jace to the belt; the Cerberus moment (which now lands with weeks of pre-bond behind it)
- **Status:** Initial draft exists; choreography file pending

---

### Scene 09: `event_intel_deal_with_jace` (Chapter 05)
- **Chapter:** Ch05
- **Date:** Just after Origin negotiation, ~2105-05 to 2105-06 (within hours-days)
- **Function:** Sylvester recruits Jace as asset; HUD reactivated
- **Status:** Not yet detailed — flagged for next worldbuilding session

---

### Scene 10: `event_falcon_departure` (Chapter 06)
- **Chapter:** Ch06
- **Date:** ~Mid-2105
- **Function:** Boarding and departure
- **Status:** Not yet detailed

---

## Time-Gap Reference Table

| From → To | Gap | Notes |
|-----------|-----|-------|
| Pinta voyage → Mars arrival (Scene 02a) | None | Scenes flow continuously |
| Scene 02a → 02b | None | Continuous (terminal processing) |
| Scene 02b → 02c | ~5 hours (lunch + arrival) | Lunch beat in 02b |
| Scene 02c → 02d | ~1.5 hours | Walk to command office |
| Scene 02d → Scene 03 | ~14–16 hours | Jace sleeps overnight |
| Scene 03 → Scene 04 | ~0 minutes (~15 min walk) | Same morning, transitions directly |
| Scene 04 → Scene 06a | Days–weeks | Off-page processing time |
| Scene 06a → Scene 06b | Days–weeks | Rich reaches out off-page |
| Scene 06a/06b → Scene 06e (first visit) | Days–weeks | Jace discovers the dog breeder |
| Scene 06e (recurring) | Throughout the hard months | Visits continue across all of Ch03–Ch04 |
| Scene 06b → Scene 06c | Days–weeks | More bar visits |
| Scene 06c → Scene 07 | Days | Artemis's request, package preparation |
| Scene 07 → Scene 06f | Days–weeks | Parents' decision matures off-page |
| Scene 06f → Scene 06d | Days | Final bar / Rat formal introduction |
| Scene 06d → Scene 08 | Weeks | Crash certification period |
| Scene 08 → Scene 09 | Hours-days | Triggered by Origin signing |
| Scene 09 → Scene 10 | Days-weeks | Final preparations |
| Scene 10 → Falcon transit | None | Continuous |

---

## Chapter Structure (Working Candidate)

### Chapter 01 — Arrival Day
- Scene 02a: Shuttle descent and pickup
- Scene 02b: Rover tour (WiFi excitement, Coffee Tree Dome, Bird Dome, HUD/fiscal + Pangu)
- Scene 02c: Drone center tour (1000 drones, half corporate)
- Scene 02d: Commander welcome
- (sleep)

**Total chapter duration:** ~16 hours of clock time
**Estimated word count:** ~10,000–14,000
**Emotional arc:** Awe and golden-boy confidence; planted ironies the reader sees but Jace doesn't
**Cliffhanger:** Jace asleep, certain his life is finally beginning

### Chapter 02 — Disaster Day
- Scene 03: Gym arrival + multitasking messaging home (failed Artemis send, oblivious to flirtation, Jelly/Jinx anchors planted)
- Scene 04: Doctor's appointment (the discharge)

**Total chapter duration:** ~6 hours
**Estimated word count:** ~6,000–9,000
**Emotional arc:** Confidence → Devastation
**Cliffhanger:** Jace's apartment door closing on his old life

### Chapter 03 — Hard Months Begin
- Scene 06a: First bar visit
- Scene 06b: Rich's comms favor
- Scene 06e (visits 1–4): Dog breeder visits — mother gives birth, litter grows, attachment forms
- Scene 06c: Bar visits 2–3 (escalating rumors)

**Total chapter duration:** Weeks
**Estimated word count:** ~7,000–11,000
**Emotional arc:** Devastation → Survival; Rich's compassion as structural support; the dogs as Jace's only un-priced joy
**Cliffhanger:** Artemis's request — the package errand — lands

### Chapter 04 — The Package and the Decision
- Scene 06e (visits 5–6): Dog breeder visits continue; Cerberus is named on the walk home
- Scene 07: Package delivery to the Rat
- Scene 06f: Horse farm offer call — Jace refuses, commits to Origin
- Scene 06d: Final bar visit / formal Rat introduction

**Total chapter duration:** Days–weeks
**Estimated word count:** ~6,000–10,000
**Emotional arc:** Survival → Reluctant entanglement → Committed
**Cliffhanger:** Origin meeting on the schedule

### Chapter 05 — The Deals
- Scene 08: Origin negotiation (Cerberus moment lands with weeks of pre-bond behind it)
- Scene 09: Sylvester recruitment (HUD reactivated)

**Total chapter duration:** Days
**Estimated word count:** ~7,000–10,000
**Emotional arc:** Reluctant Hope (compromised); Cerberus as the saved thing
**Cliffhanger:** Final farewells, the *Falcon* on the launch pad

### Chapter 06 — Departure
- Scene 10: Falcon boarding and departure burn

**Total chapter duration:** Hours
**Estimated word count:** ~3,000–5,000
**Emotional arc:** Mars below, the unknown ahead
**Transition into:** *Falcon* transit arc

---

## Off-Page Events Affecting Character State

### Between Doctor Scene and First Bar Visit (Days–Weeks)
- Jace processes the discharge over 24 hours, mostly alone
- Calls family — tells them. Dawn cries. Chris is angry at the system. Athena is heartbroken.
- Tries Artemis multiple times — failures continue. Eventually a degraded connection lets through fragments.
- Artemis offers 50,000 credits and the package errand
- Jace stops shaving daily
- Loses 5–7 pounds in the first two weeks (stress, reduced appetite, cheap-food economy)
- Begins menial labor — cleaning, fixing, errand running
- Daily exercise drops from 2–3 hours to whatever fits between gigs
- His HUD remains deactivated throughout — he has to re-learn unaugmented life
- Begins frequenting the bar for cheap food
- **Begins exploring the Mars dog breeder facility as free recreation** (he can no longer afford coffee, real food, or paid entertainment); becomes a regular over the following weeks (see Scene 06e)

### Between Rich's Comms Favor and Subsequent Bar Visits (Days–Weeks)
- Whatever the favor reveals (depending on selected option) shapes Jace's understanding of the comms situation going forward
- Rich does not formally see Jace again for a while; a deliberate cooling-off
- Jace processes what he learned — alone

### Between Bar Visits and Origin Negotiation (Weeks)
- Picks up his Pangu repair gig — one-time trip to the Chinese settlement; shudders about the experience afterward when reminiscing to Rich; ate well there, off the Chinese government's free-food policy
- Continues the dog breeder visits; learns the boy puppy will not be shipped off-world; names him **Cerberus** on the walk home from one of the later visits
- Receives the **horse farm offer** call from his parents (Scene 06f); refuses; commits internally to taking the Origin asteroid contract

### Between Origin Signing and Sylvester Recruitment (Hours)
- Jace returns from the Origin meeting feeling small wins (Cerberus secured, contract signed)
- Sylvester moves quickly — within 24 hours of the Origin signature, he and Mei make contact
- The HUD reactivation is the main hook

### Between Sylvester Recruitment and Falcon Departure (Days–Weeks)
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
7. **Respect address conventions** — apply `/knowledge/universe-spec/concept_military_address_culture.md` consistently (Rich calls Jace "Jace"; junior enlisted call him "LT"; etc.)
8. **Respect the family-anchor details** — Jelly the family dog and Jinx the family horse exist on Earth; they recur in messaging beats and are load-bearing for the horse farm offer beat. Their continued well-being is canon.
9. **Respect the Cerberus pre-bond** — by the time of the Origin negotiation, Jace has had weeks of attachment to the puppy at the Mars dog breeder facility. The negotiation ask is not impulse; it is the inevitable outcome of the recurring breeder scene.
10. **Respect Rich's coffee canister** — it is part of his physical presence in every scene he appears in. The pause-and-sip is part of his speech rhythm.

When information is missing, the StoryBot may extrapolate consistently — but must flag any extrapolation that could affect canon (new character names, plot events, world rules) for author review.

---

## Cross-References

- See individual scene files in `/knowledge/scenes/` and `/knowledge/scenes/choreography/`
- See `/knowledge/timeline/timeline_master.md` for higher-level chronology
- See `/knowledge/characters/` for full character bios and voice profiles
- See `/knowledge/storybot/metadata_template_guide.md` for full metadata schema
- See `/knowledge/control/scene-registry.yaml` for the scene-id source-of-truth
- See `/knowledge/control/story-structure.yaml` for narrative ordering
- See `/knowledge/review-queue/session_notes_2026-05-02.md` for the session log

## Revision Notes

- 2026-04-30: Initial detailed temporal map covering Scenes 02–04 (early arrival arc).
- 2026-05-02 (round 2): **Major restructure.** Day 1 split into four sub-scenes (02a–02d) reflecting `scene-registry.yaml`. Drone center tour added as Scene 02c. Scene 03 (gym) merged with deprecated Scene 05 (messages_home) into a single multitasking-aware scene. Rich's comms favor added as Scene 06b within the hard months. Bar rumors split into 06a/06c/06d to reflect recurring-visit structure. Chapter assignments (Ch01–Ch06) added to all scenes. Time-gap table updated. Address-convention cross-reference added to StoryBot rules.
- 2026-05-02 (round 3): **Hard-months expansion.** Dog breeder visits added as recurring Scene 06e. Horse farm offer added as Scene 06f. Scene 02b expanded to include WiFi excitement, Coffee Tree Dome, Bird Dome stops. Scene 03 family-message contents expanded to include Jelly and Jinx asks. Scene 02c expanded to include "1000 drones / half corporate" line. Off-page events updated with Pangu gig, dog breeder visits, horse farm refusal as Origin driver. Two new StoryBot continuity rules added (family anchors, Cerberus pre-bond, Rich's canister).
