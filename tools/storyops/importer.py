from __future__ import annotations
import argparse, json, re, zipfile
from dataclasses import dataclass, field
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterable
from tools.storyops.common.paths import ensure_dir

TYPE_DIR_MAP={"character":"characters","faction":"factions","location":"locations","timeline":"timeline","magic":"magic-systems","technology":"technology","scene":"scenes","ship":"ships","universe":"universe-spec"}

@dataclass
class ImportResult:
    added:list[str]=field(default_factory=list)
    modified:list[str]=field(default_factory=list)
    skipped:list[str]=field(default_factory=list)
    errors:list[str]=field(default_factory=list)

def parse_frontmatter(text:str)->tuple[dict[str,str],str]:
    if not text.startswith('---\n'):
        return {}, text
    end_meta=text.find('\n---\n',4)
    if end_meta==-1:
        return {}, text
    raw_meta=text[4:end_meta]
    meta={}
    for line in raw_meta.splitlines():
        if ':' in line:
            k,v=line.split(':',1);meta[k.strip()]=v.strip()
    body=text[end_meta+5:]
    return meta, body

def parse_frontmatter_chunks(text:str)->list[tuple[dict[str,str],str]]:
    starts=[m.start() for m in re.finditer(r"(?m)^---\n",text)]
    if not starts:return [({},text)]
    chunks=[]
    for i,start in enumerate(starts):
        end_meta=text.find('\n---\n',start+4)
        if end_meta==-1:continue
        body_start=end_meta+5
        next_start=starts[i+1] if i+1<len(starts) else len(text)
        raw_meta=text[start+4:end_meta]
        meta={}
        for line in raw_meta.splitlines():
            if ':' in line:
                k,v=line.split(':',1);meta[k.strip()]=v.strip()
        chunks.append((meta,text[body_start:next_start].strip()+"\n"))
    return chunks or [({},text)]

def infer_target_subdir(doc_type:str,file_id:str)->str:
    t=doc_type.lower()
    for p,d in TYPE_DIR_MAP.items():
        if t.startswith(p):return d
    for p,d in [("char_","characters"),("faction_","factions"),("location_","locations"),("ship_","ships"),("tech_","technology"),("magic_","magic-systems"),("event_","scenes"),("scene_","scenes")]:
        if file_id.startswith(p):return d
    return "review-queue"

def all_markdown_files(source:Path)->Iterable[Path]:
    if source.is_dir():yield from source.rglob("*.md")
    else:yield source

def render_doc(meta:dict[str,str],body:str)->str:
    if not meta:return body.strip()+"\n"
    return f"---\n"+"\n".join(f"{k}: {v}" for k,v in meta.items())+f"\n---\n\n{body.strip()}\n"

def import_from_path(source:Path,knowledge_root:Path,look_to_separate:bool=False)->ImportResult:
    r=ImportResult();processed=[]
    for md in all_markdown_files(source):
        errs_before=len(r.errors)
        text=md.read_text(encoding='utf-8')
        parsed=parse_frontmatter_chunks(text) if look_to_separate else [parse_frontmatter(text)]
        for i,(meta,body) in enumerate(parsed):
            fid=meta.get('id','').strip();typ=meta.get('type','').strip()
            if not fid:
                r.errors.append(f"{md}: chunk {i+1} missing 'id'");continue
            target=ensure_dir(knowledge_root/infer_target_subdir(typ,fid))/f"{fid}.md"
            incoming=render_doc(meta,body)
            if target.exists():
                existing=target.read_text(encoding='utf-8')
                if incoming==existing:r.skipped.append(str(target))
                elif len(incoming)>=len(existing):target.write_text(incoming,encoding='utf-8');r.modified.append(str(target))
                else:r.skipped.append(f"{target} (incoming shorter)")
            else:target.write_text(incoming,encoding='utf-8');r.added.append(str(target))
        if len(r.errors)==errs_before:processed.append(md)
    if not r.errors:
        if source.is_file():source.unlink(missing_ok=True)
        else:
            for p in processed:p.unlink(missing_ok=True)
    return r

def main()->None:
    ap=argparse.ArgumentParser(description='Import markdown knowledge files into /knowledge')
    ap.add_argument('source', nargs='?', default='knowledge/to_import')
    ap.add_argument('--knowledge-root',default='knowledge')
    ap.add_argument('--report',default='generated/reports/import-report.json')
    ap.add_argument('--look-to-separate',action='store_true',help='Split a single concatenated markdown file into multiple frontmatter chunks')
    a=ap.parse_args();source=Path(a.source);k=Path(a.knowledge_root)
    if not source.exists():raise SystemExit(f'Source does not exist: {source}')
    if source.suffix.lower()=='.zip':
        with TemporaryDirectory() as td:
            with zipfile.ZipFile(source,'r') as z: z.extractall(td)
            result=import_from_path(Path(td),k,look_to_separate=a.look_to_separate)
            if not result.errors: source.unlink(missing_ok=True)
    else:result=import_from_path(source,k,look_to_separate=a.look_to_separate)
    report={"added_count":len(result.added),"modified_count":len(result.modified),"skipped_count":len(result.skipped),"error_count":len(result.errors),"added":result.added,"modified":result.modified,"skipped":result.skipped,"errors":result.errors}
    rp=Path(a.report);ensure_dir(rp.parent);rp.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))
    if result.errors:raise SystemExit(1)

if __name__=='__main__':main()
