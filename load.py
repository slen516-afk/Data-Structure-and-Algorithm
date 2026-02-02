# load.py
from __future__ import annotations

from pathlib import Path
from typing import List


def load_numbers(file_name):
    numbers = []
    with open(file_name) as f:
        for line in f:
            # 去除換行符號並轉成整數
            numbers.append(int(line.strip()))
    return numbers



def load_strings(
    file_path: str | Path,
    *,
    encoding: str = "utf-8",
    strip: bool = True,
    skip_empty: bool = True,
    unique: bool = False,
) -> List[str]:
    """
    Load strings from a text file (one item per line).

    Args:
        file_path: path to the .txt file
        encoding: file encoding (default: utf-8)
        strip: strip whitespace on both ends
        skip_empty: ignore empty lines
        unique: remove duplicates while preserving order

    Returns:
        List[str]
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.resolve()}")

    lines = path.read_text(encoding=encoding).splitlines()

    if strip:
        lines = [s.strip() for s in lines]

    if skip_empty:
        lines = [s for s in lines if s != ""]

    if unique:
        seen = set()
        deduped = []
        for s in lines:
            if s not in seen:
                seen.add(s)
                deduped.append(s)
        lines = deduped

    return lines


if __name__ == "__main__":
    # quick self-test
    # print(load_strings("names_100k.txt")[:5])
    pass

