---
id: voice_char_jace_apollo
character_ref: char_jace_apollo
type: character_voice_profile
status: detailed (POV character; drafted from Ch01-20)
last_updated: 2026-08-15
description: "Vocal, narration, and speech-pattern profile for Jace Apollo Grant, the Book 1 POV character, formatted for local TTS audiobook generation (Orpheus, Kokoro, Chatterbox). Supersedes the older freeform-bracket voice notes referenced by storybot_orpheus_voice_tag_reference.md, which pointed at a file that does not exist in the current repo."
storybot_extrapolation_allowed: true
cross_references:
  - "[[char_jace_apollo]]"
  - "[[visual_profile_jace_apollo]]"
  - "[[storybot_orpheus_voice_tag_reference]]"
  - "[[spec_audiobook_narration_style]]"
open_flags:
  - "char_jace_apollo.md is currently a nine-line stub that describes Jace as the Falcon's pilot and captain. That contradicts every drafted chapter, in which he is an Origin courier contractor riding as a passenger. This voice profile is built from the chapter drafts and the arc files, not from the stub. Rebuilding char_jace_apollo.md is Priority 0 in review_2026-08-14_chapters_00_20_contract_reconciliation.md and remains open."
  - "storybot_orpheus_voice_tag_reference.md cross-references [[voice_char_jace_apollo]] and describes it as an earlier file using freeform bracket tags. No such file exists in the repo. Either it was deleted or it was never committed. This file is written as its replacement, in the current Orpheus-compatible format. Confirm before assuming any earlier version needs merging."
---

# Character Voice Profile — Jace Apollo Grant

Jace is the POV character for the overwhelming majority of Book 1. That makes
this profile carry two jobs that the other voice files do not: his **spoken
dialogue voice**, and the **narration register** the audiobook lives inside for
roughly nineteen of twenty-one chapters. If the narrator and Jace's dialogue are
cast as two different voices, the book will feel wrong in a way listeners will
not be able to name. See `spec_audiobook_narration_style.md` for the house
narration rules this profile has to sit inside.

## Vocal Characteristics

### Audio Profile
- **Voice type:** Baritone, mid-to-low, unforced. He is 6'1" and physically
  capable, and the voice should carry that without being performed as "tough."
- **Accent:** General American with a light Virginia softening. Present in
  vowel length rather than in any marked drawl. It should be audibly the same
  origin as Artemis's accent (see `voice_char_sister_artemis.md`), but less worn
  down. She has had years of belt work on hers; his still has transit cushioning.
- **Pitch:** Medium-low, narrow working range. He does not use pitch to signal
  emotion. When he is upset the pitch stays put and the pacing changes.
- **Speech rate:** Moderate, with a distinctive habit of accelerating into
  technical explanation and then stopping dead when he realizes he is doing it.
- **Volume:** Moderate. Drops rather than rises under stress. In the plumbing
  crisis and the Chapter 17 escape he gets quieter and more procedural.
- **Resonance:** Chest-forward, some warmth, no polish. Not a broadcast voice.
- **Distinctive features:** Answers questions with a diagnosis rather than a
  feeling. Asked how he is, he reports a system state. This is the single most
  castable thing about him and it should survive into the narration.

**Casting note:** A capable, dry, unshowy adult male voice that can hold long
stretches of interior technical narration without becoming monotonous, and can
land a deadpan joke without signalling it. The trap to avoid is a "heroic
audiobook protagonist" read. Jace is competent and frequently wrong, and the
voice should leave room for the second half of that.

### Vocal Variations by Emotional State

**Default (working / diagnostic):**
- Even, unhurried, slightly clipped. Sentence fragments when he is thinking.
- The register of someone narrating a repair to himself.

**Deflecting (his most common defensive mode):**
- A joke arrives a half-beat early, delivered flat, and the subject changes.
- Do not let the performance signal that the joke is a defense. The reader
  should notice it; the voice should not admit it.

**Under real stress (Ch04 crisis, Ch17 escape, Ch20 rescue):**
- Quieter, shorter, more procedural. Numbers and checklists.
- Any panic lives in the gaps between sentences, not in the sentences.

