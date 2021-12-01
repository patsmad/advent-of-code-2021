from get_input import get_input

input = get_input(1).text
input = list(map(int, input.strip().split('\n')))

# part 1
count = 0
for i in range(1, len(input)):
    if input[i] > input[i - 1]:
        count += 1
print(count)

# part 3

count = 0
for i in range(3, len(input)):
    if input[i] > input[i - 3]:
        count += 1
print(count)