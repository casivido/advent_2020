# Count the number of valid passwords. A valid password must include the given letter as many times as the range allows.

import re

pattern = r'''(\d*)-(\d*) ([a-z]): (\w*)'''
with open('input1.txt', 'r') as input:
    lines = [re.match(pattern, line.strip()).groups() for line in input.readlines()]

num_passwords = 0
for line in lines:
    char_min = int(line[0])
    char_max = int(line[1])
    char = line[2]
    text = line[3]

    occurences = text.count(char)
    if occurences >= char_min and occurences <= char_max:
        num_passwords += 1

print(num_passwords)