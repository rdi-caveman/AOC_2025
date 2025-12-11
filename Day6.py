# python
import re
from pathlib import Path

from Common import read_char_array

INPUT = Path('day6_input.txt')

if __name__ == '__main__':
    # part 1
    with INPUT.open('r', encoding='utf-8') as f:
        worksheet = []
        for line in f:
            worksheet.append(re.split(r'\s+', line.strip()))

    grand_total = 0
    for col in range(len(worksheet[0])):
        if worksheet[len(worksheet)-1][col] == '+':
            col_total = 0
            for row in range(len(worksheet)-1):
                col_total +=int(worksheet[row][col])
        else:
            col_total = 1
            for row in range(len(worksheet)-1):
                col_total *= int(worksheet[row][col])
        grand_total += col_total
    print(f'Part 1: {grand_total}')

    #part 2
    worksheet = read_char_array(INPUT)
    grand_total = 0
    last_row = len(worksheet)-1
    nums = []
    for col in reversed(range(len(worksheet[0]))):
        num = ''
        for row in range(last_row):
            if worksheet[row][col] == ' ':
                continue
            num += worksheet[row][col]
        if num != '':
            nums.append(int(num))
        if worksheet[last_row][col] == '+':
            partial_total = 0
            for i in range(len(nums)):
                partial_total += nums[i]
            grand_total += partial_total
            nums = []
        elif worksheet[last_row][col] =='*':
            partial_total = 1
            for i in range(len(nums)):
                partial_total *= nums[i]
            grand_total += partial_total
            nums = []
    print(f'Part 2: {grand_total}')