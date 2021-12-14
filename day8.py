from get_input import get_input

actual_input = get_input(8).text

test_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

c = 0
s = 0
for line in actual_input.strip().split("\n"):
    input = [set(a) for a in line.split(" | ")[0].split(" ")]
    output = [set(a) for a in line.split(" | ")[1].split(" ")]

    key = {
        0: set('abcefg'),
        1: set('cf'),
        2: set('acdeg'),
        3: set('acdfg'),
        4: set('bcdf'),
        5: set('abdfg'),
        6: set('abdefg'),
        7: set('acf'),
        8: set('abcdefg'),
        9: set('abcdfg')
    }
    counter = {len(v): [] for k, v in key.items()}
    for number in input:
        counter[len(number)].append(number)
    out = {
        1: counter[2][0],
        4: counter[4][0],
        7: counter[3][0],
        8: counter[7][0]
    }

    idx_9 = [len(a - counter[4][0]) for a in counter[6]].index(2)
    idx_6 = [len(a - counter[3][0]) for a in counter[6]].index(4)

    out[0] = counter[6][({0, 1, 2} - {idx_6, idx_9}).pop()]
    out[6] = counter[6][idx_6]
    out[9] = counter[6][idx_9]

    idx_5 = [len(out[6] - a) for a in counter[5]].index(1)
    idx_2 = [len(a - out[4]) for a in counter[5]].index(3)

    out[3] = counter[5][({0, 1, 2} - {idx_5, idx_2}).pop()]
    out[5] = counter[5][idx_5]
    out[2] = counter[5][idx_2]

    target = [out[1], out[4], out[7], out[8]]
    for o in output:
        if o in target:
            c += 1
    s += int(''.join([str([k for k, v in out.items() if v == o][0]) for o in output]))
print(c)
print(s)