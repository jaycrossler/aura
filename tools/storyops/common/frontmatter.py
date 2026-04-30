from pathlib import Path

def parse_markdown(path: Path):
    text = path.read_text(encoding='utf-8')
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            raw_meta = text[4:end]
            try:
                import yaml  # type: ignore
                meta = yaml.safe_load(raw_meta) or {}
            except Exception:
                meta = {}
                for line in raw_meta.splitlines():
                    if ':' in line:
                        k, v = line.split(':', 1)
                        meta[k.strip()] = v.strip().strip('"\'')
            return meta, text[end + 5 :]
    return {}, text
