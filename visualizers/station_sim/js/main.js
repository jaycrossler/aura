/**
 * main.js — SpinningStationSim entry point
 * Aura Space Station Simulator (Falcon)
 */

import { GameLoop } from './game.js';
import { StationRenderer } from './renderer.js';
import { UIManager } from './ui.js';
import { bus, gameState, shipConfig } from './state.js';
import { hitTestTorus, canvasToTorusPos } from '../../shared/js/canvas-utils.js';

let gameLoop;
let renderer;
let uiManager;

function init() {
  const canvas = document.getElementById('visualizer-canvas');
  if (!canvas) {
    console.error('Canvas element "visualizer-canvas" not found!');
    return;
  }

  // 1. Instantiate modules
  gameLoop = new GameLoop();
  renderer = new StationRenderer(canvas);
  uiManager = new UIManager();

  // 2. Initialise modules
  gameLoop.init();
  uiManager.init();
  
  // Resize handler for canvas
  renderer.resize();
  window.addEventListener('resize', () => {
    renderer.resize();
  });

  // 3. Connect Event Bus
  
  // Game state changes: redraw
  bus.on('state:updated', (state) => {
    renderer.draw(shipConfig, state.computed, state);
  });

  // Tab View Change
  bus.on('view:changed', (viewName) => {
    renderer.setView(viewName);
    renderer.draw(shipConfig, gameState.computed, gameState);
  });

  // Game control triggers
  bus.on('game:control', (action) => {
    if (action === 'play') gameLoop.start();
    if (action === 'pause') gameLoop.pause();
    if (action === 'speed-1') gameLoop.setSpeed(1);
    if (action === 'speed-5') gameLoop.setSpeed(5);
  });

  // Disaster manually triggered
  bus.on('action:trigger-disaster', (typeId) => {
    gameLoop.triggerRandomDisaster(typeId);
  });

  // Click handler on canvas to select crew or command them
  bus.on('canvas:click', ({ px, py }) => {
    const w = canvas.width / window.devicePixelRatio;
    const h = canvas.height / window.devicePixelRatio;
    const cx = w / 2;
    const cy = h / 2;
    
    // Scale must match renderer scale
    const maxRadiusPx = Math.min(w, h) * 0.4;
    const scale = maxRadiusPx / 150;

    const rMajor = shipConfig.majorRadius;
    const rMinor = shipConfig.minorRadius;

    // 1. Calculate clicking pos in torus (0..1) and rim
    const clickedTorusPos = canvasToTorusPos(px, py, cx, cy);
    
    // Calculate distance from center to find if click is inner or outer rim
    const distFromCenter = Math.hypot(px - cx, py - cy) / scale;
    const clickRim = distFromCenter < rMajor ? 'inner' : 'outer';

    // 2. Check crew hit tests first
    const closestCrew = gameLoop.entityManager.findClosestEntity(clickedTorusPos, clickRim, gameState.crew, 0.05);
    if (closestCrew) {
      uiManager.setSelectedEntity(closestCrew);
      gameState.selectedEntity = closestCrew;
      return;
    }

    // 3. Check animal / drone hit tests
    const closestAnimal = gameLoop.entityManager.findClosestEntity(clickedTorusPos, clickRim, gameState.animals, 0.05);
    if (closestAnimal) {
      uiManager.setSelectedEntity(closestAnimal);
      gameState.selectedEntity = closestAnimal;
      return;
    }

    const closestDrone = gameLoop.entityManager.findClosestEntity(clickedTorusPos, clickRim, gameState.drones, 0.05);
    if (closestDrone) {
      uiManager.setSelectedEntity(closestDrone);
      gameState.selectedEntity = closestDrone;
      return;
    }

    // Clicked empty space on canvas -> clear selection
    uiManager.setSelectedEntity(null);
    gameState.selectedEntity = null;
  });

  // Dragging state for lopsided containers simulation
  let draggedContainer = null;
  let draggedRim = null; // 'inner' | 'outer'

  canvas.addEventListener('mousedown', (e) => {
    const rect = canvas.getBoundingClientRect();
    const px = e.clientX - rect.left;
    const py = e.clientY - rect.top;

    const w = canvas.width / window.devicePixelRatio;
    const h = canvas.height / window.devicePixelRatio;
    const cx = w / 2;
    const cy = h / 2;

    const maxRadiusPx = Math.min(w, h) * 0.4;
    const scale = maxRadiusPx / 150;

    const rMajor = shipConfig.majorRadius;
    const rMinor = shipConfig.minorRadius;

    const clickedTorusPos = canvasToTorusPos(px, py, cx, cy);
    const distFromCenter = Math.hypot(px - cx, py - cy) / scale;
    const clickRim = distFromCenter < rMajor ? 'inner' : 'outer';

    // Find if click hit a container segment
    const containerList = clickRim === 'inner' ? shipConfig.innerContainers : shipConfig.outerContainers;
    let hitIdx = -1;

    containerList.forEach((c, idx) => {
      // Calculate angular distance
      let diff = Math.abs(c.pos - clickedTorusPos);
      if (diff > 0.5) diff = 1.0 - diff;
      if (diff < 0.08) { // angular tolerance for drag selection
        hitIdx = idx;
      }
    });

    if (hitIdx !== -1) {
      draggedContainer = containerList[hitIdx];
      draggedRim = clickRim;
      // Pause loop during drag for precision
      gameLoop.pause();
    } else {
      // Normal click entity selection if no container is hit
      bus.emit('canvas:click', { px, py });
    }
  });

  canvas.addEventListener('mousemove', (e) => {
    if (!draggedContainer) return;

    const rect = canvas.getBoundingClientRect();
    const px = e.clientX - rect.left;
    const py = e.clientY - rect.top;

    const w = canvas.width / window.devicePixelRatio;
    const h = canvas.height / window.devicePixelRatio;
    const cx = w / 2;
    const cy = h / 2;

    const currentTorusPos = canvasToTorusPos(px, py, cx, cy);
    // Correct for spin phase since station is spinning
    // Angle in renderer = spinAngle + pos * 2pi - pi/2 => pos = (Angle + pi/2 - spinAngle) / 2pi
    // To make drag position line up exactly with mouse cursor under rotation, we subtract spinAngle:
    let adjustedPos = (currentTorusPos - (renderer.spinAngle / (Math.PI * 2))) % 1.0;
    if (adjustedPos < 0) adjustedPos += 1.0;

    draggedContainer.pos = adjustedPos;
    
    // Broadcast config change to force recomputing center of mass lopsided wobble
    updateConfig(draggedRim === 'inner' ? 'innerContainers' : 'outerContainers', 
                 draggedRim === 'inner' ? shipConfig.innerContainers : shipConfig.outerContainers);
  });

  canvas.addEventListener('mouseup', () => {
    if (draggedContainer) {
      draggedContainer = null;
      draggedRim = null;
      gameLoop.start(); // resume loop
    }
  });

  canvas.addEventListener('mouseleave', () => {
    if (draggedContainer) {
      draggedContainer = null;
      draggedRim = null;
      gameLoop.start();
    }
  });

  // 4. Start loop immediately (starts paused)
  gameLoop.start();
  gameLoop.pause(); // force pause visual state
  
  // Force initial paint/render
  bus.emit('state:updated', gameState);
}

// Kick off when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
