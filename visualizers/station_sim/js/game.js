/**
 * game.js — Main game loop and random event scheduler
 * Aura Space Station Simulator (Falcon)
 */

import { updateGameState, gameState, bus, shipConfig } from './state.js';
import { compute } from './physics.js';
import { EntityManager } from './entities.js';
import { DisasterSimulator } from './disasters.js';

export class GameLoop {
  constructor() {
    this.lastTime = 0;
    this.animationId = null;
    this.entityManager = new EntityManager();
    this.disasterSimulator = new DisasterSimulator();
    this.eventTimer = 0;

    // Bind event bus handlers
    bus.on('config:changed', () => this.recomputePhysics());
  }

  init() {
    // Spawn initial crew (FTL feel, let's give them roles)
    const initialCrew = [
      this.entityManager.createCrew('engineer', 'Avery Petrov'),
      this.entityManager.createCrew('pilot', 'Blake Nakamura'),
      this.entityManager.createCrew('scientist', 'Chen Kapoor'),
      this.entityManager.createCrew('medic', 'Elena Santos'),
      this.entityManager.createCrew('cook', 'Gao Ibrahim'),
      this.entityManager.createCrew('farmer', 'Zara Kowalski')
    ];

    // Spawn some initial animals
    const initialAnimals = [
      this.entityManager.createAnimal('chicken', 'Clucky'),
      this.entityManager.createAnimal('pig', 'Sir Oinks-a-lot'),
      this.entityManager.createAnimal('goat', 'Billy')
    ];

    // Spawn a couple of drones
    const initialDrones = [
      this.entityManager.createDrone('welder', 'Fixer-Bot'),
      this.entityManager.createDrone('sensor', 'Scan-Bot')
    ];

    gameState.crew = initialCrew;
    gameState.animals = initialAnimals;
    gameState.drones = initialDrones;
    
    // First physics computation
    this.recomputePhysics();

    // Log start
    gameState.logs.push({
      time: 0,
      message: `System Online. Rotating habitat "Falcon" initialized at ${shipConfig.rpm} RPM.`,
      type: 'info'
    });
  }

  start() {
    if (!gameState.paused) return;
    gameState.paused = false;
    this.lastTime = performance.now();
    this.tick();
    bus.emit('game:status', { running: true });
  }

