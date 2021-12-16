from get_input import get_input

actual_input = get_input(16).text

test_input = """
9C0141080250320F1802104A08
"""

input = actual_input.strip()

class Operator:
    def __init__(self, input):
        self.input = input
        self.process()

    def process(self):
        self.version = eval('0b' + self.input[:3])
        self.type = eval('0b' + self.input[3:6])
        self.remainder = self.input[6:]
        self.children = []
        self.literal_value = None
        if self.type == 4:
            self.process_literal()
        else:
            self.process_operator()

    def process_literal(self):
        literal = ''
        while self.remainder[0] == '1':
            literal += self.remainder[1:5]
            self.remainder = self.remainder[5:]
        literal += self.remainder[1:5]
        self.remainder = self.remainder[5:]
        self.literal_value = eval('0b' + literal)

    def process_operator(self):
        length_id = int(self.remainder[0])
        self.remainder = self.remainder[1:]
        if length_id == 0:
            self.process_length_operator()
        else:
            self.process_packet_operator()

    def process_length_operator(self):
        length = eval('0b' + self.remainder[:15])
        self.remainder = self.remainder[15:]
        while length > 0:
            operator = Operator(self.remainder)
            self.children.append(operator)
            length -= len(self.remainder) - len(operator.remainder)
            self.remainder = operator.remainder

    def process_packet_operator(self):
        packets = eval('0b' + self.remainder[:11])
        self.remainder = self.remainder[11:]
        while packets > 0:
            operator = Operator(self.remainder)
            self.children.append(operator)
            self.remainder = operator.remainder
            packets -= 1

    def value(self):
        return {
            0: lambda: sum([c.value() for c in self.children]),
            1: self.product,
            2: lambda: min([c.value() for c in self.children]),
            3: lambda: max([c.value() for c in self.children]),
            4: lambda: self.literal_value,
            5: lambda: 1 if self.children[0].value() > self.children[1].value() else 0,
            6: lambda: 1 if self.children[0].value() < self.children[1].value() else 0,
            7: lambda: 1 if self.children[0].value() == self.children[1].value() else 0
        }[self.type]()

    def product(self):
        p = 1
        for child in self.children:
            p *= child.value()
        return p

    def print(self):
        print('version: {}, type: {}, number of children: {}, self.value: {}'.format(self.version, self.type, len(self.children), self.literal_value))
        if len(self.children) > 0:
            print('children:')
            for child in self.children:
                child.print()
        print()

class Computer:
    to_binary = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    def __init__(self, input):
        self.input = input
        self.convert()

    def convert(self):
        self.binary = ''.join([self.to_binary[c] for c in self.input])
        self.base = Operator(self.binary)

    def version_sum(self):
        s = 0
        q = [self.base]
        while len(q) > 0:
            operator = q.pop(0)
            q += operator.children
            s += operator.version
        return s

c = Computer(input)
print(c.version_sum())
print(c.base.value())