**With Cerberus:**
- The warmest register he has, and the only one with unguarded affection in it.
- Higher, faster, sillier. He talks to the dog the way he talks to no person.
  This contrast is load-bearing across the whole book.

**With Artemis:**
- Sibling shorthand, faster, more teasing, more willing to be irritated.
  He is more openly emotional with her than with anyone else human.

**With Sophia (post-Ch13):**
- Increasingly collaborative. He finishes her practical sentences and she
  finishes his theoretical ones. By Ch15-16 this should be audibly comfortable.

**Caught out (Nick, Ch17; Kim, Ch16 and Ch18):**
- Stops deflecting and goes flat and short. He does not argue well when he
  knows he is wrong; he goes quiet and takes it. Do not add defensiveness.

## Speech Patterns

### Verbal Tics and Habits
- Restates a problem before solving it, out loud, as a way of thinking.
- Uses "okay" as a reset token between phases of a task, not as agreement.
- Undersells: "that's not great" for a serious failure.
- Rarely finishes a sentence about his own feelings. He starts one, then
  redirects to the mechanism.

### Vocabulary Range
- **Technical:** Deep and fluent in mechanical, thermal, propulsion, drone
  operations, and fabrication. He reaches for engineering analogies for
  non-engineering things and is aware it is a tell.
- **Military residue:** Present but not performed. Procedural cadence under
  pressure, chain-of-custody instincts, threat scanning. He does not use
  service jargon socially.
- **Emotional:** Thin by choice. When it does arrive it is plain and short,
  and should be delivered without added weight.
- **Casual/gamer:** Extensive with Nick specifically; almost absent elsewhere.

### Relationship-Specific Speech

| With | Register |
|---|---|
| Cerberus | Warmest, silliest, highest. The tell that the rest is armor. |
| Nick | Fastest, funniest, most callback-dense. Accent-free, shorthand-heavy. |
| Sophia | Collaborative, curious, increasingly unguarded from Ch15 on. |
| Artemis | Sibling teasing over real affection; more openly annoyed than anywhere else. |
| Maureen | Respectful, shorter sentences, closer to a subordinate register. |
| Lanchee | Compliant and slightly sheepish. She is one of the few people who flatly beats him. |
| Kim | Professional, and after Ch16 audibly on the back foot. |
| Carlos | Easy, warm, unguarded in a low-stakes way. |
| {Alex} | Curt. He talks to {Alex} the way people talk to an automated phone system. |
| {Aura} (post-Ch18) | Noticeably different from how he talks to {Alex}. Conversational, occasionally thinking out loud. This contrast is a deliberate story signal. |

## Internal Monologue Style

This is the majority of the audiobook. Rules:

- **Free indirect style, close third.** The narration is already coloured by
  him. The reader should not switch voices between narration and his dialogue.
- **Diagnostic, not lyrical.** He notices load paths, failure modes, tolerances,
  and what a thing costs. Landscape gets described by what it is made of.
- **Humor lives in the narration, delivered straight.** The chapter epigraphs
  attributed to "Jace Grant, unpublished notes" are the purest sample of his
  written voice: wry, self-deprecating, structurally deadpan. Read them as if
  he thinks they are informative rather than funny.
- **Feelings arrive late and short.** When a paragraph of technical observation
  ends in one plain emotional sentence, that sentence is the point. Slow down
  slightly for it. Do not add tremor.

## Example Dialogue Anchors

- *"The procedures are already authorized. I encoded them."* (Ch16, to Kim)
- *"Who reviewed it?" / "I did."* (Ch16 — the flat admission that he knows is bad)
- *"I'm Jace."* (Ch13, correcting "the delivery boy")
- *"Former military officer. Engineer. Current Origin support. So, uh, 'Delivery man' would be more accurate. And dog."* (Ch13 — the self-deprecating downgrade in real time)
- *"Cerberus. And also real. I have half an hour of oxygen left."* (Ch13 — wonder and a hard operational fact in the same breath; do not let the second half sound like an afterthought)
- *"He does not vote."* (Ch15, deadpan)
- *(epigraph register, Ch15)* *"Most people do not know this, but entering another dimension on purpose begins like most bad decisions. Dinner. One glass of wine. Then someone asks whether you want to go back to their place."*
- *(epigraph register, Ch16)* *"Most people do not know this, but the first settlement in another dimension was one folding stool, a cold thermometer, and a paper sign that said LAB."*

