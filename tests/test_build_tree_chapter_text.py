from pathlib import Path
import shutil
import subprocess
import sys


BUILD_TREE = Path("knowledge/build_tree.py").resolve()


def make_knowledge_tree(tmp_path: Path) -> tuple[Path, Path]:
    knowledge = tmp_path / "knowledge"
    scenes = knowledge / "scenes"
    scenes.mkdir(parents=True)
    shutil.copy2(BUILD_TREE, knowledge / "build_tree.py")
    return knowledge, scenes


def write_chapter(scenes: Path, number: int, title: str, body: str) -> Path:
    path = scenes / f"draft_ch{number:02d}_{title.lower().replace(' ', '_')}.md"
    path.write_text(
        "---\n"
        f"id: draft_ch{number:02d}\n"
        f"name: Chapter {number}. {title}\n"
        "status: staged_draft\n"
        "description: Test chapter fixture.\n"
        "---\n\n"
        f"# Chapter {number}. {title}\n\n"
        "> *An emphasized epigraph about {{Aura}}.*\n\n"
        f"{body}\n\n"
        "## Contract coverage (`X-01`)\n\n"
        "| Item | Status |\n"
        "|---|---|\n"
        "| Editorial material | done |\n\n"
        "## Open Notes\n\n"
        "This note must not be spoken.\n",
        encoding="utf-8",
    )
    return path


def run_build_tree(knowledge: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "build_tree.py", *args],
        cwd=knowledge,
        check=True,
        capture_output=True,
        text=True,
    )


def test_chapter_text_removes_metadata_markdown_tags_and_editorial_sections(tmp_path):
    knowledge, scenes = make_knowledge_tree(tmp_path)
    write_chapter(
        scenes,
        0,
        "Prologue",
        "First paragraph names {Aura} and a [Transfer] label.\n\n"
        "##\n\n"
        "Second paragraph keeps [linked words](https://example.com) but not markup.",
    )

    run_build_tree(knowledge, "--chapter-text-only")

    output = (knowledge / "generated_text" / "chapter_00.txt").read_text(
        encoding="utf-8"
    )
    assert output.startswith("Chapter 0. Prologue\n\n")
    assert "An emphasized epigraph about Aura." in output
    assert "First paragraph names Aura and a Transfer label." in output
    assert "linked words" in output
    assert "\n\n\n\nSecond paragraph" in output
    assert "Contract coverage" not in output
    assert "Open Notes" not in output
    assert "This note must not be spoken" not in output
    assert not any(marker in output for marker in ("{", "}", "#", "*", "`", "[["))


def test_chapter_text_chunks_use_five_chapter_number_windows(tmp_path):
    knowledge, scenes = make_knowledge_tree(tmp_path)
    for number in (0, 1, 4, 5, 9, 10, 14, 15):
        write_chapter(scenes, number, f"Title {number}", f"Body for chapter {number}.")

    run_build_tree(knowledge, "--chapter-text-only")
    output = knowledge / "generated_text"

    assert (output / "chapters_00-04.txt").exists()
    assert (output / "chapters_05-09.txt").exists()
    assert (output / "chapters_10-14.txt").exists()
    assert (output / "chapters_15-19.txt").exists()

    first_chunk = (output / "chapters_00-04.txt").read_text(encoding="utf-8")
    assert first_chunk.index("Chapter 0.") < first_chunk.index("Chapter 1.")
    assert first_chunk.index("Chapter 1.") < first_chunk.index("Chapter 4.")
    assert "Chapter 5." not in first_chunk


def test_generator_removes_only_stale_managed_outputs(tmp_path):
    knowledge, scenes = make_knowledge_tree(tmp_path)
    write_chapter(scenes, 0, "Prologue", "Current chapter body.")
    output = knowledge / "generated_text"
    output.mkdir()
    (output / "chapter_99.txt").write_text("stale", encoding="utf-8")
    (output / "chapters_95-99.txt").write_text("stale", encoding="utf-8")
    (output / "listening_notes.txt").write_text("preserve", encoding="utf-8")

    run_build_tree(knowledge, "--chapter-text-only")

    assert not (output / "chapter_99.txt").exists()
    assert not (output / "chapters_95-99.txt").exists()
    assert (output / "listening_notes.txt").read_text(encoding="utf-8") == "preserve"


def test_default_mode_builds_index_and_chapter_text(tmp_path):
    knowledge, scenes = make_knowledge_tree(tmp_path)
    write_chapter(scenes, 0, "Prologue", "Current chapter body.")

    result = run_build_tree(knowledge)

    assert "Wrote audiobook text for 1 chapter(s) and 1 chunk(s)" in result.stdout
    assert (knowledge / "_index.md").exists()
    assert (knowledge / "generated_text" / "chapter_00.txt").exists()
    index = (knowledge / "_index.md").read_text(encoding="utf-8")
    assert "generated_text/" in index
    assert "chapter_00.txt" in index



def test_duplicate_chapter_numbers_stop_export(tmp_path):
    knowledge, scenes = make_knowledge_tree(tmp_path)
    write_chapter(scenes, 1, "First Draft", "First body.")
    write_chapter(scenes, 1, "Second Draft", "Second body.")

    result = subprocess.run(
        [sys.executable, "build_tree.py", "--chapter-text-only"],
        cwd=knowledge,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "Duplicate chapter 1" in result.stderr
