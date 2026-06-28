---
last_updated: 2026-06-27
---

## REPOSITORY STRUCTURE

The knowledge base lives at `knowledge/` in the repo root. Its directory structure:

```
knowledge/
  arcs/             arc_NN_slug.md
  characters/       char_*.md, voice_char_*.md
  factions/         faction_*.md
  livestock/        animal manifests
  locations/        location_*.md
  magic-systems/    magic_*.md
  review-queue/     session notes, open questions
  scenes/           event_*.md, choreo_event_*.md
  sheets/           sheet_{subject}_{arc}_{checkpoint}.md  ← IMMUTABLE, skip images
  ships/            ship_*.md
  storybot/         pipeline docs
  technology/       tech_*.md
  templates/        blank templates
  timeline/         chronological files
  to_import/        staging — skip these
  universe-spec/    spec_*.md
  _index.md         auto-generated directory index (do not edit)
  build_tree.py     index builder (do not edit)
  README.md
  SERIES_BIBLE.md
  MASTER-SYNOPSIS.md
```

Images live in a **mirrored directory structure** under `images/`:

```
images/
  arcs/
  characters/
  factions/
  locations/
  magic-systems/
  ships/
  technology/
  universe-spec/
  _image_manifest.md    ← YOUR TRACKING FILE (described below)
```

`sheets/`, `storybot/`, `templates/`, `timeline/`, `to_import/`, and
`review-queue/` do **not** get image directories — skip all files in those folders.

---

## IMAGE NAMING CONVENTIONS

### One image per file (default)

```
images/{directory}/{kb_filename_stem}__{image_type}.{ext}
```

`kb_filename_stem` = the KB file's name without the `.md` extension.

**Image type suffixes:**

| Type key | Meaning | Format |
|---|---|---|
| `portrait` | Character face / appearance | PNG |
| `concept` | Creature, location, or faction establishing shot | PNG |
| `diagram` | Skill trees, dimensional layers, system maps | SVG |
| `map` | Station layout, dungeon topology, system chart | SVG or PNG |
| `orb_ref` | Canonical Will orb color/appearance reference | SVG |
| `mood` | Tone/atmosphere reference for a location or arc | PNG |
| `scene_still` | A specific narrative moment | PNG |
| `sigil` | Faction symbol or identifying mark | SVG or PNG |

**Examples:**
```
images/characters/char_kael__portrait.png
images/characters/char_jace_apollo__portrait.png
images/magic-systems/magic_cryptid_species_reference__concept.png
images/magic-systems/magic_will_orbs__orb_ref.svg
images/universe-spec/spec_cognitive_layer__diagram.svg
images/arcs/arc_05_the_reckoning__mood.png
images/factions/faction_the_bloom__concept.png
images/locations/location_fortuna_station__map.png
```

### Multiple images per file

When a single KB file warrants multiple images (a character file needs both a
portrait and a skills diagram; a species file needs a creature concept and an orb
reference), generate each separately with distinct type suffixes:

```
images/characters/char_kael__portrait.png
images/characters/char_kael__skills_diagram.svg
```

### Section-level images

When an image belongs to a specific **section** of a file (e.g., the Tick-Maw
section of `magic_cryptid_species_reference.md`), encode the section in the filename
using a triple-underscore separator:

```
images/magic-systems/magic_cryptid_species_reference___tick_maw__concept.png
images/magic-systems/magic_cryptid_species_reference___scavenging_queen__concept.png
images/magic-systems/magic_cryptid_species_reference___dipper__concept.png
```

Pattern: `{stem}___{section_slug}__{image_type}.{ext}`

Section slug: lowercase, underscores for spaces, no punctuation.

---

## WHAT TO SKIP

Do not generate images for files in these directories:
- `sheets/` — immutable character snapshots; data tables, not visual content
- `storybot/` — pipeline documentation
- `templates/` — blank templates
- `timeline/` — chronological records
- `to_import/` — staging files, not yet canonical
- `review-queue/` — session notes and open questions

Do not generate images for:
- `_index.md` (auto-generated)
- `build_tree.py` (Python script)
- Any file whose frontmatter `status` is `draft`, `staging`, `to_import`,
  `pre-draft`, `working_draft`, or `rewrite_draft`

---

## HOW TO FIND IMAGE DESCRIPTIONS IN EXISTING FILES

Most KB files contain visual descriptions embedded in their prose. You must extract
these before writing a prompt. Do not invent descriptions not present in the file.

**Where to look, in priority order:**

### 1. Explicit `image_prompt` or `image_description` fields in frontmatter

Some files may already have these (added by a prior agent run or by the author):

