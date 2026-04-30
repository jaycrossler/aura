from dataclasses import dataclass, asdict
from typing import Any
@dataclass
class Finding:
    rule_id:str; rule_name:str; category:str; severity:str; file:str; line:int=1; column:int=1; message:str=''; suggestion:str=''; evidence:str=''; confidence:float=0.5
    def to_dict(self): return asdict(self)
@dataclass
class Document:
    path:str; rel_path:str; text:str; frontmatter:dict[str,Any]; lines:list[str]
