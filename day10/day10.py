"""day10.py
"""
import re
import pathlib


cwd = pathlib.Path(__file__).parent.absolute()
data = pathlib.PurePath(cwd, 'data')
test = pathlib.PurePath(cwd, 'test')


class Planet:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def __repr__(self):
        return f'Planet({self.pos}, {self.vel})'

    def next(self):
        self.pos = [a+b for a, b in zip(self.pos, self.vel)]


class Nav:
    def __init__(self, fname):
        self.planets = {}
        self.init_planets(fname)

    def init_planets(self, fname):
        planets = {}
        prog = re.compile('position=<[ ]*([-]?[0-9]+),[ ]*([-]?[0-9]+)> velocity=<[ ]*([-]?[0-9]+),[ ]*([-]?[0-9]+)>')
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                r = prog.match(line)
                groups = list(map(int, r.groups()))
                planet = Planet(groups[:2], groups[2:])
                planets[tuple(planet.pos)] = planets.get(tuple(planet.pos), []) + [planet]
        self.planets = planets

    def next(self):
        planets = {}
        for planet_list in self.planets.values():
            for planet in planet_list:
                planet.next()
                planets[tuple(planet.pos)] = planets.get(tuple(planet.pos), []) + [planet]
        self.planets = planets

    def get_range(self):
        minx = min(self.planets.keys(), key=lambda x: x[0])[0]
        maxx = max(self.planets.keys(), key=lambda x: x[0])[0]
        miny = min(self.planets.keys(), key=lambda x: x[1])[1]
        maxy = max(self.planets.keys(), key=lambda x: x[1])[1]
        return (minx, maxx), (miny, maxy)

    def draw(self):
        (minx, maxx), (miny, maxy) = self.get_range()
        pad = 5
        fullout = []
        for y in range(miny-pad, maxy+pad+1):
            line = []
            for x in range(minx-pad, maxx+pad+1):
                coord = (x, y)
                if coord in self.planets:
                    out = '#'
                else:
                    out = '.'
                line.append(out)
            fullout.append(''.join(line))
        return '\n'.join(fullout)


if __name__ == '__main__':
    nav = Nav(data)

    i = 0
    while True:
        rangex, rangey = nav.get_range()
        if abs(rangex[0] - rangex[1]) < 100 and abs(rangey[0] - rangey[1]) < 100:
            out = nav.draw()
            print(f'time: {i} seconds')
            print(out)
            input()
        nav.next()
        i += 1











