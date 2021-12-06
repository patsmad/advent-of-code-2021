from get_input import get_input

actual_input = get_input(5).text

test_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

input = [[[int(coord) for coord in coords.split(',')] for coords in line.split(' -> ')] for line in actual_input.strip().split("\n")]

rocks = {}
for line in input:
    dx = (0, 0)
    length = -1
    if line[0][0] == line[1][0]:
        dx = (0, 1 - 2 * (line[1][1] < line[0][1]))
        length = abs(line[0][1] - line[1][1])
    elif line[0][1] == line[1][1]:
        dx = (1 - 2 * (line[1][0] < line[0][0]), 0)
        length = abs(line[0][0] - line[1][0])

    for i in range(length + 1):
        pos = (line[0][0] + dx[0] * i, line[0][1] + dx[1] * i)
        if pos not in rocks:
            rocks[pos] = 0
        rocks[pos] += 1
print(len([rock for rock in rocks if rocks[rock] > 1]))

rocks = {}
for line in input:
    if line[0][0] == line[1][0]:
        dx = (0, 1 - 2 * (line[1][1] < line[0][1]))
        length = abs(line[0][1] - line[1][1])
    elif line[0][1] == line[1][1]:
        dx = (1 - 2 * (line[1][0] < line[0][0]), 0)
        length = abs(line[0][0] - line[1][0])
    elif line[0][0] > line[1][0] and line[0][1] > line[1][1]:
        dx = (-1, -1)
        length = line[0][0] - line[1][0]
    elif line[0][0] > line[1][0] and line[0][1] < line[1][1]:
        dx = (-1, 1)
        length = line[0][0] - line[1][0]
    elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
        dx = (1, -1)
        length = line[1][0] - line[0][0]
    else:
        dx = (1, 1)
        length = line[1][0] - line[0][0]

    for i in range(length + 1):
        pos = (line[0][0] + dx[0] * i, line[0][1] + dx[1] * i)
        if pos not in rocks:
            rocks[pos] = 0
        rocks[pos] += 1

print(len([rock for rock in rocks if rocks[rock] > 1]))
