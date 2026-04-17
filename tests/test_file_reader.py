from pathlib import Path

import pytest

from src.file_reader import filter_lines_by_keyword
from src.file_reader import read_txt_file
from src.file_reader import write_filtered_file


def test_read_txt_file_success(sample_txt_file) -> None:
    lines = read_txt_file(str(sample_txt_file))

    assert lines == [
        "python keyword line",
        "regular text",
        "another keyword match",
    ]


def test_read_txt_file_invalid_extension(invalid_file) -> None:
    with pytest.raises(ValueError):
        read_txt_file(str(invalid_file))


@pytest.mark.parametrize(
    ("keyword", "expected"),
    [
        ("keyword", ["python keyword line", "another keyword match"]),
        ("python", ["python keyword line"]),
        ("missing", []),
    ],
)
def test_filter_lines_by_keyword(sample_lines, keyword: str, expected: list[str]) -> None:
    assert filter_lines_by_keyword(sample_lines, keyword) == expected


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        (["one", "two"], "one\ntwo"),
        (["single"], "single"),
        ([], ""),
    ],
)
def test_write_filtered_file(tmp_path, lines: list[str], expected: str) -> None:
    output_file = tmp_path / "filtered.txt"

    write_filtered_file(lines, str(output_file))

    assert output_file.read_text(encoding="utf-8") == expected
    assert Path(output_file).name == "filtered.txt"