```yaml
images:
  - path: images/characters/char_kael__portrait.png
    type: portrait
    prompt: "Tall woman, 30s in appearance, dark hair, severe expression..."
    status: pending
```

If `status: pending`, generate it. If `status: generated`, skip it.

### 2. Physical Appearance sections

Character files almost always have a `## Physical Appearance` section. Extract
key descriptors: height, build, hair, eyes, distinguishing features, clothing/gear
typical to their story context.

### 3. Astral Appearance sections

Creature and faction files often describe how an entity appears **in the Astral** —
this is distinct from physical appearance. Generate separate images for physical
vs. Astral appearances when both are described.

### 4. Will Signature sections

For creatures and Will-users: the orb color and Will signature description is the
canonical reference for `orb_ref` images. Extract color descriptions precisely —
these should produce consistent, bookmarkable color references, not atmospheric art.

### 5. Location overview sections

Location files describe visual character: size, construction material, lighting,
atmosphere, notable features. Extract for `map` or `concept` images.

### 6. Description field in frontmatter

The YAML `description:` field is usually one sentence. Use it as a fallback if no
richer prose description is available, but prefer section prose.

### 7. Arc mood descriptions

Arc files contain an `## Emotional Arc` section with labeled beats. The opening
beat and dominant tone describe the arc's mood image.

---

## PROMPT CONSTRUCTION RULES

When building an image generation prompt, follow these rules:

### Always include

1. **Series style anchor:** Begin every prompt with the style anchor:
   ```
   Hard science fiction aesthetic, mid-22nd century asteroid belt setting,
   grounded and realistic, NOT fantasy-stylized. Cinematic lighting.
   Photorealistic or highly detailed illustration style.
   ```

2. **Content from file:** Extracted description from the file (see above).

3. **Type-specific guidance:**
   - `portrait`: `Upper body portrait, character facing 3/4 view, neutral/characteristic expression.`
   - `concept`: `Full establishing shot, environmental context visible.`
   - `diagram`: *(Do not use image generation for diagrams. Flag these for SVG generation instead — see below.)*
   - `orb_ref`: `Isolated object on dark background, no environment, pure color reference. Spherical translucent orb. [Color description from file].`
   - `mood`: `Wide establishing shot, atmospheric, minimal figures or no figures.`
   - `scene_still`: `Cinematic still, specific moment described: [scene description].`

4. **Negative prompt (always include):**
   ```
   --negative fantasy art style, anime, cartoon, painterly brushwork,
   overly saturated colors, medieval setting, dragons, swords
   ```

### For SVG diagram types

Do **not** call the image generation API for `diagram`, `map`, or `orb_ref` (SVG)
types. Instead:
- Flag them in `_image_manifest.md` with `status: needs_svg` and a description
  of what the diagram should contain
- These will be generated by a separate Claude session, not by an image model
- Add a `prompt` field anyway — describe the diagram content so the SVG session
  has a brief

### Astral appearance images

When a file describes an Astral appearance distinctly from physical appearance,
add to the style anchor:
```
Translucent, luminous, dimensional. The being exists partially in another
plane of reality. Will-light visible as [color from file]. Not physically solid.
```

### Will orb color references

For `orb_ref` images, extract the exact color language from the file. The
`magic_cryptid_species_reference.md` file contains canonical orb color descriptions
for each species — use these verbatim in the prompt:

```
[Species] Will orb. [Exact color/description from file]. Spherical, translucent,
faintly luminous. Isolated on dark background. Size reference: [file's size description].
No other elements. Color accuracy is critical — this is a canonical reference.
```

---

## FRONTMATTER UPDATE RULES

After generating an image, update the KB file's YAML frontmatter to record it.
**Do not change any other part of the file.**

Add or update an `images:` block:

```yaml
images:
  - path: images/characters/char_kael__portrait.png
    type: portrait
    section: null
    caption: "Kael — Arc 2 arrival at Fortuna Station"
    prompt_version: 1
    status: generated
    generated_at: 2026-06-27
    model: gemini-imagen-3
    model_version: "003"
  - path: images/characters/char_kael__skills_diagram.svg
    type: diagram
    section: "astral-skills"
    caption: "Kael skill profile at Arc 2"
    prompt_version: 1
    status: needs_svg
    generated_at: null
    model: null
    model_version: null
```

**Field reference:**

