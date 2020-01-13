"""day6.py
"""
import pathlib
import math


ALPHA = 'abcdefghijklmnopqrstuvwxyz'
ALPHA = ALPHA + ALPHA.upper()

cwd = pathlib.Path(__file__).parent.absolute()
data_path = pathlib.PurePath(cwd, 'data')

test_data = '''
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
'''.strip().splitlines()
test_data = [tuple(map(int, x.strip().split(','))) for x in test_data]

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

    def create_map(self, xdomain, ydomain, mark=None):
        """

        Parameters
        ----------
        mark: set
            A set of coordinates to mark.

        """
        out = []
        self.m = {}
        if mark is None:
            mark = set()
        for y in range(ydomain[0], ydomain[1]):
            line = []
            for x in range(xdomain[0], xdomain[1]):
                cl = self.get_closest((x, y))
                self.m[(x, y)] = cl
                a = ALPHA[cl] if cl is not None else '.'
                if (x, y) in self.coord_set:
                    a = '●'
                if (x, y) in mark:
                    a = '■'
                line.append(a)
            out.append(''.join(line))
        return '\n'.join(out)

    def brute_draw_region(self, thresh=32):
        group = set()
        xdom = (0, 50)
        ydom = (0, 50)
        for y in range(*ydom):
            for x in range(*xdom):
                coord = x, y
                dist = self.find_total_distance(coord)
                if dist < thresh:
                    group.add(coord)
        out = self.create_map(xdom, ydom, mark=group)
        return out

    def find_total_distance(self, c):
        return sum(self.get_man_dist(c, coords) for coords in self.coords)

    def find_equidistant(self):
        """Find all points equidistant to all coordinates.
        """
        domain = self.find_domain()
        xdom, ydom = domain
        min_dist = float('inf')
        group = []
        for y in range(ydom[0], ydom[1]):
            for x in range(xdom[0], xdom[1]):
                coord = (x, y)
                dist = self.find_total_distance(coord)
                if dist < min_dist:
                    group = [coord]
                    min_dist = dist
                elif dist == min_dist:
                    group.append(coord)
        print(f'Min Total Dist: {min_dist}')
        return group

    def find_perimeter(self, thresh=10_000):
        ranges = {}
        group = self.find_equidistant()
        xvals = sorted([c[0] for c in group])
        yvals = sorted([c[1] for c in group])
        xmin, xmax = xvals[0], xvals[-1]
        ymin, ymax = yvals[0], yvals[-1]

        xmidl = xmin + math.floor((xmax - xmin) / 2)
        xmidr = xmin + math.ceil((xmax - xmin) / 2)

        ymidt = ymin + math.floor((ymax - ymin) / 2)
        ymidb = ymin + math.ceil((ymax - ymin) / 2)

        c = [xmidr, ymax]
        dist = self.find_total_distance(c)
        while dist <= thresh:
            cmax = list(c)
            c[1] += 1
            dist = self.find_total_distance(c)
        c = cmax

        # top left
        c2 = [xmidl, ymax]
        while (dist := self.find_total_distance(c2)) <= thresh:
            cmax2 = list(c2)
            c2[1] += 1
        c2 = cmax2

        # bottom left
        c3 = [xmidl, ymin]
        while (dist := self.find_total_distance(c3)) <= thresh:
            cmax3 = list(c3)
            c3[1] -= 1
        c3 = cmax3

        # bottom right
        c4 = [xmidr, ymin]
        while (dist := self.find_total_distance(c4)) <= thresh:
            cmax4 = list(c4)
            c4[1] -= 1
        c4 = cmax4

        # top right quad
        while c[1] > ymidb - 1:
            # print(f'found edge {c}: {self.find_total_distance(c)}')
            ranges[c[0]] = ranges.get(c[0], []) + [c[1]]
            c[0] += 1
            while self.find_total_distance(c) >= thresh:
                # print(f'Trying to find edge at {c}')
                c[1] -= 1
                if c[1] < ymidb - 1:
                    break

        # top left quadrant
        while c2[1] > ymidb - 1:
            ranges[c2[0]] = ranges.get(c2[0], []) + [c2[1]]
            c2[0] -= 1
            while self.find_total_distance(c2) >= thresh:
                # print(f'Trying to find edge at {c2}')
                c2[1] -= 1
                if c2[1] < ymidb - 1:
                    break

        # bottom left quadrant
        while c3[1] < ymidt + 1:
            ranges[c3[0]] = ranges.get(c3[0], []) + [c3[1]]
            c3[0] -= 1
            while self.find_total_distance(c3) >= thresh:
                # print(f'Trying to find edge at {c3}')
                c3[1] += 1
                if c3[1] > ymidt + 1:
                    break

        # bottom right quadrant
        while c4[1] < ymidt + 1:
            ranges[c4[0]] = ranges.get(c4[0], []) + [c4[1]]
            c4[0] += 1
            while self.find_total_distance(c4) >= thresh:
                # print(f'Trying to find edge at {c4}')
                c4[1] += 1
                if c4[1] > ymidt + 1:
                    break

        total = 0
        for x, rg in ranges.items():
            rg = set(rg)
            top, bot = max(rg), min(rg)
            total += abs(top - bot) + 1
        print(f'Total area {total}')
        return total




if __name__ == '__main__':
    data = get_data(data_path)
    # data = test_data
    g = Grid(list(data))
    domain = g.find_domain()
    # out = g.create_map(*domain)
    count = g.count()
    big = max(count, key=lambda x: count[x])
    print(f'The biggest area is letter {ALPHA[big]} with area {count[big]}.')
    equi = g.find_equidistant()
    print(equi)
    # out = g.create_map(*domain, mark=set(equi))
    # print(out)
    # out = g.brute_draw_region(thresh=62)
    # print(out)
    g.find_perimeter()


    
