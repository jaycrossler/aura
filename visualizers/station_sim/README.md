# SpinningStationSim

SpinningStationSim is a interactive, multi-file ES module space station physics simulator designed for the *Aura Chronicles* science fiction universe (~2100). The simulation helps test what is plausible or not for rotating habitats and ship propulsion designs.

## File Structure

```
d:/Projects/aura/visualizers/station_sim/
├── css/
│   └── station.css       # Layout styles for the sim panels and HUD
├── js/
│   ├── constants.js     # Engine specs, container load properties, default config
│   ├── state.js         # Central event bus and reactive states
│   ├── physics.js       # Structural/hoop stress and propellant calculations
│   ├── entities.js      # Crew, Animals, and Drones classes
│   ├── disasters.js     # System blowout and leakage event manager
│   ├── renderer.js      # Canvas rendering (Torus, Profile, Comfort Map)
│   ├── ui.js            # Control bindings and result tables
│   └── main.js          # Simulator setup and coordination
├── tests/
│   ├── test-utils.js    # Basic custom test suite runner
│   ├── physics.test.js  # Math and physics formulas tests
│   ├── entities.test.js # Character drift and movement tests
│   └── test-runner.html # In-browser test dashboard
├── index.html           # Main user interface entry point
├── package.json         # serve command dependencies script
└── README.md            # This documentation file
```

## Running the Simulator

To run the simulator locally:

1. Open your terminal in the `station_sim/` directory.
2. Run the development server command:
   ```bash
   npm run serve
   ```
3. Open your browser and navigate to `http://localhost:3000`.

## Testing

To run the unit tests:
1. Open the file `station_sim/tests/test-runner.html` directly in your web browser (or browse to `http://localhost:3000/tests/test-runner.html` while the server is active).
2. The page will run the test suites for both shared math modules and specific entity actions, reporting immediate pass/fail status.