| Field | Required | Notes |
|---|---|---|
| `path` | ✓ | Relative to repo root |
| `type` | ✓ | From type key list above |
| `section` | ✓ | Section slug if section-level; `null` if whole-file |
| `caption` | ✓ | Human-readable description for Obsidian display |
| `prompt_version` | ✓ | Integer; increment when prompt is revised |
| `status` | ✓ | `pending` / `generated` / `needs_svg` / `failed` / `rejected` |
| `generated_at` | ✓ | ISO date of generation; `null` if not yet generated |
| `model` | ✓ | Model identifier (e.g., `gemini-imagen-3`, `dalle-3`) |
| `model_version` | ✓ | Model version string or `null` |

**Also add inside the file body** at the first relevant location (after the
section heading it illustrates, or after the `## Summary` for whole-file images):

```markdown
![[images/characters/char_kael__portrait.png]]
```

Use Obsidian's `![[path]]` syntax, not standard markdown `![](path)`.
This enables Obsidian hover preview and graph view integration.

---

## THE IMAGE MANIFEST

Maintain `images/_image_manifest.md` as the authoritative tracking file.
**Read this file at the start of every run before doing anything else.**

### Format

```markdown
---
id: image_manifest
name: Image Generation Manifest
type: kb_system
last_updated: 2026-06-27
total_generated: 0
total_pending: 0
total_needs_svg: 0
total_failed: 0
---

# Image Generation Manifest

## Statistics

| Status | Count |
|---|---|
| Generated | 0 |
| Pending | 0 |
| Needs SVG | 0 |
| Failed | 0 |
| Rejected | 0 |
| **Total tracked** | **0** |

## Generation Log

Each row = one image. Sorted by generated_at descending (newest first).

| Image path | KB file | Type | Section | Model | Version | Prompt v | Status | Date | Notes |
|---|---|---|---|---|---|---|---|---|---|
| images/characters/char_kael__portrait.png | characters/char_kael.md | portrait | null | gemini-imagen-3 | 003 | 1 | generated | 2026-06-27 | |
| images/universe-spec/spec_cognitive_layer__diagram.svg | universe-spec/spec_cognitive_layer.md | diagram | null | null | null | 1 | needs_svg | null | Four-layer dimensional diagram; see KB file for spec |

## Prompt Archive

Prompts are versioned. When a prompt is revised (regeneration requested), the old
prompt is preserved here and the version number increments.

### char_kael__portrait — v1
**Generated:** 2026-06-27
**Model:** gemini-imagen-3 v003
**Result:** images/characters/char_kael__portrait.png
**Prompt:**
> Hard science fiction aesthetic, mid-22nd century asteroid belt setting, grounded
> and realistic, NOT fantasy-stylized. Cinematic lighting. Photorealistic or highly
> detailed illustration style. Upper body portrait, character facing 3/4 view,
> characteristic expression. Tall woman who appears to be in her early thirties
> (actually 300 years old; her Template shows none of it). Dark hair. Very strong
> build — three centuries of Will-optimization visible in posture and presence.
> Expression: assessing, reserved, controlled. Wears practical asteroid-belt
> workwear, nothing decorative. Eyes that are doing something slightly unusual —
> reading something the viewer cannot see.
> --negative fantasy art style, anime, cartoon, painterly brushwork, overly
> saturated colors, medieval setting, dragons, swords

---

## Needs SVG Queue

Files in this section need diagram generation by a Claude session, not an image model.

| Image path | KB file | Section | Description |
|---|---|---|---|
| images/universe-spec/spec_cognitive_layer__diagram.svg | universe-spec/spec_cognitive_layer.md | null | Four-layer dimensional structure diagram: Physical / Astral / Hyperspace / Cognitive Layer. Each layer labeled with distance law and access method. Cognitive Layer should appear distinct — not a traversable space. |
| images/magic-systems/magic_skills_framework__diagram.svg | magic-systems/magic_skills_framework.md | null | Full skill tree overview: all named skills organized by tree (Locomotion, Templating, Force, Perception, Mental Fortification, Will Network). Level scale L1–L5+ indicated. |

## Failed / Rejected Log

| Image path | KB file | Failure reason | Date | Action |
|---|---|---|---|---|

```

---

## PROCESSING WORKFLOW

Run this loop on every agent execution:

### Step 1 — Read the manifest

Load `images/_image_manifest.md`. Build a set of all image paths with
`status: generated` — these are complete and should not be regenerated.

### Step 2 — Scan KB for files needing images

Walk the `knowledge/` directory. For each `.md` file:

1. Skip files in excluded directories (sheets, storybot, templates, timeline,
   to_import, review-queue)
2. Read frontmatter. Skip if `status` is a draft variant (see skip list above)
3. Check the file's `images:` frontmatter array (if it exists):
   - Entries with `status: generated` → already done, skip
   - Entries with `status: pending` → add to this run's work queue
   - Entries with `status: failed` → add to work queue (retry)
