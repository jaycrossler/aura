from pathlib import Path
from tools.storyops.common.git_utils import utc_now
import json

def write_proposal(path, aid, body, sources):
 path.parent.mkdir(parents=True, exist_ok=True)
 fm=['---',f'id: {aid}', 'type: agent_proposal', 'status: proposed', f"generated_at: '{utc_now()}'", f'source_files: {sources}', '---\n']
 path.write_text('\n'.join(fm)+body, encoding='utf-8')

def run_master_continuity():
 state=Path('generated/status/story_state.json'); lint=Path('generated/lint/lint-summary.json')
 body='# Master Continuity Proposal\n\n- Review open questions and lint errors before canon updates.\n'
 if lint.exists(): body += f"- Lint summary loaded with findings.\n"
 write_proposal(Path('proposals/agents/master_continuity.md'),'master_continuity',body,[str(p) for p in [state,lint] if p.exists()])

def run_character_voice():
 chars=sorted(Path('knowledge/characters').glob('*.md')) if Path('knowledge/characters').exists() else []
 body='# Character Voice Proposal\n\n' + '\n'.join([f'- Add voice profile checks for `{c.name}`.' for c in chars])
 write_proposal(Path('proposals/agents/character_voice.md'),'character_voice',body,[str(c) for c in chars])
