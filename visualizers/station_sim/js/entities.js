/**
 * entities.js — Simulation entities (Crew, Animals, Drones) and EntityManager
 * Aura Space Station Simulator (Falcon)
 */

import { randomName, moveTowardOnRing } from '../../shared/js/ui-utils.js';
import { CREW_ROLES, ANIMAL_TYPES, DRONE_TYPES } from './constants.js';

export class BaseEntity {
  constructor(id, name, type, icon, color) {
    this.id = id;
    this.name = name;
    this.type = type; // 'crew' | 'animal' | 'drone'
    this.icon = icon;
    this.color = color;
    
    this.pos = Math.random(); // 0..1 circular position along torus major radius
    this.targetPos = null; // target for movement
    this.speed = 0.05; // fraction of ring per second (default: ~20s for full circle)
    this.moving = false;
    
    // Orbit level: 'inner' or 'outer'
    this.rim = Math.random() > 0.5 ? 'inner' : 'outer';
    this.targetRim = null;
  }

  update(dt) {
    if (this.targetPos !== null) {
      this.moving = true;
      this.pos = moveTowardOnRing(this.pos, this.targetPos, this.speed, dt);
      
      // If we arrived, clear target
      if (this.pos === this.targetPos) {
        this.targetPos = null;
        if (this.targetRim !== null) {
          this.rim = this.targetRim;
          this.targetRim = null;
        }
        this.moving = false;
        this.onArrival();
      }
    } else {
      this.moving = false;
    }
  }

  moveTo(targetPos, targetRim = null) {
    this.targetPos = targetPos;
    this.targetRim = targetRim;
  }

  onArrival() {
    // Override in subclass
  }
}

export class CrewMember extends BaseEntity {
  constructor(id, name, roleId) {
    const role = CREW_ROLES[roleId] || CREW_ROLES.engineer;
    super(id, name, 'crew', role.icon, role.color);
    this.role = roleId;
    this.skill = role.skill;
    
    // Character stats (0 - 100)
    this.health = 100;
    this.hunger = 0; // 0 is full, 100 is starving
    this.fatigue = 0; // 0 is rested, 100 is exhausted
    this.morale = 80;
    
    this.status = 'Idle'; // 'Idle' | 'Repairing' | 'Resting' | 'Eating' | 'Stressed'
    this.currentTask = null;
    this.speed = 0.04; // Crew walks a bit slower
  }

  update(dt) {
    super.update(dt);
    
    // Slow stats drift over time
    this.hunger = Math.min(100, this.hunger + dt * 0.05); // increases hunger
    this.fatigue = Math.min(100, this.fatigue + dt * 0.03); // increases fatigue
    
    // Morale checks
    if (this.hunger > 60 || this.fatigue > 60) {
      this.morale = Math.max(0, this.morale - dt * 0.1);
    } else {
      this.morale = Math.min(100, this.morale + dt * 0.02);
    }

    // Health checks
    if (this.hunger > 90 || this.fatigue > 90) {
      this.health = Math.max(0, this.health - dt * 0.2);
      this.status = 'Suffering';
    } else if (this.health < 100 && this.hunger < 30 && this.fatigue < 30) {
      this.health = Math.min(100, this.health + dt * 0.1); // slow healing
    }
    
    // Auto needs resolution if idle (simple simulation agent behavior)
    if (!this.moving && this.status === 'Idle') {
      if (this.hunger > 50) {
        this.goToEat();
      } else if (this.fatigue > 50) {
        this.goToSleep();
      }
    }
  }

  goToEat() {
    this.status = 'Searching for food';
    // Find a cafeteria or kitchen. For simplicity, move to a random position
    this.moveTo((this.pos + 0.3) % 1.0);
  }

  goToSleep() {
    this.status = 'Going to quarters';
    this.moveTo((this.pos + 0.5) % 1.0);
  }

  onArrival() {
    if (this.status === 'Searching for food') {
      this.hunger = 0;
      this.status = 'Eating';
      setTimeout(() => { if (this.status === 'Eating') this.status = 'Idle'; }, 3000);
    } else if (this.status === 'Going to quarters') {
      this.fatigue = 0;
      this.status = 'Sleeping';
      setTimeout(() => { if (this.status === 'Sleeping') this.status = 'Idle'; }, 5000);
    } else {
      this.status = 'Idle';
    }
  }
}

export class Animal extends BaseEntity {
  constructor(id, name, animalTypeId) {
    const typeInfo = ANIMAL_TYPES[animalTypeId] || ANIMAL_TYPES.chicken;
    super(id, name, 'animal', typeInfo.icon, typeInfo.color);
    this.animalType = animalTypeId;
    this.moraleBoost = typeInfo.moraleBoost;
    this.speed = 0.02; // Animals are slow
  }

  update(dt) {
    super.update(dt);
    
    // Animals occasionally wander around a small neighborhood
    if (!this.moving && Math.random() < 0.01) {
      const delta = (Math.random() - 0.5) * 0.1;
      this.moveTo((this.pos + delta + 1.0) % 1.0);
    }
  }
}

export class Drone extends BaseEntity {
  constructor(id, name, droneTypeId) {
    const typeInfo = DRONE_TYPES[droneTypeId] || DRONE_TYPES.welder;
    super(id, name, 'drone', typeInfo.icon, typeInfo.color);
    this.droneType = droneTypeId;
    this.speed = typeInfo.speed;
    this.battery = 100;
    this.status = 'Standby';
  }

  update(dt) {
    super.update(dt);
    
    if (this.moving) {
      this.battery = Math.max(0, this.battery - dt * 0.2);
    } else {
      // Recharging
      this.battery = Math.min(100, this.battery + dt * 0.5);
    }
    
    if (this.battery < 10) {
      this.status = 'Low Power';
      // go back to drone hangar (assume hangar is at pos 0.48)
      if (!this.moving && Math.abs(this.pos - 0.48) > 0.02) {
        this.moveTo(0.48, 'outer');
      }
    }
  }
}

export class EntityManager {
  constructor() {
    this.nextId = 1;
  }

  createCrew(roleId, name = null) {
    const finalName = name || randomName();
    const c = new CrewMember(this.nextId++, finalName, roleId);
    return c;
  }

  createAnimal(typeId, name = null) {
    const finalName = name || `${ANIMAL_TYPES[typeId].name} #${this.nextId}`;
    const a = new Animal(this.nextId++, finalName, typeId);
    return a;
  }

  createDrone(typeId, name = null) {
    const finalName = name || `${DRONE_TYPES[typeId].name} #${this.nextId}`;
    const d = new Drone(this.nextId++, finalName, typeId);
    return d;
  }

  /**
   * Find entity closest to a given torus circle fraction
   */
  findClosestEntity(pos, rim, list, maxDiff = 0.05) {
    let closest = null;
    let minDiff = maxDiff;
    
    list.forEach(ent => {
      if (ent.rim !== rim) return;
      
      // Calculate angular distance accounting for wrap around
      let diff = Math.abs(ent.pos - pos);
      if (diff > 0.5) diff = 1.0 - diff;
      
      if (diff < minDiff) {
        minDiff = diff;
        closest = ent;
      }
    });
    
    return closest;
  }
}
