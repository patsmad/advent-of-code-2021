from get_input import get_input

actual_input = get_input(13).text

test_input = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

input, folds = actual_input.strip().split("\n\n")

class Grid:
    def __init__(self, input):
        self.dots = set()
        for line in input.split("\n"):
            x, y = line.split(",")
            self.dots |= {(int(x), int(y))}
        self.max_x = max([a[0] for a in self.dots])
        self.max_y = max([a[1] for a in self.dots])

    def fold(self, fold):
        if 'y' in fold:
            self.fold_y(int(fold.split("fold along y=")[1]))
        else:
            self.fold_x(int(fold.split("fold along x=")[1]))

    def fold_y(self, y):
        dots_to_fold = [dot for dot in self.dots if dot[1] > y]
        for dot in dots_to_fold:
            if dot[1] > y:
                self.dots -= {dot}
                self.dots |= {(dot[0], dot[1] - 2 * (dot[1] - y))}

    def fold_x(self, x):
        dots_to_fold = [dot for dot in self.dots if dot[0] > x]
        for dot in dots_to_fold:
            if dot[0] > x:
                self.dots -= {dot}
                self.dots |= {(dot[0] - 2 * (dot[0] - x), dot[1])}

    def print(self):
        self.max_x = max([a[0] for a in self.dots])
        self.max_y = max([a[1] for a in self.dots])
        for j in range(self.max_y + 1):
            print(''.join(['#' if (i, j) in self.dots else '.' for i in range(self.max_x + 1)]))
        print()

g = Grid(input)
g.fold(folds.split("\n")[0])
print(len(g.dots))
for fold in folds.split("\n")[1:]:
    g.fold(fold)
print(len(g.dots))
g.print()