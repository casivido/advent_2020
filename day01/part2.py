# Return the product of the three numbers whose sum is 2020

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
        for k, k_value in enumerate(lines):
            if k == j or k == i:
                continue
            elif (i_value + j_value + k_value) == 2020:
                result = (i_value, j_value, k_value)
                break

print(result)
print(result[0] * result[1] * result[2])