from get_input import get_input

actual_input = get_input(20).text

test_input = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

algorithm, base_image = actual_input.strip().split("\n\n")

class Enhancer:
    def __init__(self, algorithm):
        self.algorithm = [0 if c == '.' else 1 for c in algorithm]
        self.v = 0

    def buffer_image(self, bin_image):
        return [[self.v] * (len(bin_image[0]) + 4) for _ in range(2)] + \
               [[self.v] * 2 + line + [self.v] * 2 for line in bin_image] + \
               [[self.v] * (len(bin_image[0]) + 4) for _ in range(2)]

    def reset_base_index(self):
        if self.v == 0 and self.algorithm[0] == 1:
            self.v = 1
        elif self.v == 1 and self.algorithm[-1] == 0:
            self.v = 0

    def enhance(self, bin_image):
        buffered_image = self.buffer_image(bin_image)
        new_image = [[0] * (len(buffered_image[0]) - 2) for _ in range(len(buffered_image) - 2)]
        for i in range(1, len(buffered_image) - 1):
            for j in range(1, len(buffered_image[i]) - 1):
                new_image[i-1][j-1] = self.algorithm[int(''.join(map(str, buffered_image[i-1][j-1:j+2] + buffered_image[i][j-1:j+2] + buffered_image[i+1][j-1:j+2])), 2)]
        self.reset_base_index()
        return new_image

def print_image(image):
    for line in image:
        print(''.join(['.' if c == 0 else '#' for c in line]))

e = Enhancer(algorithm)
bin_image = [[0 if c == '.' else 1 for c in line] for line in base_image.split("\n")]
for step in range(2):
    bin_image = e.enhance(bin_image)

print(sum([sum(line) for line in bin_image]))

e = Enhancer(algorithm)
bin_image = [[0 if c == '.' else 1 for c in line] for line in base_image.split("\n")]
for step in range(50):
    bin_image = e.enhance(bin_image)

print(sum([sum(line) for line in bin_image]))
