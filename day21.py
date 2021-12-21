from get_input import get_input

actual_input = get_input(21).text

test_input = """
Player 1 starting position: 4
Player 2 starting position: 8
"""

player1_input, player2_input = actual_input.strip().split("\n")
p1 = int(player1_input.split("Player 1 starting position: ")[1]) - 1
p2 = int(player2_input.split("Player 2 starting position: ")[1]) - 1

class Die:
    def roll(self):
        pass

class DeterministicDie(Die):
    N = 100
    val = 0
    rolls = 0

    def roll(self):
        self.rolls += 1
        out = self.val + 1
        self.val = (self.val + 1) % self.N
        return [out]

class DiracDie(Die):
    def roll(self):
        return [1, 2, 3]

class Game:
    S = 10

    def __init__(self, p1, p2, die, win):
        self.win = win
        self.w1 = {}
        self.w2 = {}
        self.s = {(p1, p2, 0, 0): 1}
        self.die = die

    r1 = lambda self, k, roll: ((k[0] + roll) % self.S, k[1], k[2], k[3])
    r2 = lambda self, k, roll: (k[0], (k[1] + roll) % self.S, k[2], k[3])
    s1 = lambda self, k: (k[0], k[1], k[2] + k[0] + 1, k[3])
    s2 = lambda self, k: (k[0], k[1], k[2], k[3] + k[1] + 1)

    def roll(self, roll_f):
        rolls = [r % self.S for r in self.die.roll()]
        out = {}
        for k in self.s:
            for roll in rolls:
                new_key = roll_f(k, roll)
                if new_key not in out:
                    out[new_key] = 0
                out[new_key] += self.s[k]
        return out

    def score(self, score_f):
        out = {}
        for k in self.s:
            new_key = score_f(k)
            if new_key[2] >= self.win:
                if new_key not in self.w1:
                    self.w1[new_key] = 0
                self.w1[new_key] += self.s[k]
            elif new_key[3] >= self.win:
                if new_key not in self.w2:
                    self.w2[new_key] = 0
                self.w2[new_key] += self.s[k]
            else:
                if new_key not in out:
                    out[new_key] = 0
                out[new_key] += self.s[k]
        return out

    def play(self):
        while sum(self.s.values()) > 0:
            for _ in range(3):
                self.s = self.roll(self.r1)
            self.s = self.score(self.s1)
            if sum(self.s.values()) == 0:
                break
            for _ in range(3):
                self.s = self.roll(self.r2)
            self.s = self.score(self.s2)

    def part1_score(self):
        if len(self.w1) > 0:
            return self.die.rolls * list(self.w1.keys())[0][3]
        if len(self.w2) > 0:
            return self.die.rolls * list(self.w2.keys())[0][2]

det_die = DeterministicDie()
g = Game(p1, p2, det_die, win=1000)
g.play()
print(g.part1_score())

dirac_die = DiracDie()
g = Game(p1, p2, dirac_die, win=21)
g.play()
w1 = sum(g.w1.values())
w2 = sum(g.w2.values())
if w1 > w2:
    print(w1)
else:
    print(w2)

