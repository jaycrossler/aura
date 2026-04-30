import re
from ...finding import Finding
BAD=r'(<\s*(script|iframe|style|object|embed)\b)|(on\w+\s*=)|(javascript\s*:)' 
def run(docs,cfg):
 out=[]
 for d in docs:
  if re.search(BAD,d.text,re.I): out.append(Finding('interactive.html_safety','HTML safety','interactive',cfg.get('severity','error'),d.rel_path,1,1,'Unsafe HTML or JS-like behavior found','Remove unsafe tags/handlers','html block',0.95))
 return out
