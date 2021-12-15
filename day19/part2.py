# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)
index = 0

with open('/Users/christian.asivido/repos/advent_2020/day19/input2.txt', 'r') as input:
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

def simplify(rule_num, rule, simplified_rules, cur_list):
    simplified_rule = ['']
    for part in rule:
        if part.isnumeric():
            rule_pointer = int(part)
            repeater = False
            if rule_pointer == rule_num:
                repeater = True
            elif rule_pointer not in simplified_rules:
                return False


            if repeater:
                # Repeater
                new_cur_list = copy.deepcopy(cur_list)
                # if rule_num == 8:
                #     for match_list in new_cur_list:
                #         for match in match_list:
                #             multiplier = 2
                #             while (len(match) * multiplier) < 50:
                #                 match_list.append(match*multiplier)
                #                 multiplier += 1
                #                 print((len(match) * multiplier))
                # if rule_num == 11:
                #     for match_list in new_cur_list:
                #         for match in match_list:
                #             multiplier = 2
                #             half_match_len = int(len(match)/2)
                #             while (len(match) * multiplier) < 50:
                #                 match_list.append((match[:half_match_len]*multiplier)+(match[half_match_len:]*multiplier))
                #                 multiplier += 1
                #                 (len(match) * multiplier)
                pointer_rules = new_cur_list
                # print('REPEATER POINTER: ', rule_num, pointer_rules)
            else:
                pointer_rules = simplified_rules[rule_pointer]
                # print('NORMAL POINTER: ', pointer_rules)

            print('appending', rule_num)
            sum = 1
            for simple_rule_cur in simplified_rule:
                for new_simple_suffix_list in pointer_rules:
                    sum += len(new_simple_suffix_list)

            print('sum: ', sum)


            new_simplified_rule = []
            for simple_rule_cur in simplified_rule:
                for new_simple_suffix_list in pointer_rules:
                    for new_simple_suffix in new_simple_suffix_list:
                        new_simplified_rule.append(simple_rule_cur + new_simple_suffix)
            simplified_rule = new_simplified_rule
            #########
        else:
            new_simplified_rule = []
            for simple_rule_cur in simplified_rule:
                new_simplified_rule.append(simple_rule_cur + part)
            simplified_rule = new_simplified_rule
    return simplified_rule


# Simplify rules
updated = True
simplified_rules = {}
disabled_rule_nums = [0,8,11]
while updated == True:
    print('----------')
    updated = False
    for rule_num, rule_list in rules.items():
        if rule_num in simplified_rules or rule_num in disabled_rule_nums:
            continue
        ready = True
        simplified_list = []
        for rule in rule_list:
            simplified_rule = simplify(rule_num, rule, simplified_rules, simplified_list)
            if not simplified_rule:
                print('NOT READY: ', rule_num)
                ready = False
                break
            simplified_list.append(simplified_rule)
        if ready:
            updated = True
            simplified_rules[rule_num] = simplified_list
    # pp.pprint(simplified_rules)

pp.pprint(simplified_rules)

# [ 42 | 42 8 ]
rule8 = [42 , 8]
rule42 = simplified_rules[42]
def testRule8(message, rules):
    remainders = []

    done = False
    remainder = message
    while not done:
        cur_match = False
        done = True
        for match_list in rule42:
            if cur_match:
                break
            for match in match_list:
                if remainder.startswith(match):
                    cur_match = True
                    remainder = remainder[len(match):]
                    remainders.append(remainder)
                    done = False
                    break
                elif len(remainder) < len(match):
                    done = True

    return remainders

# [ 42 31 | 42 11 31]
rule11 = [42, 11, 31]
rule42 = simplified_rules[42]
rule31 = simplified_rules[31]
def testRule11(message, rules):
    cur_message = message
    done = False
    while not done:
        matched = False
        for match42_list in rule42:
            if matched:
                break
            for match42 in match42_list:
                if cur_message.startswith(match42):
                    matched = True
                    cur_message = cur_message[len(match42):]
                    break
                if len(match42) > len(cur_message):
                    return False

        if not matched:
            return False

        matched = False
        for match31_list in rule31:
            if matched:
                break
            for match31 in match31_list:
                if cur_message.endswith(match31):
                    matched = True
                    cur_message = cur_message[:-len(match31)]
                    break
                if len(match31) > len(cur_message):
                    return False

        if not matched:
            return False
        if cur_message == '':
            return True

    return False




# Test the messages
index += 1
counter = 0
while index < len(inputs):
    message = inputs[index]
    print('Message:', message)

    print('Testing Rule 8')
    remainders = testRule8(message, simplified_rules)
    print('8 Remainders: ', remainders)

    print('Testing Rule 11')
    success = False
    for remainder in remainders:
        passed = testRule11(remainder, simplified_rules)
        print('11 Passed: ', passed)
        if passed:
            success = True
            print('SUCESS!')
            break

    if success:
        counter += 1

    index += 1


print(counter)