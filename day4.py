from get_input import get_input

actual_input = get_input(4).text

test_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

input = actual_input.strip().split("\n\n")

class Board:
    def __init__(self, str_board):
        self.rows = [[int(n) for n in row.split(" ") if len(n) > 0] for row in str_board.split("\n")]
        self.cols = [[self.rows[i][j] for i in range(len(self.rows))] for j in range(len(self.rows[0]))]

    def remaining_numbers(self):
        return sum([sum(a) for a in self.rows])

    def call_number_rows(self, n, rows):
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                if col == n:
                    rows[i].pop(j)
                    if len(rows[i]) == 0:
                        return True
        return False

    def call_number(self, n):
        bingo_row = self.call_number_rows(n, self.rows)
        bingo_col = self.call_number_rows(n, self.cols)
        return bingo_row or bingo_col

class BingoGame:
    def __init__(self, input):
        self.numbers = [int(a) for a in input[0].split(",")]
        self.boards = [Board(board) for board in input[1:]]

    def run_game(self):
        for number in self.numbers:
            for board in self.boards:
                bingo = board.call_number(number)
                if bingo:
                    return number * board.remaining_numbers()

    def run_second_game(self):
        bingos = [False] * len(self.boards)
        for number in self.numbers:
            for i, board in enumerate(self.boards):
                if not bingos[i]:
                    bingos[i] = board.call_number(number)
                    if all(bingos):
                        return number * board.remaining_numbers()

g = BingoGame(input)
print(g.run_game())
g = BingoGame(input)
print(g.run_second_game())
