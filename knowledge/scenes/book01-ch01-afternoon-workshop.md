---
description: "Draft scene detailing Jace's engineering work, tinkering prototypes, the Sparky naming incident, the controller print, and project development on the Falcon ship."
id: book01-ch01-afternoon-workshop
title: "Chapter 1 — Afternoon Workshop + Day 2 + Dream"
type: scene_draft
book: book01
chapter: Ch01-Ch02 bridge
arc: falcon_transit
pov: jace
timeline_anchor: "~Month 3 of transit, Mars to Fortuna"
characters: [char_jace_apollo, char_cerberus, char_maureen, char_nick_lee, char_saul]
location: ship_falcon_machine_shop
status: draft
last_updated: 2026-07-14
notes: >
  REWRITE (2026-07-14 session): Sparky is no longer a near-complete drone under
  assembly. Jace's workbench is an ongoing tinkering practice — multiple prototypes,
  fun failures, nothing operational by arrival. The hover-jet short-circuit incident
  is the naming origin of "Sparky" (the project, not a finished drone). Frustration
  targets Origin drone LOCKDOWNS (proprietary firmware, permission walls) — NOT
  telemetry; Jace must not know about the monitoring (sealed slow-burn). Controller
  print + Nick mecha dialogue added; drone-as-{Aura}-testbed motivation added.
  Still establishes: junior engineer, Thing One/Two workflow, Nick Lee pre-arrival
  friendship, Saul remote oversight, Maureen/printer arrangement, Cerberus dinner
  beat, first crystal dream, Day 3 alarm break.
  EPIGRAPH: light-lag gaming epigraph assigned to this chapter — see
  spec_chapter_epigraphs.md (new entry, transit track).
---

# Chapter 1 — Afternoon Workshop (Draft — Rewrite)

The machine shop smelled like warm polymer and burnt ambition. Jace had claimed a corner of the bench two months ago and hadn't given it back.

"Thing One — junction schematic, left overlay."

The diagram bloomed in his peripheral. He slid under panel B-7, seal replacement in hand, Thing One hovering behind him with its camera on the gap his knuckles kept finding. Four minutes of awkward. New seal seated clean.

"Log it. Thirty-day flag."

*LOGGED.*

He worked through the queue — a degraded rotor on Drone 44 that turned out to be a microfracture he found with his thumb, a filter clog in ring segment twelve tracing back to a loose baffle plate two segments upstream. Thing One crawled the duct. Thing Two handled the toilet fan. Small fixes. The ship accumulating quiet improvements nobody noticed until they weren't there.

Somewhere in the middle of the rotor job he tried to push a custom diagnostic routine to Thing One and got the same answer he always got: *MODIFICATION NOT AUTHORIZED. ORIGIN FIRMWARE INTEGRITY REQUIRED.* He'd written better diagnostics than the stock package back in the service. The drone would run them fine. The drone was not allowed to run them. The drone was not, in any way that mattered, his.

"Yeah, yeah," he told it. "Integrity."

He finished the last item and checked for Saul's notes. Two had arrived while he worked — the lag was down to about eight minutes now, the orbital geometry finally cooperating.

*B-7 looks good. Clean bead. — S*

*Drone 44 frame replacement is right call, don't patch it. — S*

Brief. Approving. Jace had started leaving the mic hot while he worked, narrating the steps slightly more than strictly necessary. He would deny this if asked.

Around 1600 he cleared enough of the queue to justify what he actually wanted to be doing.

He pulled the tray from under the bench.

The tray was a graveyard. A gripper arm that had worked beautifully for eleven minutes. Two chassis designs, abandoned. A sensor cluster he'd rebuilt four times, which currently detected everything except the things he pointed it at. And the newest resident: a squat, ugly little frame with four micro-jets he'd printed off a design he was maybe sixty percent sure he understood.

The plan — his and Nick's, argued out across a couple hundred million kilometers of shrinking lag — was a drone of his own. Not Origin's. His. Something that would run a full local {Aura} instance instead of a locked corporate stack, something he could actually open up and modify without a firmware integrity lecture. Survey work, scouting, whatever he needed it to be when he got to Fortuna. Nick had opinions about the payload bay. Nick had opinions about everything.

Nick's last voice note was still queued, arriving with a lag that was now closer to conversation than correspondence: *I'm so excited to try all these new code branches on your drone. Found one that should run really well against milspec hardware — you could offload processing to it automatically, your HUD to the drone, seamless. Oh, and there's one somebody built that mirrors how Origin structures drone control — if that works, it might talk to your dispatcher desk when you're on station. Which would be extremely funny and possibly a fireable offense, so, you know. Science.*

Jace snorted. "I'm not your test rig, Lee."

He was absolutely Nick's test rig. They both knew it. He queued the complaint for the next message anyway, on principle.

Today's experiment: the hover jets. In theory, four micro-jets and a cheap gyro would let the frame hold station in the shop's rotational gravity. In theory.

He clamped the frame to the bench, connected the power bus, and brought the jets up to ten percent.

The frame hummed. Lifted a centimeter against the clamp. Held.

"Ha," Jace said. "Okay. Okay okay okay."

Twenty percent. The hum climbed to a whine. Thirty. The frame strained against the clamp, beautifully stable, and for exactly four seconds Jace felt the specific joy of a thing behaving the way the math said it would.

Then the number two jet housing — the one he'd printed at the old tolerance, the one he'd been meaning to reprint — let go.