  pause() {
    if (gameState.paused) return;
    gameState.paused = true;
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
      this.animationId = null;
    }
    bus.emit('game:status', { running: false });
  }

  setSpeed(multiplier) {
    gameState.speed = multiplier;
    bus.emit('game:speed', multiplier);
  }

  recomputePhysics() {
    const computed = compute(shipConfig);
    updateGameState({ computed });
  }

  tick() {
    if (gameState.paused) return;

    this.animationId = requestAnimationFrame((now) => {
      const realDt = (now - this.lastTime) / 1000;
      this.lastTime = now;

      // Limit dt to prevent giant jumps when tab is backgrounded
      const dt = Math.min(0.1, realDt) * gameState.speed;

      this.update(dt);
      this.tick();
    });
  }

  update(dt) {
    // 1. Advance simulation time
    gameState.time += dt;

    // 2. Update entities
    gameState.crew.forEach(c => c.update(dt));
    gameState.animals.forEach(a => a.update(dt));
    gameState.drones.forEach(d => d.update(dt));

    // 3. Update disasters
    this.disasterSimulator.update(gameState, gameState.computed, dt);

    // 4. Update core life support consumption and recovery
    this.updateLifeSupport(dt);

    // 5. Trigger random event scheduler
    this.handleRandomEvents(dt);

    // 6. Notify UI/Renderer
    bus.emit('state:updated', gameState);
  }

  updateLifeSupport(dt) {
    const computed = gameState.computed;
    if (!computed) return;

    // Base life support needs:
    // If we have greenhouse, it generates oxygen (+ load factor).
    // Crew consumption drains O2.
    const crewCount = gameState.crew.length;
    
    // Total O2 generated (from green houses) vs consumed (by crew and animal pens)
    const O2NetChange = (computed.lifeSupportBaseLoad * -0.5 * crewCount) * dt; 
    // greenhouse balances this. If O2NetChange is negative, oxygenLevel declines.
    
    // For visualizer simplicity, calculate O2 decline based on disasters + general crew pressure
    if (gameState.activeDisasters.some(d => d.type === 'air_leak')) {
      // handled in disaster.update
    } else {
      // Natural recovery towards 100 if we have functioning power and life support load is met
      if (gameState.powerLevel > 20) {
        gameState.oxygenLevel = Math.min(100, gameState.oxygenLevel + dt * 1.0);
        gameState.waterLevel = Math.min(100, gameState.waterLevel + dt * 0.8);
      } else {
        gameState.oxygenLevel = Math.max(0, gameState.oxygenLevel - dt * 0.5);
        gameState.waterLevel = Math.max(0, gameState.waterLevel - dt * 0.3);
      }
    }

    // Power natural recovery
    if (!gameState.activeDisasters.some(d => d.type === 'power_loss' || d.type === 'engine_failure')) {
      gameState.powerLevel = Math.min(100, gameState.powerLevel + dt * 3.0);
    }

    // Hull natural recovery if drones are repairing it (automatic drone logic)
    if (gameState.hullIntegrity < 100 && !gameState.activeDisasters.some(d => d.type === 'structural_stress')) {
      const droneWelders = gameState.drones.filter(d => d.droneType === 'welder' && d.battery > 20);
      if (droneWelders.length > 0) {
        gameState.hullIntegrity = Math.min(100, gameState.hullIntegrity + dt * 0.2 * droneWelders.length);
        droneWelders.forEach(d => {
          d.status = 'Repairing Hull';
          if (!d.moving && Math.random() < 0.05) {
            d.moveTo(Math.random()); // Move to a spot to weld
          }
        });
      }
    }

    // Calculate overall crew morale based on environmental stats
    let totalMorale = 0;
    gameState.crew.forEach(c => {
      totalMorale += c.morale;
    });
    
    // Average
    gameState.crewMorale = gameState.crew.length > 0 ? (totalMorale / gameState.crew.length) : 0;
  }

  handleRandomEvents(dt) {
    this.eventTimer += dt;
    
    // Check for random event every 20-30 seconds
    if (this.eventTimer > 25) {
      this.eventTimer = 0;

      // 15% chance of disaster trigger if structural parameters are safe
      // Higher chance if stress safety factors are low!
      let disasterChance = 0.15;
      const computed = gameState.computed;
      
      if (computed) {
        if (computed.hoopSafety < 1.5 || computed.containerSafety < 1.5) {
          disasterChance = 0.6; // High risk of structural failure
        }
      }

      if (Math.random() < disasterChance) {
        this.triggerRandomDisaster();
      }
    }
  }

  triggerRandomDisaster(forceType = null) {
    const disasterTypes = ['air_leak', 'water_leak', 'structural_stress', 'engine_failure', 'power_loss'];
    const selectedType = forceType || disasterTypes[Math.floor(Math.random() * disasterTypes.length)];
    
    const isAlreadyActive = gameState.activeDisasters.some(d => d.type === selectedType);
    if (isAlreadyActive && !forceType) return; // avoid duplicate random triggers of same type

    const pos = Math.random();
    const rim = Math.random() > 0.5 ? 'inner' : 'outer';
    const newDisaster = this.disasterSimulator.trigger(selectedType, pos, rim);

    if (newDisaster) {
      gameState.activeDisasters.push(newDisaster);
      gameState.logs.push({
        time: gameState.time,
        message: `WARNING: ${newDisaster.name} detected at section ${(pos * 360).toFixed(0)}° (${rim} rim)!`,
        type: 'danger'
      });
      bus.emit('disaster:triggered', newDisaster);
    }
  }
}
