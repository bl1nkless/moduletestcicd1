import pytest


@pytest.fixture
def sample_lines() -> list[str]:
    return [
        "python keyword line",
        "regular text",
        "another keyword match",
    ]


@pytest.fixture
def sample_txt_file(tmp_path):
    file_path = tmp_path / "input.txt"
    file_path.write_text("python keyword line\nregular text\nanother keyword match\n", encoding="utf-8")
    return file_path


@pytest.fixture
def invalid_file(tmp_path):
    file_path = tmp_path / "input.csv"
    file_path.write_text("a,b,c\n", encoding="utf-8")
    return file_path
