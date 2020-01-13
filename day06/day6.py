"""day6.py
"""
import pathlib


ALPHA = 'abcdefghijklmnopqrstuvwxyz'
ALPHA = ALPHA + ALPHA.upper()

cwd = pathlib.Path(__file__).parent.absolute()
data_path = pathlib.PurePath(cwd, 'data')

def get_data(fname):
    with open(fname, 'r') as f:
        return [tuple(map(int, x.split(','))) for x in f.readlines()]


class Grid():
    def __init__(self, coords):
        self.coords = coords
        self.coord_set = set(coords)
        self.m = {}

    def count(self, edges=False):
        not_allowed = set()
        count = {}
        domain = self.find_domain()
        (xmin, xmax), (ymin, ymax) = domain
        xmax, ymax = xmax-1, ymax-1
        if not self.m:
            self.create_map(*domain)
        for coord, l in self.m.items():
            x, y = coord
            if x in (0, xmax) or y in (0, ymax):
                not_allowed.add(l)
            else:
                count[l] = count.get(l, 0) + 1
        if not edges:
            for l in not_allowed:
                del count[l]
        return count

    def find_domain(self):
        xmin = ymin = float('inf')
        xmax = ymax = -float('inf')
        for x, y in self.coords:
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
        return ((xmin, xmax+1), (ymin, ymax+1))

    def get_man_dist(self, c1, c2):
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

    def get_closest(self, c):
        """Get closest coordinate to a given coordinate.

        Parameters
        ----------
        c : tuple

        Returns
        -------
        int or None

        """
        count = 0
        min_dist = float('inf')
        index = None
        for i, co in enumerate(self.coords):
            dist = self.get_man_dist(co, c)
            if dist < min_dist:
                index = i
                min_dist = dist
                count = 1
            elif dist == min_dist:
                count += 1
        return index if count == 1 else None


    def create_map(self, xdomain, ydomain):
        out = []
        self.m = {}
        for y in range(ydomain[0], ydomain[1]):
            line = []
            for x in range(xdomain[0], xdomain[1]):
                cl = self.get_closest((x, y))
                self.m[(x, y)] = cl
                a = ALPHA[cl] if cl is not None else '.'
                if (x, y) in self.coord_set:
                    a = '●'
                line.append(a)
            out.append(''.join(line))
        return '\n'.join(out)


if __name__ == '__main__':
    data = get_data(data_path)
    g = Grid(list(data))
    domain = g.find_domain()
    out = g.create_map(*domain)
    count = g.count()
    big = max(count, key=lambda x: count[x])
    print(f'The biggest area is letter {ALPHA[big]} with area {count[big]}.')

