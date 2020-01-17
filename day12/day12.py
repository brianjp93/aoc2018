"""day12.py
"""
import pathlib


cwd = pathlib.Path(__file__).parent.absolute()
data = pathlib.PurePath(cwd, 'data')
test = pathlib.PurePath(cwd, 'test')


class PlantGen:
    def __init__(self, fname):
        self.state = {}
        self.pmap = {}
        self.gen = 0
        self.minpot = 0
        self.maxpot = 0
        self.process(fname)

    def process(self, fname):
        pmap = {}
        with open(fname, 'r') as f:
            for line in f:
                if 'initial' in line:
                    init_state = line.split(':')[-1].strip()
                    self.state = {i: x for i, x in enumerate(init_state)}
                elif '=>' in line:
                    parts = line.split('=>')
                    pmap[parts[0].strip()] = parts[1].strip()
        self.pmap = pmap
        self.maxpot = len(self.state) - 1

    def get_state(self):
        return ''.join([self.state[x] for x in range(self.minpot, self.maxpot + 1)])

    def next(self):
        new_state = {}
        pad = 5
        minpot = float('inf')
        maxpot = -float('inf')
        for i in range(self.minpot - pad, self.maxpot + 1 + pad):
            piece = [self.state.get(x, '.') for x in range(i-2, i+3)]
            piece = ''.join(piece)
            new_state[i] = self.pmap.get(piece, '.')
            if new_state[i] == '#' and i < minpot:
                minpot = i
            if new_state[i] == '#' and i > maxpot:
                maxpot = i
        self.state = new_state
        self.minpot = minpot
        self.maxpot = maxpot
        self.gen += 1

    def do_next(self, i):
        for _ in range(i):
            if _ % 100000 == 0:
                print(f'loop: {_}')
            self.next()

    def get_sum(self):
        return sum(i if val == '#' else 0 for i, val in self.state.items())

    def find_repeat(self):
        sum_new = self.get_sum()
        new_state = self.get_state()
        while True:
            sum_old = sum_new
            old_state = new_state
            self.next()
            sum_new = self.get_sum()
            new_state = self.get_state()
            if old_state == new_state:
                break
        sum_dif = sum_new - sum_old
        return self.gen, sum_dif, sum_new


if __name__ == '__main__':
    pg = PlantGen(data)
    pg.do_next(20)
    print(f'state: {pg.get_state()}')
    print(f'sum: {pg.get_sum()}')

    DO_GEN = 50000000000
    pg = PlantGen(data)
    gen, sum_dif, cur_sum = pg.find_repeat()
    print(f'State repeats at generation {gen} with a sum change of {sum_dif}.')
    end_sum = (DO_GEN - gen) * sum_dif + cur_sum
    print(f'part 2: {end_sum}')

