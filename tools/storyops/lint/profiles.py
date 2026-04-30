import json
from pathlib import Path

def load_profiles():
    return json.loads(Path('control/lint-profiles.yaml').read_text())
