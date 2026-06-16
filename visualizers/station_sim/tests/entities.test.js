/**
 * entities.test.js — Testing crew and agent classes
 */

import { describe, it, expect } from './test-utils.js';
import { CrewMember, EntityManager } from '../js/entities.js';

describe('Crew Members & Agents', () => {
  it('creates a crew member with default stats', () => {
    const manager = new EntityManager();
    const crew = manager.createCrew('engineer', 'Avery Petrov');

    expect(crew.name).toBe('Avery Petrov');
    expect(crew.role).toBe('engineer');
    expect(crew.health).toBe(100);
    expect(crew.hunger).toBe(0);
    expect(crew.fatigue).toBe(0);
    expect(crew.status).toBe('Idle');
  });

  it('updates stats and hunger increases over time', () => {
    const crew = new CrewMember(1, 'Avery Petrov', 'engineer');
    crew.update(10); // simulate 10 seconds passing
    
    // hunger should increase by 10 * 0.05 = 0.5
    expect(crew.hunger).toBeCloseTo(0.5, 2);
    // fatigue should increase by 10 * 0.03 = 0.3
    expect(crew.fatigue).toBeCloseTo(0.3, 2);
  });

  it('navigates around the torus correctly', () => {
    const crew = new CrewMember(1, 'Avery Petrov', 'engineer');
    crew.pos = 0.0;
    
    // Command to move to pos 0.1
    crew.moveTo(0.1);
    expect(crew.targetPos).toBe(0.1);
    
    // Update by 1 second (speed = 0.04)
    crew.update(1.0);
    expect(crew.pos).toBeCloseTo(0.04, 3);
    expect(crew.moving).toBeTruthy();
  });
});
