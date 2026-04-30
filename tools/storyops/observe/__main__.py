from pathlib import Path
import json
from tools.storyops.common.jsonl import write_json, append_jsonl
from tools.storyops.common.config import load_yaml
from .scan_repo import scan_markdown
from .build_story_state import build_story_state
from .build_progress_log import progress_snapshot
from .build_inventory_report import build_inventory
from .build_charts import build_word_count_chart

def main():
    root=Path('.')
    project=load_yaml(root/'control/project.yaml')['project']
    kdocs=scan_markdown(root/project['knowledge_root'])
    mroot=root/project['manuscript_root']; mroot.mkdir(exist_ok=True)
    mdocs=scan_markdown(mroot)
    lint_path=root/'generated/lint/lint-summary.json'
    lint=json.loads(lint_path.read_text()) if lint_path.exists() else None
    state=build_story_state(project,kdocs,mdocs,lint)
    write_json(root/'generated/status/story_state.json', state)
    append_jsonl(root/'generated/status/progress_log.jsonl', progress_snapshot(state))
    (root/'generated/reports/knowledge_inventory.md').write_text(build_inventory(kdocs), encoding='utf-8')
    build_word_count_chart(state, root/'generated/charts/word_counts_by_category.png')
    print('observe complete')
if __name__=='__main__': main()
