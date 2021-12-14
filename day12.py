from get_input import get_input

actual_input = get_input(12).text

test_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

input = actual_input.strip().split("\n")

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, n):
        self.connections.append(n)
        n.connections.append(self)

    def is_start(self):
        return self.name == 'start'

    def is_end(self):
        return self.name == 'end'

    def is_big(self):
        return self.name == self.name.upper()

    def is_small(self):
        return self.name == self.name.lower() and not self.is_start() and not self.is_end()

class Graph:
    def __init__(self, input):
        self.start_node = Node('start')
        self.nodes = {'start': self.start_node}
        for line in input:
            n1, n2 = line.split("-")
            if n1 not in self.nodes:
                self.nodes[n1] = Node(n1)
            if n2 not in self.nodes:
                self.nodes[n2] = Node(n2)
            self.nodes[n1].add_connection(self.nodes[n2])

    def get_path(self, sequence, second_small_used):
        curr_node = sequence[-1]
        if curr_node.is_end():
            return [sequence]
        sequences = []
        for c in curr_node.connections:
            small_check = c.is_small() and (c not in sequence or not second_small_used)
            if small_check or c.is_end() or c.is_big():
                sequences += self.get_path(sequence + [c], second_small_used or (c in sequence and c.is_small()))
        return sequences

g = Graph(input)
print(len(g.get_path([g.start_node], second_small_used=False)))


