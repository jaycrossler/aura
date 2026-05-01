from pathlib import Path

from tools.storyops.generate.chapter_generator import generate_chapter


def test_generate_chapter_without_scene_files(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    (tmp_path / 'knowledge/scenes').mkdir(parents=True)
    (tmp_path / 'knowledge/MASTER-SYNOPSIS.md').write_text('# Synopsis', encoding='utf-8')

    out = generate_chapter(
        {
            'id': 'gen_empty',
            'kind': 'chapter_draft',
            'output_file': 'generated/drafts/empty.md',
            'overwrite': True,
            'chapter_title': 'Empty Scene Draft',
        }
    )
    assert out is not None
    assert Path(out).exists()
    assert Path(out).with_suffix('.meta.json').exists()
