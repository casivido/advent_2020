# Determine bags given rules

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

outer_bag_regex = r'^\w* \w*'
inner_bags_regex = r'\d* \w* \w* bags?'

rule_parents = {}
for line in lines:
    if 'contain no other bags' in line:
        continue
    outer_bag = re.findall(outer_bag_regex, line)
    inner_bags = re.findall(inner_bags_regex, line)
    inner_bags = list(map(lambda inner_list: inner_list[2:-4].strip(), inner_bags))

    for child in inner_bags:
        if child in rule_parents:
            rule_parents[child] += outer_bag
        else:
            rule_parents[child] = [outer_bag[0]]

starting_bag = 'shiny gold'
current_parents = rule_parents[starting_bag]

final_parents = {}
while len(current_parents):
    new_parents = []
    for parent in current_parents:
        if parent in final_parents:
            continue
        else:
            final_parents[parent] = True
            if parent in rule_parents:
                pp.pprint(rule_parents[parent])
                new_parents += rule_parents[parent]

    current_parents = new_parents

print(len(final_parents))