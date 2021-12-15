# Count all valid passwords. A password is valid if the given letter appears in either index location given.

import re
text = '1-3 a: abcde'
pattern = r'''(\d*)-(\d*) ([a-z]): (\w*)'''
match = re.match(pattern, text)
with open('input1.txt', 'r') as input:
    lines = [re.match(pattern, line.strip()).groups() for line in input.readlines()]

num_passwords = 0
for line in lines:
    char_pos1 = int(line[0]) - 1
    char_pos2 = int(line[1]) - 1
    char = line[2]
    text = line[3]
    text_len = len(text)

    char1_exists = char_pos1 < text_len and text[char_pos1] == char
    char2_exists = char_pos2 < text_len and text[char_pos2] == char

    if char1_exists ^ char2_exists:
        num_passwords += 1

print(num_passwords)