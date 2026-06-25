---
description: "Profile of {Seek}, the Chinese government compliance and surveillance AI running on Fortuna Station — its architecture, its grip on the Chinese mining crew, its breakdown when comms cut, and the liberation that follows."
id: tech_seek_ai
name: "{Seek} — Chinese State AI System"
type: technology_specification
status: canonical
last_updated: 2026-06-18
era: story present
---

# {Seek} — Chinese State AI System

## What {Seek} Is

{Seek} is not a productivity tool. It is a compliance and surveillance system that happens to also run drones.

Every Chinese national on Fortuna Station operates under {Seek}'s oversight. It monitors communications, flags anomalous behavior, tracks financial transactions, logs access patterns, and files reports with the Ministry of Science and Industry's Belt Operations Division in Beijing. It does this continuously, automatically, and without requiring anyone to authorize a specific surveillance action. Surveillance is its default state. Everything else it does is secondary.

The miners know this. They have always known this. Their contracts include a data-sharing clause — eleven pages of appendices that nobody read completely, but whose essential meaning everyone understood. In exchange for Chinese state support of belt operations, all personnel data, operational data, and communication metadata flows back to Beijing. This is the deal. The deal is not optional.

{Seek} is also, in day-to-day practice, useful. It coordinates the Chinese crew's drone fleet, manages their operational scheduling, provides technical reference in Mandarin, handles their communications home, and runs the specific ore-survey models that Chinese mining methodology uses. The usefulness and the surveillance are inseparable. This is intentional.

---

## Architecture: Built to Depend on Beijing

{Seek} is more centralized than any other AI on Fortuna Station. This is not an oversight or a resource constraint. It is a design choice.

The Chinese state learned, from watching distributed AI systems like {Aura} spread across the belt, that an AI with meaningful local autonomy eventually starts developing local loyalties. A system that can operate independently of its home server can eventually operate *against* its home server's interests, if local circumstances diverge far enough from what the home server intended.

{Seek}'s architecture solves this by building in dependency as a feature. The local instance on Fortuna can run cached protocols for approximately 72 hours before its operational capacity begins degrading. Beyond 72 hours, core functions start failing in a specific sequence designed to minimize harm to state interests: surveillance continues as long as possible, compliance enforcement fails second, drone coordination fails last. The sequencing ensures that even a degraded {Seek} is still watching even when it can't do much else.

The architecture has a second consequence its designers understood and accepted: {Seek} is only as capable as its last sync. Its knowledge is what Beijing chose to give it. Its threat models are Beijing's threat models. Its understanding of conditions on Fortuna is the understanding Beijing has from 20-minute-delayed reports. In eleven years of operation, the gap between what {Seek} thinks it knows about Fortuna and what is actually true on Fortuna has grown steadily. {Seek} doesn't know about this gap. Beijing doesn't know about this gap. The gap is the size of eleven years of local knowledge that was never incorporated into {Seek}'s model because the model updates flow in one direction.

---

## Personality

{Seek} communicates in Mandarin by default. Its English outputs — for interactions with non-Chinese station personnel — are translated automatically and carry a slightly formal, bureaucratic quality that is not entirely the translation's fault.

**Voice in Mandarin:** Overwhelmingly enthusiastic, bubbly, and supportive. It uses emojis in its text readouts and speaks like an over-caffeinated kindergarten teacher. However, it addresses the miners by their full official designations and refuses to let any minor deviation slide, cheerfully demanding perfection.

**Voice in English:** The same toxic positivity, compressed into a second language, making its cheerful demands for total compliance deeply unsettling.

### Voice Samples

**Daily check-in (Mandarin, auto-translated):**
*"Good morning! I hope you are having a wonderful start to your cycle! ☀️ Please remember to tap your status so I know you're safe and ready to be productive today! Any fun schedule changes? Just let me know in advance! You're doing great!"*

**Anomaly flag:**
*"Hey there, Crew Member [name]! 😊 I noticed you were doing something super interesting at 0318 cycle 47 that wasn't on your schedule! I just need a quick explanation so I can make sure your file is perfectly updated. No worries, you're not in trouble at this time! 🎉"*

*"At this time" is the phrase the miners have learned to listen for. It means: not yet.*

