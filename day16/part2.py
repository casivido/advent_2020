# Count the one and three chain links

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]

field_pattern = r'''(.*): (\d*)-(\d*) or (\d*)-(\d*)'''
field_rules = {}
index = 0

# Fields
while instructions[index] != '':
    rule = re.match(field_pattern, instructions[index]).groups()

    field = rule[0]

    min1 = int(rule[1])
    max1 = int(rule[2])

    min2 = int(rule[3])
    max2 = int(rule[4])

    field_rules[field] = {
        'min1': min1,
        'max1': max1,
        'min2': min2,
        'max2': max2
    }

    index += 1

print('MIN MAXES:')
print(field_rules)

# My Ticket
index += 2
my_ticket = instructions[index].split(',')
print(my_ticket)

index += 3

invalid_nums = []
invalid_indices = [39, 42, 46, 48, 49, 53, 61, 63, 64, 65, 69, 74, 77, 80, 94, 98, 102, 103, 106, 117, 120, 129, 130, 133, 140, 142, 147, 150, 151, 152, 153, 155, 158, 159, 161, 164, 169, 182, 190, 199, 201, 210, 213, 222, 224, 225, 228, 236, 245, 251, 252, 253, 257, 258, 269]
# invalid_indices = [9,10,11]

num_fields = len(field_rules)
field_validity = {}
for field_name in field_rules:
    field_validity[field_name] = list(range(num_fields))
print(field_validity)



def check_num(num, rules):
    if rules['min1'] <= num <= rules['max1']:
        return True
    if rules['min2'] <= num <= rules['max2']:
        return True
    return False

# Nearby Tickets
while index < len(instructions):
    if index in invalid_indices:
        index += 1
        continue

    nums = instructions[index].split(',')
    for field_index, num in enumerate(nums):
        for field, validities in field_validity.items():
            if field_index in validities:
                if not check_num(int(num), field_rules[field]):
                    field_validity[field].remove(field_index)
    index+=1

updated = True
done = {}
while updated == True:
    updated = False
    for field, validities in field_validity.items():
        for num in done:
            if num in validities:
                updated = True
                validities.remove(num)
        if len(validities) == 1:
            done[validities[0]] = field
            updated = True

print(done)

product = 1
for index, field in done.items():
    if field.startswith('departure'):
        product *= int(my_ticket[index])

print(product)