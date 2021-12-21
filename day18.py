from get_input import get_input

actual_input = get_input(18).text

test_input = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""

input = actual_input.strip().split("\n")

class Node:
    def __init__(self, level, parent):
        self.val = None
        self.level = level
        self.parent = parent
        self.left = None
        self.right = None

    def explode(self):
        if self.level >= 5 and self.parent.left and self.parent.right:
            l, r = self.parent.left.val, self.parent.right.val
            self.parent.left = None
            self.parent.right = None
            self.parent.val = 0
            self.parent.level = self.level - 1
            return l, r
        else:
            return None, None

    def split(self):
        if self.val > 9:
            l = Node(self.level + 1, self)
            r = Node(self.level + 1, self)
            l.val = self.val // 2
            r.val = self.val // 2 + self.val % 2
            self.val = None
            self.left = l
            self.right = r
            return True
        return False

    def magnitude(self):
        if self.val is not None:
            return self.val
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def node_list(self):
        if self.val is not None:
            return [self]
        else:
            return self.left.node_list() + self.right.node_list()

    def str(self):
        if self.val is None:
            return '[{},{}]'.format(self.left.str(), self.right.str())
        else:
            return str(self.val)

class Tree:
    def __init__(self, base):
        self.base = base

    @staticmethod
    def build(remainder, level, parent):
        n = Node(level, parent)
        if remainder[0] == '[':
            n.left, remainder = Tree.build(remainder[1:], level + 1, n)
            n.right, remainder = Tree.build(remainder[1:], level + 1, n)
            return n, remainder[1:]
        else:
            n.val = int(remainder[0])
            return n, remainder[1:]

    def print(self):
        print(self.base.str())

    def node_list(self):
        return self.base.node_list()

    def explode(self):
        n_list = self.node_list()
        for i, n in enumerate(n_list):
            l, r = n.explode()
            if l is not None and r is not None:
                if i > 0:
                    n_list[i - 1].val += l
                if i < len(n_list) - 2:
                    n_list[i + 2].val += r
                return True
        return False

    def split(self):
        for n in self.node_list():
            if n.split():
                return True
        return False

    def step_fnc(self):
        orig_str = self.base.str()
        while 1:
            if not self.explode():
                self.split()
            new_str = self.base.str()
            if new_str == orig_str:
                break
            orig_str = new_str

    def step(self):
        orig_str = self.base.str()
        while 1:
            self.step_fnc()
            new_str = self.base.str()
            if new_str == orig_str:
                break
            orig_str = new_str

    def __add__(self, other):
        for n in self.node_list():
            n.level += 1
        for n in other.node_list():
            n.level += 1
        n = Node(0, None)
        n.left = self.base
        n.right = other.base
        self.base.parent = n
        other.base.parent = n
        t = Tree(n)
        t.step()
        return t

    def magnitude(self):
        return self.base.magnitude()

trees = []
for line in input:
    base, _ = Tree.build(line, 0, None)
    trees.append(Tree(base))

final_tree = trees[0]
for tree in trees[1:]:
    final_tree += tree
final_tree.print()
print(final_tree.magnitude())

trees = []
for line in input:
    base, _ = Tree.build(line, 0, None)
    trees.append(Tree(base))

max_val = 0
for i in range(len(trees)):
    for j in range(len(trees)):
        if i != j:
            t1, _ = Tree.build(input[i], 0, None)
            t2, _ = Tree.build(input[j], 0, None)
            new_tree = Tree(t1) + Tree(t2)
            tmp = new_tree.magnitude()
            if tmp > max_val:
                max_val = tmp
print(max_val)
