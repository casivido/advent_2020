# Return the product of the two numbers whose sum is 2020

lines = []
with open('input1.txt', 'r') as input:
    lines = [int(i) for i in input.readlines()]

result = None
for i, i_value in enumerate(lines):
    if result:
        break
    for j, j_value in enumerate(lines):
        if i == j:
            continue
        elif (i_value + j_value) == 2020:
            result = (i_value, j_value)
            break

print(result)
print(result[0] * result[1])