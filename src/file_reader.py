from pathlib import Path


def read_txt_file(file_path: str) -> list[str]:
    path = Path(file_path)

    if path.suffix != ".txt":
        raise ValueError("Підтримуються лише .txt файли")

    return path.read_text(encoding="utf-8").splitlines()
