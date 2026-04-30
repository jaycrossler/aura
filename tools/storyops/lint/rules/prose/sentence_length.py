import re
from ...finding import Finding

def run(docs,cfg):
 m=cfg.get('config',{}).get('max_words',35); out=[]
 for d in docs:
  for i,s in enumerate(re.split(r'(?<=[.!?])\s+', d.text)):
   wc=len(s.split());
   if wc>m: out.append(Finding('prose.sentence_length','Sentence length','prose',cfg.get('severity','warning'),d.rel_path,i+1,1,f'Sentence has {wc} words',f'Keep under {m}',s[:120],0.8))
 return out
