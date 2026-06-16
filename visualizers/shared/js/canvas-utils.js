/**
 * canvas-utils.js — Shared canvas drawing primitives
 * Aura Visualizers shared library
 */

// ── Color Helpers ─────────────────────────────────────────────

/**
 * Convert a CSS hex color to rgba() string.
 * @param {string} hex    - '#rrggbb' or '#rgb'
 * @param {number} alpha  - 0..1
 * @returns {string}
 */
export function hexToRgba(hex, alpha = 1) {
  if (!hex || hex[0] !== '#') return `rgba(128,160,200,${alpha})`;
  let h = hex.slice(1);
  if (h.length === 3) h = h.split('').map(c => c + c).join('');
  const r = parseInt(h.slice(0, 2), 16);
  const g = parseInt(h.slice(2, 4), 16);
  const b = parseInt(h.slice(4, 6), 16);
  return `rgba(${r},${g},${b},${alpha})`;
}

/**
 * Interpolate between two hex colors.
 * @param {string} hexA  - start color
 * @param {string} hexB  - end color
 * @param {number} t     - 0..1
 * @returns {string}     - rgba string
 */
export function lerpColor(hexA, hexB, t) {
  const parse = h => {
    const s = h.slice(1);
    return [parseInt(s.slice(0,2),16), parseInt(s.slice(2,4),16), parseInt(s.slice(4,6),16)];
  };
  const [r1,g1,b1] = parse(hexA);
  const [r2,g2,b2] = parse(hexB);
  const r = Math.round(r1 + (r2-r1)*t);
  const g = Math.round(g1 + (g2-g1)*t);
  const b = Math.round(b1 + (b2-b1)*t);
  return `rgb(${r},${g},${b})`;
}

/** Color for a stress level 0..1 (blue → green → yellow → red). */
export function stressColor(normalized) {
  const t = Math.min(normalized, 1);
  if (t < 0.33) return lerpColor('#00bcd4', '#69f0ae', t / 0.33);
  if (t < 0.66) return lerpColor('#69f0ae', '#ffd54f', (t - 0.33) / 0.33);
  return lerpColor('#ffd54f', '#ff5252', (t - 0.66) / 0.34);
}

// ── Drawing Primitives ────────────────────────────────────────

/**
 * Draw a filled + stroked circle (glow dot).
 */
export function drawGlowCircle(ctx, x, y, r, fillColor, glowColor = fillColor, glowBlur = 10) {
  ctx.save();
  ctx.shadowColor = glowColor;
  ctx.shadowBlur  = glowBlur;
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fillStyle = fillColor;
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.strokeStyle = 'rgba(255,255,255,0.3)';
  ctx.lineWidth = 0.8;
  ctx.stroke();
  ctx.restore();
}

/**
 * Draw a donut (annular ring) with a fill style.
 * Uses evenodd winding so the inner circle punches through.
 */
export function drawDonut(ctx, cx, cy, outerR, innerR, fillStyle) {
  ctx.beginPath();
  ctx.arc(cx, cy, outerR, 0, Math.PI * 2, false);
  ctx.arc(cx, cy, innerR, 0, Math.PI * 2, true);
  ctx.fillStyle = fillStyle;
  ctx.fill('evenodd');
}

/**
 * Stroke a donut outline (two concentric circles).
 */
export function strokeDonut(ctx, cx, cy, outerR, innerR, strokeStyle, lineWidth = 1.5) {
  ctx.strokeStyle = strokeStyle;
  ctx.lineWidth   = lineWidth;
  ctx.beginPath();
  ctx.arc(cx, cy, outerR, 0, Math.PI * 2);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(cx, cy, innerR, 0, Math.PI * 2);
  ctx.stroke();
}

/**
 * Draw a radial gradient filled circle.
 */
export function drawRadialGradientCircle(ctx, cx, cy, r, innerColor, outerColor) {
  const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, r);
  grad.addColorStop(0, innerColor);
  grad.addColorStop(1, outerColor);
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.fillStyle = grad;
  ctx.fill();
}

/**
 * Draw an arc segment (sector of a ring) — used for torus sections.
 * @param {number} startAngle - rad
 * @param {number} endAngle   - rad
 */
export function drawArcSegment(ctx, cx, cy, innerR, outerR, startAngle, endAngle, fillStyle) {
  ctx.beginPath();
  ctx.arc(cx, cy, outerR, startAngle, endAngle, false);
  ctx.arc(cx, cy, innerR, endAngle, startAngle, true);
  ctx.closePath();
  ctx.fillStyle = fillStyle;
  ctx.fill();
}

/**
 * Draw a line between two points.
 */
export function drawLine(ctx, x1, y1, x2, y2, strokeStyle, lineWidth = 1, dashed = false) {
  ctx.save();
  ctx.strokeStyle = strokeStyle;
  ctx.lineWidth   = lineWidth;
  if (dashed) ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.restore();
}

/**
 * Draw a label with a background pill.
 */
export function drawLabel(ctx, text, x, y, {
  font = "10px 'Roboto Mono', monospace",
  color = 'rgba(255,255,255,0.85)',
  bg = 'rgba(0,0,0,0.55)',
  padding = 3,
  align = 'left',
} = {}) {
  ctx.font = font;
  ctx.textAlign = align;
  ctx.textBaseline = 'middle';
  const w = ctx.measureText(text).width + padding * 2;
  const h = 14;
  const ox = align === 'center' ? -w / 2 : align === 'right' ? -w : 0;
  ctx.fillStyle = bg;
  ctx.beginPath();
  ctx.roundRect(x + ox - padding, y - h / 2, w, h, 3);
  ctx.fill();
  ctx.fillStyle = color;
  ctx.fillText(text, x, y);
}

