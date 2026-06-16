/**
 * ui-utils.js — Shared DOM helpers and EventBus
 * Aura Visualizers shared library
 */

// ── EventBus ──────────────────────────────────────────────────

/**
 * Lightweight publish/subscribe event bus.
 * @example
 *   bus.on('config:changed', data => console.log(data));
 *   bus.emit('config:changed', { key: 'rpm', value: 3 });
 */
export class EventBus {
  constructor() {
    /** @type {Map<string, Set<Function>>} */
    this._listeners = new Map();
  }

  /**
   * Subscribe to an event.
   * @param {string}   event
   * @param {Function} callback
   * @returns {Function} unsubscribe function
   */
  on(event, callback) {
    if (!this._listeners.has(event)) this._listeners.set(event, new Set());
    this._listeners.get(event).add(callback);
    return () => this.off(event, callback);
  }

  /** Unsubscribe from an event. */
  off(event, callback) {
    this._listeners.get(event)?.delete(callback);
  }

  /** Emit an event with optional data payload. */
  emit(event, data) {
    this._listeners.get(event)?.forEach(cb => {
      try { cb(data); } catch (e) { console.error(`EventBus error [${event}]:`, e); }
    });
  }

  /** Remove all listeners. */
  clear() { this._listeners.clear(); }
}

// ── DOM Helpers ───────────────────────────────────────────────

/** Set textContent of element by ID (no-op if element doesn't exist). */
export function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

/** Set innerHTML of element by ID. */
export function setHtml(id, html) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = html;
}

/** Set a CSS style on element by ID. */
export function setStyle(id, prop, value) {
  const el = document.getElementById(id);
  if (el) el.style[prop] = value;
}

/** Set the value of an input element by ID. */
export function setInputValue(id, value) {
  const el = document.getElementById(id);
  if (el) el.value = value;
}

/** Show an element (removes .hidden class). */
export function show(idOrEl) {
  const el = typeof idOrEl === 'string' ? document.getElementById(idOrEl) : idOrEl;
  el?.classList.remove('hidden');
}

/** Hide an element (adds .hidden class). */
export function hide(idOrEl) {
  const el = typeof idOrEl === 'string' ? document.getElementById(idOrEl) : idOrEl;
  el?.classList.add('hidden');
}

/** Toggle element visibility. Returns new visibility state. */
export function toggle(id) {
  const el = document.getElementById(id);
  if (!el) return false;
  el.classList.toggle('hidden');
  return !el.classList.contains('hidden');
}

/** Set the width of an element's fill bar (0-100 %). */
export function setBarWidth(fillId, pct, color) {
  const el = document.getElementById(fillId);
  if (!el) return;
  el.style.width = `${Math.max(0, Math.min(100, pct))}%`;
  if (color) el.style.background = color;
}

/** Update a range slider value and its background gradient. */
export function updateSlider(el, value) {
  if (!el) return;
  el.value = value;
  const min = parseFloat(el.min || 0);
  const max = parseFloat(el.max || 100);
  const pct = ((value - min) / (max - min)) * 100;
  el.style.setProperty('--pct', `${pct.toFixed(1)}%`);
}

/** Bind a range slider with live label update. Returns cleanup fn. */
export function bindSlider(sliderId, labelId, { decimals = 0, multiplier = 1, onChange } = {}) {
  const slider = document.getElementById(sliderId);
  const label  = document.getElementById(labelId);
  if (!slider) return () => {};

  const update = () => {
    const v = parseFloat(slider.value) * multiplier;
    if (label) label.textContent = v.toFixed(decimals);
    updateSlider(slider, parseFloat(slider.value));
    onChange?.(parseFloat(slider.value));
  };

  slider.addEventListener('input', update);
  update(); // initialise
  return () => slider.removeEventListener('input', update);
}

// ── Color helpers ─────────────────────────────────────────────

/** Return a status color based on a 0-1 normalised value (good → bad). */
export function statusColor(t) {
  if (t < 0.5) return 'var(--status-ok)';
  if (t < 0.8) return 'var(--status-warn)';
  return 'var(--status-crit)';
}

