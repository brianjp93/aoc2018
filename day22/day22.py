"""day22.py
"""
from queue import PriorityQueue


DEPTH = 5913
TARGET = (8, 701)

ROCKY = '.'
WET = '='
NARROW = '|'
TORCH = 'torch'
GEAR = 'gear'
NEITHER = 'neither'
ALLOWED = {
    ROCKY: [GEAR, TORCH],
    WET: [GEAR, NEITHER],
    NARROW: [TORCH, NEITHER]
}


class Cave:
    def __init__(self, target, depth):
        self.target = target
        self.depth = depth
        self.geo_index = {}
        self.risk = {}
        self.dirs = [
            (1, 0), (0, 1),
            (-1, 0), (0, -1)
        ]

    def get_geological_index(self, coord):
        x, y = coord
        if coord in self.geo_index:
            out = self.geo_index[coord]
        elif coord == (0, 0):
            out = 0
        elif coord == self.target:
            out = 0
        elif y == 0:
            out = x * 16807
        elif x == 0:
            out = y * 48271
        else:
            out = self.get_erosion_level((x-1, y)) * self.get_erosion_level((x, y-1))
        if coord not in self.geo_index:
            self.geo_index[coord] = out
        return out

    def get_erosion_level(self, coord):
        geo_index = self.get_geological_index(coord)
        erosion_level = (geo_index + self.depth) % 20183
        return erosion_level

    def get_type(self, coord):
        ero_level = self.get_erosion_level(coord)
        ero_level = ero_level % 3
        if ero_level == 0:
            out = ROCKY
        elif ero_level == 1:
            out = WET
        elif ero_level == 2:
            out = NARROW
        return out

    def draw(self, coord):
        out = []
        for y in range(coord[1] + 1):
            out.append(''.join(self.get_type((x, y)) for x in range(coord[0] + 1)))
        return '\n'.join(out)

    def get_risk(self, coord):
        if coord in self.risk:
            out = self.risk[coord]
        else:
            x, y = coord
            risk = {'.': 0, '=': 1, '|': 2}
            if coord == (0, 0):
                out = risk[self.get_type(coord)]
            elif y == 0:
                out = self.get_risk((x-1, y)) + risk[self.get_type(coord)]
            elif x == 0:
                out = self.get_risk((x, y-1)) + risk[self.get_type(coord)]
            else:
                up = self.get_risk((x, y-1))
                upleft = self.get_risk((x-1, y-1))
                left = self.get_risk((x-1, y))
                out = up - upleft + left
                out += risk[self.get_type(coord)]
        if coord not in self.risk:
            self.risk[coord] = out
        return out

    def climb_to(self, target=None):
        if target is None:
            target = self.target
        history = {}
        q = PriorityQueue()
        q.put((0, (0, 0), TORCH))
        while not q.empty():
            t, coord, equipped = q.get()
            current_type = self.get_type(coord)
            hist_key = (coord, equipped)
            if t < history.get(hist_key, float('inf')):
                history[hist_key] = t
                if coord == target:
                    out = t
                    break
                for d in self.dirs:
                    ncoord = tuple(a+b for a, b in zip(coord, d))
                    if ncoord == target:
                        if equipped != TORCH:
                            nt = t + 8
                        else:
                            nt = t + 1
                        q.put((nt, ncoord, TORCH))
                    elif ncoord[0] >= 0 and ncoord[1] >= 0:
                        terrain_type = self.get_type(ncoord)
                        if equipped in ALLOWED[terrain_type]:
                            q.put((t+1, ncoord, equipped))
                        else:
                            for new_equip in ALLOWED[terrain_type]:
                                if new_equip in ALLOWED[current_type]:
                                    q.put((t+8, ncoord, new_equip))
        return out


if __name__ == '__main__':
    cave = Cave(TARGET, DEPTH)
    risk = cave.get_risk(TARGET)
    print(f'Part 1: {risk}')
    fastest_climb = cave.climb_to()
    print(f'Part 2: {fastest_climb}')

