from get_input import get_input

actual_input = get_input(3).text

test_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

input = actual_input.strip().split("\n")

N = len(input[0])
out = [0] * N
for line in input:
    for i, c in enumerate(line):
        if c == '1':
            out[i] += 1 / len(input)
gamma = sum([(2**(N - i - 1)) * (a > 0.5) for i, a in enumerate(out)])
epsilon = 2**N - 1 - gamma
print(gamma * epsilon)

def sort_array(a, i):
    hi = len(a) - 1
    lo = 0
    while lo < hi:
        while a[lo][i] == '0':
            lo += 1
        while a[hi][i] == '1':
            hi -= 1
        if lo < hi:
            temp = a[lo]
            a[lo] = a[hi]
            a[hi] = temp
    return lo, a

sorted_array = input
for i in range(N):
    idx, sorted_array = sort_array(sorted_array, i)
    if idx > len(sorted_array) // 2:
        sorted_array = sorted_array[:idx]
    else:
        sorted_array = sorted_array[idx:]
O2 = sum([(2**(N - i - 1)) * (a == "1") for i, a in enumerate(sorted_array[0])])

sorted_array = input
for i in range(N):
    idx, sorted_array = sort_array(sorted_array, i)
    if idx > len(sorted_array) // 2:
        sorted_array = sorted_array[idx:]
    else:
        sorted_array = sorted_array[:idx]
    if len(sorted_array) == 1:
        break
CO2 = sum([(2**(N - i - 1)) * (a == "1") for i, a in enumerate(sorted_array[0])])

print(O2 * CO2)
