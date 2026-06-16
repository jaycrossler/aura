/**
 * physics.js — Station-specific physics calculations
 * Aura Space Station Simulator (Falcon)
 */

import * as phys from '../../shared/js/physics-utils.js';
import { ENGINE_TYPES, CONTAINER_TYPES } from './constants.js';

/**
 * Perform full physical calculation for the space station based on the current configuration.
 * @param {Object} config - shipConfig
 * @returns {Object} ComputedValues
 */
export function compute(config) {
  const {
    majorRadius,
    minorRadius,
    spokesCount,
    spokeThickness,
    wallThicknessMm,
    rpm,
    engineType,
    fuelMassFraction,
    innerContainers,
    outerContainers
  } = config;

  const omega = phys.rpmToOmega(rpm);
  const activeEngine = ENGINE_TYPES[engineType] || ENGINE_TYPES.ntr;

  // 1. Calculate structural masses
  // Volume of torus outer skin (approximate hollow tube volume using wall thickness)
  // V_skin = 2π·R · π·(r_outer² − r_inner²)
  const outerR = minorRadius;
  const innerR = minorRadius - (wallThicknessMm / 1000);
  const shellVolume = phys.torusVolume(majorRadius, outerR, innerR, 1.0); // 100% steel fill for shell
  const shellMass = shellVolume * phys.STEEL_DENSITY;

  // Spoke mass: approximate as cylinders
  const spokeVolume = spokesCount * Math.PI * ((spokeThickness / 2) ** 2) * majorRadius;
  const spokesMass = spokeVolume * phys.STEEL_DENSITY;

  // Hull structural mass
  const structuralMass = shellMass + spokesMass;

  // 2. Engine and systems mass
  const engineMass = activeEngine.engineMass;
  // Let's add reactor/power system mass depending on the engine
  let systemsMass = 10000; // Base power / life support system weight
  if (engineType === 'vasimr') systemsMass += 30000; // heavy electrical power systems
  if (engineType === 'ntr' || engineType === 'bimodal') systemsMass += 15000; // shielding/liquid hydrogen equipment

  // 3. Container mass (dry) and contents capacity
  let containerDryMass = 0;
  let maxCrewCapacity = 0;
  let totalVolume = 0;
  let lifeSupportBaseLoad = 0; // standard life support factors
  let cost = activeEngine.cost;

  const sumContainers = (list) => {
    list.forEach(c => {
      const typeInfo = CONTAINER_TYPES[c.type];
      if (typeInfo) {
        containerDryMass += typeInfo.mass;
        maxCrewCapacity += typeInfo.occupants || 0;
        totalVolume += typeInfo.volume;
        lifeSupportBaseLoad += typeInfo.lifeSupportLoad;
        cost += typeInfo.cost;
      }
    });
  };

  sumContainers(innerContainers);
  sumContainers(outerContainers);

  // Dry mass of the station is structural + systems + empty containers
  const dryMass = structuralMass + engineMass + systemsMass + containerDryMass;

  // Propellant/Fuel mass
  // fuelMassFraction = m_fuel / m_wet => m_wet = dryMass / (1 - fuelMassFraction)
  const wetMass = dryMass / (1 - Math.max(0.01, Math.min(0.95, fuelMassFraction)));
  const fuelMass = wetMass - dryMass;

  // Total inertia
  // Torus shell inertia
  const torusI = phys.torusInertia(shellMass + containerDryMass, majorRadius, minorRadius);
  // Spokes inertia: treat as rods rotating about one end (1/3 M L²)
  const spokesI = (spokesMass * (majorRadius ** 2)) / 3;
  // Engines + systems: concentrated at center hub mostly, but let's assume engines are offset or counterweight is at center.
  // We'll treat engine mass at center hub (negligible I) or slightly offset. Let's assume hub mounting.
  const centralI = phys.pointInertia(engineMass + systemsMass, 2.0); // very close to center
  
  // Containers: point masses at their respective radii.
  let containersI = 0;
  innerContainers.forEach(c => {
    const typeInfo = CONTAINER_TYPES[c.type];
    if (typeInfo) {
      // Inner containers are attached to inner rim: radius = majorRadius - minorRadius
      containersI += phys.pointInertia(typeInfo.mass, majorRadius - minorRadius);
    }
  });
  outerContainers.forEach(c => {
    const typeInfo = CONTAINER_TYPES[c.type];
    if (typeInfo) {
      // Outer containers are attached to outer rim: radius = majorRadius + minorRadius
      containersI += phys.pointInertia(typeInfo.mass, majorRadius + minorRadius);
    }
  });

  const totalInertia = torusI + spokesI + centralI + containersI;

  // 4. Gravity & Comfort at inner/outer rim
  const innerRadius = majorRadius - minorRadius;
  const outerRadius = majorRadius + minorRadius;

  const innerG = phys.artificialGravity(omega, innerRadius);
  const outerG = phys.artificialGravity(omega, outerRadius);

  const comfort = phys.comfortForRpm(rpm);

  // 5. Propulsion calculations (Tsiolkovsky)
  const dv = phys.deltaV(activeEngine.isp, wetMass, dryMass);
  const burnTimeSec = phys.burnTime(fuelMass, activeEngine.isp, activeEngine.thrust);
  
  // Spin-up torque (using RCS engines, let's assume standard RCS thrust of 40 kN at radius = majorRadius)
  const rcsThrust = 40000; // N
  const spinUpTorque = rcsThrust * majorRadius;
  const spinUpSec = phys.spinUpTime(totalInertia, omega, spinUpTorque);

  // 6. Structural Stress
  // Centrifugal force on a single container mass at outer rim
  const sampleContainerMass = 15000; // kg
  const centForce = phys.centrifugalForce(sampleContainerMass, omega, outerRadius);
  // Area of connector bolt assembly: say 0.02 m²
  const boltArea = 0.02;
  const containerStressMPa = phys.axialStressMPa(centForce, boltArea);
  const containerSafety = phys.safetyFactor(containerStressMPa);

  // Torus hoop stress (approximate: σ = ρ · v² = ρ · ω² · R²)
  const hoopStressMPa = ((phys.STEEL_DENSITY * ((omega * majorRadius) ** 2)) / 1e6);
  const hoopSafety = phys.safetyFactor(hoopStressMPa);

  // 7. Imbalance / Center of Mass shift calculation
  // The central command hub is at (0, 0). Structural shell and spokes are symmetric.
  // The mass imbalance is determined by the positions of the containers.
  let sumMassX = 0;
  let sumMassY = 0;
  let totalStationMass = dryMass; // or wetMass, let's use dryMass for structure COM shift

  const addImbalanceContribution = (list, r) => {
    list.forEach(c => {
      const typeInfo = CONTAINER_TYPES[c.type];
      if (typeInfo) {
        // Position angle on the torus
        const angle = c.pos * Math.PI * 2;
        sumMassX += typeInfo.mass * r * Math.cos(angle);
        sumMassY += typeInfo.mass * r * Math.sin(angle);
      }
    });
  };

  addImbalanceContribution(innerContainers, innerRadius);
  addImbalanceContribution(outerContainers, outerRadius);

  // Center of mass offset (in meters)
  const comX = sumMassX / totalStationMass;
  const comY = sumMassY / totalStationMass;
  const imbalanceShift = Math.hypot(comX, comY); // COM distance from center

  // Wobbly vibration / strain factor:
  // F_wobble = M_total * omega^2 * imbalanceShift
  const wobbleForce = imbalanceShift > 0.1 ? totalStationMass * (omega ** 2) * imbalanceShift : 0;
  // Dynamic wobble stress factor
  const wobbleStressMPa = wobbleForce / (0.1 * 1e6); // arbitrary structural joint area
  
  // Adjusted structural safety factors due to imbalance stress
  const adjustedHoopSafety = hoopStressMPa > 0 ? phys.STEEL_YIELD_MPA / (hoopStressMPa + wobbleStressMPa) : Infinity;

  // 8. Life Support and consumables
  // O2 usage: 0.84 kg per human per day
  // Water usage: 2.5 kg per human per day
  const o2PerPersonDay = 0.84;
  const waterPerPersonDay = 2.5;

  return {
    structuralMass,
    engineMass,
    containerDryMass,
    dryMass,
    wetMass,
    fuelMass,
    totalInertia,
    innerG,
    outerG,
    comfort,
    deltaV: dv,
    burnTime: burnTimeSec,
    spinUpTime: spinUpSec,
    maxCrewCapacity,
    totalVolume,
    lifeSupportBaseLoad,
    cost,
    containerStressMPa,
    containerSafety,
    hoopStressMPa,
    hoopSafety: adjustedHoopSafety, // Use the wobble-adjusted safety factor
    rawHoopSafety: hoopSafety,
    imbalanceShift,
    wobbleForce,
    o2PerPersonDay,
    waterPerPersonDay
  };
}
