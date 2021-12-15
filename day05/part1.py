import math

#

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

max_id = 0
for line in lines:
    row = line[:7]
    column = line[7:]
#FFFBBBB LRR
    row_range = [0,127]
    for letter in row:
        half_amount = max(1, math.ceil((row_range[1] - row_range[0])/2))
        if letter == 'B':
            row_range[0] += half_amount
        elif letter == 'F':
            row_range[1] -= half_amount
    row = row_range[0]

    col_range = [0,7]
    for letter in column:
        half_amount = max(1, math.ceil((col_range[1] - col_range[0])/2))
        if letter == 'R':
            col_range[0] += half_amount
        elif letter == 'L':
            col_range[1] -= half_amount
    column = col_range[0]

    max_id = max(row * 8 + column, max_id)

print(max_id)