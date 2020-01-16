"""day11.py
"""


class Chronal:
    GRIDSIZE = 300

    def __init__(self, serial):
        self.serial = serial
        self.grid = {}
        self.fill_grid(self.GRIDSIZE, self.GRIDSIZE)
        self.power_grid = {}

    def power(self, x, y):
        rack_id = x + 10
        power = rack_id * y
        power += self.serial
        power *= rack_id
        power = ((power // 100) % 10) - 5
        return power

    def fill_grid(self, rangex, rangey):
        for y in range(1, rangey+1):
            for x in range(1, rangex+1):
                coord = (x, y)
                self.grid[coord] = self.power(*coord)

    def get_power_at(self, x, y, width, height):
        total = 0
        for y in range(y, y+height):
            total += sum(self.grid[(x, y)] for x in range(x, x+height))
        return total

    def find_max_power(self, width, height):
        largest = -float('inf')
        largest_coord = None
        for y in range(1, self.GRIDSIZE-height+1):
            for x in range(1, self.GRIDSIZE-height+1):
                total = self.get_power_at(x, y, width, height)
                if total > largest:
                    largest = total
                    largest_coord = (x, y)
        return largest_coord, largest



if __name__ == '__main__':
    # test = Chronal(18)
    # coord, power = test.find_max_power(3, 3)
    # print(coord, power)
    # print(test.power(122, 79))
    serial = 7139
    chronal = Chronal(serial)
    coord, power = chronal.find_max_power(3, 3)
    print(coord, power)
    # print(chronal.grid)