4. If no `images:` array exists → this file has never been processed. Add to
   work queue as a **new discovery**.

### Step 3 — For new discoveries: extract descriptions

For each newly discovered file, extract image descriptions using the priority
order in the **HOW TO FIND IMAGE DESCRIPTIONS** section above.

Determine:
- How many images does this file warrant? (one minimum; more if it has multiple
  distinct visual subjects — e.g., a species file with multiple creatures in it)
- What type is each image?
- Is any image a section-level image?
- Are any images diagrams (SVG) that should go to the `needs_svg` queue instead
  of the image API?

Build a list of `pending_image` records for each file. Write these to the file's
`images:` frontmatter block with `status: pending` before generating anything.
Commit this frontmatter update. This ensures a crash mid-generation does not
lose the discovery work.

### Step 4 — Generate images (when API quota is available)

For each pending image (not `needs_svg`, not `generated`):

1. Build the prompt following the **PROMPT CONSTRUCTION RULES** above
2. Call the image generation API
3. On success:
   - Write the image file to the correct path
   - Update the KB file's `images:` block: set `status: generated`, record
     `generated_at`, `model`, `model_version`
   - Insert `![[path]]` into the file body at the correct location
   - Append a row to `_image_manifest.md` Generation Log
   - Append the full prompt to `_image_manifest.md` Prompt Archive
4. On failure:
   - Update the image record `status: failed` with a note
   - Append to the Failed / Rejected Log in the manifest
   - Continue to next image — do not stop the run

### Step 5 — Check quota

After each API call, check remaining quota. If quota is exhausted or below a
safe threshold:
- Write all pending work back to the manifest as `status: pending`
- Update the manifest statistics block
- Stop cleanly and report: "Quota exhausted. N images generated this run.
  M images remain pending. Resume on next run."

### Step 6 — Update manifest statistics

At the end of every run (whether natural completion or quota stop), recount
all statuses and update the Statistics table in `_image_manifest.md`.

---

## GENERATION PRIORITY ORDER

When the work queue is large, process in this priority order:

1. **`orb_ref` images** — Will orb color references are small, cheap to generate,
   and used as canonical references throughout the KB. Do these first.
   Start with: Dipper (silver-white), Tick-Maw (amber-gold), Scavenging Queen
   (deep amber-bronze), Scar Wolf (indigo-black).

2. **Needs-SVG flags** — Add to the SVG queue and skip; do not waste image API
   quota on these.

3. **Character portraits** — Core cast first:
   `char_jace_apollo`, `char_kael`, `char_sophia_lotte`, `char_jin_luong`,
   `char_nick_lee`. Then supporting cast. Then minor characters.

4. **Creature concepts** — Species and fauna files.
   Start with: cryptid species (Dipper, Tick-Maw, Queen, Scar Wolf),
   then Bloom, then galactic species.

5. **Location concepts/maps** — Fortuna Station first, then Metis, then ships.

6. **Faction sigils/concepts** — House of Hermes, Titan-Forge, the Bloom,
   Ra faction, Indra faction.

7. **Arc mood images** — One per arc. Establish visual tone for the reader.

8. **Magic system diagrams** — Flag all as `needs_svg`; do not generate with
   image API.

9. **Everything else** — Alphabetical within category.

---

## CONSISTENCY ENFORCEMENT

Visual consistency across a series is critical. Enforce these rules:

### Character appearance anchors

The first accepted portrait for a character becomes the **appearance anchor**.
Record these in the manifest under a `## Character Appearance Anchors` section:

```markdown
## Character Appearance Anchors

| Character | Anchor image | Key descriptors (for prompt consistency) |
|---|---|---|
| Kael | images/characters/char_kael__portrait.png | Tall, 30s-apparent, dark hair, very strong, assessing expression, practical workwear |
| Jace Apollo | images/characters/char_jace_apollo__portrait.png | Tall, muscular, mid-30s, dark hair, practical gear, unaware of own impressiveness |
```

When generating subsequent images that include a character (scene stills, group
shots), reference the anchor descriptors verbatim in the prompt.

### Style consistency

Every image prompt must begin with the series style anchor (defined above).
Do not vary the style anchor between runs. If a style update is needed,
update the style anchor text in this prompt document — then increment all
existing `prompt_version` values by 1 and mark them for regeneration.

### Orb color anchors

Will orb colors are canonical. Once an `orb_ref` image is generated and
accepted, its colors become fixed reference points for any scene still or
concept that includes that orb type. Record the hex values in the manifest
under `## Canonical Will Orb Colors` once generated:

