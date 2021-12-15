# Verify all passports have the required fields.

import re

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

value_pattern = r'''(.*):(.*)'''

passports = [{}]
index = 0
for line in lines:
    if line == '':
        index += 1
        passports.append({})
        continue

    value_pairs = line.split(' ')
    for pair in value_pairs:
        pair_tuple = re.match(value_pattern, pair).groups()
        passports[index][pair_tuple[0]] = pair_tuple[1]

valid_passports = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    valid = True
    for field in required_fields:
        if field not in passport:
            valid = False

    if valid:
        valid_passports += 1

print(valid_passports)

