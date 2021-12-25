from get_input import get_input

actual_input = get_input(25).text

test_input = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

input = [c for c in actual_input.strip().split("\n")]

class Node:
    def __init__(self, input):
        self.east = None
        self.south = None
        self.cucumber = Cucumber(input) if input in ['>', 'v'] else None

    def can_move_east(self):
        return self.cucumber is not None and self.east is not None and self.east.cucumber is None and self.cucumber.is_east()

    def can_move_south(self):
        return self.cucumber is not None and self.south is not None and self.south.cucumber is None and self.cucumber.is_south()

    def move_east(self):
        self.east.cucumber = self.cucumber
        self.cucumber = None

    def move_south(self):
        self.south.cucumber = self.cucumber
        self.cucumber = None

    def print(self):
        return self.cucumber.typ if self.cucumber is not None else '.'

class Cucumber:
    def __init__(self, typ):
        self.typ = typ

    def is_east(self):
        return self.typ == '>'

    def is_south(self):
        return self.typ == 'v'

class Grid:
    def __init__(self, input):
        self.nodes = [Node(input[i][j]) for i in range(len(input)) for j in range(len(input[i]))]
        self.N = len(input[0])
        for i in range(len(input)):
            for j in range(len(input[i])):
                self.nodes[i * self.N + j].east = self.nodes[i * self.N + ((j + 1) % len(input[i]))]
                self.nodes[i * self.N + j].south = self.nodes[((i + 1) % len(input)) * self.N + j]

    def step(self):
        moves = 0
        moving_nodes = [n for n in self.nodes if n.can_move_east()]
        for n in moving_nodes:
            moves += 1
            n.move_east()
        moving_nodes = [n for n in self.nodes if n.can_move_south()]
        for n in moving_nodes:
            moves += 1
            n.move_south()
        return moves

    def print(self):
        return '\n'.join([''.join([n.print() for n in self.nodes[i * self.N:(i + 1) * self.N]]) for i in range(len(self.nodes) // self.N)]) + '\n'

g = Grid(input)
total_moves = 1
moves = g.step()
while moves > 0:
    total_moves += 1
    moves = g.step()
    print(total_moves, moves)
