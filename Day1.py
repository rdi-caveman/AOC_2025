# python
import re
from pathlib import Path

INPUT = Path('day1_input.txt')
pattern = re.compile(r'^\s*([A-Za-z])\s*(\d+)\s*$')  # letter then digits, with optional spaces

def read_letter_number_pairs(path: Path):
    pairs = []
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            m = pattern.match(line)
            if not m:
                continue  # skip empty/invalid lines
            letter = m.group(1)
            number = int(m.group(2))
            pairs.append([letter, number])
    return pairs

if __name__ == '__main__':
    data = read_letter_number_pairs(INPUT)
    #print(f'Parsed {len(data)} entries')

    password = 0
    current = 50
    for pair in data:
        if pair[0] == 'R':
            current = current + pair[1]
        else:
            current = current - pair[1]
        if current % 100 == 0:
            password += 1
    print(f'Part 1: {password}')

    # part 2
    password = 0
    current = 50
    for pair in data:
        # count the times we pass/land on 0
        # each complete rotation of 100 adds one to the password
        password += pair[1] // 100
        rotation = pair[1] % 100
        if rotation == 0:
            continue
        if pair[0] == 'R':
            if current + rotation >= 100:
                password += 1
            current = (current + rotation) % 100
        else:
            if current - rotation < 0 and current != 0:
                password += 1
            if current - rotation == 0:
                password += 1
            current = (current + 100 - rotation) % 100
        #print(f'After {pair[0]} {pair[1]} current is {current} password is {password}')
    print(f'Part 2: {password}')