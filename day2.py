from get_input import get_input

test_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
actual_input = get_input(2).text

input = [a.split(" ") for a in actual_input.strip().split("\n")]

# part 1
h = 0
v = 0
for d in input:
    if d[0] == "forward":
        h += int(d[1])
    elif d[0] == "down":
        v += int(d[1])
    else:
        v -= int(d[1])
print(h * v)

# part 2
a = 0
h = 0
v = 0
for d in input:
    if d[0] == "forward":
        h += int(d[1])
        v += int(d[1]) * a
    elif d[0] == "down":
        a += int(d[1])
    else:
        a -= int(d[1])
print(h * v)