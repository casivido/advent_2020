# Find a contiguous set of numbers whose sum is the erroneous number from part 1

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    input_numbers = [int(line.strip()) for line in input.readlines()]

# magic_number = 127 # testing
magic_number = 69316178

answer = 0
sum_lists = []
index = 0
while not answer:
    number = input_numbers[index]
    index += 1
    if number == magic_number:
        continue

    sum_lists.append([])
    sum_index = 0
    while sum_index < len(sum_lists):
        current_list = sum_lists[sum_index]
        current_list.append(number)
        current_sum = sum(current_list)

        if current_sum > magic_number:
            sum_lists.pop(sum_index)
            continue
        if current_sum == magic_number:
            answer = max(current_list) + min(current_list)
            break
        sum_index += 1




print(answer)