## Speech-Affecting Conditions

- **Rebreather / Astral mask:** Present for most crossing scenes from Ch12 on.
  Slight muffling and audible breath cycles. Do not overdo it; the drafts treat
  the mask as routine equipment, not as an effect.
- **Suit comms:** Thinner band, slight compression, no reverb tail.
- **HUD subvocalization:** When addressing {Alex} or {Aura} silently, quieter and
  flatter, closer to the narration register than to his spoken voice.
- **Exhaustion (Ch16 into Ch17):** Slower, longer gaps, fewer jokes. The
  withdrawal of humor is how the drafts signal his decline. Preserve it.
- **Blood loss (Ch06 forearm; Ch20 wound):** Shorter sentences, more pauses,
  no dramatization.

## Local TTS Engine Notes

These sections exist because this production targets several local models with
different control surfaces. Nothing below is canon; it is production guidance
that a pipeline operator should verify against the model version actually
installed.

### Orpheus
| Story tone | Orpheus rendering |
|---|---|
| default / diagnostic | No inline tags |
| with Cerberus | `<chuckle>` sparingly; his warmth is in pace and pitch, not vocalizations |
| deflecting joke | No tag. Tagging it tells the listener it is a defense, which the prose deliberately does not |
| exhaustion (Ch16-17) | `<sigh>` is appropriate at most twice per chapter, and never before a joke |
| pain (Ch06, Ch20) | `<groan>` only where the prose describes an audible sound; otherwise silence |
| wonder (Ch12-13, first crossings) | `<gasp>` at most once in the whole sequence, in Ch12. Overuse destroys the "engineer looking at an impossible thing and reaching for a measurement" effect |

Base speaker: pick the flattest, lowest-affect male base voice available and
steer with the casting note. Avoid any base speaker with a naturally bright or
smiling placement.

### Kokoro
- Suggested starting voice: an American male pack in the `am_*` family with a
  low, even delivery. `am_michael` and `am_eric` are reasonable first tries;
  audition against the Ch16 epigraph, which exposes any tendency to sing.
- Kokoro has no emotion control, so **all** of Jace's emotional range has to be
  produced by segmentation and speed rather than by tags. Practical approach:
  narration at baseline speed; drop speed roughly 10 percent for the plain
  emotional sentences flagged above; raise it slightly for Cerberus dialogue.
- Kokoro voices can be blended as weighted vectors. If a single pack reads too
  young, a blend weighted toward the lower pack usually fixes it faster than
  changing speed.
- Kokoro will mispronounce the invented proper nouns. Build a lexicon entry set
  for at least: Cerberus, Fortuna, Adama, Astral, Never-Never, Lóng, Lanchee,
  Petroski, Nikos Petrou, Colmar, Trittenheimer.

### Chatterbox
- Reference clip brief, roughly 12 to 20 seconds: an adult American man
  explaining a mechanical failure calmly to someone who is not panicking.
  Conversational, no projection, no smile.
- `exaggeration` low. Jace's whole characterization is affect suppression, and
  Chatterbox's expressivity control will fight that setting if pushed.
- `cfg_weight` moderate, biased toward adherence, so the pacing stays flat
  through long technical passages.
- Because Chatterbox drifts over long generations, chunk on scene breaks rather
  than on chapter breaks and re-seed the reference each chunk.

### All engines
Jace narrates about ninety percent of this book. Whatever voice is chosen, run
a full Ch16 pass before committing, because that chapter contains the widest
spread he has: comedy with Kim, warmth with Cerberus, technical density in the
foundry, and a flat dread ending on {Penny}'s message.

## Revision Notes

- 2026-08-15: Initial file in this format. Built from `draft_ch13`, `draft_ch15`,
  `draft_ch16`, the chapter epigraphs, `arc_01_falcon_and_fortuna.md`, and
  `visual_profile_jace_apollo.md`. Written as the replacement for the
  `voice_char_jace_apollo` file that `storybot_orpheus_voice_tag_reference.md`
  references but which is not present in the repo. Not reconciled against
  `char_jace_apollo.md`, which is a contradictory stub pending rebuild.
