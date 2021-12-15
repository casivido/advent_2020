# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    init = [line.strip() for line in input.readlines()]

space = []
space.append(init)

def countAdjEnabled(x, y, z, space):
    xs = [x-1, x, x+1]
    ys = [y-1, y, y+1]
    zs = [z-1, z, z+1]
    counter = 0
    for zcur in zs:
        if 0 > zcur or zcur >= len(space):
            continue
        for ycur in ys:
            if 0 > ycur or ycur >= len(space[zcur]):
                continue
            for xcur in xs:
                if 0 > xcur or xcur >= len(space[zcur][ycur]):
                    continue
                if zcur == z and ycur == y and xcur == x:
                    continue
                if space[zcur][ycur][xcur] == '#':
                    counter += 1
    return counter

def makeSpace(space, range_index):
    y_len = len(space[0])
    x_len = len(space[0][0])
    blank_y = '.' * x_len
    blank_z = [blank_y for y in range(y_len)]

    space.insert(0, copy.deepcopy(blank_z))
    space.append(copy.deepcopy(blank_z))

    for z_ind, z in enumerate(space):
        z.insert(0, blank_y)
        z.append(blank_y)
        for y_ind, y in enumerate(z):
            space[z_ind][y_ind] = '.'+space[z_ind][y_ind]+'.'

def printSpace(space):
    z_len = len(space)
    for z_ind in range(z_len):
        z_ind = z_ind
        print(z_ind, '--------')
        for y in space[z_ind]:
            print(y)

for index in range(6):
    makeSpace(space, index)
    spaceCopy = copy.deepcopy(space)

    active_counter = 0
    for z_ind, z_space in enumerate(space):
        for y_ind, y_space in enumerate(z_space):
            for x_ind, x_space in enumerate(y_space):
                count = countAdjEnabled(x_ind, y_ind, z_ind, spaceCopy)
                if x_space == '#':
                    if count != 2 and count != 3:
                        space[z_ind][y_ind] = space[z_ind][y_ind][:x_ind] + '.' + space[z_ind][y_ind][x_ind + 1:]
                if x_space == '.':
                    if count == 3:
                        space[z_ind][y_ind] = space[z_ind][y_ind][:x_ind] + '#' + space[z_ind][y_ind][x_ind + 1:]
                if space[z_ind][y_ind][x_ind] == '#':
                    active_counter += 1

# printSpace(space)
print(active_counter)