/** Return 'ok' | 'warn' | 'crit' class name based on normalised 0-1. */
export function statusClass(t) {
  if (t < 0.5) return 'ok';
  if (t < 0.8) return 'warn';
  return 'crit';
}

// ── Misc utilities ────────────────────────────────────────────

/**
 * Debounce a function — only calls it after `wait` ms of inactivity.
 */
export function debounce(fn, wait = 100) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), wait);
  };
}

/**
 * Throttle a function — calls at most once per `interval` ms.
 */
export function throttle(fn, interval = 100) {
  let last = 0;
  return (...args) => {
    const now = Date.now();
    if (now - last >= interval) { last = now; fn(...args); }
  };
}

/**
 * Clamp a number between min and max.
 */
export function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

/**
 * Linear interpolate from a to b by t (0..1).
 */
export function lerp(a, b, t) {
  return a + (b - a) * t;
}

/**
 * Move `current` toward `target` by `step`, without overshoot.
 * Useful for smooth entity movement.
 */
export function moveToward(current, target, step) {
  const diff = target - current;
  if (Math.abs(diff) <= step) return target;
  return current + Math.sign(diff) * step;
}

/**
 * Move `currentAngle` toward `targetAngle` on a 0-1 wrap-around circle,
 * always taking the shorter arc.
 * @param {number} speed - revolutions per second
 * @param {number} dt    - delta time in seconds
 * @returns {number}     - new angle (0..1)
 */
export function moveTowardOnRing(currentAngle, targetAngle, speed, dt) {
  let diff = ((targetAngle - currentAngle + 1.5) % 1.0) - 0.5;
  const step = speed * dt;
  if (Math.abs(diff) <= step) return targetAngle;
  return ((currentAngle + Math.sign(diff) * step) + 1.0) % 1.0;
}

/**
 * Format a game-time value (seconds) as HH:MM:SS or D HH:MM.
 */
export function formatGameTime(seconds) {
  const s  = Math.floor(seconds % 60);
  const m  = Math.floor((seconds / 60) % 60);
  const h  = Math.floor((seconds / 3600) % 24);
  const d  = Math.floor(seconds / 86400);
  if (d > 0) return `Day ${d}  ${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}`;
  return `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}

/**
 * Append a new row to a log element, capping at maxRows.
 */
export function appendLog(containerId, timeStr, message, cssClass = '') {
  const container = document.getElementById(containerId);
  if (!container) return;

  const div = document.createElement('div');
  div.className = 'log-entry anim-fadeIn';
  div.innerHTML =
    `<span class="log-time">${timeStr}</span>` +
    `<span class="log-message ${cssClass}">${message}</span>`;
  container.prepend(div);

  // Cap at 60 entries
  while (container.children.length > 60) {
    container.removeChild(container.lastChild);
  }
}

/**
 * Generate a random name from a seed list (for crew names).
 */
const FIRST_NAMES = [
  'Avery','Blake','Chen','Dakota','Elena','Finn','Gao','Harper','Ines','Jin',
  'Kai','Lena','Marco','Noa','Osei','Pita','Quinn','Reza','Suki','Theo',
  'Uma','Vega','Wren','Xiao','Yuki','Zara','Amir','Bex','Cyra','Dex',
];
const LAST_NAMES = [
  'Okonkwo','Petrov','Nakamura','Singh','Martinez','Erikson','Adeyemi','Park',
  'Torres','Müller','Nakamura','Johansson','Kapoor','Santos','Reyes','Weber',
  'Ibrahim','Papadopoulos','Nguyen','Kowalski',
];
let _nameIndex = 0;
export function randomName() {
  const first = FIRST_NAMES[_nameIndex % FIRST_NAMES.length];
  const last  = LAST_NAMES[Math.floor(_nameIndex / FIRST_NAMES.length) % LAST_NAMES.length];
  _nameIndex++;
  return `${first} ${last}`;
}

/** Simple seeded pseudo-random (deterministic for reproducible tests). */
export function seededRandom(seed) {
  let s = seed;
  return () => {
    s = (s * 1664525 + 1013904223) & 0xffffffff;
    return (s >>> 0) / 0x100000000;
  };
}
