# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    rows = [line.strip() for line in input.readlines()]

row_length = len(rows[0])

def countAdjFilled(row_index, seat_index, rows):
    toCheck_Raw = [
        (row_index-1,seat_index-1), (row_index-1,seat_index), (row_index-1,seat_index+1),
        (row_index,seat_index-1), (row_index,seat_index+1),
        (row_index+1,seat_index-1), (row_index+1,seat_index), (row_index+1,seat_index+1)
    ]

    toCheck = []
    for place in toCheck_Raw:
        if -1 < place[0] < len(rows) and -1 < place[1] < len(rows[0]):
            toCheck.append(place)

    filled = 0
    for place in toCheck:
        if rows[place[0]][place[1]] == '#':
            filled += 1

    return filled



def getNewSeat(row_index, seat_index, rows):
    seat = rows[row_index][seat_index]
    if seat == '.':
        return '.'

    filledAdjSeats = countAdjFilled(row_index, seat_index, rows)
    if seat == '#' and filledAdjSeats > 3:
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
                updated = True
            if newSeat == '#':
                filled += 1
    rows = new_rows

print(filled)