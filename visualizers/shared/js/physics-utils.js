/**
 * physics-utils.js — Shared physics / math utilities
 * Aura Visualizers shared library
 *
 * All functions are pure (no side-effects) so they are trivially testable.
 * Export style: named ES module exports.
 */

// ── Physical Constants ────────────────────────────────────────
export const G0         = 9.80665;   // standard gravity, m/s²
export const STEEL_DENSITY   = 7850; // kg/m³, mild steel
export const STEEL_YIELD_MPA = 250;  // MPa, mild steel yield strength
export const STEEL_E_GPA     = 200;  // GPa, Young's modulus
export const AIR_GAMMA  = 1.4;       // ratio of specific heats for air
export const AIR_R      = 287.0;     // J/(kg·K), specific gas constant for air
export const AIR_TEMP_K = 293.0;     // K, 20 °C cabin temperature
export const AIR_P_PA   = 101_325;   // Pa, standard atmospheric pressure
export const AIR_RHO    = 1.204;     // kg/m³, air density at 20 °C, 1 atm

// ── Orbital / Mission Delta-v Budgets (m/s) ───────────────────
/** Approximate round-trip Δv budgets for common mission profiles */
export const MISSION_DV = {
  earth_mars:  { needed: 5_500, name: 'Earth → Mars',       dist: '~78 M km avg' },
  mars_belt:   { needed: 3_500, name: 'Mars → Belt',         dist: '~190 M km' },
  earth_belt:  { needed: 7_200, name: 'Earth → Belt',        dist: '~265 M km' },
  belt_patrol: { needed: 2_000, name: 'Belt Patrol',         dist: 'Regional ops' },
};

// ── Rotation Physics ──────────────────────────────────────────

/**
 * Angular velocity from RPM.
 * @param {number} rpm  - revolutions per minute
 * @returns {number}    - rad/s
 */
export function rpmToOmega(rpm) {
  return (2 * Math.PI * rpm) / 60;
}

/**
 * RPM from angular velocity.
 * @param {number} omega - rad/s
 * @returns {number}     - RPM
 */
export function omegaToRpm(omega) {
  return (omega * 60) / (2 * Math.PI);
}

/**
 * Artificial gravity at a given radius and angular velocity.
 * g_art = ω² · r
 * @param {number} omega  - rad/s
 * @param {number} radius - m
 * @returns {number}      - acceleration in m/s²
 */
export function centripetAccel(omega, radius) {
  return omega * omega * radius;
}

/**
 * Artificial gravity relative to Earth g.
 * @returns {number} - g-units
 */
export function artificialGravity(omega, radius) {
  return centripetAccel(omega, radius) / G0;
}

/**
 * Required angular velocity for a target gravity at radius.
 * @param {number} gTarget  - desired gravity in g-units
 * @param {number} radius   - m
 * @returns {number}        - rad/s
 */
export function omegaForGravity(gTarget, radius) {
  return Math.sqrt((gTarget * G0) / radius);
}

/**
 * Coriolis force felt by a person walking.
 * F = 2·m·v·ω
 * @param {number} mass   - kg
 * @param {number} speed  - m/s (walking speed)
 * @param {number} omega  - rad/s
 * @returns {number}      - N
 */
export function coriolisForce(mass, speed, omega) {
  return 2 * mass * speed * omega;
}

/**
 * Coriolis force as a percentage of the person's effective weight.
 * @param {number} mass      - kg
 * @param {number} speed     - m/s
 * @param {number} omega     - rad/s
 * @param {number} gEff      - effective gravity in g-units
 * @returns {number}         - percentage 0-100+
 */
export function coriolisPct(mass, speed, omega, gEff) {
  const fCor = coriolisForce(mass, speed, omega);
  const weight = mass * G0 * gEff;
  return weight > 0 ? (fCor / weight) * 100 : 0;
}

/**
 * Comfort level label for a given RPM.
 * Based on human factors research (NASA/ESA guidelines).
 * @param {number} rpm
 * @returns {{ level: string, label: string, color: string }}
 */
export function comfortForRpm(rpm) {
  if (rpm < 2.0) return { level: 'excellent', label: 'Excellent — imperceptible Coriolis',   color: '#69f0ae' };
  if (rpm < 3.0) return { level: 'good',      label: 'Good — mild Coriolis, most unaffected', color: '#69f0ae' };
  if (rpm < 4.0) return { level: 'ok',        label: 'Acceptable — noticeable, adaptation needed', color: '#ffd54f' };
  if (rpm < 6.0) return { level: 'poor',      label: 'Poor — significant space-sickness risk', color: '#ff9800' };
  return               { level: 'danger',     label: 'Dangerous — severe disorientation',    color: '#ff5252' };
}

// ── Moment of Inertia ─────────────────────────────────────────

/**
 * Moment of inertia of a thin torus (hollow ring).
 * I = m·(R² + ¾·r²)
 * @param {number} mass       - kg
 * @param {number} majorRadius - m  (centre of tube to axis)
 * @param {number} minorRadius - m  (tube cross-section radius)
 * @returns {number}           - kg·m²
 */
export function torusInertia(mass, majorRadius, minorRadius) {
  return mass * (majorRadius ** 2 + 0.75 * minorRadius ** 2);
}

/**
 * Moment of inertia of a point mass (ring attachment).
 * I = m·r²
 */
export function pointInertia(mass, radius) {
  return mass * radius ** 2;
}

