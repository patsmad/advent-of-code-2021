from get_input import get_input

actual_input = get_input(9).text

test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

input = [[int(a) for a in b] for b in actual_input.strip().split("\n")]

class Node:
    def __init__(self, n, idx):
        self.idx = idx
        self.n = n
        self.neighbors = []
        self.parent = self

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
        neighbor_node.neighbors.append(self)

    def is_min(self):
        return all([self.n < neighbor.n for neighbor in self.neighbors])

    def set_parent(self):
        curr_parent = self.get_parent()
        if curr_parent is not None:
            parents = [curr_parent] + [n.get_parent() for n in self.neighbors]
            parents = [a for a in parents if a is not None]
            min_parent = sorted(parents, key=lambda x: x.idx)[0]
            for parent in parents:
                parent.parent = min_parent

    def get_parent(self):
        if self.n < 9:
            node = self
            while node is not node.parent:
                node = node.parent
            return node

class Graph:
    def __init__(self, input):
        self.initialize_graph(input)

    def initialize_graph(self, input):
        self.idx = 0
        self.nodes = {}
        self.add_node(0, 0)
        for i in range(1, len(input[0])):
            self.add_node(0, i)
            self.nodes[(0, i)].add_neighbor(self.nodes[(0, i - 1)])
        for i in range(1, len(input)):
            self.add_node(i, 0)
            self.nodes[(i, 0)].add_neighbor(self.nodes[(i - 1, 0)])
        for i in range(1, len(input)):
            for j in range(1, len(input[i])):
                self.add_node(i, j)
                self.nodes[(i, j)].add_neighbor(self.nodes[(i - 1, j)])
                self.nodes[(i, j)].add_neighbor(self.nodes[(i, j - 1)])

    def add_node(self, i, j):
        self.nodes[(i, j)] = Node(input[i][j], self.idx)
        self.idx += 1

    def get_min_sum(self):
        s = 0
        for k in self.nodes:
            if self.nodes[k].is_min():
                s += self.nodes[k].n + 1
        return s

    def set_parents(self):
        for node in self.nodes.values():
            node.set_parent()

    def sorted_group_sizes(self):
        out = {}
        for k, n in self.nodes.items():
            parent = n.get_parent()
            if parent:
                if parent.idx not in out:
                    out[parent.idx] = 0
                out[parent.idx] += 1
        m = 1
        for size in sorted(out.values())[-3:]:
            m *= size
        return m

g = Graph(input)
print(g.get_min_sum())
g.set_parents()
print(g.sorted_group_sizes())