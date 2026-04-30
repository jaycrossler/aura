import json, re, csv
from pathlib import Path
from collections import Counter
from tools.storyops.common.frontmatter import parse_markdown
from tools.storyops.common.config import load_yaml
from tools.storyops.common.jsonl import write_json, append_jsonl
from tools.storyops.common.git_utils import utc_now
from .finding import Document
from .registry import RULES

def load_docs(path=None):
    files=[Path(path)] if path else sorted(Path('knowledge').rglob('*.md')) + (sorted(Path('manuscript').rglob('*.md')) if Path('manuscript').exists() else [])
    docs=[]
    for p in files:
        if not p.exists(): continue
        fm, txt = parse_markdown(p)
        docs.append(Document(str(p), str(p), txt, fm, txt.splitlines()))
    return docs

def run_lint(profile, path=None):
    profiles=load_yaml(Path('control/lint-profiles.yaml'))
    cfg=load_yaml(Path('control/lint-rules.yaml'))
    docs=load_docs(path)
    findings=[]
    for rid in profiles['profiles'][profile]:
        rcfg=cfg['rules'].get(rid, {})
        if not rcfg.get('enabled',True): continue
        findings += RULES[rid](docs, rcfg)
    out=Path('generated/lint'); out.mkdir(parents=True, exist_ok=True)
    write_json(out/'lint-results.json', [f.to_dict() for f in findings])
    sev=Counter(f.severity for f in findings); by_rule=Counter(f.rule_id for f in findings); by_file=Counter(f.file for f in findings)
    summary={'profile':profile,'total_findings':len(findings),'by_severity':dict(sev),'by_rule':dict(by_rule),'generated_at':utc_now()}
    write_json(out/'lint-summary.json', summary)
    (out/'lint-summary.md').write_text('# Lint Summary\n\n'+json.dumps(summary,indent=2), encoding='utf-8')
    with (out/'lint-by-file.csv').open('w',newline='',encoding='utf-8') as f: w=csv.writer(f); w.writerow(['file','count']); [w.writerow([k,v]) for k,v in by_file.items()]
    with (out/'lint-by-rule.csv').open('w',newline='',encoding='utf-8') as f: w=csv.writer(f); w.writerow(['rule','count']); [w.writerow([k,v]) for k,v in by_rule.items()]
    append_jsonl(out/'lint-trend.jsonl', summary)
    fail = cfg.get('errors_fail_ci',True) and sev.get('error',0)>0
    return 1 if fail else 0
