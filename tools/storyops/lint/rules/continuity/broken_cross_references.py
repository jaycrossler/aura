import re
from pathlib import Path
from ...finding import Finding

def run(docs,cfg):
 out=[]
 for d in docs:
  for m in re.finditer(r'(/knowledge/[\w\-/\.]+\.md)', d.text):
   if not Path(m.group(1).lstrip('/')).exists(): out.append(Finding('continuity.broken_cross_references','Broken cross references','continuity',cfg.get('severity','error'),d.rel_path,1,1,f'Broken reference: {m.group(1)}','Fix path',m.group(1),1.0))
 return out
