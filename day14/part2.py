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
    register_values = [bin(int(inputs[0]))[2:].zfill(36)]
    value = int(inputs[1])

    for index, char in enumerate(mask):
        if char == '0':
            continue
        elif char == '1':
            new_register_values = []
            for register in register_values:
                new_register_values.append(register[:index] + char + register[index + 1:])
            register_values = new_register_values
        elif char == 'X':
            new_register_values = []
            for register in register_values:
                new_register_values.append(register[:index] + '0' + register[index + 1:])
                new_register_values.append(register[:index] + '1' + register[index + 1:])
            register_values = new_register_values

    for register in register_values:
        registers[register] = value

print(sum(registers.values()))
