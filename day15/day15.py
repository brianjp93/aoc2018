"""day15.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Cave:
    def __init__(self, fname):
        self.data = []
        self.moves = [
            (1, 0), (0, 1),
            (-1, 0), (0, -1)
        ]
        self.round = 0
        self.goblin_count = 0
        self.elf_count = 0
        self.process(fname)
        

    def process(self, fname):
        with open(fname, 'r') as f:
            for y, line in enumerate(f.readlines()):
                line = line.strip()
                if line:
                    self.data.append([0] * len(line))
                    for x, c in enumerate(line):
                        if c in 'GE':
                            val = (c, 200)
                            if c == 'G':
                                self.goblin_count += 1
                            elif c == 'E':
                                self.elf_count += 1
                        else:
                            val = c
                        self.data[y][x] = val

    def next(self):
        pass


if __name__ == '__main__':
    c = Cave(dpath)
    for line in c.data:
        print(''.join(x if len(x) == 1 else x[0] for x in line))
    print(c.goblin_count)
    print(c.elf_count)

