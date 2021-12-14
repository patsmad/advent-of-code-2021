from get_input import get_input

actual_input = get_input(11).text

test_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

input = actual_input.strip().split("\n")

class Node:
    def __init__(self, n, idx):
        self.idx = idx
        self.n = n
        self.neighbors = []
        self.flashes = 0

    def step(self):
        self.n += 1
        if self.n == 10:
            for neighbor in self.neighbors:
                neighbor.step()

    def reset(self):
        if self.n > 9:
            self.n = 0
            self.flashes += 1
            return True
        return False

    def add_neighbor(self, other_node):
        other_node.neighbors.append(self)
        self.neighbors.append(other_node)

class Grid:
    def __init__(self, input):
        self.nodes = []
        self.N = len(input[0])
        self.M = len(input)
        self.initialize(input)

    def initialize(self, input):
        for line in input:
            for c in line:
                self.nodes.append(Node(int(c), len(self.nodes)))
        for i in range(1, len(input[0])):
            self.nodes[i].add_neighbor(self.nodes[i - 1])
            self.nodes[i].add_neighbor(self.nodes[self.N + i - 1])
        for i in range(1, len(input)):
            self.nodes[i * self.N].add_neighbor(self.nodes[(i - 1) * self.N])
        for i in range(1, len(input)):
            for j in range(1, len(input[i])):
                self.nodes[(i * self.N) + j].add_neighbor(self.nodes[(i * self.N) + (j - 1)])
                self.nodes[(i * self.N) + j].add_neighbor(self.nodes[(i - 1) * self.N + j])
                self.nodes[(i * self.N) + j].add_neighbor(self.nodes[(i - 1) * self.N + (j - 1)])
                if (i * self.N) + j < (self.M - 1) * self.N:
                    self.nodes[(i * self.N) + j].add_neighbor(self.nodes[(i + 1) * self.N + (j - 1)])

    def step(self):
        for node in self.nodes:
            node.step()
        return sum([node.reset() for node in self.nodes])

    def print(self):
        for i in range(self.M):
            print(''.join([str(g.nodes[i * self.N + j].n) for j in range(self.N)]))

g = Grid(input)
for _ in range(100):
    flashes = g.step()
print(sum([n.flashes for n in g.nodes]))

g = Grid(input)
flashes = 0
steps = 0
while flashes != 100:
    flashes = g.step()
    steps += 1
print(steps)
