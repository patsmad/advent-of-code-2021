from get_input import get_input

actual_input = get_input(24).text

test_input = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
"""

input = actual_input.strip().split("\n")

inp_idx = [i for i, command in enumerate(input) if 'inp' in command]
l = inp_idx[1] - inp_idx[0]
x = [int(input[i * l + 4].split(" ")[2]) for i in range(len(input) // l)]
y = [int(input[i * l + 5].split(" ")[2]) for i in range(len(input) // l)]
z = [int(input[i * l + 15].split(" ")[2]) for i in range(len(input) // l)]

w_max = [9, 1, 3, 9, 8, 2, 9, 9, 6, 9, 7, 9, 9, 6]
print(''.join(map(str, w_max)))

out = [0]
w = w_max
for i in range(len(w)):
    b = 1 * ((out[i] % 26) + y[i] != w[i])
    out.append((out[i] // x[i] * (25 * b + 1) + (w[i] + z[i]) * b))
print(out)

w_min = [4, 1, 1, 7, 1, 1, 8, 3, 1, 4, 1, 2, 9, 1]
print(''.join(map(str, w_min)))

out = [0]
w = w_min
for i in range(len(w)):
    b = 1 * ((out[i] % 26) + y[i] != w[i])
    print(b, out[i] % 26, y[i], w[i])
    out.append((out[i] // x[i] * (25 * b + 1) + (w[i] + z[i]) * b))
print(out)




