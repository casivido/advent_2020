# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)
index = 0

with open('input1.txt', 'r') as input:
    inputs = [line.strip() for line in input.readlines()]

# Extract rules
rules = {}
rule_pattern = r'''(\d*): (.*)'''
while inputs[index] != '':
    line = re.match(rule_pattern, inputs[index]).groups()
    rule_list_raw = line[1].split(' | ')
    rule_list = []
    for rule in rule_list_raw:
        rule_list.append(rule.replace('"','').split(' '))
    rules[int(line[0])] = rule_list

    index += 1

def simplify(rule, simplified_rules):
    simplified_rule = ['']
    for part in rule:
        if part.isnumeric():
            rule_pointer = int(part)
            if rule_pointer not in simplified_rules:
                return False
            new_simplified_rule = []
            for simple_rule_cur in simplified_rule:
                for new_simple_suffix_list in simplified_rules[rule_pointer]:
                    for new_simple_suffix in new_simple_suffix_list:
                        new_simplified_rule.append(simple_rule_cur + new_simple_suffix)
            simplified_rule = new_simplified_rule
        else:
            new_simplified_rule = []
            for simple_rule_cur in simplified_rule:
                new_simplified_rule.append(simple_rule_cur + part)
            simplified_rule = new_simplified_rule
    return simplified_rule


# Simplify rules
updated = True
simplified_rules = {}
while updated == True:
    updated = False
    for rule_num, rule_list in rules.items():
        if rule_num in simplified_rules:
            continue
        ready = True
        simplified_list = []
        for rule in rule_list:
            simplified_rule = simplify(rule, simplified_rules)
            if not simplified_rule:
                ready = False
                break
            simplified_list.append(simplified_rule)
        if ready:
            updated = True
            simplified_rules[rule_num] = simplified_list

# pp.pprint(simplified_rules)


# Test the messages
index += 1
counter = 0
testing_rule = 0
while index < len(inputs):
    valid = False
    message = inputs[index]
    for rule_list in simplified_rules[testing_rule]:
        if valid:
            break
        for rule in rule_list:
            if rule == message:
                valid = True
                break
    if valid:
        counter += 1
    index += 1


print(counter)