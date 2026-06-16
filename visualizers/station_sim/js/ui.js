/**
 * ui.js — UIManager class binding inputs and rendering reports
 * Aura Space Station Simulator (Falcon)
 */

import { updateConfig, updateConfigBatch, gameState, bus, shipConfig } from './state.js';
import { ENGINE_TYPES, CONTAINER_TYPES } from './constants.js';
import * as ui from '../../shared/js/ui-utils.js';
import { fmt, fmtTime } from '../../shared/js/physics-utils.js';

export class UIManager {
  constructor() {
    this.selectedEntity = null;
  }

  init() {
    this.bindControls();
    this.setupListeners();
  }

  bindControls() {
    // 1. Text input for Ship Name
    const nameInput = document.getElementById('ship-name-input');
    if (nameInput) {
      nameInput.value = shipConfig.shipName;
      nameInput.addEventListener('input', (e) => {
        updateConfig('shipName', e.target.value || 'Falcon');
      });
    }

    // 2. Physical geometry sliders
    ui.bindSlider('major-radius-slider', 'major-radius-val', {
      onChange: (v) => updateConfig('majorRadius', v)
    });
    ui.bindSlider('minor-radius-slider', 'minor-radius-val', {
      onChange: (v) => updateConfig('minorRadius', v)
    });
    ui.bindSlider('spokes-slider', 'spokes-val', {
      onChange: (v) => updateConfig('spokesCount', v)
    });
    ui.bindSlider('spoke-thickness-slider', 'spoke-thickness-val', {
      decimals: 1,
      onChange: (v) => updateConfig('spokeThickness', v)
    });
    ui.bindSlider('wall-thickness-slider', 'wall-thickness-val', {
      onChange: (v) => updateConfig('wallThicknessMm', v)
    });
    ui.bindSlider('rpm-slider', 'rpm-val', {
      decimals: 1,
      onChange: (v) => updateConfig('rpm', v)
    });
    ui.bindSlider('fuel-fraction-slider', 'fuel-fraction-val', {
      decimals: 2,
      onChange: (v) => updateConfig('fuelMassFraction', v)
    });

    // 3. Engine type selectors
    const engineContainer = document.getElementById('engine-selector-container');
    if (engineContainer) {
      engineContainer.innerHTML = '';
      Object.keys(ENGINE_TYPES).forEach(key => {
        const eng = ENGINE_TYPES[key];
        const btn = document.createElement('button');
        btn.className = `pill-btn ${shipConfig.engineType === key ? 'active' : ''}`;
        btn.id = `btn-engine-${key}`;
        btn.textContent = eng.name;
        btn.addEventListener('click', () => {
          // deactivate siblings
          engineContainer.querySelectorAll('button').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          updateConfig('engineType', key);
        });
        engineContainer.appendChild(btn);
      });
    }

    // 4. View Tabs
    const tabs = document.querySelectorAll('.tab-btn');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        bus.emit('view:changed', tab.dataset.view);
      });
    });

    // 5. Game speed controls
    document.getElementById('btn-play')?.addEventListener('click', () => bus.emit('game:control', 'play'));
    document.getElementById('btn-pause')?.addEventListener('click', () => bus.emit('game:control', 'pause'));
    document.getElementById('btn-speed-1x')?.addEventListener('click', () => bus.emit('game:control', 'speed-1'));
    document.getElementById('btn-speed-5x')?.addEventListener('click', () => bus.emit('game:control', 'speed-5'));

    // 6. Action: Disaster trigger simulation
    document.getElementById('btn-trigger-leak')?.addEventListener('click', () => bus.emit('action:trigger-disaster', 'air_leak'));
    document.getElementById('btn-trigger-stress')?.addEventListener('click', () => bus.emit('action:trigger-disaster', 'structural_stress'));
    document.getElementById('btn-trigger-fire')?.addEventListener('click', () => bus.emit('action:trigger-disaster', 'engine_failure'));

    // 7. Click listener on canvas for entity selection
    const canvas = document.getElementById('visualizer-canvas');
    if (canvas) {
      canvas.addEventListener('click', (e) => this.handleCanvasClick(e, canvas));
    }
  }

  setupListeners() {
    bus.on('state:updated', (state) => {
      this.updateHUD(state);
      this.updateMetricsPanel(state);
      this.updateReportsPanel(state);
      this.updateLogs(state);
      this.updateSelectedEntityPanel(state);
    });

    // Handle incoming events / logs
    bus.on('disaster:triggered', (disaster) => {
      this.flashWarningPanel(disaster);
    });
  }

  updateHUD(state) {
    ui.setText('hud-time', ui.formatGameTime(state.time));
    ui.setText('hud-ship-name', shipConfig.shipName);
    
    // Play/pause btn highlight
    if (state.paused) {
      document.getElementById('btn-pause')?.classList.add('active');
      document.getElementById('btn-play')?.classList.remove('active');
    } else {
      document.getElementById('btn-pause')?.classList.remove('active');
      document.getElementById('btn-play')?.classList.add('active');
    }
  }

  updateMetricsPanel(state) {
    // Top right system indicators
    ui.setBarWidth('bar-oxygen', state.oxygenLevel, state.oxygenLevel > 50 ? '#00e5ff' : '#ff5252');
    ui.setText('val-oxygen', `${state.oxygenLevel.toFixed(0)}%`);

    ui.setBarWidth('bar-power', state.powerLevel, state.powerLevel > 40 ? '#ffd54f' : '#ff5252');
    ui.setText('val-power', `${state.powerLevel.toFixed(0)}%`);

    ui.setBarWidth('bar-water', state.waterLevel, '#2979ff');
    ui.setText('val-water', `${state.waterLevel.toFixed(0)}%`);

    ui.setBarWidth('bar-hull', state.hullIntegrity, state.hullIntegrity > 60 ? '#69f0ae' : state.hullIntegrity > 30 ? '#ffd54f' : '#ff5252');
    ui.setText('val-hull', `${state.hullIntegrity.toFixed(0)}%`);

    ui.setText('val-morale', `${state.crewMorale.toFixed(0)}%`);
  }

  updateReportsPanel(state) {
    const comp = state.computed;
    if (!comp) return;

    // Mass Breakdown
    ui.setText('report-dry-mass', `${fmt(comp.dryMass / 1000, 1)} t`);
    ui.setText('report-fuel-mass', `${fmt(comp.fuelMass / 1000, 1)} t`);
    ui.setText('report-total-mass', `${fmt(comp.wetMass / 1000, 1)} t`);

    // Gravity Report
    ui.setText('report-inner-g', `${comp.innerG.toFixed(2)} g`);
    ui.setText('report-outer-g', `${comp.outerG.toFixed(2)} g`);
    ui.setText('report-comfort-level', comp.comfort.label);
    const comfortIndicator = document.getElementById('report-comfort-level');
    if (comfortIndicator) {
      comfortIndicator.style.color = comp.comfort.color;
    }

    // Propulsion
    ui.setText('report-deltav', `${fmt(comp.deltaV, 0)} m/s`);
    ui.setText('report-burntime', fmtTime(comp.burnTime));
    ui.setText('report-spinup', fmtTime(comp.spinUpTime));

    // Structural Stress & Wobble Imbalance
    ui.setText('report-hoop-stress', `${fmt(comp.hoopStressMPa, 1)} MPa`);
    ui.setText('report-hoop-safety', `SF = ${fmt(comp.hoopSafety, 2)}`);
    ui.setText('report-container-safety', `SF = ${fmt(comp.containerSafety, 2)}`);

    const hoopEl = document.getElementById('report-hoop-safety');
    if (hoopEl) {
      hoopEl.className = `badge ${comp.hoopSafety > 2.0 ? 'badge-ok' : comp.hoopSafety > 1.2 ? 'badge-warn' : 'badge-crit'}`;
    }

    const cEl = document.getElementById('report-container-safety');
    if (cEl) {
      cEl.className = `badge ${comp.containerSafety > 2.0 ? 'badge-ok' : comp.containerSafety > 1.2 ? 'badge-warn' : 'badge-crit'}`;
    }

    // Display imbalance displacement stats dynamically
    let imbalanceLabel = 'Balanced';
    let imbalanceColor = 'var(--status-ok)';
    if (comp.imbalanceShift > 0.5) {
      imbalanceLabel = `Lopsided (Shift: ${comp.imbalanceShift.toFixed(1)}m)`;
      imbalanceColor = comp.imbalanceShift > 2.0 ? 'var(--status-crit)' : 'var(--status-warn)';
    }
    ui.setText('report-wobble-displacement', imbalanceLabel);
    const wobbleEl = document.getElementById('report-wobble-displacement');
    if (wobbleEl) wobbleEl.style.color = imbalanceColor;

    // Cost and crew
    ui.setText('report-crew-cap', `${state.crew.length} / ${comp.maxCrewCapacity} Px`);
    ui.setText('report-cost', `${comp.cost.toFixed(1)} M Cr`);
  }

  updateLogs(state) {
    const container = document.getElementById('event-logs-container');
    if (!container) return;

    // Rebuild logs list if length changed
    if (container.children.length !== state.logs.length) {
      container.innerHTML = '';
      // Slice last 30 logs
      state.logs.slice().reverse().forEach(log => {
        const div = document.createElement('div');
        div.className = `log-entry ${log.type || 'info'}`;
        div.innerHTML = `<span class="log-time">${ui.formatGameTime(log.time)}</span> <span class="log-message">${log.message}</span>`;
        container.appendChild(div);
      });
    }
  }

  handleCanvasClick(e, canvas) {
    // Translate click client coordinates to canvas space
    const rect = canvas.getBoundingClientRect();
    const px = e.clientX - rect.left;
    const py = e.clientY - rect.top;
    
    // Send event to main controller to do hit testing
    bus.emit('canvas:click', { px, py });
  }

  setSelectedEntity(entity) {
    this.selectedEntity = entity;
    const panel = document.getElementById('command-panel');
    if (!panel) return;

    if (entity) {
      ui.show(panel);
      ui.setText('selected-name', entity.name);
      ui.setText('selected-role', entity.type.toUpperCase() + (entity.role ? ` — ${entity.role}` : ''));
      ui.setText('selected-icon', entity.icon);
      
      const statsDiv = document.getElementById('selected-stats');
      if (statsDiv) {
        if (entity.type === 'crew') {
          statsDiv.innerHTML = `
            <div>HP: ${entity.health.toFixed(0)}%</div>
            <div>Hunger: ${entity.hunger.toFixed(0)}%</div>
            <div>Fatigue: ${entity.fatigue.toFixed(0)}%</div>
            <div>Morale: ${entity.morale.toFixed(0)}%</div>
            <div>Task: ${entity.status}</div>
          `;
        } else {
          statsDiv.innerHTML = `
            <div>Type: ${entity.type}</div>
            <div>Rim: ${entity.rim} rim</div>
            <div>Sector: ${(entity.pos * 360).toFixed(0)}°</div>
          `;
        }
      }

      // Re-populate command actions based on active disasters
      this.rebuildActionButtons(entity);

    } else {
      ui.hide(panel);
    }
  }

  rebuildActionButtons(entity) {
    const actionContainer = document.getElementById('selected-actions');
    if (!actionContainer) return;
    actionContainer.innerHTML = '';

    if (entity.type !== 'crew') {
      // Animals/Drones can't be commanded explicitly in this version, or have automated tasks
      const p = document.createElement('p');
      p.textContent = 'Automated Agent Behavior Active.';
      p.className = 'text-dim';
      actionContainer.appendChild(p);
      return;
    }

    // Add movement action buttons for active disasters
    if (gameState.activeDisasters.length === 0) {
      const p = document.createElement('p');
      p.textContent = 'No active system threats. Crew is performing standard maintenance.';
      p.className = 'text-ok';
      actionContainer.appendChild(p);
    } else {
      gameState.activeDisasters.forEach(d => {
        const btn = document.createElement('button');
        btn.className = 'btn-action';
        btn.innerHTML = `Fix ${d.icon} ${d.name}`;
        btn.addEventListener('click', () => {
          // Set target for crew member to this disaster
          entity.moveTo(d.pos, d.rim);
          entity.status = 'Responding';
          d.assignedCrewId = entity.id;
          
          gameState.logs.push({
            time: gameState.time,
            message: `COMMAND: ${entity.name} dispatched to secure ${d.name} at sector ${(d.pos * 360).toFixed(0)}°.`,
            type: 'info'
          });
          
          this.setSelectedEntity(entity); // refresh UI
        });
        actionContainer.appendChild(btn);
      });
    }
  }

  updateSelectedEntityPanel(state) {
    if (this.selectedEntity) {
      // Find fresh copy in list
      const fresh = state.crew.find(c => c.id === this.selectedEntity.id) ||
                    state.animals.find(a => a.id === this.selectedEntity.id) ||
                    state.drones.find(d => d.id === this.selectedEntity.id);
      
      if (fresh) {
        this.selectedEntity = fresh;
        // selectively update dynamic numbers
        const statsDiv = document.getElementById('selected-stats');
        if (statsDiv && fresh.type === 'crew') {
          statsDiv.innerHTML = `
            <div>HP: ${fresh.health.toFixed(0)}%</div>
            <div>Hunger: ${fresh.hunger.toFixed(0)}%</div>
            <div>Fatigue: ${fresh.fatigue.toFixed(0)}%</div>
            <div>Morale: ${fresh.morale.toFixed(0)}%</div>
            <div>Task: ${fresh.status}</div>
          `;
        }
      } else {
        this.selectedEntity = null;
        ui.hide('command-panel');
      }
    }
  }

  flashWarningPanel(disaster) {
    // Visual flash or sound alert indicator could go here.
    // For now, it leverages logs warning styling.
  }
}
