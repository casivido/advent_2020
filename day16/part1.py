# Count the one and three chain links

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]

field_pattern = r'''(.*): (\d*)-(\d*) or (\d*)-(\d*)'''
min_maxes = []

def add_min_max(min, max, min_maxes):
    added = False
    # [5,6]
    # ADDING [ 1, 10 ]
    for min_max in min_maxes:
        if min > min_max[0]: # Check for upper half
            if min > min_max[1]: # Outside this rule
                continue
            if max < min_max[1]: # Already inside
                added = True
                break
            min_max[1] = max # Increase max
            added = True
            break
        if max <= min_max[1]: # Check lower half
            if max < min_max[0]: # Outside this rule
                continue
            if min > min_max[0]: # Already inside
                added = True
                break
            min_max[0] = min # Decrease min
            added = True
            break
        if min < min_max[0] and max > min_max[1]:
            min_max[0] = min
            min_max[1] = max
            added = True
            break

    if added == False:
        min_maxes.append([min, max])

index = 0

# Fields
while instructions[index] != '':
    rule = re.match(field_pattern, instructions[index]).groups()

    field = rule[0]

    min1 = int(rule[1])
    max1 = int(rule[2])

    min2 = int(rule[3])
    max2 = int(rule[4])

    add_min_max(min1,max1, min_maxes)
    add_min_max(min2,max2, min_maxes)

    index += 1

print('MIN MAXES:')
print(min_maxes)

# My Ticket
index += 2
my_ticket = instructions[index].split(',')
print(my_ticket)

index += 3

def check_num(num, min_maxes):
    for min_max in min_maxes:
        if num >= min_max[0]:
            if num <= min_max[1]:
                return True

    return False

invalid_nums = []
invalid_indices = []
# Nearby Tickets
while index < len(instructions):
    # print(instructions[index])
    # print(index)
    ticket = instructions[index].split(',')
    # print(ticket)

    invalid_num = None
    for raw_num in ticket:
        num = int(raw_num)
        if not check_num(num, min_maxes):
            invalid_num = num
            invalid_indices.append(index)
            break

    if invalid_num != None:
        invalid_nums.append(invalid_num)
    index +=1

print('Inv Nums:', sum(invalid_nums))
print('Inv Indices:', invalid_indices)