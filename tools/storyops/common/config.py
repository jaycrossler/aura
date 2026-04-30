from __future__ import annotations
import json
from pathlib import Path
from typing import Any


def _simple_yaml(text: str) -> Any:
    # Minimal fallback parser for JSON-or-simple-YAML mappings/lists.
    lines = [l.rstrip() for l in text.splitlines() if l.strip() and not l.strip().startswith('#')]
    if not lines:
        return {}
    if text.lstrip().startswith('{') or text.lstrip().startswith('['):
        return json.loads(text)
    data: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(0, data)]
    for raw in lines:
        indent = len(raw) - len(raw.lstrip(' '))
        line = raw.strip()
        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        cur = stack[-1][1]
        if line.startswith('- '):
            if not isinstance(cur, list):
                raise ValueError('List item without list container')
            cur.append(line[2:].strip())
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            k = k.strip(); v = v.strip()
            if v == '':
                nxt: Any = {}
                cur[k] = nxt
                stack.append((indent + 2, nxt))
            else:
                if v.lower() in ('true','false'): val = v.lower() == 'true'
                else:
                    try: val = int(v)
                    except: val = v.strip('"\'')
                cur[k] = val
    return data


def load_yaml(path: Path) -> Any:
    txt = path.read_text(encoding='utf-8')
    try:
        import yaml  # type: ignore
        return yaml.safe_load(txt)
    except Exception:
        return _simple_yaml(txt)
