from get_input import get_input

input = list(map(int, get_input(1).text.strip().split('\n')))

def get_count(window_size):
    count = 0
    for i in range(window_size, len(input)):
        if input[i] > input[i - window_size]:
            count += 1
    return count

# part 1
print(get_count(1))

# part 2
print(get_count(3))