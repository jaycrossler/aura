from ...finding import Finding

def run(docs,cfg):
 out=[]
 for d in docs:
  if d.rel_path.lower().endswith('readme.md'): continue
  if not d.frontmatter: out.append(Finding('continuity.missing_frontmatter','Missing frontmatter','continuity',cfg.get('severity','info'),d.rel_path,1,1,'Missing YAML front matter','Add --- metadata ---','',1.0))
 return out
