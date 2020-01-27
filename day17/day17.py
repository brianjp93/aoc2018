import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Ground:
    def __init__(self, fname):
        self.m = {}
        self.rangex = [float('inf'), -float('inf')]
        self.rangey = [float('inf'), -float('inf')]
        self.process(fname)

    def process(self, fname):
        program = re.compile('([xy])=([0-9]+), ([xy])=([0-9]+)..([0-9]+)')
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                r = program.search(line)
                coord = [0, 0]
                groups = r.groups()
                if groups[0] == 'x':
                    coord[0] = int(groups[1])
                    variant = 1
                else:
                    coord[1] = int(groups[1])
                    variant = 0
                for i in range(int(groups[3]), int(groups[4]) + 1):
                    coord[variant] = i
                    self.m[tuple(coord)] = '#'
                    self.rangex[0] = min(self.rangex[0], coord[0])
                    self.rangex[1] = max(self.rangex[1], coord[0])
                    self.rangey[0] = min(self.rangey[0], coord[1])
                    self.rangey[1] = max(self.rangey[1], coord[1])

    def draw(self):
        full = []
        for y in range(self.rangey[0], self.rangey[1]+1):
            line = []
            for x in range(self.rangex[0], self.rangex[1]+1):
                coord = (x, y)
                out = self.m.get(coord, ' ')
                line.append(out)
            full.append(''.join(line))
        return '\n'.join(full)



if __name__ == '__main__':
    g = Ground(dpath)
    print(g.draw())

