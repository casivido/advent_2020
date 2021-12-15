# Find loop in instruction set

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]
history = dict.fromkeys(range(len(instructions)), False)

# (instr_index, acc)
accum = (0, 0)
functions = {
    'nop': lambda val: (accum[0]+1, accum[1]),
    'acc': lambda val: (accum[0]+1, accum[1] + val),
    'jmp': lambda val: (accum[0]+val, accum[1])
}

# print(history)
pattern = r'''(\w*) ([+-]\d*)'''
while not history[accum[0]]:
    instruction = re.match(pattern, instructions[accum[0]]).groups()
    print(instruction)

    history[accum[0]] = True
    accum = functions[instruction[0]](int(instruction[1]))
    print(accum)

    if history[accum[0]]:
        break
print(accum)