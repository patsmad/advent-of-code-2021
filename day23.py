from get_input import get_input
import math

actual_input = get_input(23).text

test_input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

added_rows = """
  #D#C#B#A#
  #D#B#A#C#
"""

input = actual_input.strip()

split_input = input.split("\n")
input = '\n'.join(split_input[:3] + added_rows.split("\n")[1:-1] + split_input[3:])
print(input)

class Grid:
    correct_y = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    correct_letter = {3: 'A', 5: 'B', 7: 'C', 9: 'D'}

    def __init__(self, input, cols):
        self.cols = cols
        self.input = [[c for c in line] for line in input.split("\n")]
        self.moveable_spots = [(1, j) for j in [1, 2, 4, 6, 8, 10, 11]] + [b for j in [3, 5, 7, 9] for b in [(k, j) for k in range(2, self.cols + 2)]]
        self.to_complete = [b for col in [3, 5, 7, 9] for b in [(row, col, self.correct_letter[col]) for row in range(2, self.cols + 2)]]

    def can_move(self, f, t):
        if self.input[t[0]][t[1]] != '.' or self.input[f[0]][f[1]] == '.':
            return False
        if f[0] == 1 and t[0] > 1:
            return self.path_clear(f, t) and self.correct_spot(f, t)
        if f[0] > 1 and t[0] == 1:
            return self.path_clear(t, f) and not self.correct_spot(t, f)
        return False

    def path_clear(self, o, i):
        if o[1] < i[1]:
            for j in range(o[1] + 1, i[1] + 1):
                if self.input[1][j] != '.':
                    return False
        else:
            for j in range(i[1], o[1]):
                if self.input[1][j] != '.':
                    return False
        if any([self.input[j][i[1]] != '.' for j in range(2, i[0])]):
            return False
        return True

    def correct_spot(self, o, i):
        letter = self.input[i[0]][i[1]] if self.input[i[0]][i[1]] != '.' else self.input[o[0]][o[1]]
        return self.correct_y[letter] == i[1] and all([self.input[j][i[1]] == letter for j in range(i[0] + 1, self.cols + 2)])

    def all_moves(self):
        return [(f, t) for f in self.moveable_spots for t in self.moveable_spots if self.can_move(f, t)]

    def get_new_input(self, move):
        return '\n'.join([''.join([self.get_val(i, j, move) for j in range(len(self.input[i]))]) for i in range(len(self.input))])

    def get_val(self, i, j, move):
        return self.input[move[0][0]][move[0][1]] if (i, j) == move[1] else '.' if (i, j) == move[0] else self.input[i][j]

    def is_complete(self):
        return all([self.input[i][j] == l for i, j, l in self.to_complete])

    def print(self):
        return '\n'.join([''.join(line) for line in self.input])

score = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

mem = {}

def recurse(grid):
    if grid.is_complete():
        return 0
    state = grid.print()
    if state not in mem:
        possible_moves = grid.all_moves()
        out = [math.inf]
        for move in possible_moves:
            move_score = score[grid.input[move[0][0]][move[0][1]]] * (abs(move[0][0] - move[1][0]) + abs(move[0][1] - move[1][1]))
            out.append(move_score + recurse(Grid(grid.get_new_input(move), grid.cols)))
        mem[state] = min(out)
    return mem[state]

print(recurse(Grid(input, 4)))
