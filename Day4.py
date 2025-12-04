# python
from pathlib import Path
from typing import List

from Common import read_char_array, count_neighbors

INPUT = Path('day4_input.txt')

def find_accessible_rolls(my_matrix: List[List[str]]) -> list[list[int]]:
    """Return the list of accessible rolls ('@') in the matrix."""
    accessible_rolls = []
    for row in range(len(my_matrix)):
        for col in range(len(my_matrix[row])):
            if matrix[row][col] == '@' and count_neighbors(my_matrix, row, col, '@') < 4:
                accessible_rolls.append([row,col])
    return accessible_rolls

def remove_accessible_rolls(my_matrix: List[List[str]]) -> int:
    """Modify the matrix in place to remove accessible rolls ('@')."""
    count_removed = 0
    for location in find_accessible_rolls(my_matrix):
        row, col = location
        my_matrix[row][col] = '.'
        count_removed += 1
    return count_removed

if __name__ == '__main__':
    matrix = read_char_array(INPUT)
    print(f'Part 1: {len(find_accessible_rolls(matrix))}')
    # part 2
    matrix = read_char_array(INPUT)
    rolls_removed = 0
    all_removed = False
    while not all_removed:
        removed = remove_accessible_rolls(matrix)
        if removed == 0:
            all_removed = True
        else:
            rolls_removed += removed
    print(f'Part 2: {rolls_removed}')

