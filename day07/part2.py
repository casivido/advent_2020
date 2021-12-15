# Determine bags given rules

import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

outer_bag_regex = r'^\w* \w*'
inner_bags_regex = r'\d* \w* \w* bags?'

rule_children = {}
for line in lines:
    if 'contain no other bags' in line:
        continue
    outer_bag = re.findall(outer_bag_regex, line)
    parent = outer_bag[0]

    inner_bags = re.findall(inner_bags_regex, line)
    inner_bags = list(map(lambda inner_list: (int(inner_list[0]), inner_list[2:-4].strip()), inner_bags))

    for child in inner_bags:
        if parent in rule_children:
            rule_children[parent].append(child)
        else:
            rule_children[parent] = [child]

starting_bag = 'shiny gold'
starting_bags = rule_children[starting_bag]

# children = [(num_bags, bag_color), ...]
def count_bag (children):
    bags = 0
    for child in children:
        bags += child[0]
        if child[1] in rule_children:
            bags += child[0] * count_bag(rule_children[child[1]])
    return bags

print(count_bag(starting_bags))