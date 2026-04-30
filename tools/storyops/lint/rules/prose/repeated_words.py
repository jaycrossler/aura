import re
from collections import Counter
from ...finding import Finding
STOP={'the','and','a','to','of','in','is','it','for','on','that','with'}
def run(docs,cfg):
 c=cfg.get('config',{}); mx=c.get('max_repeats',6); ig=set(c.get('ignore_words',[])); out=[]
 for d in docs:
  words=[w.lower() for w in re.findall(r"[A-Za-z']+", d.text) if w.lower() not in STOP|ig]
  cnt=Counter(words)
  for w,n in cnt.items():
   if n>mx: out.append(Finding('prose.repeated_words','Repeated words','prose',cfg.get('severity','warning'),d.rel_path,1,1,f'Word "{w}" repeated {n}x','Vary wording',w,0.7))
 return out
