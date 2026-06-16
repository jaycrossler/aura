/**
 * renderer.js — Station visualizer rendering logic (3 views)
 * Aura Space Station Simulator (Falcon)
 */

import * as canv from '../../shared/js/canvas-utils.js';
import { CONTAINER_TYPES } from './constants.js';

export class StationRenderer {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.view = 'torus'; // 'torus' | 'profile' | 'comfort'
    this.spinAngle = 0; // cumulative rotation phase
    
    // Animation particle systems
    this.particles = [];
  }

  resize() {
    const rect = this.canvas.parentElement.getBoundingClientRect();
    this.canvas.width = rect.width * window.devicePixelRatio;
    this.canvas.height = rect.height * window.devicePixelRatio;
    this.canvas.style.width = `${rect.width}px`;
    this.canvas.style.height = `${rect.height}px`;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  setView(viewName) {
    this.view = viewName;
  }

  draw(config, computed, state) {
    const ctx = this.ctx;
    const w = this.canvas.width / window.devicePixelRatio;
    const h = this.canvas.height / window.devicePixelRatio;

    // Clear background
    ctx.fillStyle = '#05070c';
    ctx.fillRect(0, 0, w, h);

    if (!computed) return;

    if (this.view === 'torus') {
      this.drawTorusView(ctx, w, h, config, computed, state);
    } else if (this.view === 'profile') {
      this.drawProfileView(ctx, w, h, config, computed, state);
    } else if (this.view === 'comfort') {
      this.drawComfortView(ctx, w, h, config, computed, state);
    }
  }

  drawTorusView(ctx, w, h, config, computed, state) {
    let cx = w / 2;
    let cy = h / 2;
    
    // Auto-fit radius to screen size
    const maxRadiusPx = Math.min(w, h) * 0.4;
    // Let's create a scale where max majorRadius is 150m.
    const scale = maxRadiusPx / 150; // px per meter

    // Visualise wobble strain by dynamically oscillating the hub center (cx, cy)
    if (computed.imbalanceShift > 2.0 && !state.paused) {
      // wobble frequency matches the spin rate (rpm)
      const omega = (config.rpm / 60) * Math.PI * 2;
      const wobbleRadius = Math.min(15, computed.imbalanceShift * 0.8 * scale);
      cx += Math.cos(state.time * omega * 2) * wobbleRadius;
      cy += Math.sin(state.time * omega * 2) * wobbleRadius;
    }

    const rMajor = config.majorRadius * scale;
    const rMinor = config.minorRadius * scale;
    
    // Draw starfield background or ambient grid
    this.drawBackgroundGrid(ctx, w, h);

    // If imbalances are high, draw warning overlay for lopsided center of mass
    if (computed.imbalanceShift > 2.0) {
      ctx.save();
      ctx.strokeStyle = 'rgba(255, 82, 82, 0.2)';
      ctx.lineWidth = 1;
      ctx.setLineDash([2, 4]);
      ctx.beginPath();
      ctx.arc(w / 2, h / 2, computed.imbalanceShift * scale, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = '#ff5252';
      ctx.beginPath();
      ctx.arc(w / 2 + Math.cos(this.spinAngle) * computed.imbalanceShift * scale, h / 2 + Math.sin(this.spinAngle) * computed.imbalanceShift * scale, 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }

    // Update spin angle based on RPM
    if (!state.paused) {
      // RPM = rot / min => rot / sec = RPM / 60 => rad / sec = (RPM / 60) * 2pi
      const radPerSec = (config.rpm / 60) * Math.PI * 2;
      this.spinAngle += radPerSec * 0.016 * state.speed;
    }

    // 1. Draw connecting spokes
    const spokeRad = config.spokeThickness * scale;
    ctx.strokeStyle = '#263238';
    ctx.lineWidth = spokeRad;
    for (let i = 0; i < config.spokesCount; i++) {
      const angle = this.spinAngle + (i / config.spokesCount) * Math.PI * 2;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + Math.cos(angle) * rMajor, cy + Math.sin(angle) * rMajor);
      ctx.stroke();
    }

    // 2. Draw outer & inner torus tube rings
    // Inner tube radius is rMajor - rMinor, Outer is rMajor + rMinor
    const rInner = rMajor - rMinor;
    const rOuter = rMajor + rMinor;

    ctx.save();
    // Torus fill (radial ambient gradient for depth)
    canv.drawDonut(ctx, cx, cy, rOuter, rInner, '#0d131f');
    // Rim outlines
    canv.strokeDonut(ctx, cx, cy, rOuter, rInner, '#1d2a45', 2.0);
    // Grid center line
    ctx.strokeStyle = 'rgba(79, 195, 247, 0.05)';
    ctx.lineWidth = 1;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.arc(cx, cy, rMajor, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.restore();

    // 3. Draw engine thrust effect at hub if engines are active (not paused)
    this.drawEngineAtHub(ctx, cx, cy, scale, config.engineType, state.paused);

    // 4. Draw containers as segments
    this.drawContainers(ctx, cx, cy, rMajor, rMinor, scale, config.innerContainers, 'inner');
    this.drawContainers(ctx, cx, cy, rMajor, rMinor, scale, config.outerContainers, 'outer');

    // 5. Draw entities (Crew, Animals, Drones)
    this.drawEntities(ctx, cx, cy, rMajor, rMinor, scale, state);

    // 6. Draw active disasters & particle leaks
    this.drawDisasters(ctx, cx, cy, rMajor, rMinor, scale, state);

    // 7. Scale Indicator
    canv.drawScaleBar(ctx, 30, h - 35, 50, scale);
  }

  drawBackgroundGrid(ctx, w, h) {
    ctx.strokeStyle = 'rgba(30, 45, 80, 0.1)';
    ctx.lineWidth = 1;
    const step = 40;
    
    ctx.beginPath();
    for (let x = 0; x < w; x += step) {
      ctx.moveTo(x, 0); ctx.lineTo(x, h);
    }
    for (let y = 0; y < h; y += step) {
      ctx.moveTo(0, y); ctx.lineTo(w, y);
    }
    ctx.stroke();
  }

  drawEngineAtHub(ctx, cx, cy, scale, engineType, isPaused) {
    const hubRad = 15 * scale;
    // Hub cylinder
    ctx.beginPath();
    ctx.arc(cx, cy, hubRad, 0, Math.PI * 2);
    ctx.fillStyle = '#212936';
    ctx.fill();
    ctx.strokeStyle = '#37474f';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Reactor core glow
    const glowRad = hubRad * 0.5;
    const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, glowRad);
    
    let coreColor = '#4fc3f7';
    if (engineType === 'vasimr') coreColor = '#b388ff';
    if (engineType === 'chemical') coreColor = '#ffb74d';
    if (engineType === 'bimodal') coreColor = '#81c784';

    grad.addColorStop(0, coreColor);
    grad.addColorStop(1, 'rgba(0,0,0,0)');
    
    ctx.beginPath();
    ctx.arc(cx, cy, glowRad, 0, Math.PI * 2);
    ctx.fillStyle = grad;
    ctx.fill();
  }

  drawContainers(ctx, cx, cy, rMajor, rMinor, scale, containerList, rim) {
    const hullRadius = rim === 'inner' ? rMajor - rMinor : rMajor + rMinor;
    // Set container radial offset (inner containers hang inside, outer hang outside)
    const radialOffset = rim === 'inner' ? -3 * scale : 3 * scale;
    const arcRadius = hullRadius + radialOffset;
    const containerW = 5 * scale; // thickness radial
    
    containerList.forEach(c => {
      const typeInfo = CONTAINER_TYPES[c.type];
      if (!typeInfo) return;

      // Container covers a small angular span based on size
      const angularSpan = (typeInfo.volume / 800) * Math.PI * 0.15; 
      const centerAngle = this.spinAngle + c.pos * Math.PI * 2 - Math.PI / 2;
      const startAngle = centerAngle - angularSpan / 2;
      const endAngle = centerAngle + angularSpan / 2;

      const innerArcR = arcRadius - containerW / 2;
      const outerArcR = arcRadius + containerW / 2;

      ctx.save();
      
      // 1. Draw attachment struts/brackets connecting container to the hull rim
      ctx.strokeStyle = '#546e7a';
      ctx.lineWidth = 1.5;
      
      // Left bracket anchor
      const lCos = Math.cos(startAngle);
      const lSin = Math.sin(startAngle);
      ctx.beginPath();
      ctx.moveTo(cx + lCos * hullRadius, cy + lSin * hullRadius);
      ctx.lineTo(cx + lCos * arcRadius, cy + lSin * arcRadius);
      ctx.stroke();

      // Right bracket anchor
      const rCos = Math.cos(endAngle);
      const rSin = Math.sin(endAngle);
      ctx.beginPath();
      ctx.moveTo(cx + rCos * hullRadius, cy + rSin * hullRadius);
      ctx.lineTo(cx + rCos * arcRadius, cy + rSin * arcRadius);
      ctx.stroke();

      // Bolt circles at anchors
      ctx.fillStyle = '#90a4ae';
      [startAngle, endAngle].forEach(ang => {
        const hx = cx + Math.cos(ang) * hullRadius;
        const hy = cy + Math.sin(ang) * hullRadius;
        ctx.beginPath();
        ctx.arc(hx, hy, 2, 0, Math.PI * 2);
        ctx.fill();
      });

      // 2. Set distinct color per compartment category
      let compColor = 'rgba(79, 110, 138, 0.55)';
      if (c.type.includes('crew') || c.type.includes('dormitory')) compColor = 'rgba(100, 255, 218, 0.45)';
      if (c.type.includes('greenhouse')) compColor = 'rgba(129, 199, 132, 0.45)';
      if (c.type.includes('medical')) compColor = 'rgba(239, 83, 80, 0.45)';
      if (c.type.includes('fuel')) compColor = 'rgba(255, 183, 77, 0.45)';
      if (c.type.includes('observation')) compColor = 'rgba(79, 195, 247, 0.65)';

      canv.drawArcSegment(ctx, cx, cy, innerArcR, outerArcR, startAngle, endAngle, compColor);
      
      // 3. Draw container outline rib details
      ctx.strokeStyle = 'rgba(255,255,255,0.35)';
      ctx.lineWidth = 1;
      
      // outer border
      ctx.beginPath();
      ctx.arc(cx, cy, outerArcR, startAngle, endAngle, false);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx, cy, innerArcR, startAngle, endAngle, false);
      ctx.stroke();
      
      // end caps
      ctx.beginPath();
      ctx.moveTo(cx + lCos * innerArcR, cy + lSin * innerArcR);
      ctx.lineTo(cx + lCos * outerArcR, cy + lSin * outerArcR);
      ctx.moveTo(cx + rCos * innerArcR, cy + rSin * innerArcR);
      ctx.lineTo(cx + rCos * outerArcR, cy + rSin * outerArcR);
      ctx.stroke();

      // internal ribbed partitions to emphasize shipping container modular structure
      ctx.strokeStyle = 'rgba(255,255,255,0.15)';
      const segments = 3;
      for (let i = 1; i < segments; i++) {
        const segAngle = startAngle + (i / segments) * angularSpan;
        const sCos = Math.cos(segAngle);
        const sSin = Math.sin(segAngle);
        ctx.beginPath();
        ctx.moveTo(cx + sCos * innerArcR, cy + sSin * innerArcR);
        ctx.lineTo(cx + sCos * outerArcR, cy + sSin * outerArcR);
        ctx.stroke();
      }

      // 4. Draw emoji icon label for FTL visual feel inside container segment
      ctx.font = '8px sans-serif';
      ctx.fillStyle = 'rgba(255,255,255,0.7)';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      const labelRadius = (innerArcR + outerArcR) / 2;
      const lx = cx + Math.cos(centerAngle) * labelRadius;
      const ly = cy + Math.sin(centerAngle) * labelRadius;
      
      let containerEmoji = '📦';
      if (c.type.includes('crew') || c.type.includes('dormitory')) containerEmoji = '🏠';
      if (c.type.includes('greenhouse')) containerEmoji = '🌿';
      if (c.type.includes('medical')) containerEmoji = '❤️';
      if (c.type.includes('fuel')) containerEmoji = '🔥';
      if (c.type.includes('observation')) containerEmoji = '👁️';
      if (c.type.includes('lab')) containerEmoji = '🧪';
      if (c.type.includes('manufacturing')) containerEmoji = '⚙️';
      if (c.type.includes('drone')) containerEmoji = '🤖';
      if (c.type.includes('animal')) containerEmoji = '🐖';
      
      ctx.fillText(containerEmoji, lx, ly);

      ctx.restore();
    });
  }

  drawEntities(ctx, cx, cy, rMajor, rMinor, scale, state) {
    const drawList = (list) => {
      list.forEach(ent => {
        const radius = ent.rim === 'inner' ? rMajor - rMinor + 2 : rMajor + rMinor - 2;
        // Absolute angular coordinate on circle
        const angle = this.spinAngle + ent.pos * Math.PI * 2 - Math.PI / 2;
        const x = cx + Math.cos(angle) * radius;
        const y = cy + Math.sin(angle) * radius;
        
        const isSelected = state.selectedEntity && state.selectedEntity.id === ent.id;
        
        if (ent.type === 'crew') {
          canv.drawCrewDot(ctx, x, y, 5, ent.color, ent.health, isSelected, ent.moving);
        } else {
          // Animal or Drone
          ctx.font = '10px sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(ent.icon, x, y);
          
          if (isSelected) {
            ctx.beginPath();
            ctx.arc(x, y, 7, 0, Math.PI * 2);
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      });
    };

    drawList(state.crew);
    drawList(state.animals);
    drawList(state.drones);
  }

  drawDisasters(ctx, cx, cy, rMajor, rMinor, scale, state) {
    const timeSec = state.time;
    
    state.activeDisasters.forEach(disaster => {
      const radius = disaster.rim === 'inner' ? rMajor - rMinor : rMajor + rMinor;
      const angle = this.spinAngle + disaster.pos * Math.PI * 2 - Math.PI / 2;
      const x = cx + Math.cos(angle) * radius;
      const y = cy + Math.sin(angle) * radius;

      // Draw pulse warning ring
      canv.drawPulseRing(ctx, x, y, 16, timeSec * 6, disaster.color);

      // Hazard icon
      ctx.font = '12px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(disaster.icon, x, y - 1);

      // Warning text tag above
      ctx.font = '9px monospace';
      ctx.fillStyle = '#ff5252';
      ctx.fillText(`${disaster.progress.toFixed(0)}%`, x, y - 14);

      // Spawn leak particle spray
      if (!state.paused) {
        if (disaster.type === 'air_leak' || disaster.type === 'water_leak') {
          disaster.particleSpawnTimer -= 0.016 * state.speed;
          if (disaster.particleSpawnTimer <= 0) {
            disaster.particleSpawnTimer = 0.1; // reset spawn interval
            
            // Spray direction points outward or inward depending on breach
            const sprayAngle = disaster.rim === 'outer' ? angle : angle + Math.PI;
            const spray = canv.createParticleBurst(x, y, 3, {
              speed: [30, 80],
              life: [0.6, 1.2],
              angleSpread: 0.4,
              baseAngle: sprayAngle,
              color: disaster.color
            });
            this.particles.push(...spray);
          }
        }
      }
    });

    // Update and draw live particles
    if (this.particles.length > 0) {
      this.particles = canv.updateParticles(ctx, this.particles, 0.016 * state.speed, scale);
    }
  }

  drawProfileView(ctx, w, h, config, computed, state) {
    // Render side-on cross section showing the central spire/hub and the spoke + torus profile
    const cx = w / 2;
    const cy = h / 2;
    const scale = (h * 0.4) / 120; // scale factor to fit

    const rad = config.majorRadius * scale;
    const minorRad = config.minorRadius * scale;

    ctx.save();
    this.drawBackgroundGrid(ctx, w, h);

    // Draw central axis rod
    ctx.strokeStyle = '#263238';
    ctx.lineWidth = 14;
    ctx.beginPath();
    ctx.moveTo(cx, cy - 80);
    ctx.lineTo(cx, cy + 80);
    ctx.stroke();

    // Spokes profile extending horizontally to left and right rims
    ctx.lineWidth = config.spokeThickness * scale;
    ctx.beginPath();
    ctx.moveTo(cx - rad, cy);
    ctx.lineTo(cx + rad, cy);
    ctx.stroke();

    // Left and Right Torus Cross-sections (cut circles)
    const drawCrossSection = (xPos) => {
      // Outer rim
      ctx.beginPath();
      ctx.arc(xPos, cy, minorRad, 0, Math.PI * 2);
      ctx.fillStyle = '#0d131f';
      ctx.fill();
      ctx.strokeStyle = '#1d2a45';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Show levels/floors inside cross section
      ctx.beginPath();
      // floor of outer rim (at maximum radius)
      ctx.arc(xPos, cy, minorRad - 1, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(79, 195, 247, 0.15)';
      ctx.stroke();
    };

    drawCrossSection(cx - rad);
    drawCrossSection(cx + rad);

    // Label dimensions
    ctx.fillStyle = 'rgba(255,255,255,0.7)';
    ctx.font = '10px monospace';
    ctx.textAlign = 'center';
    
    // Spire label
    ctx.fillText('Central Command Spire', cx, cy - 90);
    // Spokes label
    ctx.fillText(`${config.spokesCount} Structural Spokes`, cx, cy + 25);
    // Torus width label
    ctx.fillText(`Torus Tube r = ${config.minorRadius}m`, cx + rad, cy + minorRad + 15);
    // Total diameter label
    ctx.fillText(`Total Diameter = ${(config.majorRadius * 2).toFixed(0)}m`, cx, cy + 110);
    ctx.restore();
  }

  drawComfortView(ctx, w, h, config, computed, state) {
    // Draws comfort boundaries diagram (RPM vs Gravity)
    const padding = 50;
    const graphW = w - padding * 2;
    const graphH = h - padding * 2;

    ctx.save();
    // Graph area background
    ctx.fillStyle = '#0a0d16';
    ctx.fillRect(padding, padding, graphW, graphH);

    // Grid lines & labels
    ctx.strokeStyle = 'rgba(255,255,255,0.05)';
    ctx.lineWidth = 1;
    ctx.fillStyle = 'rgba(255,255,255,0.5)';
    ctx.font = '9px monospace';

    // Draw X axis (0 - 1.5 g)
    const xMaxG = 1.5;
    for (let g = 0; g <= xMaxG; g += 0.25) {
      const x = padding + (g / xMaxG) * graphW;
      ctx.beginPath();
      ctx.moveTo(x, padding);
      ctx.lineTo(x, padding + graphH);
      ctx.stroke();
      ctx.textAlign = 'center';
      ctx.fillText(`${g}g`, x, padding + graphH + 15);
    }

    // Draw Y axis (0 - 8 RPM)
    const yMaxRpm = 8;
    for (let r = 0; r <= yMaxRpm; r += 1) {
      const y = padding + graphH - (r / yMaxRpm) * graphH;
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(padding + graphW, y);
      ctx.stroke();
      ctx.textAlign = 'right';
      ctx.fillText(`${r} RPM`, padding - 10, y + 3);
    }

    // Draw Comfort Zones boundaries
    // RPM < 2.0 (Green / Excellent)
    const y2RPM = padding + graphH - (2.0 / yMaxRpm) * graphH;
    ctx.fillStyle = 'rgba(105, 240, 174, 0.05)';
    ctx.fillRect(padding, y2RPM, graphW, padding + graphH - y2RPM);

    // RPM 2.0 to 4.0 (Yellow / Moderate Adaptation)
    const y4RPM = padding + graphH - (4.0 / yMaxRpm) * graphH;
    ctx.fillStyle = 'rgba(255, 213, 79, 0.03)';
    ctx.fillRect(padding, y4RPM, graphW, y2RPM - y4RPM);

    // Current operating point dot
    const currentG = computed.outerG;
    const currentRpm = config.rpm;

    const dotX = padding + (currentG / xMaxG) * graphW;
    const dotY = padding + graphH - (currentRpm / yMaxRpm) * graphH;

    // Pulse dot
    const pulseRadius = 6 + Math.sin(state.time * 5) * 2;
    ctx.beginPath();
    ctx.arc(dotX, dotY, pulseRadius, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(0, 229, 255, 0.25)';
    ctx.fill();

    ctx.beginPath();
    ctx.arc(dotX, dotY, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#00e5ff';
    ctx.fill();

    // Line pointing to axes
    ctx.strokeStyle = '#00e5ff';
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(dotX, dotY);
    ctx.lineTo(padding, dotY);
    ctx.moveTo(dotX, dotY);
    ctx.lineTo(dotX, padding + graphH);
    ctx.stroke();
    ctx.setLineDash([]);

    // Label of dot
    ctx.font = '10px monospace';
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'left';
    ctx.fillText(`Operating Point (${currentG.toFixed(2)}g @ ${currentRpm.toFixed(1)} RPM)`, dotX + 10, dotY - 5);

    // Axis titles
    ctx.font = '11px sans-serif';
    ctx.fillStyle = 'rgba(255,255,255,0.7)';
    ctx.textAlign = 'center';
    ctx.fillText('Effective Centrifugal Gravity (g)', padding + graphW / 2, padding + graphH + 32);
    
    ctx.save();
    ctx.translate(padding - 35, padding + graphH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('Rotation Speed (RPM)', 0, 0);
    ctx.restore();

    ctx.restore();
  }
}
