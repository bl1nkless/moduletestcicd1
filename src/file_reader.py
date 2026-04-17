import argparse
from pathlib import Path


def read_txt_file(file_path: str) -> list[str]:
    path = Path(file_path)

    if path.suffix != ".txt":
        raise ValueError("Підтримуються лише .txt файли")

    return path.read_text(encoding="utf-8").splitlines()


def filter_lines_by_keyword(lines: list[str], keyword: str) -> list[str]:
    return [line for line in lines if keyword in line]


def write_filtered_file(
    lines: list[str],
    output_path: str = "filtered.txt",
) -> None:
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    parser.add_argument("keyword")
    parser.add_argument("--output", default="filtered.txt")
    args = parser.parse_args()

    lines = read_txt_file(args.file_path)
    filtered_lines = filter_lines_by_keyword(lines, args.keyword)
    write_filtered_file(filtered_lines, args.output)
