# python
import re
from pathlib import Path

fresh_pattern = re.compile(r'^(\d+)-(\d+)$')
ingredient_pattern = re.compile(r'^(\d+)$')

fresh = []      # list of [first, last] ranges
ingredient = [] # list of ingredient IDs

# read fresh ingredient ranges and ingredient IDs from file
def read_fresh_ingredients(file: Path):
    with file.open('r', encoding='utf-8') as f:
        for line in f:
            m = fresh_pattern.match(line)
            if m:
                first = int(m.group(1))
                last = int(m.group(2))
                fresh.append([first,last])
                continue
            m = ingredient_pattern.match(line)
            if m:
                ingredient.append(int(m.group(1)))
    return

if __name__ == '__main__':
    read_fresh_ingredients(Path('day5_input.txt'))
    # part 1
    # count ingredients that are in any fresh range
    total_fresh = 0
    for ing in ingredient:
        for fr in fresh:
            start = int(fr[0])
            end = fr[1]
            if start <= ing <= end:
                total_fresh += 1
                break
    print(f'Part 1: {total_fresh}')
    # part 2
    # identify total number of ingredient IDs that are fresh
    # sort ranges and merge overlapping ones
    fresh.sort(key=lambda x: x[0])
    merged_fresh = []
    for fr in fresh:
        if not merged_fresh:
            merged_fresh.append(fr)
        else:
            last_end = merged_fresh[len(merged_fresh)-1][1]
            if fr[0] <= last_end:
                merged_fresh[len(merged_fresh)-1][1] = max(last_end, fr[1])
            else:
                merged_fresh.append(fr)
    # now count ingredient IDs that are in any fresh range
    num_fresh_ingredient_ids = 0
    for fr in merged_fresh:
        num_fresh_ingredient_ids += fr[1] - fr[0] + 1
    print(f'Part 2: {num_fresh_ingredient_ids}')
