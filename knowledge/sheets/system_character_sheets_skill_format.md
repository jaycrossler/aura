---
id: system_character_sheets_skill_format
name: Character Sheet Skill Format — Design Spec
type: kb_system
status: canonical
canonical: true
last_updated: 2026-06-27
description: >
  Defines the skill category system used in character progression sheets:
  Astral Skills, Physical Attributes, Trained Skills, Companions & Bonds,
  Traumas & Burdens, and Resources & Constraints. Draws on GURPS, FATE,
  Blades in the Dark, and Ironsworn for structural inspiration, adapted
  for the Aura Chronicles' physics-first worldbuilding and web-novel pacing.
cross_references:
  - "[[system_character_sheets]]"
  - "[[magic_skills_framework]]"
---

# Character Sheet Skill Format — Design Spec

## Design Principles

The sheet system must serve three purposes simultaneously:
1. **Continuity anchor** — freeze state for consistency checking and resurrection
2. **Progression legibility** — reader and author can track where a character is
3. **Drama surface** — the sheet reveals what a character can do and what limits them;
   both matter equally

The balance of reference games consulted:
- **GURPS** — granular skill lists; the "what can you do" axis
- **FATE** — aspects as compressed character truth; the "who are you" axis
- **Blades in the Dark** — trauma and stress as visible burdens; the "what cost" axis
- **Ironsworn** — bonds and vows as progression units; the "what do you owe" axis

The sheet format keeps these categories readable at a glance, avoids numeric
inflation, and makes the most important things (Astral Skills, Traumas,
Relationships) the most prominent.

---

## Skill Categories

### 1. Astral Skills
Named [Skill] entries with level, acquisition method, and current capability.
All bracketed skills appear here. Unknown/unconscious skills (e.g. [Mind Wall]
for all Sol humans) are listed in italics with a "(passive/unconscious)" tag.

Format:
```
| [Skill Name] | L# | How acquired | Current capability summary |
```

### 2. Physical Attributes
What the body can do. Not a stat array — a small set of descriptive ratings
in the categories that matter for this character. Uses a five-step scale:
**Minimal / Developing / Capable / Strong / Exceptional**

Categories used:
- **Strength / Endurance** — raw physical capacity, load-bearing, fatigue threshold
- **Coordination / Reflexes** — precision, fast response, fine motor work
- **Pain tolerance / Will to continue** — how far they push through damage
- **Combat readiness** — trained or untrained for physical fighting; experience level

### 3. Trained Skills
Mundane expertise, professional knowledge, and acquired competencies.
These are not magic but are equally load-bearing for the story.

Format: list of skill + brief descriptor. No numeric levels — descriptive tiers:
*Novice / Competent / Expert / Master*

Examples: Drone Operations (Expert), Structural Engineering (Expert),
Xenobiology (Novice — developing), Astrophysics (Master — Sophia)

### 4. Companions & Bonds
Named relationships that affect capability. Includes familiars, crew partnerships,
equipment bonds, and significant Will-linked relationships. Each bond has a
strength rating and notes on what the bond enables.

Strength scale: **Nascent / Forming / Established / Deep / Unbreakable**

### 5. Traumas & Burdens
Inspired by Blades in the Dark's trauma clock. Each trauma is a named condition
acquired through story events, with a brief description of what it costs the
character. Traumas are permanent unless addressed through story events.

Format: **[Trauma Name]** — acquired when, what it does, current status.

Examples:
- **[Alone in the Dark]** — Sophia, month of solo crossings; hyper-vigilance in
  Astral environments she can't immediately exit
- **[The Drop]** — character realizes how close they came to dying; manifests as
  hesitation before Astral commitment

### 6. Resources & Constraints
The material and structural facts of this character's life. Not skills — context.
Debt, contracts, equipment owned, ongoing obligations, faction relationships.

---

## Sheet Length Target

A completed character sheet should be readable in under five minutes. If it runs
long, the Trained Skills section is usually the culprit — keep descriptions tight.

## Revision Notes

- 2026-06-27: New file. Skill category system designed and documented.
