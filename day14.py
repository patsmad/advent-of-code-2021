from get_input import get_input

actual_input = get_input(14).text

test_input = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

start, raw_rules = actual_input.strip().split("\n\n")
rules = {}
for rule in raw_rules.split("\n"):
    k, v = rule.split(" -> ")
    rules[k] = v
counter = {k: 0 for k in rules.keys()}
for i in range(len(start) - 1):
    if start[i:i+2] in counter:
        counter[start[i:i+2]] += 1

letter_counter = {s: 0 for s in start}
letter_counter.update({a: 0 for k, v in rules.items() for a in [k[0], k[1], v]})
for s in start:
    letter_counter[s] += 1

for _ in range(40):
    new_counter = {k: 0 for k in rules.keys()}
    for k, c in counter.items():
        letter = rules[k]
        l = k[0] + letter
        r = letter + k[1]
        new_counter[l] += c
        new_counter[r] += c
        letter_counter[letter] += c
    counter = new_counter

print(max(letter_counter.values()) - min(letter_counter.values()))