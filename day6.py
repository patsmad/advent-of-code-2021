from get_input import get_input

actual_input = get_input(6).text

test_input = """
3,4,3,1,2
""".strip()

input = [int(a) for a in actual_input.split(",")]

# dynamic programming solution
def run(N):
    v = [0] * (N + 9)
    for i in range(len(v) - 1, -1, -1):
        s = 0
        v[i] = 1
        j = i + 9
        while j < len(v):
            v[i] += v[j]
            j += 7
    print(sum([v[a] for a in input]))

run(80)
run(256)
