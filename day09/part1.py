# Find the first number that is not the sum in the previous 25

import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    input_numbers = [int(line.strip()) for line in input.readlines()]

preamble_length = 25
preamble = input_numbers[0:preamble_length]

def create_sums(numbers):
    sums = []
    for index, number in enumerate(numbers):
        if index == preamble_length - 1:
            break

        for second_number in numbers[index+1:]:
            sums.append(number + second_number)
    return sums
current_sums = create_sums(preamble)


index = preamble_length
while True:
    number = input_numbers[index]

    print('index', index)
    print('number', number)
    print('current_sums', current_sums)
    if number not in current_sums:
        break

    current_sums = create_sums(input_numbers[index-preamble_length+1:index+1])
    index += 1


print(number)