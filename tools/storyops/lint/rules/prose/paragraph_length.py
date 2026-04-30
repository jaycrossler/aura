from ...finding import Finding

def run(docs,cfg):
 m=cfg.get('config',{}).get('max_words',180); out=[]
 for d in docs:
  for i,p in enumerate([x.strip() for x in d.text.split('\n\n') if x.strip()]):
   wc=len(p.split())
   if wc>m: out.append(Finding('prose.paragraph_length','Paragraph length','prose',cfg.get('severity','warning'),d.rel_path,i+1,1,f'Paragraph has {wc} words',f'Split paragraph under {m}',p[:100],0.9))
 return out
