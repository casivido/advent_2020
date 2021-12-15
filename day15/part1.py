# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

input = [2,0,1,9,5,19]
# input = [0,3,6]

tracker = {}
turn = 1
for number in input[0:-1]:
    tracker[number] = turn
    turn += 1

cur_number = input[-1]
while turn < 30000000:
    new_number = 0
    if cur_number in tracker:
        new_number = turn - tracker[cur_number]

    tracker[cur_number] = turn
    cur_number = new_number
    turn += 1

print(cur_number)