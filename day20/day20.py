"""day20.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
test1 = '^ENWWW(NEEE|SSE(EE|N))$'
test2 = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
test3 = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'


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
            self.m[coord] = '.'
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
                self.m[coord] = '.'
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
                if self.m.get(nc, '#') not in '.|-':
                    self.m[nc] = '#'

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
        q = [(coord, 0)]
        while q:
            coord, dist = q.pop()
            for d in self.dirs.values():
                pass

if __name__ == '__main__':
    # s = Space(test2)
    # print(s.draw())
    with open(dpath, 'r') as f:
        reg = f.read().strip()
        # print(reg)
        s = Space(reg)
        print(s.draw())
        # print(s.m)

