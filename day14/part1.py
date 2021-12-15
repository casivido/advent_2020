# Count the one and three chain links

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]

mem_pattern = r'''mem\[(\d*)] = (\d*)'''
registers = {}
mask = ''

for instruction in instructions:
    if instruction[0:4] == 'mask':
        mask = instruction[7:]
        continue

    inputs = re.match(mem_pattern, instruction).groups()
    register = inputs[0]
    value = int(inputs[1])
    value_bin = bin(value)[2:].zfill(36)

    for index, char in enumerate(mask):
        if char == 'X':
            continue
        value_bin = value_bin[:index] + char + value_bin[index + 1:]

    registers[register] = int(value_bin, 2)

print(sum(registers.values()))
