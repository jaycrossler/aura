from builtins import __import__ as real_import
from pathlib import Path

from tools.storyops.observe.build_charts import build_word_count_chart


def test_chart_writes_dependency_message_when_matplotlib_missing(monkeypatch, tmp_path):
    def fake_import(name, *args, **kwargs):
        if name.startswith('matplotlib'):
            raise ImportError('matplotlib missing')
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr('builtins.__import__', fake_import)
    output = tmp_path / 'generated/charts/word_counts_by_category.svg'
    build_word_count_chart({'summary': {'word_counts_by_category': {'characters': 10}}}, output)
    note = output.with_suffix('.txt')
    assert note.exists()
    assert 'matplotlib dependency is not available' in note.read_text(encoding='utf-8')


def test_chart_writes_no_data_message(tmp_path):
    output = tmp_path / 'generated/charts/word_counts_by_category.svg'
    build_word_count_chart({'summary': {'word_counts_by_category': {}}}, output)
    note = output.with_suffix('.txt')
    assert note.exists()
    assert 'no category word-count data found' in note.read_text(encoding='utf-8')
