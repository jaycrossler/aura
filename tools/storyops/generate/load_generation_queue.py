from pathlib import Path
from tools.storyops.common.config import load_yaml
import json

def load_queue(): return load_yaml(Path('control/generation-queue.yaml')).get('queue',[])
