from pathlib import Path

def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def word_count(text: str) -> int:
    return len([w for w in text.replace('\n',' ').split() if w.strip()])