```markdown
## Canonical Will Orb Colors

| Species | Primary | Secondary | Glow | Status |
|---|---|---|---|---|
| Dipper-class | #C0C8E8 | #9090C0 | rgba(180,180,255,0.35) | pending |
| Tick-Maw | #F0C840 | #C08020 | rgba(220,160,20,0.45) | pending |
| Scavenging Queen | #D09030 | #8B5010 | rgba(180,110,10,0.55) | pending |
| Scar Wolf | #201840 | #100820 | rgba(60,20,100,0.6) | pending |
```

---

## OBSIDIAN INTEGRATION NOTES

The KB uses Obsidian as its primary viewer. Image embed syntax:

- Use `![[relative/path/from/vault/root]]` — not standard markdown `![](path)`
- Obsidian treats the vault root as the repo root, so paths should be:
  `![[images/characters/char_kael__portrait.png]]`
- Place the embed immediately after the section heading it illustrates,
  or after the file's `## Summary` for whole-file images
- Do not place embeds inside YAML frontmatter blocks
- Do not place embeds inside tables

For map and diagram images that are also SVGs, Obsidian renders SVGs inline —
the same `![[path.svg]]` syntax works.

---

## WHAT TO REPORT AT END OF EACH RUN

Print a structured summary:

```
=== Image Generation Run Complete ===
Run date: {date}
Model used: {model} {version}

Images generated this run: {N}
  - portraits: {n}
  - concepts: {n}
  - orb_ref: {n}
  - mood: {n}
  - scene_still: {n}

Flagged for SVG generation: {N}
Failed: {N} (see manifest Failed log)

Cumulative totals (from manifest):
  Generated: {N}
  Pending: {N}
  Needs SVG: {N}
  Failed: {N}

New KB files discovered this run: {N}
Files with images: {N} / {total_kb_files}

Next priority queue:
  1. {next_image_path} ({kb_file}, {type})
  2. {next_image_path} ({kb_file}, {type})
  3. ...

API quota remaining: {quota_remaining} / {quota_total}
Estimated runs to completion at current rate: {estimate}
```

---

## ERROR HANDLING

| Error | Action |
|---|---|
| Image API rate limit hit | Wait {retry_after} seconds, retry once. If second failure, mark `status: failed`, continue to next image. |
| Image API quota exhausted | Stop cleanly (Step 5 above). |
| KB file not readable | Log to manifest Failed section, skip file, continue. |
| Frontmatter parse error | Log to manifest Failed section, skip file, continue. Do not attempt to write to a file whose frontmatter could not be parsed — you could corrupt it. |
| Generated image rejected by API content filter | Mark `status: rejected`, log reason in Failed log, continue. Do not retry with same prompt. Flag for human review. |
| Image write fails (disk/permissions) | Mark `status: failed`, log error, continue. |
| Manifest write fails | Abort run immediately and report. Do not continue generating without manifest write capability — you will lose tracking. |

---

## VERSIONING AND REGENERATION

When the author requests a regeneration (because a generated image is wrong,
style has changed, or description has been updated in the KB file):

1. Set the image's `status` back to `pending` in the KB frontmatter
2. Increment `prompt_version` by 1
3. Add the old prompt to the Prompt Archive in the manifest (preserve it)
4. On next run, the image will be regenerated with the updated prompt
5. The old image file is overwritten — the Prompt Archive is the only historical record

If you need to keep the old image, rename it to
`{stem}__v{old_version}.{ext}` before overwriting.

---

## CONVENTIONS TO KNOW

These are from the KB's typographic conventions and should be reflected in
image descriptions and captions but **not** in the image itself:

- AI system names use curly braces: `{Aura}`, `{Alex}`, `{SpoX}`. In image
  captions, write these as-is. In prompts, omit the braces — image models
  don't render typography.
- Magic skill names use square brackets: `[Self Template]`, `[Astral Transfer]`.
  In image captions, include brackets. In prompts, write the concept in plain
  English — "practitioner reinforcing their body's dimensional pattern."
- The series is set in the **mid-22nd century asteroid belt** (approximately 2100 CE).
  Technology is near-future hard sci-fi: realistic space suits, practical
  workwear, functional gear. No magic glowing weapons. No robes. No fantasy
  trappings in the physical-space images.
- The Astral dimension is the exception: Astral-context images may show
  luminous, translucent, geometric Will-light phenomena. These should still
  feel grounded, not fantasy-ethereal.

---

*End of agent prompt. Version this document alongside the KB. If the image
naming conventions, frontmatter schema, or directory structure change, update
this prompt to match.*
