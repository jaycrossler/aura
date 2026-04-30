import subprocess
from datetime import datetime, timezone

def _run(args):
    try:
        return subprocess.check_output(args, text=True).strip()
    except Exception:
        return None

def git_commit_hash(): return _run(['git','rev-parse','HEAD'])
def git_changed_files():
    out = _run(['git','status','--porcelain']) or ''
    return [l[3:] for l in out.splitlines() if len(l) > 3]
def utc_now(): return datetime.now(timezone.utc).isoformat()
