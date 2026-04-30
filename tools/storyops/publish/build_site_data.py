from pathlib import Path
import json
from tools.storyops.common.jsonl import write_json

def build():
 s=json.loads(Path('generated/status/story_state.json').read_text()) if Path('generated/status/story_state.json').exists() else {}
 l=json.loads(Path('generated/lint/lint-summary.json').read_text()) if Path('generated/lint/lint-summary.json').exists() else {}
 write_json(Path('generated/site-data/dashboard.json'), {'story_state':s,'lint_summary':l})
