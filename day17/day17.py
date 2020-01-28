import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')


FALLINGWATER = '|'
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
            if self.m.get(coord, OPEN) == CLAY:
                out.append([(coord[0]-dx, coord[1]), False])
        return out

    def fill_up(self, coord):
        out = []
        left_is_open = right_is_open = False
        while not left_is_open and not right_is_open:
            (left, left_is_open), (right, right_is_open) = self.find_clay(coord)
            fill_with = FALLINGWATER if left_is_open or right_is_open else WATER
            for x in range(left[0], right[0]+1):
                self.m[(x, left[1])] = fill_with
            coord = (coord[0], coord[1]-1)
        for x in range(left[0], right[0]+1):
            self.m[(x, left[1])] = FALLINGWATER
        if left_is_open:
            out.append(left)
        if right_is_open:
            out.append(right)
        return out

    def fill_down(self, coord):
        while self.m.get(coord, OPEN) != CLAY:
            self.m[coord] = FALLINGWATER
            last_coord = coord
            coord = (coord[0], coord[1]+1)
            if coord[1] > self.rangey[1]:
                return None
            if self.m.get(coord, OPEN) in (WATER, FALLINGWATER):
                (left, left_is_open), (right, right_is_open) = self.find_clay(coord)
                if left_is_open or right_is_open:
                    return None
        return last_coord

    def fill(self, x=500):
        q = [(x, 0)]
        while q:
            coord = q.pop(0)
            coord = self.fill_down(coord)
            if coord is not None:
                new_coords = self.fill_up(coord)
                q += new_coords

    def count_water(self):
        return sum(1 if val in (WATER, FALLINGWATER) and coord[1] >= self.rangey[0] else 0 for coord, val in self.m.items())

    def count_after_dry(self):
        return sum(1 if val == WATER and coord[1] >= self.rangey[0] else 0 for coord, val in self.m.items())


if __name__ == '__main__':
    g = Ground(dpath)
    g.fill()
    # print(g.draw())
    print(f'Part 1: {g.count_water()}')
    print(f'Part 2: {g.count_after_dry()}')

