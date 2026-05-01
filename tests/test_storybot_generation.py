from pathlib import Path

from tools.storyops.generate.chapter_generator import generate_chapter


def test_generate_chapter_with_metadata(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "knowledge/scenes").mkdir(parents=True)
    (tmp_path / "knowledge/characters").mkdir(parents=True)
    (tmp_path / "knowledge/locations").mkdir(parents=True)
    (tmp_path / "knowledge/technology").mkdir(parents=True)
    (tmp_path / "knowledge/magic-systems").mkdir(parents=True)
    (tmp_path / "knowledge/MASTER-SYNOPSIS.md").write_text("# Synopsis", encoding="utf-8")

    (tmp_path / "knowledge/scenes/s1.md").write_text(
        "---\nid: scene_alpha\ntitle: Alpha\nlast_updated: 2026-04-01\n---\n\nJace meets Mei at Fortuna Station.",
        encoding="utf-8",
    )
    (tmp_path / "knowledge/characters/char_jace_apollo.md").write_text("---\nid: jace\n---\nJace profile", encoding="utf-8")
    (tmp_path / "knowledge/characters/char_mei.md").write_text("---\nid: mei\n---\nMei profile", encoding="utf-8")
    (tmp_path / "knowledge/locations/location_fortuna_station.md").write_text("---\nid: fortuna\n---\nFortuna profile", encoding="utf-8")

    out = generate_chapter(
        {
            "id": "gen1",
            "kind": "chapter_draft",
            "output_file": "generated/drafts/ch1.md",
            "overwrite": True,
            "chapter_title": "Ch 1",
        }
    )
    assert out is not None
    chapter_path = Path(out)
    meta_path = chapter_path.with_suffix(".meta.json")
    assert chapter_path.exists()
    assert meta_path.exists()
    assert "llm_provider: mock" in chapter_path.read_text(encoding="utf-8")
    assert "dialogue" in meta_path.read_text(encoding="utf-8")
