# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    rows = [line.strip() for line in input.readlines()]

row_length = len(rows[0])

def countVisibleFilled(row_index, seat_index, rows):
    checkingPattern = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1)
    ]

    filled = 0
    for pattern in checkingPattern:
        curRow = row_index + pattern[0]
        curSeat = seat_index + pattern[1]
        while True:
            # No filled seat in sight
            if (curRow < 0 or curRow >= len(rows)) or (curSeat < 0 or curSeat >= len(rows[0])):
                break
            seat = rows[curRow][curSeat]

            # Floor, continue
            if seat == '.':
                curRow += pattern[0]
                curSeat += pattern[1]
                continue

            if seat == '#':
                filled += 1
            break

    return filled



def getNewSeat(row_index, seat_index, rows):
    seat = rows[row_index][seat_index]
    if seat == '.':
        return '.'

    filledAdjSeats = countVisibleFilled(row_index, seat_index, rows)
    if seat == '#' and filledAdjSeats > 4:
        return 'L'
    if seat == 'L' and filledAdjSeats == 0:
        return '#'

    return seat
updated = True
while updated == True:
    filled = 0
    new_rows = []
    updated = False
    for row_index, row in enumerate(rows):
        new_rows.append([])
        for seat_index, seat in enumerate(row):
            newSeat = getNewSeat(row_index, seat_index, rows)
            new_rows[row_index].append(newSeat)
            if newSeat != seat:
                updated = True # Set back to true
            if newSeat == '#':
                filled += 1
    rows = new_rows

print(filled)