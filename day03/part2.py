# Count how many trees your sled would hit if you sled at different angles than part 1.

import functools

with open('input1.txt', 'r') as input:
    map = [line.strip() for line in input.readlines()]

x_length = len(map[0])
y_length = len(map)

def getMapValue(x, y):
    return map[y][x%x_length]

num_trees_list = []
increments_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]
for increments in increments_list:
    x = 0
    y = 0
    num_trees = 0
    while y < y_length:
        if getMapValue(x,y) == '#':
            num_trees += 1
        x += increments[0]
        y += increments[1]

    num_trees_list.append(num_trees)

print(functools.reduce(lambda a,b : a*b, num_trees_list))