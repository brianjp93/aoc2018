class Computer:
    def __init__(self, register=None, instructions=None, pointer=0):
        self.register = register[:] if register else [0] * 6
        self.pointer = pointer
        self.instructions = instructions
        self.m = {
            'addr': self.addr,
            'addi': self.addi,
            'mulr': self.mulr,
            'muli': self.muli,
            'borr': self.borr,
            'bori': self.bori,
            'banr': self.banr,
            'bani': self.bani,
            'setr': self.setr,
            'seti': self.seti,
            'gtir': self.gtir,
            'gtri': self.gtri,
            'gtrr': self.gtrr,
            'eqir': self.eqir,
            'eqri': self.eqri,
            'eqrr': self.eqrr
        }

    def run_until_finished(self):
        while self.get_pointer() >= 0 and self.get_pointer() < len(self.instructions):
            self.run()

    def get_pointer(self):
        return self.register[self.pointer]

    def run(self):
        index = self.get_pointer()
        instruction = self.instructions[index]
        self.m[instruction[0]](instruction)
        self.register[self.pointer] += 1

    def addr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] + self.register[rb]

    def addi(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] + b

    def mulr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] * self.register[rb]

    def muli(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] * b

    def borr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] | self.register[rb]

    def bori(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] | b

    def banr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] & self.register[rb]

    def bani(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = self.register[ra] & b

    def setr(self, instruction):
        ra, _, rc = instruction[1: 4]
        self.register[rc] = self.register[ra]

    def seti(self, instruction):
        a, _, rc = instruction[1: 4]
        self.register[rc] = a

    def gtir(self, instruction):
        a, rb, rc = instruction[1: 4]
        self.register[rc] = 1 if a > self.register[rb] else 0

    def gtri(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] > b else 0

    def gtrr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] > self.register[rb] else 0

    def eqir(self, instruction):
        a, rb, rc = instruction[1: 4]
        self.register[rc] = 1 if a == self.register[rb] else 0

    def eqri(self, instruction):
        ra, b, rc = instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] == b else 0

    def eqrr(self, instruction):
        ra, rb, rc = instruction[1: 4]
        self.register[rc] = 1 if self.register[ra] == self.register[rb] else 0

