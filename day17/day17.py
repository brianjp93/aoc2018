import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


WATER = '~'
CLAY = '#'
OPEN = ' '

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
                    self.m[tuple(coord)] = CLAY
                    self.rangex[0] = min(self.rangex[0], coord[0])
                    self.rangex[1] = max(self.rangex[1], coord[0])
                    self.rangey[0] = min(self.rangey[0], coord[1])
                    self.rangey[1] = max(self.rangey[1], coord[1])

    def draw(self, miny=None, maxy=None):
        full = []
        for y in range(0, self.rangey[1]+1 if maxy is None else maxy):
            line = []
            for x in range(self.rangex[0], self.rangex[1]+1):
                coord = (x, y)
                out = self.m.get(coord, ' ')
                line.append(out)
            full.append(''.join(line))
        return '\n'.join(full)

    def find_clay(self, coord):
        out = []
        init_coord = tuple(coord)
        for dx in [-1, 1]:
            coord = init_coord
            while self.m.get(coord, OPEN) != CLAY:
                below = (coord[0], coord[1] + 1)
                if self.m.get(below, OPEN) == OPEN:
                    out.append([coord, True])
                    break
                else:
                    coord = (coord[0] + dx, coord[1])
            # coord = (coord[0] - dx, coord[1])
            if self.m.get(coord, OPEN) == CLAY:
                out.append([(coord[0]-dx, coord[1]), False])
        return out

    def fill(self, x=500):
        q = [(x, 0)]
        while q:
            coord = q.pop()
            is_stop = False
            while self.m.get(coord, OPEN) != CLAY:
                if coord[1] > self.rangey[1]:
                    is_stop = True
                    break
                self.m[coord] = WATER
                coord = (coord[0], coord[1] + 1)
                if self.m.get(coord, OPEN) == WATER:
                    coord = (coord[0], coord[1] + 1)
                    break
            coord = (coord[0], coord[1] - 1)
            if is_stop:
                continue

            left_is_open = False
            right_is_open = False
            while left_is_open == False and right_is_open == False:
                left, right = self.find_clay(coord)
                left_is_open = left[1]
                right_is_open = right[1]
                for x in range(left[0][0], right[0][0]+1):
                    self.m[(x, left[0][1])] = WATER
                coord = (coord[0], coord[1]-1)
            if left_is_open:
                q.append(tuple(left[0]))
            if right_is_open:
                q.append(tuple(right[0]))
            # print(self.draw())
            # input()


if __name__ == '__main__':
    g = Ground(dpath)
    # g = Ground(tpath)
    g.fill()
    print(g.draw())

