import argparse
from .runner import run_lint
p=argparse.ArgumentParser(); p.add_argument('--profile', default='hard_scifi_novel'); p.add_argument('--path')
a=p.parse_args(); raise SystemExit(run_lint(a.profile,a.path))
