# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]

# [N, E, S, W]
waypoint = [1, 10, 0, 0]
waypoint_directions = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

position = {
    'N': 0,
    'E': 0,
    'S': 0,
    'W': 0
}

for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'L':
        value = value / 90
        while value != 0:
            value -= 1
            waypoint.append(waypoint.pop(0))
    elif command == 'R':
        value = value / 90
        while value != 0:
            value -= 1
            waypoint.insert(0, waypoint.pop())
    elif command == 'F':
        for way, index in waypoint_directions.items():
            position[way] += waypoint[index] * value
    else:
        waypoint[waypoint_directions[command]] += value

pp.pprint(position)
print(abs(position['N']-position['S'])+abs(position['E']-position['W']))