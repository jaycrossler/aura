/**
 * constants.js — SpinningStationSim specific constants
 * Aura Space Station Simulator (Falcon)
 */

export const ENGINE_TYPES = {
  chemical: {
    id: 'chemical',
    name: 'Chemical (LH2/LOX)',
    isp: 450, // seconds
    thrust: 4000000, // N (4 MN)
    engineMass: 15000, // kg
    cost: 50, // M credits
    requiredSystems: 'Cryo fuel storage, high-pressure pumps',
    description: 'High thrust, simple chemical combustion. Heavy fuel mass requirements.'
  },
  ntr: {
    id: 'ntr',
    name: 'Nuclear Thermal (NTR)',
    isp: 900, // seconds
    thrust: 1200000, // N (1.2 MN)
    engineMass: 35000, // kg
    cost: 120, // M credits
    requiredSystems: 'Liquid hydrogen feed, shielding, reactor cooling',
    description: 'High efficiency nuclear reactor heats hydrogen propellant. Moderate thrust, high Isp.'
  },
  vasimr: {
    id: 'vasimr',
    name: 'VASIMR (Plasma Electric)',
    isp: 5000, // seconds
    thrust: 20000, // N (20 kN)
    engineMass: 25000, // kg
    cost: 180, // M credits
    requiredSystems: 'Gigawatt-class reactor or massive solar array, magnetic coils',
    description: 'Variable Specific Impulse Magnetoplasma Rocket. Extremely efficient, very low thrust.'
  },
  bimodal: {
    id: 'bimodal',
    name: 'Bimodal NTR',
    isp: 920, // seconds
    thrust: 800000, // N (800 kN)
    engineMass: 42000, // kg
    cost: 220, // M credits
    requiredSystems: 'Electricity generation taps, closed-loop radiator system',
    description: 'Dual-mode reactor. Generates thrust (propulsion) and high electrical power (auxiliary power).'
  }
};

export const CONTAINER_TYPES = {
  crew_cabin: {
    id: 'crew_cabin',
    name: 'Crew Cabin (2 Px)',
    mass: 8000, // kg
    volume: 50, // m3
    occupants: 2,
    lifeSupportLoad: 1, // unit factor
    cost: 15,
    description: 'Standard living quarters for 2 crew members.'
  },
  dormitory: {
    id: 'dormitory',
    name: 'Dormitory (8 Px)',
    mass: 25000, // kg
    volume: 180, // m3
    occupants: 8,
    lifeSupportLoad: 3,
    cost: 40,
    description: 'Bunk beds and minimal privacy for 8 crew members.'
  },
  medical: {
    id: 'medical',
    name: 'Medical Bay',
    mass: 12000, // kg
    volume: 60, // m3
    occupants: 2, // 2 patients/beds
    lifeSupportLoad: 1.5,
    cost: 35,
    description: 'Equipped with diagnostic scanners, surgical suite, and recovery beds.'
  },
  laboratory: {
    id: 'laboratory',
    name: 'Science Laboratory',
    mass: 15000, // kg
    volume: 80, // m3
    occupants: 0,
    lifeSupportLoad: 1,
    cost: 50,
    description: 'Zero-g and spin-gravity experimental benches and sensors.'
  },
  cargo: {
    id: 'cargo',
    name: 'Cargo Container',
    mass: 5000, // empty mass kg
    volume: 120, // m3
    occupants: 0,
    lifeSupportLoad: 0,
    cost: 5,
    description: 'Standard container for supplies, water reserves, and spare parts.'
  },
  animal_pen: {
    id: 'animal_pen',
    name: 'Biosphere / Animal Pen',
    mass: 14000, // kg
    volume: 100, // m3
    occupants: 0, // animals do not count toward crew capacity
    lifeSupportLoad: 2.5, // high O2/waste demand
    cost: 30,
    description: 'Maintains chickens, goats, or micro-pigs for food and ecological study.'
  },
  manufacturing: {
    id: 'manufacturing',
    name: '3D Fab Workshop',
    mass: 18000, // kg
    volume: 90, // m3
    occupants: 0,
    lifeSupportLoad: 1.2,
    cost: 45,
    description: 'Metal printers and CNC tools to manufacture replacement parts in-situ.'
  },
  drone_bay: {
    id: 'drone_bay',
    name: 'Drone Hangar',
    mass: 10000, // kg
    volume: 70, // m3
    occupants: 0,
    lifeSupportLoad: 0.2, // minimal power/comm load
    cost: 25,
    description: 'Maintains and launches autonomous repair and patrol drones.'
  },
  fuel_tank: {
    id: 'fuel_tank',
    name: 'Extra Propellant Tank',
    mass: 4000, // empty mass kg
    volume: 150, // m3
    occupants: 0,
    lifeSupportLoad: 0,
    cost: 10,
    description: 'Increases hydrogen/propellant storage capacity (mass when loaded is much higher).'
  },
  observation: {
    id: 'observation',
    name: 'Observation Cupola',
    mass: 9000, // kg
    volume: 40, // m3
    occupants: 0,
    lifeSupportLoad: 0.5,
    cost: 28,
    description: 'Large armored-glass viewing windows for crew morale and navigation.'
  },
  cafeteria: {
    id: 'cafeteria',
    name: 'Mess Hall & Galley',
    mass: 16000, // kg
    volume: 110, // m3
    occupants: 0,
    lifeSupportLoad: 2.0,
    cost: 30,
    description: 'Dining area, food prep, and social hub to boost crew morale.'
  },
  greenhouse: {
    id: 'greenhouse',
    name: 'Hydroponics Greenhouse',
    mass: 11000, // kg
    volume: 120, // m3
    occupants: 0,
    lifeSupportLoad: -1.0, // negative load! produces O2 and absorbs CO2
    cost: 32,
    description: 'Algae bioreactors and LED crop racks. Recycles air and generates food.'
  }
};

