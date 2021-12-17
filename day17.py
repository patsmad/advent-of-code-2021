from get_input import get_input

actual_input = get_input(17).text

test_input = """
target area: x=20..30, y=-10..-5
"""

input = actual_input.strip()
xmin = int(input.split('target area: x=')[1].split('..')[0])
xmax = int(input.split('target area: x=')[1].split('..')[1].split(', ')[0])
ymin = int(input.split(', y=')[1].split('..')[0])
ymax = int(input.split(', y=')[1].split('..')[1])

# Basically it should always be possible (if you can shoot it upwards at all) to have it reach a
# velocity of -ymin at a point above the target area at y = 0, so the peak is (y - 1) * y / 2
print((-ymin - 1) * (-ymin) // 2)

# I'm sure there is an equally fancy way to ask the question: how many ways can you hit the target with an x velocity of x*
# Then you can sum those up ... but whatever, since I know the maximum y from part 1 you can quickly brute force it.
out = []
for i in range(0, xmax + 1):
    for j in range(ymin, -ymin):
        x, y = 0, 0
        vx, vy = i, j
        while x <= xmax and y >= ymin:
            x += vx
            y += vy
            vx = vx - 1 if vx > 0 else 0
            vy -= 1
            if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
                out.append((i, j))
                break
print(len(out))