import re
from ...finding import Finding
ATTR=('said','asked','replied','whispered','shouted')
def run(docs,cfg):
 out=[]
 for d in docs:
  lines=d.lines
  for i,l in enumerate(lines):
   if '"' in l and re.search(r'".+"',l):
    window=' '.join(lines[max(0,i-1):min(len(lines),i+2)]).lower()
    if not any(a in window for a in ATTR): out.append(Finding('fiction.dialogue_speaker_tags','Dialogue speaker tags','fiction',cfg.get('severity','warning'),d.rel_path,i+1,1,'Dialogue may lack speaker attribution','Add speaker tag/action beat',l[:80],0.5))
 return out
