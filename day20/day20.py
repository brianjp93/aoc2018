"""day20.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


DOORS = '|-'
WALL = '#'
OPEN = '.'


class Space:
    def __init__(self, data):
        self.data = data.strip('^').strip('$')
        self.m = {}
        self.dirs = {
            'N': (0, -1),
            'E': (1, 0),
            'S': (0, 1),
            'W': (-1, 0)
        }
        self.process()
        self.surround()

    def process(self, coord=tuple((0, 0)), data=None):
        if data is None:
            data = self.data
            self.m[coord] = OPEN
        walls = {'N': '-', 'S': '-', 'E': '|', 'W': '|'}
        coord = tuple(coord)
        init_coord = tuple(coord)
        i = 0
        while i < len(data):
            val = data[i]
            if val in self.dirs.keys():
                coord = tuple(a+b for a, b in zip(coord, self.dirs[val]))
                self.m[coord] = walls[val]
                coord = tuple(a+b for a, b in zip(coord, self.dirs[val]))
                self.m[coord] = OPEN
            elif val == '(':
                endindex = self.find_closing(i, data)
                coord = self.process(coord, data[i+1: endindex])
                i = endindex
            elif val == '|':
                coord = init_coord
            i += 1
        return coord

    def surround(self):
        keys = list(self.m.keys())
        for coord in keys:
            for d in list(self.dirs.values()) + [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                nc = tuple(a+b for a, b in zip(coord, d))
                if self.m.get(nc, WALL) not in '.|-':
                    self.m[nc] = WALL

    def get_range(self):
        minx = min(key[0] for key in self.m.keys())
        maxx = max(key[0] for key in self.m.keys())
        miny = min(key[1] for key in self.m.keys())
        maxy = max(key[1] for key in self.m.keys())
        return (minx, maxx), (miny, maxy)

    def draw(self):
        (minx, maxx), (miny, maxy) = self.get_range()
        out = []
        for y in range(miny, maxy+1):
            out.append(''.join(self.m.get((x, y), ' ') for x in range(minx, maxx+1)))
        return '\n'.join(out)


    def find_closing(self, index, data):
        """Return the index of the matching paren.

        Returns
        -------
        int

        """
        stack = 1
        i = index + 1
        while stack > 0:
            val = data[i]
            if val == ')':
                stack -= 1
            elif val == '(':
                stack += 1
            i += 1
        return i-1

    def find_path_lengths(self, coord=tuple((0, 0))):
        paths = {}
        q = [(coord, 0)]
        while q:
            coord, dist = q.pop(0)
            if dist < paths.get(coord, float('inf')):
                paths[coord] = dist
                for d in self.dirs.values():
                    ncoord = tuple(a+b for a, b in zip(coord, d))
                    if self.m.get(ncoord, WALL) in DOORS:
                        ncoord = tuple(a+b for a, b in zip(ncoord, d))
                        q.append((ncoord, dist + 1))
        return paths


if __name__ == '__main__':
    with open(dpath, 'r') as f:
        reg = f.read().strip()
        s = Space(reg)
        # print(s.draw())
        paths = s.find_path_lengths()
        max_dist = max(list(paths.values()))
        print(f'Part 1: {max_dist}')

        gt_1000 = len([x for x in paths.values() if x >= 1000])
        print(f'Part 2: {gt_1000}')

