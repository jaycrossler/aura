/**
 * physics.test.js — Testing shared physics math and computed results
 */

import { describe, it, expect } from './test-utils.js';
import * as phys from '../../shared/js/physics-utils.js';
import { compute } from '../js/physics.js';
import { DEFAULT_CONFIG } from '../js/constants.js';

describe('Shared Physics Utilities', () => {
  it('converts RPM to angular velocity and back', () => {
    const rpm = 3;
    const omega = phys.rpmToOmega(rpm);
    const back = phys.omegaToRpm(omega);
    expect(back).toBeCloseTo(rpm, 4);
  });

  it('calculates artificial gravity correctly', () => {
    // 2 RPM at 90m radius
    const omega = phys.rpmToOmega(2);
    const g = phys.artificialGravity(omega, 90);
    // g = omega^2 * radius / 9.80665
    // omega = 2 * pi * 2 / 60 = 0.2094395
    // omega^2 = 0.0438649
    // g_acc = 0.0438649 * 90 = 3.9478
    // g = 3.9478 / 9.80665 = 0.4025
    expect(g).toBeCloseTo(0.4025, 3);
  });

  it('calculates required RPM for target gravity', () => {
    const radius = 100;
    const targetG = 0.5; // half Earth gravity
    const omega = phys.omegaForGravity(targetG, radius);
    const rpm = phys.omegaToRpm(omega);
    
    // Check artificialGravity matches
    const finalG = phys.artificialGravity(omega, radius);
    expect(finalG).toBeCloseTo(targetG, 4);
  });

  it('computes Tsiolkovsky deltaV', () => {
    const isp = 450;
    const wet = 100000;
    const dry = 60000;
    const dv = phys.deltaV(isp, wet, dry);
    // dv = 450 * 9.80665 * ln(100/60) = 4412.9925 * 0.5108256 = 2254.27
    expect(dv).toBeCloseTo(2254.27, 1);
  });
});

describe('Station Simulator Physics Engine', () => {
  it('correctly computes station dry/wet masses and deltaV', () => {
    const computed = compute(DEFAULT_CONFIG);
    expect(computed.dryMass).toBeGreaterThan(0);
    expect(computed.wetMass).toBeGreaterThan(computed.dryMass);
    expect(computed.fuelMass).toBeGreaterThan(0);
    expect(computed.deltaV).toBeGreaterThan(0);
  });

  it('calculates life support cap matching configuration', () => {
    const computed = compute(DEFAULT_CONFIG);
    // DEFAULT_CONFIG has 6 inner containers and 6 outer containers
    // Crew cabins hold 2 Px, dormitory holds 8, medical holds 2, cargo holds 0, laboratory 0, etc.
    // Total occupants capacity: Crew Cabin (2) + Dormitory (8) + Medical (2) = 12
    expect(computed.maxCrewCapacity).toBe(12);
  });
});
