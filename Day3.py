# python
from pathlib import Path

from Common import read_input_lines

INPUT = Path('day3_input.txt')


def greatest_digit_location(line: str, start: int, end: int) -> int:
    digit_location = start
    location = start + 1
    while int(line[digit_location]) < 9 and location < end:
        if int(line[location]) > int(line[digit_location]):
            digit_location = location
        location +=  1
    return digit_location

def battery_joltage(line: str, cells: int) -> int:
    digit_location = 0
    joltage = 0
    for cell in range(0, cells):
        end = len(line) - (cells-1) + cell
        digit_location = greatest_digit_location(line, digit_location, end)
        joltage = joltage*10 + int(line[digit_location])
        digit_location += 1
    return joltage

def total_joltage(lines: list[str], cells: int) -> int:
    total = 0
    for line in lines:
        total += battery_joltage(line, cells)
    return total

if __name__ == '__main__':
    LINES = read_input_lines(INPUT)
    print("Part 1:", total_joltage(LINES, 2))
    print("Part 2:", total_joltage(LINES, 12))
