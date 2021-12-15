# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    init = [line.strip() for line in input.readlines()]

space = []
space.append([init])


def countAdjEnabled(x, y, w, z, space):
    xs = [x-1, x, x+1]
    ys = [y-1, y, y+1]
    ws = [w-1, w, w+1]
    zs = [z-1, z, z+1]
    counter = 0
    for zcur in zs:
        if 0 > zcur or zcur >= len(space):
            continue
        for wcur in ws:
            if 0 > wcur or wcur >= len(space[zcur]):
                continue
            for ycur in ys:
                if 0 > ycur or ycur >= len(space[zcur][wcur]):
                    continue
                for xcur in xs:
                    if 0 > xcur or xcur >= len(space[zcur][wcur][ycur]):
                        continue
                    if zcur == z and ycur == y and xcur == x and wcur == w:
                        continue
                    if space[zcur][wcur][ycur][xcur] == '#':
                        counter += 1
    return counter

def makeSpace(space, range_index):
    w_len = len(space[0])
    y_len = len(space[0][0])
    x_len = len(space[0][0][0])
    blank_y = '.' * x_len
    blank_w = [blank_y for y in range(y_len)]
    blank_z = [copy.deepcopy(blank_w) for w in range(w_len)]

# HERE
    space.insert(0, copy.deepcopy(blank_z))
    space.append(copy.deepcopy(blank_z))

    for z_ind, z in enumerate(space):
        z.insert(0, copy.deepcopy(blank_w))
        z.append(copy.deepcopy(blank_w))
        for w_ind, w in enumerate(z):
            w.insert(0, blank_y)
            w.append(blank_y)
            for y_ind, y in enumerate(w):
                space[z_ind][w_ind][y_ind] = '.'+space[z_ind][w_ind][y_ind]+'.'

for index in range(6):
    makeSpace(space, index)
    spaceCopy = copy.deepcopy(space)

    active_counter = 0
    for z_ind, z_space in enumerate(space):
        for w_ind, w_space in enumerate(z_space):
            for y_ind, y_space in enumerate(w_space):
                for x_ind, x_space in enumerate(y_space):
                    count = countAdjEnabled(x_ind, y_ind, w_ind, z_ind, spaceCopy)
                    if x_space == '#':
                        if count != 2 and count != 3:
                            space[z_ind][w_ind][y_ind] = space[z_ind][w_ind][y_ind][:x_ind] + '.' + space[z_ind][w_ind][y_ind][x_ind + 1:]
                    if x_space == '.':
                        if count == 3:
                            space[z_ind][w_ind][y_ind] = space[z_ind][w_ind][y_ind][:x_ind] + '#' + space[z_ind][w_ind][y_ind][x_ind + 1:]
                    if space[z_ind][w_ind][y_ind][x_ind] == '#':
                        active_counter += 1

# printSpace(space)
print(active_counter)