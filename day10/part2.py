# Find the amount of possible chain links

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    adapters = [int(line.strip()) for line in input.readlines()]

adapters.sort()
adapters.append(adapters[-1]+3)

paths = {0: 1}
for cur_adapter in adapters:
    new_paths = {}
    for leaf_adapter, leaf_quantity in paths.items():
        if leaf_adapter >= (cur_adapter - 3):
            if cur_adapter in new_paths:
                new_paths[cur_adapter] += leaf_quantity
            else:
                new_paths[cur_adapter] = leaf_quantity
        if leaf_adapter > (cur_adapter - 3):
            if leaf_adapter in new_paths:
                new_paths[leaf_adapter] += leaf_quantity
            else:
                new_paths[leaf_adapter] = leaf_quantity
    paths = new_paths

print(paths)