/**
 * Spin-up time from rest to omega using a tangential torque.
 * t = I·ω / τ
 * @param {number} I     - kg·m²  total moment of inertia
 * @param {number} omega - rad/s  target angular velocity
 * @param {number} torque - N·m  applied torque (RCS thrust × arm)
 * @returns {number}     - seconds
 */
export function spinUpTime(I, omega, torque) {
  return (I * omega) / Math.max(torque, 1e-9);
}

// ── Propulsion ────────────────────────────────────────────────

/**
 * Tsiolkovsky rocket equation.
 * Δv = Isp · g₀ · ln(m_wet / m_dry)
 * @param {number} isp      - seconds
 * @param {number} mWet     - kg, total mass including fuel
 * @param {number} mDry     - kg, mass without fuel
 * @returns {number}        - Δv in m/s
 */
export function deltaV(isp, mWet, mDry) {
  if (mDry <= 0 || mWet <= mDry) return 0;
  return isp * G0 * Math.log(mWet / mDry);
}

/**
 * Fuel burn time at constant thrust.
 * t = (m_fuel · Isp · g₀) / F
 * @param {number} fuelMass - kg
 * @param {number} isp      - seconds
 * @param {number} thrust   - N
 * @returns {number}        - seconds
 */
export function burnTime(fuelMass, isp, thrust) {
  return thrust > 0 ? (fuelMass * isp * G0) / thrust : Infinity;
}

// ── Structural ────────────────────────────────────────────────

/**
 * Centrifugal force on a section of mass rotating at omega.
 * F = m · ω² · r
 */
export function centrifugalForce(mass, omega, radius) {
  return mass * omega * omega * radius;
}

/**
 * Axial stress in a member given force and cross-sectional area.
 * σ = F / A   (Pa; divide by 1e6 for MPa)
 */
export function axialStressMPa(forceN, areaSqM) {
  return areaSqM > 0 ? forceN / (areaSqM * 1e6) : Infinity;
}

/**
 * Safety factor relative to steel yield.
 */
export function safetyFactor(stressMPa) {
  return stressMPa > 0 ? STEEL_YIELD_MPA / stressMPa : Infinity;
}

// ── Fluid / Atmosphere ────────────────────────────────────────

/**
 * Choked-flow mass-flow rate through a circular orifice (air).
 * Uses simplified isentropic choked-flow formula with Cd = 0.61.
 * @param {number} holeAreaM2 - m²
 * @returns {number}          - kg/s (at standard cabin P, T)
 */
export function chokedMassFlowRate(holeAreaM2) {
  const Cd = 0.61;
  // mdot = Cd·A·P·√(γ/RT)·(2/(γ+1))^((γ+1)/(2(γ-1)))
  const term = Math.pow(2 / (AIR_GAMMA + 1), (AIR_GAMMA + 1) / (2 * (AIR_GAMMA - 1)));
  return Cd * holeAreaM2 * AIR_P_PA * Math.sqrt(AIR_GAMMA / (AIR_R * AIR_TEMP_K)) * term;
}

/**
 * Time for compartment pressure to drop to a fraction of initial.
 * Assumes choked flow → exponential decay with time constant τ = m_air / mdot.
 * @param {number} volumeM3      - compartment volume
 * @param {number} holeAreaM2   - orifice area
 * @param {number} fraction      - target fraction (e.g. 0.5 for half pressure)
 * @returns {number}             - seconds
 */
export function timeToPressureFraction(volumeM3, holeAreaM2, fraction) {
  const mAir = AIR_RHO * volumeM3;
  const mdot = chokedMassFlowRate(holeAreaM2);
  if (mdot <= 0) return Infinity;
  const tau = mAir / mdot;
  return tau * Math.log(1 / fraction);
}

// ── Torus Geometry ────────────────────────────────────────────

/**
 * Volume of a hollow torus tube cross-section × circumference.
 * V = 2π·R · π·(r_outer² − r_inner²)
 * @param {number} majorR  - m, torus centre radius
 * @param {number} outerR  - m, tube outer radius
 * @param {number} innerR  - m, tube inner clear radius (corridor)
 * @param {number} fill    - fill fraction (0-1), portion that is solid steel
 * @returns {number}       - m³
 */
export function torusVolume(majorR, outerR, innerR, fill = 0.45) {
  const crossSection = Math.PI * (outerR ** 2 - innerR ** 2);
  return 2 * Math.PI * majorR * crossSection * fill;
}

/**
 * Curvature of the torus at a given radius — degrees per metre of arc.
 */
export function curvatureDegreesPerMetre(radius) {
  return 360 / (2 * Math.PI * radius);
}

// ── Formatting helpers (pure) ─────────────────────────────────

/**
 * Format a number to a fixed number of decimals, with locale separators.
 * Returns '—' for non-finite values.
 */
export function fmt(value, decimals = 0) {
  if (!isFinite(value) || isNaN(value)) return '—';
  return parseFloat(value.toFixed(decimals)).toLocaleString('en-US', {
    maximumFractionDigits: decimals,
    minimumFractionDigits: decimals,
  });
}

/** Format seconds into human-readable time string. */
export function fmtTime(seconds) {
  if (!isFinite(seconds)) return '∞';
  if (seconds < 60)   return `${fmt(seconds,0)} s`;
  if (seconds < 3600) return `${fmt(seconds/60, 1)} min`;
  if (seconds < 86400) return `${fmt(seconds/3600, 1)} hr`;
  return `${fmt(seconds/86400, 1)} days`;
}
