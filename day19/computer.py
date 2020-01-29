class Computer:
    def __init__(self, register=None, instructions=None):
        self.register = register[:] if register else []
        self.instructions = instructions
        self.i
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

