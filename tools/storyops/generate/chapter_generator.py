from pathlib import Path
from tools.storyops.common.git_utils import utc_now

def generate_chapter(item):
 out=Path(item['output_file']); out.parent.mkdir(parents=True, exist_ok=True)
 if out.exists() and not item.get('overwrite',False): return None
 src=[]
 for p in ['knowledge/MASTER-SYNOPSIS.md']:
  if Path(p).exists(): src.append(p)
 lines=['---',f"id: {item['id']}", 'type: generated_chapter', 'status: Draft_v_1', f"generated_at: '{utc_now()}'", 'canon_status: generated', f'source_files: {src}', '---\n', f"# {item.get('chapter_title','Generated Chapter Draft')}\n", 'This deterministic Draft_v_1 was generated from knowledge bank inputs.\n', '## Scene Seeds\n', '- Integrate core stakes from synopsis.\n\n', '> Human Review Required: This draft is generated and non-canon until approved.\n']
 out.write_text('\n'.join(lines), encoding='utf-8'); return str(out)
