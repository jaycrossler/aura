import re
from ...finding import Finding

def run(docs,cfg):
 out=[]
 for d in docs:
  for i,l in enumerate(d.lines):
   if re.search(r'".+"',l) and not re.search(r'(said|asked|replied|whispered|shouted)', l, re.I):
    out.append(Finding('audio.dialogue_attribution','Dialogue attribution','audio',cfg.get('severity','warning'),d.rel_path,i+1,1,'Dialogue may be ambiguous for audio narration','Clarify speaker near dialogue',l[:80],0.5))
 return out
