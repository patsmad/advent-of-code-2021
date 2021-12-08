from get_input import get_input

actual_input = get_input(7).text

test_input = """
16,1,2,0,4,2,7,1,2,14
""".strip()

input = sorted(list(map(int, actual_input.split(","))))
median = [(sum([abs(a - input[len(input) // 2]) for a in input]), input[len(input) // 2]), (sum([abs(a - input[len(input) // 2 + 1]) for a in input]), input[len(input) // 2 + 1])]
print(min(median)[0])

# The answer will be arond mean +- 0.5, so take the three possible integer points and print the minimum value
mean = sum(input) / len(input)
means = [
    (sum([abs(a - int(mean)) * (abs(a - int(mean)) + 1) // 2 for a in input]), int(mean)),
    (sum([abs(a - int(mean) + 1) * (abs(a - int(mean) + 1) + 1) // 2 for a in input]), int(mean) - 1),
    (sum([abs(a - int(mean) - 1) * (abs(a - int(mean) - 1) + 1) // 2 for a in input]), int(mean) + 1)
]
print(min(means)[0])