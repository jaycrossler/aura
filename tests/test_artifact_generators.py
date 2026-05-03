from tools.storyops import artifact_generators


def test_run_queue_passes_force_overwrite(monkeypatch):
    monkeypatch.setattr(
        artifact_generators,
        "load_queue",
        lambda **kwargs: [{"id": "chapter-1", "kind": "chapter_draft"}],
    )

    seen = {}

    def fake_run_item(item, force_overwrite=False):
        seen["force_overwrite"] = force_overwrite
        return "generated/drafts/ch001.md"

    monkeypatch.setattr(artifact_generators, "run_item", fake_run_item)

    out = artifact_generators.run_queue(chapter_id="ch001", force_overwrite=True)

    assert out == ["generated/drafts/ch001.md"]
    assert seen["force_overwrite"] is True
