# Count the one and three chain links

import pprint
import math

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    input_text = [line.strip() for line in input.readlines()]

buses = []
bus_ids = []
mod_num = 1
for index, bus in enumerate(input_text[1].split(',')):
    if bus == 'x':
        continue
    bus_id = int(bus)
    buses.append((bus_id, index))
    bus_ids.append(bus_id)
    mod_num *= bus_id

final_nums = []
for bus in buses:
    remainder = (bus[0]-bus[1])%bus[0]
    modder = bus[0]

    num = mod_num/modder
    multiplier = 1
    while ((multiplier*num) % modder) != remainder:
        multiplier += 1

    final_nums.append(num*multiplier)

sum = sum(final_nums)
lowest = sum
while((lowest - mod_num) >= 0):
    lowest -= mod_num

print('Mod Num', mod_num)
print('Final Nums', final_nums)
print('Sum: ', sum)
print('Lowest:', lowest)