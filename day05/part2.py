import math

#

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

largest_id = 127 * 8 + 7
seat_list = list(range(0,largest_id+1))
available_seats = dict.fromkeys(seat_list, True)

max_id = 0
for line in lines:
    row = line[:7]
    column = line[7:]

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

    id = row * 8 + column
    available_seats[id] = False

for seat in seat_list[1:-1]:
    if available_seats[seat] is True:
        if available_seats[seat-1] is False:
            if available_seats[seat+1] is False:
                print(seat)