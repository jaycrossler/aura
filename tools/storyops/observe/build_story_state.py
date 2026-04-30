from pathlib import Path
import json
from tools.storyops.common.git_utils import git_commit_hash, utc_now

def build_story_state(project, docs, manuscript_docs, lint_summary=None):
    kroot = project['knowledge_root']
    by_cat = {}
    for d in docs:
        rel = d['path'].as_posix().split(f'{kroot}/',1)[-1]
        cat = rel.split('/',1)[0] if '/' in rel else 'root'
        by_cat[cat] = by_cat.get(cat,0)+d['words']
    open_q = sum(1 for d in docs if 'open questions' in d['text'].lower())
    rev_n = sum(1 for d in docs if 'revision notes' in d['text'].lower())
    def ent(folder):
        return [d['path'].name for d in docs if f"{kroot}/{folder}/" in d['path'].as_posix()]
    return {
        'project': project,
        'last_updated_utc': utc_now(),
        'git_commit_hash': git_commit_hash(),
        'summary': {'knowledge_files': len(docs),'manuscript_files':len(manuscript_docs),'word_counts_by_category':by_cat,'open_questions_sections':open_q,'revision_notes_sections':rev_n},
        'velocity': {'last_24h': None, 'last_7d': None},
        'chapters': [d['path'].name for d in manuscript_docs],
        'characters': ent('characters'),'locations': ent('locations'),'ships': ent('ships'),
        'lint_summary': lint_summary,
        'warnings': []
    }
