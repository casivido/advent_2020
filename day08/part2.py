# Fix loop in instruction set

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

pattern = r'''(\w*) ([+-]\d*)'''
with open('input1.txt', 'r') as input:
    instructions = [list(re.match(pattern, line.strip()).groups()) for line in input.readlines()]

# (instr_index, acc)
functions = {
    'nop': lambda val: (accum[0]+1, accum[1]),
    'acc': lambda val: (accum[0]+1, accum[1] + val),
    'jmp': lambda val: (accum[0]+val, accum[1])
}

success = False
# print(history)
for index, raw_instruction in enumerate(instructions):
    new_instructions = []
    for raw_instruction in instructions:
        new_instructions.append(raw_instruction.copy())
    if new_instructions[index][0] == 'nop':
        new_instructions[index][0] = 'jmp'
    elif new_instructions[index][0] == 'jmp':
        new_instructions[index][0] = 'nop'
    else:
        continue

    accum = (0, 0)
    history = dict.fromkeys(range(len(instructions)), False)
    while not history[accum[0]]:
        instruction = new_instructions[accum[0]]

        history[accum[0]] = True
        accum = functions[instruction[0]](int(instruction[1]))

        if accum[0] not in history:
            success = True
            break
        if history[accum[0]]:
            break
    print(accum)
    if success:
        break

print(success)
print(index)