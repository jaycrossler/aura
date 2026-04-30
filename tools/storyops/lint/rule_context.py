from dataclasses import dataclass
@dataclass
class RuleContext:
    documents:list
    config:dict
    story_state:dict
    knowledge_index:dict
