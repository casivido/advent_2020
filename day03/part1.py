# Count how many trees you'd hit if you sled right 3 down 1 over and over.

with open('input1.txt', 'r') as input:
    map = [line.strip() for line in input.readlines()]

x_length = len(map[0])
y_length = len(map)

def getMapValue(x, y):
    return map[y][x%x_length]

x = 0
y = 0
num_trees = 0
while y < y_length:
    if getMapValue(x,y) == '#':
        num_trees += 1
    x += 3
    y += 1

print(num_trees)