The frame kicked sideways. The power bus shorted with a crack and a gout of blue-white sparks that arced across the bench, off the clamp, into the tray of failures, where something in the old sensor cluster decided to participate. There was a pop, a second, larger pop, a smell like the inside of a lightning strike, and a thin scream of escaping smoke as the frame spun itself into the bench guard and died, sparking, upside down, one surviving jet still pulsing pathetically like a heartbeat.

Jace killed the bus. Grabbed the extinguisher. Didn't need it. Stood there with it anyway, breathing, while the smoke curled up into the vent and the last jet gave one final, defiant sputter and quit.

Under the bench, Cerberus had relocated to the doorway and was watching him with an expression that suggested she had notes.

"It's fine," he told her. "That's — most of that was supposed to happen."

The frame lay smoking gently in the bench guard. Scorched, half-slagged, one jet housing entirely gone, and somehow — this was the insulting part — the gyro was still reporting nominal, blinking its little status light like nothing had occurred.

Jace looked at it for a long moment.

"Sparky," he said. "Your name is Sparky."

He logged the failure — cause, tolerance, the housing he should have reprinted three days ago — because that was the difference between tinkering and flailing, and Saul had beaten that into him without ever raising his voice. Then he pulled up the print queue for the thing he'd actually promised himself this week.

The controller.

His HUD was a marvel and he loved it and it was, for gaming purposes, garbage. A year in and he could text, tee up commands, drag a cursor around like a man pushing a shopping cart with his mind. Remote-desktop reflexes. Fine for strategy games, where he and Nick had spent the transit trading empires across the lag. Useless for anything that needed hands.

The controller design was Nick's, naturally — modified, naturally, because Jace couldn't leave anything alone. Twin sticks, four paddles, grip contours scanned off his own hands. Six hours of print time.

He checked Maureen's list one more time — done — and hit start. The printer hummed to life.

Maureen's voice came through the intercom, flat as a panel seal.

"Grant. You printing parts for my ship or parts for your hobby?"

He checked the queue. Her list: done. His list: running.

"Both. Yours first."

A pause.

"Junction B-7?"

"Sealed and logged. Saul signed off."

Another pause, longer.

"Was that smoke alarm in your section?"

"Handled. Logged. Educational."

The longest pause yet.

"Fine." The intercom clicked off.

Under the bench — under the doorway, now — Cerberus stretched both back legs to their full improbable length and looked up at him with the focused intent of a dog who had thoughts about dinner.

"Yeah," Jace said. "Two minutes."

He saved the job, updated the queue — fourteen items, down from seventeen — and felt the small clean satisfaction of a man who had earned his three hours. Even if he'd spent part of them setting his own robot on fire.

---

# Day 2

The next day was mostly the same.

Rounds. Repairs. The controller came out of the printer clean — grips a little rough, one paddle needing a shim, but it sat in his hands like it belonged there, which after a year of pushing cursors around with his brain felt like being handed his hands back.

He recorded a message while flexing the sticks through their detents: "Lee. I finally printed that controller. Now that the lag's only a few seconds — ready for a mecha battle?"

The answer came back eleven minutes later — they were close now, close enough that eleven minutes felt like impatience instead of distance — and Nick was grinning audibly. *Oh, it's happening. Get used to that controller now and we can send bots at each other — command-queue mode, the lag won't matter, you'll hate it, it's great. And when you're on station? Full interactive mode. Some epic punch fights. I've got a mech saved for you. It's short. You'll see why that's funny when you meet me.*

Then, because Nick was incapable of ending a message on one topic: *How's the drone? Did the hover branch work? Also Screwdriver figured out the feeder latch again. You need to fix your pig.*

Screwdriver was not his pig. Screwdriver was her own pig. But he understood the sentiment.

He recorded his reply while shimming the paddle: the hover test, the short, the smoke, the name. Nick's response, when it came, was forty seconds of laughter and then, warmly: *Sparky. That's perfect. Print the number two housing at the new tolerance, you're overthinking it.* Nick was, annoyingly, usually right.

Maureen added two items to his list. He fixed them without comment. Saul left a note on one of them: *good catch.* Three words. Jace saved it.

The animals were fine. The pigs were up to something. The geese filed a formal complaint about Tuesday.

That night he dreamed about crystals.

Not a nightmare — nothing chasing him, nothing wrong. Just a cave somewhere vast and cold and impossibly lit, walls faceted like the inside of a geode but on a scale that swallowed him whole. The light came from inside the crystal itself, blue-white, humming just below hearing. He was moving through it — not walking, more like drifting — and the ship was gone and the animals were gone and there was just the cold and the light and the feeling that the walls went on forever.

He woke up at 0400. His rebreather seal was tight against his face. Cerberus was standing on his chest, staring at him.

He lay there for a minute. The dream was already dissolving — he could feel it going, the way water drains. Just the light left. Blue-white, fading.

He slept again. In the morning he couldn't remember it clearly. Just the sense of vast cold space that wasn't space, and the feeling — strange and specific — of flying out through the hull of the ship into something that had no name yet.

---

# Day 3

He woke to an alarm.

Not his alarm. The ship.

---

*[SCENE CONTINUES — Book 1 plumbing crisis / near-drowning event. See book01-ch02-plumbing-crisis.md — NOTE: that file's "Sparky's sensor core" beat requires the staged patch (prototype board, not operational drone).]*
