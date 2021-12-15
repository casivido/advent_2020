# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]

direction = 0
directions = {
    0: 'E',
    90: 'S',
    180: 'W',
    270: 'N'
}

position = {
    'N': 0,
    'S': 0,
    'E': 0,
    'W': 0
}

for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'L':
        direction -= value
    elif command == 'R':
        direction += value

    elif command == 'F':
        position[directions[direction%360]] += value

    else:
        position[command] += value

pp.pprint(position)
print(abs(position['N']-position['S'])+abs(position['E']-position['W']))