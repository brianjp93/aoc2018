import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


OPEN = '.'
TREE = '|'
LUMBERYARD = '#'

class Lumber:
    def __init__(self, fname):
        self.m = {}
        self.dirs = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (1, -1),
            (-1, -1), (-1, 1)
        ]
        self.minx = self.miny = 0
        self.maxx = self.maxy = -float('inf')
        self.process(fname)

    def process(self, fname):
        with open(fname, 'r') as f:
            for y, line in enumerate(f):
                line = line.strip()
                if y > self.maxy:
                    self.maxy = y
                for x, c in enumerate(line):
                    self.m[(x, y)] = c
                    if x > self.maxx:
                        self.maxx = x

    def adjacent(self, coord):
        out = []
        for d in self.dirs:
            ncoord = tuple(a+b for a, b in zip(coord, d))
            out.append(self.m.get(ncoord, None))
        return out

    def next(self):
        newm = {}
        for coord, val in self.m.items():
            adj = self.adjacent(coord)
            newval = val
            if val == OPEN:
                if adj.count(TREE) >= 3:
                    newval = TREE
            elif val == TREE:
                if adj.count(LUMBERYARD) >= 3:
                    newval = LUMBERYARD
            elif val == LUMBERYARD:
                if adj.count(LUMBERYARD) >= 1 and adj.count(TREE) >= 1:
                    newval = LUMBERYARD
                else:
                    newval = OPEN
            newm[coord] = newval
        self.m = newm

    def do_next(self, n):
        for i in range(n):
            self.next()

    def draw(self, m=None):
        if m is None:
            m = self.m
        out = []
        for y in range(self.maxy+1):
            line = []
            for x in range(self.maxx+1):
                line.append(m.get((x, y), ' '))
            out.append(''.join(line))
        return '\n'.join(out)

    def count(self, m=None):
        if m is None:
            m = self.m
        counts = {}
        for val in m.values():
            counts[val] = counts.get(val, 0) + 1
        return counts

    def get_state(self):
        out = []
        for y in range(self.maxy+1):
            out.append(''.join(self.m[(x, y)] for x in range(self.maxx+1)))
        return ''.join(out)

    def find_repeat(self):
        history = {}
        history_list = []
        state = self.get_state()
        i = 0
        while state not in history:
            history[state] = i
            history_list.append(dict(self.m))
            i += 1
            self.next()
            state = self.get_state()
        return (history[state], i-history[state], history_list[history[state]: i])

    def go(self, n):
        start, rlength, history = self.find_repeat()
        true_n = n - start
        history_index = true_n % rlength
        return history[history_index]


if __name__ == '__main__':
    lumber = Lumber(dpath)
    lumber.do_next(10)
    count = lumber.count()
    resources = count[TREE] * count[LUMBERYARD]
    print(f'Part 1: {resources}')

    l = Lumber(dpath)
    while True:
        print()
        print(l.draw())
        l.next()


    lumber = Lumber(dpath)
    m = lumber.go(1000000000)
    count = lumber.count(m)
    resources = count[TREE] * count[LUMBERYARD]
    print(f'Part 2: {resources}')

