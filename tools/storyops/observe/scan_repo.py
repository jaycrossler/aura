from pathlib import Path
from tools.storyops.common.frontmatter import parse_markdown
from tools.storyops.common.markdown import word_count

def scan_markdown(root: Path):
    docs=[]
    if not root.exists(): return docs
    for p in sorted(root.rglob('*.md')):
        meta, content = parse_markdown(p)
        txt = content or ''
        docs.append({'path': p, 'frontmatter': meta, 'text': txt, 'words': word_count(txt)})
    return docs
