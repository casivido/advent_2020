# Count the one and three chain links

import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    input_text = [line.strip() for line in input.readlines()]

arrival_time = int(input_text[0])
# print('Arrival Time: ', arrival_time)
bus_ids = input_text[1].split(',')

closest_bus = (float('inf'), 0)
for id in bus_ids:
    # print('Checking bus:', id)
    if id == 'x':
        # print(' Skipping...')
        continue
    bus_id = int(id)
    shortest_time = bus_id - (arrival_time % bus_id)
    # print('Shortest Time = ', shortest_time)
    if shortest_time < closest_bus[0]:
        closest_bus = (shortest_time, bus_id)
        print('New Shortest')
    # print(closest_bus)


print('Answer: ', closest_bus[0] * closest_bus[1])
