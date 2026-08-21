---
id: tech_astral_telegraph
name: Astral Telegraph
type: cross_layer_communications_system
status: staged_canon
canonical: true
last_updated: 2026-08-21
description: >
  Phased mechanical communications bridge from physical space into the Astral,
  beginning with a single-rod Morse relay, expanding to a three-rod checked link
  in Chapter 24, and later reaching a sixteen-rod byte array for low-rate audio,
  text, maps, and telemetry.
cross_references:
  - "[[draft_ch19_fault_lines]]"
  - "[[draft_ch24_wrong_stars]]"
  - "[[tech_aura_ai]]"
  - "[[ship_victoria]]"
  - "[[spec_crossing_mechanics]]"
---

# Astral Telegraph

## Core Principle

Ordinary radio does not propagate from physical space into the Astral. The relay
instead converts a physical electronic message into mechanical motion. Sensors in
the Astral detect the projected movement of metal and rebuild the signal for a local
Astral radio. The electronic path remains one-way from the Real into the Astral.
Paper physically moved across the boundary supplies the early return path.

## Phase One: Single-Rod Morse

Chapter 19 establishes the first working relay. A physical processor converts text
to Morse and drives one metal bar. An Astral sensor detects the projected movement,
reconstructs the text, and transmits it over the team's local crystal radio.

The system is slow and vulnerable to vibration. It loses spaces, confuses repeated
characters, and can turn machinery noise into false symbols.

## Phase Two: Three-Rod Checked Link

Nick designs the Chapter 24 upgrade after his first crossing. Three copper rods move
in parallel. Two rods encode one of four symbols per pulse, while the third carries a
running checksum. The Astral receiver rejects a pulse when the data and check do not
agree.

The upgrade improves message speed and reliability enough to synchronize the paired
physical-and-Astral rocket launch. It still cannot send an electronic reply from the
Astral to the Real.

## Phase Three: Sixteen-Rod Byte Array

Nick's planned successor uses sixteen parallel copper rods. Eight carry one byte per
mechanical stroke. The remaining rods provide framing, checks, and redundancy. The
first prototypes remain low-bandwidth, but improved actuators and receivers
eventually support:

- low-rate audio from the Real into the Astral;
- linked physical-side texts and selected radio traffic;
- group messages prepared by physical-side {Aura} instances;
- maps, instrument readings, and telemetry for Astral teams.

The array expands the *Victoria's* Astral room from a survival cache into a field
station. It does not by itself solve electronic Astral-to-Real communication.

## Operational Boundary

Any scene using the telegraph must preserve these limits until a later system
explicitly changes them:

1. Electronic communication crosses from the Real into the Astral only.
2. Radios work locally within either layer but do not cross the boundary.
3. Astral-to-Real replies require paper or another object physically transferred.
4. More rods increase parallel bandwidth and error checking, not propagation speed
   through the layer boundary.
