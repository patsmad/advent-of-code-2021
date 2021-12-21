from get_input import get_input

actual_input = get_input(19).text

test_input = """
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""

input = actual_input.strip().split("\n\n")

class Scanner:
    orientations = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
    axes = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

    def __init__(self, input):
        lines = input.split("\n")
        self.number = int(lines[0].split('scanner ')[1].split(' ')[0])
        self.probes = [tuple([int(a) for a in line.split(",")]) for line in lines[1:]]
        self.position = None

    def calculateD(self, other):
        D = {}
        for i in range(len(self.probes)):
            for j in range(len(other.probes)):
                for orientation in self.orientations:
                    for axis in self.axes:
                        dx = tuple([self.probes[i][n] + orientation[n] * other.probes[j][axis[n]] for n in range(3)])
                        if dx not in D:
                            D[dx] = 0
                        D[dx] += 1
                        if D[dx] >= 12:
                            return (dx, orientation, axis)

    def set_position(self, position):
        self.probes = [tuple([position[0][m] - position[1][m] * p[position[2][m]] for m in range(3)]) for p in self.probes]
        self.position = position[0]

class Scanners:
    def __init__(self, input):
        self.set_scanners = [Scanner(input[0])]
        self.other_scanners = [Scanner(chunk) for chunk in input[1:]]
        self.set_scanners[0].position = (0, 0, 0)

    def combine_all(self):
        scanners_to_test = [a for a in self.set_scanners]
        while len(self.other_scanners) > 0:
            new_scanners = []
            for scanner in scanners_to_test:
                for other_scanner in self.other_scanners:
                    result = scanner.calculateD(other_scanner)
                    if result:
                        print(result)
                        other_scanner.set_position(result)
                new_scanners += [s for s in self.other_scanners if s.position]
                self.set_scanners += [s for s in self.other_scanners if s.position]
                self.other_scanners = [s for s in self.other_scanners if not s.position]
            scanners_to_test = new_scanners

    def all_probes(self):
        return list(set([probe for scanner in self.set_scanners for probe in scanner.probes]))

    def distances(self):
        return [sum([abs(self.set_scanners[i].position[m] - self.set_scanners[j].position[m]) for m in range(3)]) for i in range(len(self.set_scanners)) for j in range(i + 1, len(self.set_scanners))]

import time
t = time.time()
s = Scanners(input)
s.combine_all()
print(len(s.all_probes()))
print(max(s.distances()))
print(time.time() - t)