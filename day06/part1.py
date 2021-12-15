# Verify all passports have the required fields.

import re

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]
last_line = len(lines) - 1

answers_sum = 0
current_answers = {}
new_group = True
for index, line in enumerate(lines):
    persons_answers = {}
    for answer in line:
        persons_answers[answer] = True

    if new_group:
        current_answers = persons_answers
        new_group = False
    elif line != '':
        delete_answers = []
        for current_answer in current_answers:
            if current_answer not in persons_answers:
                delete_answers.append(current_answer)

        for delete_answer in delete_answers:
            del current_answers[delete_answer]

    if line == '' or index == last_line:
        new_group = True
        answers_sum += len(current_answers)
        current_answers = {}

print(answers_sum)