export const CREW_ROLES = {
  engineer: { id: 'engineer', name: 'Engineer', color: '#ffd54f', icon: '🔧', skill: 'Repairing and reactor management' },
  medic:    { id: 'medic',    name: 'Medical Officer', color: '#ff5252', icon: '🩺', skill: 'Healing and crew health' },
  pilot:    { id: 'pilot',    name: 'Pilot',     color: '#4fc3f7', icon: '🚀', skill: 'Navigation and spin adjustment' },
  scientist:{ id: 'scientist',name: 'Scientist', color: '#b388ff', icon: '🔬', skill: 'Research and event analysis' },
  security: { id: 'security', name: 'Security',  color: '#81c784', icon: '🛡️', skill: 'Crowd control and hazard response' },
  cook:     { id: 'cook',     name: 'Cook',      color: '#ffb74d', icon: '🍳', skill: 'Morale and food prep' },
  farmer:   { id: 'farmer',   name: 'Bio-Farmer',color: '#aed581', icon: '🌱', skill: 'Hydroponics and animal care' }
};

export const ANIMAL_TYPES = {
  chicken: { id: 'chicken', name: 'Space Chicken', color: '#d1c4e9', icon: '🐔', moraleBoost: 2 },
  goat:    { id: 'goat',    name: 'Dwarf Goat',    color: '#cfd8dc', icon: '🐐', moraleBoost: 5 },
  pig:     { id: 'pig',     name: 'Micro Pig',     color: '#f8bbd0', icon: '🐷', moraleBoost: 8 }
};

export const DRONE_TYPES = {
  welder: { id: 'welder', name: 'Welder Drone', color: '#ff9800', icon: '🤖', speed: 0.12, taskEfficiency: 0.8 },
  sensor: { id: 'sensor', name: 'Sensor Drone', color: '#00e5ff', icon: '👁️', speed: 0.20, taskEfficiency: 0.3 }
};

export const DEFAULT_CONFIG = {
  shipName: 'Falcon',
  majorRadius: 100, // m
  minorRadius: 4, // m
  spokesCount: 3, // spokes connecting axis to torus
  spokeThickness: 1.5, // m
  wallThicknessMm: 25, // structural shell thickness
  rpm: 2.5, // rotation speed
  engineType: 'ntr', // active propulsion engine
  fuelMassFraction: 0.4, // percentage of wet mass that is propellant (0.1 - 0.7)
  innerContainers: [
    { type: 'crew_cabin', pos: 0.05 },
    { type: 'dormitory', pos: 0.20 },
    { type: 'medical', pos: 0.38 },
    { type: 'greenhouse', pos: 0.55 },
    { type: 'cafeteria', pos: 0.72 },
    { type: 'cargo', pos: 0.88 }
  ],
  outerContainers: [
    { type: 'laboratory', pos: 0.10 },
    { type: 'manufacturing', pos: 0.30 },
    { type: 'drone_bay', pos: 0.48 },
    { type: 'animal_pen', pos: 0.65 },
    { type: 'fuel_tank', pos: 0.80 },
    { type: 'observation', pos: 0.92 }
  ]
};
