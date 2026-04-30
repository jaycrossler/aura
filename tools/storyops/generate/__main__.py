import argparse
from .load_generation_queue import load_queue
from .artifact_generators import run_item
p=argparse.ArgumentParser(); p.add_argument('--queue-id')
a=p.parse_args();
for it in load_queue():
    if a.queue_id and it['id']!=a.queue_id: continue
    if not it.get('enabled',False): continue
    r=run_item(it)
    if r: print('generated',r)