/**
 * Draw a scale bar (length indicator) on the canvas.
 */
export function drawScaleBar(ctx, x, y, metres, scale, color = 'rgba(255,255,255,0.45)') {
  const px = metres * scale;
  ctx.strokeStyle = color;
  ctx.lineWidth   = 1.5;
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x + px, y);
  ctx.stroke();
  // End ticks
  [x, x + px].forEach(tx => {
    ctx.beginPath();
    ctx.moveTo(tx, y - 3);
    ctx.lineTo(tx, y + 3);
    ctx.stroke();
  });
  ctx.font = "9px 'Roboto Mono', monospace";
  ctx.fillStyle = color;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'top';
  ctx.fillText(`${metres} m`, x + px / 2, y + 5);
}

/**
 * Draw an animated particle burst (used for leaks, explosions).
 * Returns the particles array to track them.
 */
export function createParticleBurst(cx, cy, count, {
  speed    = [1, 4],
  life     = [1.5, 3.5],
  angleSpread = Math.PI * 2,
  baseAngle   = 0,
  color = 'rgba(79,195,247,0.8)',
} = {}) {
  return Array.from({ length: count }, (_, i) => {
    const angle = baseAngle + (i / count) * angleSpread + (Math.random() - 0.5) * 0.5;
    const spd   = speed[0] + Math.random() * (speed[1] - speed[0]);
    return {
      x: cx, y: cy,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      life: life[0] + Math.random() * (life[1] - life[0]),
      born: 0,
      color,
    };
  });
}

/**
 * Update and draw particles. dt in seconds.
 * Returns filtered array (removes dead particles).
 */
export function updateParticles(ctx, particles, dt, scale = 1) {
  return particles.filter(p => {
    p.born += dt;
    if (p.born >= p.life) return false;
    p.x += p.vx * dt * scale;
    p.y += p.vy * dt * scale;
    const progress = p.born / p.life;
    const alpha    = (1 - progress) * 0.85;
    const r        = Math.max(0.5, 2.5 * (1 - progress));
    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fillStyle = p.color.replace(/[\d.]+\)$/, `${alpha.toFixed(2)})`);
    ctx.fill();
    return true;
  });
}

/**
 * Draw a pulsing ring (used for event/disaster markers).
 */
export function drawPulseRing(ctx, cx, cy, baseR, phase, color) {
  const r = baseR + Math.sin(phase) * baseR * 0.25;
  const alpha = 0.3 + Math.sin(phase) * 0.3;
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.strokeStyle = color.replace(/[\d.]+\)$/, `${alpha.toFixed(2)})`);
  ctx.lineWidth = 2;
  ctx.stroke();
}

/**
 * Draw a role-colored crew entity with a health ring.
 */
export function drawCrewDot(ctx, x, y, size, roleColor, health, selected = false, moving = false) {
  // Glow when selected
  if (selected) {
    ctx.save();
    ctx.shadowColor = 'white';
    ctx.shadowBlur  = 12;
  }
  // Health ring
  const healthAngle = (health / 100) * Math.PI * 2 - Math.PI / 2;
  ctx.beginPath();
  ctx.arc(x, y, size + 2, -Math.PI / 2, healthAngle);
  ctx.strokeStyle = health > 70 ? '#69f0ae' : health > 40 ? '#ffd54f' : '#ff5252';
  ctx.lineWidth = 2;
  ctx.stroke();
  // Body
  ctx.beginPath();
  ctx.arc(x, y, size, 0, Math.PI * 2);
  ctx.fillStyle = roleColor;
  ctx.fill();
  if (selected) ctx.restore();
  // Moving indicator
  if (moving) {
    ctx.beginPath();
    ctx.arc(x, y, size * 0.35, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(255,255,255,0.8)';
    ctx.fill();
  }
}

// ── Coordinate Helpers ────────────────────────────────────────

/**
 * Convert a torus position (fraction 0-1) to canvas XY.
 * @param {number} pos    - 0..1 (fraction of full circle)
 * @param {number} radius - m, torus major radius
 * @param {number} cx     - canvas centre X px
 * @param {number} cy     - canvas centre Y px
 * @param {number} scale  - px per metre
 */
export function torusToCanvas(pos, radius, cx, cy, scale) {
  const angle = pos * Math.PI * 2 - Math.PI / 2;
  return {
    x: cx + Math.cos(angle) * radius * scale,
    y: cy + Math.sin(angle) * radius * scale,
  };
}

/**
 * Hit-test whether a canvas point (px, py) is within a torus entity dot.
 */
export function hitTestTorus(px, py, pos, radius, cx, cy, scale, hitRadius = 10) {
  const { x, y } = torusToCanvas(pos, radius, cx, cy, scale);
  return Math.hypot(px - x, py - y) <= hitRadius;
}

/**
 * Get the angular position (0..1) on the torus closest to a canvas point.
 */
export function canvasToTorusPos(px, py, cx, cy) {
  const angle = Math.atan2(py - cy, px - cx) + Math.PI / 2;
  return ((angle / (Math.PI * 2)) + 1) % 1;
}
