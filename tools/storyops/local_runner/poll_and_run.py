import argparse, subprocess, time
from pathlib import Path

def run(cmd, cwd='.'): return subprocess.run(cmd, cwd=cwd, shell=False, check=False, capture_output=True, text=True)

def changed(repo, remote, branch):
 run(['git','fetch',remote,branch], cwd=repo)
 l=run(['git','rev-parse','HEAD'], cwd=repo).stdout.strip(); r=run(['git','rev-parse',f'{remote}/{branch}'], cwd=repo).stdout.strip()
 return l!=r

def main():
 p=argparse.ArgumentParser(); p.add_argument('--repo',default='.'); p.add_argument('--remote',default='origin'); p.add_argument('--branch',default='main'); p.add_argument('--once',action='store_true'); p.add_argument('--interval-seconds',type=int,default=0); p.add_argument('--profile',default='hard_scifi_novel'); p.add_argument('--run-generate',default='false'); p.add_argument('--run-agents',default='false'); p.add_argument('--commit',default='false'); p.add_argument('--push',default='false'); p.add_argument('--branch-prefix',default='assistant/local-run'); a=p.parse_args()
 lock=Path(a.repo)/'.storyops.lock'; log=Path(a.repo)/'generated/logs/local-runner.log'; log.parent.mkdir(parents=True, exist_ok=True)
 def loop():
  if lock.exists(): return
  lock.write_text('locked')
  try:
   if not changed(a.repo,a.remote,a.branch): log.write_text('no remote changes\n',encoding='utf-8'); return
   run(['git','pull','--ff-only',a.remote,a.branch], cwd=a.repo)
   run(['python','-m','tools.storyops.observe'], cwd=a.repo); run(['python','-m','tools.storyops.lint','--profile',a.profile], cwd=a.repo)
  finally:
   lock.unlink(missing_ok=True)
 if a.once or a.interval_seconds<=0: loop(); return
 while True: loop(); time.sleep(a.interval_seconds)
if __name__=='__main__': main()
