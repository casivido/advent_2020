# Verify and validate all required passport fields.

import re

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

passports = [{}]
index = 0
for line in lines:
    if line == '':
        index += 1
        passports.append({})
        continue

    value_pairs = line.split(' ')
    for pair in value_pairs:
        pair_tuple = re.match(r'(.*):(.*)', pair).groups()
        passports[index][pair_tuple[0]] = pair_tuple[1]

def height_func(height):
    if len(height) < 3:
        return False

    metric = height[-2:]
    value = int(height[:-2])
    if metric == 'cm':
        return value >= 150 and value <= 193
    elif metric == 'in':
        return value >= 59 and value <= 76
    return False

required_fields = {
    'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
    'hgt': height_func,
    'hcl': lambda x: re.search(r'^#[\w\d]{6}$', x),
    'ecl': lambda x: re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x),
    'pid': lambda x: re.search(r'^\d{9}$', x)
}

valid_passports = 0
for passport in passports:
    valid = True
    for field, func in required_fields.items():
        if field not in passport or not func(passport[field]):
            valid = False

    if valid:
        valid_passports += 1

print(valid_passports)

