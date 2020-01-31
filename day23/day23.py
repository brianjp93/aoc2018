"""day23.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


def mandist(c1, c2):
    return sum(abs(a-b) for a, b in zip(c1, c2))

def count_in_range(c1, r, robots):
    count = 0
    for robot in robots:
        if mandist(c1, robot[0]) <= r:
            count += 1
    return count


if __name__ == '__main__':
    robots = []
    program = re.compile('pos=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, r=(-?[0-9]+)')
    with open(dpath, 'r') as f:
        for line in f:
            line = line.strip()
            r = program.match(line)
            g = r.groups()
            g = list(map(int, g))
            coord = tuple(g[:3])
            radius = g[3]
            robots.append((coord, radius))

    strongest = max(robots, key=lambda x: x[1])
    strongest_coord = strongest[0]
    print(strongest)
    in_range = count_in_range(strongest[0], strongest[1], robots)
    print(f'In range: {in_range}')

