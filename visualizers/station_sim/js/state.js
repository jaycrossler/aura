/**
 * state.js — Reactive state container and configuration controls
 * Aura Space Station Simulator (Falcon)
 */

import { EventBus } from '../../shared/js/ui-utils.js';
import { DEFAULT_CONFIG } from './constants.js';

// The global event bus for the simulation
export const bus = new EventBus();

// Holds the physical parameters specified by the UI inputs (sliders/selections)
export const shipConfig = JSON.parse(JSON.stringify(DEFAULT_CONFIG));

// Holds the running, dynamic simulation/game state
export const gameState = {
  time: 0,             // Simulation elapsed seconds
  paused: true,
  speed: 1,            // Speed multiplier: 1x, 2x, 5x, 10x
  
  // Entity lists
  crew: [],
  animals: [],
  drones: [],
  
  // Selected entity for control
  selectedEntity: null,
  
  // Disasters
  activeDisasters: [],
  disasterHistory: [],
  
  // Logs
  logs: [],
  
  // Running stats tracking for graph / logs
  crewMorale: 80,
  oxygenLevel: 100, // %
  powerLevel: 100,  // %
  waterLevel: 100,  // %
  hullIntegrity: 100 // %
};

/**
 * Updates a configuration variable and fires an event.
 * @param {string} key
 * @param {*} val
 */
export function updateConfig(key, val) {
  shipConfig[key] = val;
  bus.emit('config:changed', { key, value: val });
}

/**
 * Updates multiple configuration variables at once.
 * @param {Object} patch
 */
export function updateConfigBatch(patch) {
  Object.assign(shipConfig, patch);
  bus.emit('config:changed', { batch: patch });
}

/**
 * Helper to update game state properties and notify listeners.
 * @param {Object} patch
 */
export function updateGameState(patch) {
  Object.assign(gameState, patch);
  bus.emit('state:changed', patch);
}

/**
 * Reset config to default values.
 */
export function resetConfig() {
  Object.assign(shipConfig, JSON.parse(JSON.stringify(DEFAULT_CONFIG)));
  bus.emit('config:changed', { reset: true });
}
