# Priority List of Things to Fix & Open Questions

This document tracks unresolved story details, technical discrepancies, missing files, and open design questions within **The Aura Chronicles** knowledge base.

---

## 1. Technical & Narrative Open Questions

- **Disentangling Jace's Mars Backstory:** Since the active narrative of Book 1 starts directly aboard the *Falcon* transit (`scenes/book01-ch01-morning-round.md`), Jace's time on Mars (shuttle landing, gym session, medical checkout, hard months of gig labor, smuggling list sprint, negotiation with Origin, and recruitment by Sylvester) needs to be formally archived as backstory. The current `control/story-structure.yaml` and `control/scene-registry.yaml` files still treat these Mars events as active, sequential on-page chapters (`ch001` through `ch007`). 
  - **Proposed Action:** Update `story-structure.yaml` to start active chapter sequencing from the *Falcon* transit (or boarding) and label the Mars chapters as "Backstory/Archive." Move or tag corresponding scene definitions in `scene-registry.yaml` as `status: archive_backstory`.
- **Naming Conventions & The Nomenclature Thread:** Check the alignment of the bracketed `[Skill]` notation across the series. Ensure that brackets do not appear in any drafted prose set before Jace establishes them in Arc 2.

---

## 2. Missing Core Files & Concepts

- **U.S. Intelligence Apparatus:** Mentioned in Mei's background and Jace's recruitment, but needs a dedicated faction/concept outline: `faction_united_states_intelligence.md`.
- **Character Stubs:** Details on the USAF Captain (direct supervisor of Rich and Jace on Mars) and the livestock breeder handler need to be finalized for historical reference.

---

## 3. Metric & Narrative Inconsistencies to Reconcile

- **Artemis Stationing (Métis vs. Odysseus Inconsistency):** 
  - In a recent revision, Artemis Grant's location and the Arc 2 rescue site were changed to **Métis Station** (on asteroid 9 Metis) to separate it from **Odysseus Station** (L4 science station). 
  - However, numerous files (e.g., `arcs/arc_01_falcon_and_fortuna.md`, `characters/char_kael.md`, `factions/faction_belter_stations.md`, `scenes/event_jace_assembles_smuggling_list.md`, `scenes/event_jace_doctor_appointment.md`, `technology/tech_communications_filtering.md`, `timeline/scenes_temporal_map.md`) still incorrectly refer to Artemis being stationed at, or sending packages to, **Odysseus Station**.
  - **Proposed Action:** Update all remaining references to Artemis's location and Jace's supply destination during the Mars era from "Odysseus" to "Métis" (except where Odysseus is referred to as the L4 science post).
- **AI Curly Braces Violations:** 
  - The `SERIES_BIBLE.md` mandates that in-universe AI names always use curly braces (e.g., `{Aura}`, `{Alex}`, `{Penny}`) in all prose, dialogue, and knowledge base documents.
  - A project-wide check revealed over 300 instances (especially in `char_nick_lee.md`, `char_jace_apollo.md`, `tech_fortuna_ai_systems.md`, etc.) where AI systems are referenced as plain text (e.g., "Aura", "Alex", "Penny") instead of `{Aura}`, `{Alex}`, `{Penny}`.
  - **Proposed Action:** Systematically edit files to wrap AI names in curly braces when referring to the AI systems/instances.

---

## 4. Unresolved Arc Goals (To-Resolve List)

This checklist tracks logical and narrative tests from the story arc documents that have not yet been met because their corresponding chapters are in outlines/notes and need to be drafted:

### Arc 1 — The Falcon and Fortuna (Unresolved Goals)
- [ ] **Jace's Identity:** Complete the process where Jace's identity collapse and reconstruction are fully shown, showing who he is and what he has lost (relegated to flashbacks/references).
- [ ] **Never-Never & Sophia:** Properly introduce Sophia Lotte and the Never-Never, establishing what has been discovered and why nobody knows yet.
- [ ] **First Crossing:** Draft the scene where Jace's first crossing and the Jace/Sophia/Cerberus partnership are established.
- [ ] **Open-Source Decision:** Draft the scene where Nick and Jace make the open-source decision, turning `{Aura}` into the belt's distributed magic-interface layer.
- [ ] **Swarm Attack:** Draft the Fortuna swarm attack to close Arc 1 with genuine danger.
- [ ] **Astral Vehicle Subplot:** Run Jace's Astral vehicle experimentation subplot as an iterative, failure-heavy, but ultimately successful thread.
- [ ] **Empirical Discovery of Rules:** Ensure the tau snap mechanic, distance² ratio, and atomic weight² crossing cost rule are discovered empirically by Jace and Sophia through experimentation, not exposition.
- [ ] **LOX Eyebrow Incident:** Draft the LOX eyebrow incident (played for comedy but with genuine stakes establishing rocket ablation rules).
- [ ] **Drone Survey Target:** Show Jace's drone survey using Astral N-1 perception to locate the platinum-rich asteroid target.
- [ ] **Maureen's Trust:** Show Jace earning Maureen's trust during the Falcon swarm rescue.
- [ ] **Cross-Dimensional Transport:** Demonstrate the first successful cross-dimensional machinery transport through the Astral.

### Arc 2 — The Woven and the Unbound (Unresolved Goals)
- [ ] **Galactic Context:** Help the reader understand what galactic Will-Network civilizations are and why humanity doesn't fit their frameworks.
- [ ] **Kael's Character:** Establish Kael's conflict between protocol and conscience, resolving it in humanity's favor at the cost of her life.
- [ ] **The Bloom:** Introduce the Bloom as a second outsider faction (alien, non-hostile, incomprehensible).
- [ ] **Metis Rescue:** Draft the Metis rescue mission to establish Artemis as a major practitioner and introduce Dr. Eugene Hart.
- [ ] **Dungeon Emergence:** Establish dungeon emergence on Earth and Mars as a separate but converging threat (introducing five POV characters, only one of whom survives).
- [ ] **Jace's Imprisonment:** Conclude Arc 2 with Jace's imprisonment by the Bloom, creating stakes about being absorbed into a hierarchy.
- [ ] **Aura HUD Recording:** Establish `{Aura}`'s recording of the Bloom transit as a future asset for Arc 3.

---
*Generated by Antigravity AI agent.*
