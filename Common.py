from pathlib import Path
from typing import List

def read_input_lines(file: Path) -> list[str]:
    """Return the lines of file as a list of strings (newline removed)."""
    with file.open('r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def read_char_array(file: Path ) -> List[List[str]]:
    """Return the file as a 2D matrix: each line becomes a list of characters (newlines removed)."""
    text = file.read_text(encoding='utf-8')
    return [list(line) for line in text.splitlines()]

def read_grid(file: Path) -> List[List[int]]:
    """Return file as a 2D list of ints: each non-empty line -> list of digit ints."""
    text = file.read_text(encoding='utf-8')
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return [[int(ch) for ch in line.split(',')] for line in lines]

def count_neighbors(matrix: List[List[str]], row: int, col: int, target: str) -> int:
    """Count how many of the 8 neighbors of matrix[row][col] are equal to target."""
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
            if matrix[r][c] == target:
                count += 1
    return count