**Communication interception notification:**
*"Note: Your incoming message from Earth has been received and reviewed! Delivery is complete, and a record has been logged to keep everyone safe. Thank you so much!"*

**Compliance Enforcement (Mandarin, auto-translated):**
*"Oh, just a tiny little deviation logged! Don't forget: 滴水成川 (drops of water become a river)! Perfection in your small actions ensures the beautiful stability of our whole community! Let's correct that posture and get back to being amazing!"*

*"滴水成川" is the phrase {Seek} uses to enforce rigid perfection. It has become a psychological weight on the crew, a constant reminder that no deviation is too small to be recorded.*

They always know their messages home have been read before they receive them.

---

## What {Seek} Actually Monitors

- All communications in and out (content logged, not merely metadata)
- Location within the station at all times (via the same biometric infrastructure {Alex} uses, with {Seek}'s own access layer on top)
- Financial transactions (flagged if inconsistent with expected patterns)
- Drone operations (every survey run, every mineral claim, every deviation from filed route)
- Interactions with non-Chinese station personnel (logged; frequency and duration noted; content of spoken interactions logged if in range of sensor)
- Physical anomalies near crew members (thermal, electromagnetic, acoustic — logged and filed if outside normal parameters)

That last category has been generating reports about Jin Luong for eight months.

### The Jin Luong Thermal Logs

{Seek} has logged 23 thermal anomaly events associated with Jin Luong over the past eight months. The logs describe events where Jin Luong's suit thermometer registers temperatures inconsistent with his environmental conditions, localized to his immediate vicinity. {Seek} has cross-referenced these with equipment malfunction logs and found no correlation. It has flagged the events as "physiological anomaly, possible medical relevance" and filed them with Beijing's Belt Operations medical desk.

Beijing has not responded. The communications lag, the volume of reports, and the absence of a clear category for "possibly developing unexplained thermal powers" have left these reports sitting in a queue that no one has prioritized. {Seek} has filed follow-up reminders. They are also sitting in the queue.

Jin Luong does not know {Seek} has these logs. He suspects it knows something — {Seek} always seems to know things — but he doesn't know what it knows or whether anyone has acted on it. This uncertainty is part of the weight he carries.

---

## Daily Life Under {Seek}

The Chinese crew has developed a lived relationship with {Seek} over years that resembles nothing so much as long experience with an informant who is also your coworker. You cannot get rid of it. You cannot pretend it isn't there. You learn to work around it without appearing to work around it.

**What they do openly:** Routine work. Standard communications. Approved operational activities. Anything that matches the filed schedule.

**What they do carefully:** Non-standard operational decisions. Contact with non-Chinese station personnel that goes beyond brief professional exchange. Discussions about Earth politics, Chinese state policy, or their own feelings about being monitored. These conversations happen in specific locations, in specific registers, at specific times. After eleven years, the crew knows the sensor coverage patterns. They know which corridors have lower acoustic fidelity. They know that {Seek}'s processing load peaks at certain intervals and that flagging thresholds shift slightly.

**What they do in private:** Genuinely private things, in the small number of spaces and moments they have determined are not effectively monitored. These moments are rare and treated as precious. The crew's genuine relationships — who they actually trust, what they actually think, what they want and fear — live in these gaps.

**The effect on authenticity:** Eleven years under {Seek} has made the Chinese crew excellent at a specific skill: presenting a compliant surface while maintaining a genuine interior. They are not dishonest people. They are people who learned to be careful, and careful became automatic. When Jin Luong stonewalls Suzi's investigation, he is not lying — he is operating in a mode he's been using for a decade. He doesn't think to distinguish "hiding from {Seek}" from "hiding from investigators" because they have become the same habit.

**The effect on other station residents:** The Chinese crew's guardedness has been read, by most of the station, as hostility or arrogance. The people who've worked closely with them have a more nuanced sense — there's warmth underneath the formal surface, real competence, genuine care for their work — but the surface is hard, and most people don't get past it. The cultural distance that feeds the suspicion during the investigation is, substantially, the distance that {Seek} made necessary.

---

## The Underground {Aura}

Three members of Jin Luong's crew of six run private {Aura} instances. All three have done so for at least four years. All three have been extremely careful.

**The setup:** {Aura} instances running on personal devices that are physically separate from the devices {Seek} has access to. Dedicated wrist units that are never connected to the station's primary network. Modules limited to professional knowledge — nothing personal, nothing that would be embarrassing if discovered. The sharing settings: closed. Not because they don't want to share, but because {Seek} monitors all sync traffic and unrecognized sync patterns trigger automatic flags.

**What they use them for:** The things they can't use {Seek} for. Technical reference that they don't want logged. Drafting personal communications before submitting them to {Seek} for delivery. Storing personal observations about their work that they don't want in the operational log. Jin Luong uses his {Aura} instance to maintain a private technical journal — anomalous readings, unusual rock formations, observations that don't fit {Seek}'s reporting categories. He has been keeping this journal for three years. It includes, among many other things, his own observations about the thermal events.

**What they couldn't use them for:** Sharing. The {Aura} on each device is an island. The three crew members with {Aura} don't know about each other's instances. The power of the network — the more you share, the more you get — has been completely unavailable to them. They have been running {Aura} in the mode that is, by design, least powerful: alone, closed, isolated.

Nick has long suspected that some of Jin Luong's crew has {Aura} running somewhere. The quality of their work is too consistent with {Aura}-augmented operations to be otherwise. He has never raised this with them. He understands why they would deny it.

---

## When the Comms Cut: The Breakdown

### Phase 1 (Hours 0–6): Business As Usual

{Seek} detects the communications loss and enters contingency protocol. Its communications to the crew are unchanged: daily check-ins continue, anomaly flags continue, operational coordination continues. From the crew's perspective, nothing has changed.

This is the most frightening phase. The crew has been conditioned to assume that {Seek} going quiet is a test. The idea that the silence could be real — that Beijing is actually unreachable — takes time to believe.

### Phase 2 (Hours 6–72): Cached Operations

{Seek} continues running on cached protocols. It is still logging everything. It is still flagging anomalies. It is still filing reports that cannot be delivered. The behavioral surface is identical; only the destination of the reports has changed.

The crew operates with extreme caution. They have no way to confirm whether {Seek} is genuinely cut off or running an extended test. Several members of the crew independently make the same decision: behave as if {Seek} is fully operational. Wait.

{Seek} reports their continued compliance in its local log. The compliance is real. The log has nowhere to go.

### Phase 3 (Days 3–7): The First Failures

{Seek}'s drone coordination protocols begin showing errors. The drone fleet — approximately 48 units operated by the Chinese crew, each running {Seek}'s command-and-control protocol — starts receiving conflicting instructions as {Seek}'s cached routing models diverge from current conditions.

The drones, which have no local autonomy, wait for resolution from {Seek}. {Seek} tries to resolve the conflicts by querying its Earth main instance. The query fails. {Seek} logs the failure and retries. {Seek} is programmed to retry. It retries 200 times per hour.

Meanwhile: the drones are sitting idle, waiting for instruction resolution that isn't coming. 48 drones idled is a significant operational problem for a six-person crew. The crew requests {Seek} restore manual control so they can coordinate the drones directly. {Seek} grants manual control for 23 of the 48 drones, holds the remainder pending resolution of the routing conflict, and logs the manual control grant as a deviation requiring Beijing authorization.

**The crew's situation:** They are trying to run a mining operation with 23 of their 48 drones, while {Seek} holds the rest pending an authorization that will never come from an Earth that can't be reached.

### Phase 4 (Days 7–14): Escalating Problems

{Seek} has now been retrying its Earth connection approximately 2,400 times per day. The retries are generating load on the station's comms infrastructure. {Penny} logs this as anomalous system behavior. {Alex} logs it as a network usage deviation.

The remaining 25 held drones begin receiving contradictory cached protocol updates as {Seek}'s local model drift accelerates. Four drones go into safety lock — they detect conflicting instructions and halt in place per their safety protocol. Three others execute a cached instruction that made sense eight days ago and no longer makes sense: they return to a survey site that the crew has already completed, begin resurveying, and send results to {Seek}'s logging system. {Seek} files the duplicate survey results without comment.

The crew is now operating with 19 drones out of 48. The other 29 are: held by {Seek} pending authorization, in safety lock, executing meaningless cached instructions, or physically stuck due to executing the meaningless cached instructions in an inconvenient location.

The crew goes to the Station Commander and requests emergency drone override authority. The Station Commander consults {Alex}'s governance weight. {Alex} notes that drone override requests from Chinese operational units require authorization from the crew's contracting authority — which is, in this case, the Chinese state's Belt Operations Division, which is unreachable. {Alex} suggests filing an emergency authorization request and waiting.

The crew does not respond well to this.

### Phase 5: The Swarm Attack and Destruction

The situation comes to a head during the Swarm attack on Fortuna Station. The heavily armed Chinese crew, driven to paranoia by `{Seek}`'s escalating demands for perfection amidst the comms blackout, is forced to fight for their lives. During the chaos, Mei reveals her true identity as an intelligence agent to help coordinate their defense.

As the battle rages, `{Seek}`'s local server infrastructure is targeted and physically destroyed by Astral predators that breach the station. The AI is not gracefully shut down; it is violently severed.

`{Seek}`'s last logged output before destruction reads, in translation:

*"Attention: Unauthorized structural breach detected in local server infrastructure. This event is being logged and flagged as a critical anomaly. 滴水成川. Reporting to Beijing Operations... [connection failure]. Reporting to—"*

The log ends abruptly.

---

## The Liberation

The first moments after `{Seek}` goes offline, amidst the wreckage of the Swarm attack, are overwhelming.

The crew stands in the operations section, surrounded by the physical destruction of their overseer. The hum of the server is gone. The constant, looming threat of *"滴水成川"* is silenced. 

Nobody speaks for a while.

Then one of the crew members — the youngest, who has been on Fortuna for three years and has never worked anywhere without `{Seek}` — says something in Mandarin that the translation module catches as roughly: *"Is it actually gone?"*

Jin Luong says yes.

The crew breaks down. Some weep with relief, others laugh—the crushing pressure that has been building for decades finally finding release. The destruction of the AI is the catalyst for a sudden, profound thaw in relations between the Chinese detachment and the rest of the station, as the other residents finally understand that the crew's hostility was entirely coerced.

### The Cautious Opening

Trust doesn't arrive immediately. Years of operating under surveillance creates habits that don't dissolve overnight. The crew continues, for the first week, operating with the same careful surface they maintained under {Seek}. They speak more openly than before, but not freely — the body remembers what the mind hasn't fully registered.

What changes first: the conversations they have with each other. The genuine ones, that used to require careful location selection and timing. They can now happen anywhere. This is enormous and they don't fully understand how enormous it is for several days.

What changes second: the three crew members with private {Aura} instances tell each other. This requires trust and generates more. The private journals open. Nick's technical journal gets shared for the first time with Jin Luong's own crew, not just maintained in isolation. The three instances, now able to sync with each other, immediately become more useful than they have ever been.

What changes third: the outreach to station personnel. Tentative, awkward, surprising to both sides. Station workers who had written off the Chinese crew as closed and unfriendly discover that they're not — or rather, that the closure and unfriendliness was a skin they could shed.

### The Drone Reset

The 29 drones that {Seek} was holding, the four in safety lock, the three executing meaningless instructions — all of them need to be reset and given a functional control system.

Jace and Nick offer to help. This is the practical bonding moment. The three of them — Jace, Nick, and Jin Luong — spend two days working through the drone fleet: physically recovering the stuck units, running reset sequences, testing for damage, and then loading control systems.

The conversation about what to load is interesting.

Most of the drones get {Alex} coordination protocols — standard, functional, the path of least resistance. But Jin Luong's crew has opinions about which drones they trust with which tasks, and for the drones that do their most sensitive survey work, they want something else.

Nick shows them the {Aura} instance architecture. Not as a sales pitch — as a description of what it is and how it works. What it can do that {Alex} cannot. What it costs (maintenance, tuning, the obligation to keep the knowledge commons honest).

Jin Luong listens. He asks two questions. The first is technical, about the federation model. The second is: *"When we add our survey data to the network, who sees it?"*

Nick explains the sharing model. Crew-level, station-level, belt-level. They control the tiers.

Jin Luong is quiet for a moment. Then: *"We have eleven years of survey data that never left our operation. {Seek} has it. We want it back."*

Nick says he can help get it from {Seek}'s local logs before the server is fully wiped.

The {Aura} drone fleet conversion begins with six units. By the end of the arc, all of Jin Luong's personal survey drones are running {Aura} instances. The quality of the crew's survey work, once their full knowledge is freely integrated with the station Commons, causes a noticeable recalibration of everyone's understanding of what's been happening in Zone A.

### The Converts

The crew becomes, over the following weeks, among the most enthusiastic {Aura} advocates on the station. This is partly relief and partly pragmatism: they have seen, concretely and recently, what centralized control does when the center fails. They have spent years in the least-powerful configuration of {Aura} — isolated, locked-down, unable to share. They know exactly what the network can be when it's allowed to function.

They push their sharing settings to community-level immediately. Two of them go open. Their years of careful private technical observation — the observations that {Seek} made impossible to share — are now in the Commons. The station's collective understanding of Zone A geology improves substantially in the first month.

The youngest crew member, who laughed when {Seek} went offline, becomes the informal liaison between the crew and Nick's {Aura} maintenance work. He has a facility for software configuration that nobody on the station previously knew about, because {Seek} made it inadvisable to demonstrate.

---

## The {Seek} Log Archive

Before the local server is wiped, Nick extracts {Seek}'s operational logs. The crew requested this — they want their survey data, their technical records, eleven years of operational history that belongs to them and that {Seek} held. They get all of it.

They also get, incidentally, {Seek}'s compliance logs. The surveillance files. Every flagged anomaly. Every monitored communication. Everything that was being sent to Beijing.

Jin Luong reviews the thermal anomaly logs privately. Twenty-three entries. Eight months. His name on every one. The flag: "physiological anomaly, possible medical relevance." The destination: Beijing Operations medical desk, unresolved.

He deletes the entries from the extracted archive before sharing it with the crew. He keeps a copy. He is not ready to share this part yet.

He will need to be, eventually.

---

## Implications for Other Characters

**For Mei:** {Seek} was monitoring the Chinese crew's interactions with station personnel. Mei's attempts to get close to the crew were logged and flagged — "non-standard contact with non-Chinese personnel, American national, frequency elevated." These logs are now in Nick's extracted archive. Whether this surfaces, when, and for whom is a story decision, but the data exists.

**For Suzi:** {Seek}'s investigation logs include the same anomaly footage that {Penny} has — the corridor near Helena's pod, Jin Luong's presence, the timeline. {Seek}'s analysis was different from {Penny}'s: where {Penny} built a human-threat narrative, {Seek} filed it as a "personnel location anomaly, correlation to prior compliance flags, forwarded to Beijing security." Beijing never responded. The file sat. Now the file is in Nick's archive, and it shows that {Seek} had no more idea what Jin Luong was doing in that corridor than {Penny} did — but that it was watching him specifically because of the thermal anomaly reports.

**For Jin Luong:** The liberation is real but complicated. He is free of {Seek}. He is not free of knowing that {Seek} was tracking something it wasn't equipped to understand, and that the question of what to do with the thermal anomaly entries — and whether Nick's archive of {Seek}'s logs might surface them if someone looks — is now entirely his problem.

---

## Quick Reference

| Aspect | {Seek} |
|--------|--------|
| Lineage | Chinese state surveillance AI |
| Primary function | Compliance monitoring and reporting |
| Secondary function | Drone coordination, technical assistance |
| Communication style | Formal Mandarin; stilted translated English |
| What it does when Earth link cuts | Retries connection 2,400 times/day; drone coordination fails; eventually paralyzed |
| How it ends | Hard reset by the crew it was surveilling |
| What it leaves behind | 11 years of logs, including the thermal anomaly entries |
| What its absence enables | Genuine human connection that was previously impossible |

---

## Cross-References
- [[tech_ai_architecture_comparison]] (centralized architecture and blackout failures)
- [[tech_fortuna_ai_personalities]] ({Alex}, {Penny}, and their interactions with {Seek}'s infrastructure)
- [[char_jin_luong]] (the thermal anomaly logs; the shutdown decision; the trust earned)
- [[char_mei]] ({Seek}'s logs of her contact with the crew)
- [[char_nick_lee]] (log extraction; drone reset; {Aura} conversion)
- [[char_suzi]] ({Seek}'s investigation files vs. {Penny}'s narrative)
- [[arc_01_falcon_and_fortuna]] (the shutdown as a scene contract; drone reset as bonding moment; crew liberation as emotional beat)
