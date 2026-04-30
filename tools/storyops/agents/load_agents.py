from pathlib import Path
from tools.storyops.common.config import load_yaml
import json

def load_agents(): return load_yaml(Path('control/agents.yaml')).get('agents',[])
