from pathlib import Path

def build_word_count_chart(state, out_path: Path):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.with_suffix('.txt').write_text('matplotlib not available; chart skipped', encoding='utf-8')
        return
    data = state['summary']['word_counts_by_category']
    if not data: return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8,4)); plt.bar(list(data.keys()), list(data.values())); plt.xticks(rotation=45, ha='right'); plt.tight_layout(); plt.savefig(out_path); plt.close()
