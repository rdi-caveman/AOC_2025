# python
import re
from pathlib import Path
from typing import List, Tuple, Pattern

RANGE_RE = re.compile(r'(\d+)-(\d+)')
INVALID_RE = re.compile(r'^(\d+)\1$')     # some sequence of digits repeated twice
INVALID_RE2 = re.compile(r'^(\d+)\1+$')   # some sequence of digits repeated two or more times

def read_ranges(path: Path) -> List[Tuple[int, int]]:
    """Return a list of (start, end) tuples parsed from `path`."""
    text = path.read_text(encoding='utf-8')
    return [(int(a), int(b)) for a, b in RANGE_RE.findall(text)]

def sum_invalid_ids(ranges: List[Tuple[int, int]], invalid_re: Pattern[str]) -> int:
    """Return the sum of integers in `ranges` that match `invalid_re` when converted to strings."""
    return sum(
        i
        for start, end in ranges
        for i in range(start, end + 1)
        if invalid_re.match(str(i))
    )

if __name__ == '__main__':
    data = read_ranges(Path('day2_input.txt'))
    print(f'Part 1: {sum_invalid_ids(data, INVALID_RE)}')   # Sum of invalid IDs
    print(f'Part 2: {sum_invalid_ids(data, INVALID_RE2)}')  # Sum of invalid IDs with longer repeated sequences
