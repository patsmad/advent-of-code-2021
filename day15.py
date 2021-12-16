from get_input import get_input
import math

actual_input = get_input(15).text

test_input = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

input = actual_input.strip().split("\n")

class Node:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self.neighbors = []

        self.visited = False
        self.parent = self
        self.total_val = math.inf

    def add_neighbor(self, n):
        n.neighbors.append(self)
        self.neighbors.append(n)


class Grid:
    def __init__(self, input):
        self.input = input
        self.nodes = []
        self.initialize(5)

    def initialize(self, N):
        self.nodes = []
        for i in range(len(self.input) * N):
            for j in range(len(self.input[0]) * N):
                v = (int(self.input[i % len(self.input)][j % len(self.input[0])]) + (i // len(self.input)) + (j // len(self.input[0])) - 1) % 9 + 1
                self.nodes.append(Node(len(self.input[0]) * N * i + j, v))
        for j in range(1, len(self.input[0]) * N):
            self.nodes[j].add_neighbor(self.nodes[j - 1])
        for i in range(1, len(self.input) * N):
            self.nodes[len(self.input[0]) * N * i].add_neighbor(self.nodes[len(self.input[0]) * N * (i - 1)])
        for i in range(1, len(self.input) * N):
            for j in range(1, len(self.input[0]) * N):
                self.nodes[len(self.input[0]) * N * i + j].add_neighbor(self.nodes[len(self.input[0]) * N * (i - 1) + j])
                self.nodes[len(self.input[0]) * N * i + j].add_neighbor(self.nodes[len(self.input[0]) * N * i + j - 1])

    def shortest_path(self, start_node):
        start_node.total_val = 0
        queue = [start_node]
        while len(queue) > 0:
            n = queue.pop(0)
            n.visited = True
            for child in n.neighbors:
                new_val = n.total_val + child.val
                if not child.visited and child.total_val > new_val:
                    child.parent = n
                    child.total_val = new_val
                if child not in queue and not child.visited:
                    queue.append(child)
            # This is obviously very slow. Use a priority queue, but I couldn't be bothered
            queue = sorted(queue, key=lambda x: x.total_val)
        print(self.nodes[-1].total_val)

g = Grid(input)
g.shortest_path(g.nodes[0])
