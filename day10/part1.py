# Count the one and three chain links

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    adapters = [int(line.strip()) for line in input.readlines()]

adapters.sort()
print(adapters)

one_diffs = 0
three_diffs = 1
prev_value = 0
for index, value in enumerate(adapters):
    if value - prev_value == 1:
        one_diffs += 1
        print('ONE DIFF')
        print('index:', index)
        print(adapters[index-1], value)
    if value - prev_value == 3:
        print('THREE DIFF')
        print('index:', index)
        print(adapters[index-1], value)
        three_diffs += 1
    prev_value = value

print(one_diffs)
print(three_diffs)
print(one_diffs*three_diffs)