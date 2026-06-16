/**
 * disasters.js — Disaster simulation physics, conditions, and calculations
 * Aura Space Station Simulator (Falcon)
 */

import { createParticleBurst } from '../../shared/js/canvas-utils.js';

export const DISASTER_TYPES = {
  air_leak: {
    id: 'air_leak',
    name: 'Atmosphere Blowout',
    icon: '💨',
    color: '#00e5ff',
    baseSeverity: 0.15,
    description: 'A micrometeoroid or structural failure has breached the pressure hull. Air is rushing into the vacuum.',
    recommendation: 'Send an Engineer to the breach location to weld a patch plate.'
  },
  water_leak: {
    id: 'water_leak',
    name: 'Hydro-Main Rupture',
    icon: '💧',
    color: '#2979ff',
    baseSeverity: 0.1,
    description: 'Water recycling line has burst. Fluid is pooling in corridors, ruining electronics.',
    recommendation: 'Send any crew member to shut off the isolation valve and repair the pipe.'
  },
  structural_stress: {
    id: 'structural_stress',
    name: 'Hull Stress Fracture',
    icon: '⚡',
    color: '#ff9100',
    baseSeverity: 0.2,
    description: 'Centrifugal forces are exceeding materials tolerances. Micro-fissures spreading.',
    recommendation: 'Reduce station RPM immediately, or deploy welding drones to reinforce structural joints.'
  },
  engine_failure: {
    id: 'engine_failure',
    name: 'Engine Melt-down / Misfire',
    icon: '🔥',
    color: '#ff1744',
    baseSeverity: 0.25,
    description: 'Coolant leak in the engine reactor block. Thermal runaway imminent!',
    recommendation: 'Requires an Engineer or Pilot to trigger emergency shutdown and vent fuel.'
  },
  power_loss: {
    id: 'power_loss',
    name: 'Grid Overload / Short Circuit',
    icon: '🔌',
    color: '#ffea00',
    baseSeverity: 0.12,
    description: 'Power distribution junction blew a fuse. Life support and artificial gravity controls failing.',
    recommendation: 'Send an Engineer or Scientist to replace the superconducting capacitor bank.'
  }
};

export class DisasterSimulator {
  constructor() {
    this.particles = [];
  }

  /**
   * Spawns a new active disaster state.
   */
  trigger(typeId, pos = null, rim = 'outer') {
    const info = DISASTER_TYPES[typeId];
    if (!info) return null;

    return {
      id: Math.random().toString(36).substr(2, 9),
      type: typeId,
      name: info.name,
      icon: info.icon,
      color: info.color,
      pos: pos !== null ? pos : Math.random(),
      rim,
      severity: info.baseSeverity, // 0..1 scale
      progress: 0, // 0 to 100% (escalation/countdown to critical failure)
      description: info.description,
      resolved: false,
      assignedCrewId: null,
      particleSpawnTimer: 0
    };
  }

  /**
   * Run simulation tick on the active disasters.
   * @param {Object} gameState
   * @param {Object} computed
   * @param {number} dt - seconds
   */
  update(gameState, computed, dt) {
    const active = gameState.activeDisasters;
    if (!active || active.length === 0) return;

    active.forEach(disaster => {
      // 1. Escalate progress of disaster
      // NTR engine failures leak faster, structural stress escalates faster at high RPM
      let escalationRate = 1.5; // percent per second
      if (disaster.type === 'structural_stress') {
        const rpmFactor = Math.max(0.5, computed.hoopStressMPa / 100);
        escalationRate *= rpmFactor;
      }
      
      // If crew is actively fixing it, progress goes DOWN instead
      if (disaster.assignedCrewId !== null) {
        const crewMember = gameState.crew.find(c => c.id === disaster.assignedCrewId);
        if (crewMember) {
          // Check if crew member has reached the disaster location
          let dist = Math.abs(crewMember.pos - disaster.pos);
          if (dist > 0.5) dist = 1.0 - dist;
          
          if (dist < 0.03 && crewMember.rim === disaster.rim) {
            // Arrived and repairing!
            crewMember.status = 'Repairing';
            let repairSpeed = 4.0; // % per second base
            if (crewMember.role === 'engineer') repairSpeed *= 1.8; // engineers fix faster
            
            disaster.progress = Math.max(0, disaster.progress - repairSpeed * dt);
            disaster.severity = Math.max(0.01, disaster.severity - 0.05 * dt);
            
            if (disaster.progress <= 0) {
              disaster.resolved = true;
              crewMember.status = 'Idle';
              crewMember.currentTask = null;
            }
          } else {
            // Still travelling
            crewMember.status = 'Responding';
            escalationRate *= 0.5; // slower escalation because help is on the way
          }
        } else {
          // Assigned crew is missing
          disaster.assignedCrewId = null;
        }
      }

      if (!disaster.resolved) {
        disaster.progress = Math.min(100, disaster.progress + escalationRate * dt);
      }

      // Apply effects to ship integrity and metrics
      const impactFactor = disaster.severity * dt;
      switch (disaster.type) {
        case 'air_leak':
          gameState.oxygenLevel = Math.max(0, gameState.oxygenLevel - impactFactor * 4);
          gameState.hullIntegrity = Math.max(0, gameState.hullIntegrity - impactFactor * 1.5);
          break;
        case 'water_leak':
          gameState.waterLevel = Math.max(0, gameState.waterLevel - impactFactor * 3);
          break;
        case 'structural_stress':
          gameState.hullIntegrity = Math.max(0, gameState.hullIntegrity - impactFactor * 5);
          break;
        case 'engine_failure':
          gameState.powerLevel = Math.max(0, gameState.powerLevel - impactFactor * 4);
          gameState.hullIntegrity = Math.max(0, gameState.hullIntegrity - impactFactor * 2.5);
          break;
        case 'power_loss':
          gameState.powerLevel = Math.max(0, gameState.powerLevel - impactFactor * 8);
          break;
      }
    });

    // Clean up resolved disasters
    const resolved = active.filter(d => d.resolved);
    resolved.forEach(d => {
      gameState.disasterHistory.push({
        type: d.type,
        name: d.name,
        time: gameState.time,
        outcome: 'Successfully Resolved'
      });
      // push log
      gameState.logs.push({
        time: gameState.time,
        message: `RESOLVED: ${d.name} has been secured.`,
        type: 'success'
      });
    });

    gameState.activeDisasters = active.filter(d => !d.resolved);
  }
}
