from get_input import get_input

actual_input = get_input(10).text

test_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

input = actual_input.strip().split("\n")

lookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

lookup2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

invert = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

score = 0
for line in input:
    s = []
    for c in line:
        if c in invert:
            s.append(c)
        else:
            open_c = s.pop()
            if invert[open_c] != c:
                score += lookup[c]
                break
print(score)

scores = []
for line in input:
    s = []
    score = 0
    for c in line:
        if c in invert:
            s.append(c)
        else:
            open_c = s.pop()
            if invert[open_c] != c:
                score = lookup[c]
                break
    if score == 0:
        score = 0
        while len(s) > 0:
            score *= 5
            score += lookup2[invert[s.pop()]]
        scores.append(score)
print(sorted(scores)[len(scores) // 2])