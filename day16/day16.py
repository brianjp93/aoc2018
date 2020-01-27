import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
data = pathlib.PurePath(cwd, 'data')


class Computer:
    def __init__(self, register=None, instruction=None):
        self.register = register[:] if register else []
        self.instruction = instruction[:] if instruction else []
        self.m = [
            self.addr,
            self.addi,
            self.mulr,
            self.muli,
            self.borr,
            self.bori,
            self.banr,
            self.bani,
            self.setr,
            self.seti,
            self.gtir,
            self.gtri,
            self.gtrr,
            self.eqir,
            self.eqri,
            self.eqrr
        ]

    def run(self):
        self.m[self.instruction[0]]()

    def addr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] + self.register[rb]

    def addi(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] + b

    def mulr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] * self.register[rb]

    def muli(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] * b

    def borr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] | self.register[rb]

    def bori(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] | b

    def banr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] & self.register[rb]

    def bani(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra] & b

    def setr(self):
        ra, _, rc = self.instruction[1: 4]
        self.register[rc] = self.register[ra]

    def seti(self):
        a, _, rc = self.instruction[1: 4]
        self.register[rc] = a

    def gtir(self):
        a, rb, rc = self.instruction[1: 4]
        self.register[rc] = 1 if a > self.register[rb] else 0

    def gtri(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] > b else 0

    def gtrr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] > self.register[rb] else 0

    def eqir(self):
        a, rb, rc = self.instruction[1: 4]
        self.register[rc] = 1 if a == self.register[rb] else 0

    def eqri(self):
        ra, b, rc = self.instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] == b else 0

    def eqrr(self):
        ra, rb, rc = self.instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] == self.register[rb] else 0


if __name__ == '__main__':
    with open(data, 'r') as f:
        d = f.read().split('\n\n\n')
        part1 = d[0].splitlines()
        p1_groups = []
        for i in range(0, len(part1), 4):
            group = part1[i:i+3]
            before = list(map(int, group[0].split(':')[-1].replace('[', '').replace(']', '').split(',')))
            after = list(map(int, group[2].split(':')[-1].replace('[', '').replace(']', '').split(',')))
            instruction = list(map(int, group[1].split()))
            p1_groups.append((instruction, before, after))

        p1_valid = []
        op_map = {x: set(list(range(16))) for x in range(16)}
        computer = Computer()
        for (instruction, before, after) in p1_groups:
            valid_codes = []
            for i in range(16):
                computer.instruction = instruction[:]
                computer.register = before[:]
                computer.instruction[0] = i
                computer.run()
                if computer.register == after:
                    valid_codes.append(i)
            p1_valid.append(valid_codes)
            op_map[instruction[0]] = op_map[instruction[0]] & set(valid_codes)

        done_keys = set()
        while len(done_keys) != len(op_map):
            found = False
            for key, valset in op_map.items():
                if key not in done_keys and len(valset) == 1:
                    done_keys.add(key)
                    remval = list(valset)[0]
                    found = True
                    break
            if found:
                for key, valset in op_map.items():
                    if key not in done_keys:
                        op_map[key] = op_map[key] - set([remval])
            else:
                break

        out = sum([1 if len(x) >= 3 else 0 for x in p1_valid])
        print(f'Part 1: {out}')


        op_map = {key: list(val)[0] for key, val in op_map.items()}
        computer = Computer(register=[0]*4)
        part2 = d[1].splitlines()
        for line in part2:
            instruction = [int(x) for x in line.split()]
            if instruction:
                instruction[0] = op_map[instruction[0]]
                computer.instruction = instruction
                computer.run()

        print(f'Part 2: {computer.register[0]}')

