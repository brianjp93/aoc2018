"""day13.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
data = pathlib.PurePath(cwd, 'data')
test = pathlib.PurePath(cwd, 'test')


class MineCart:
    def __init__(self, fname):
        self.map = []
        self.carts = {}
        self.dindex = '^>v<'
        self.directions = {
            '^': (0, -1),
            '>': (1, 0),
            'v': (0, 1),
            '<': (-1, 0)
        }
        self.process(fname)

    def get(self, x, y):
        return self.map[y][x]

    def set(self, x, y, z):
        self.map[y][x] = z

    def next_cart(self, cart, curve, turn_count):
        out = cart
        if curve == '/':
            if cart == '>':
                out = '^'
            elif cart == '^':
                out = '>'
            elif cart == '<':
                out = 'v'
            elif cart == 'v':
                out = '<'
        elif curve == '\\':
            if cart == '^':
                out = '<'
            elif cart == '>':
                out = 'v'
            elif cart == 'v':
                out = '>'
            elif cart == '<':
                out = '^'
        elif curve == '+':
            index = self.dindex.index(cart)
            turn_count = turn_count % 3
            if turn_count == 0:
                index -= 1
                index = index % len(self.dindex)
                out = self.dindex[index]
                turn_count += 1
            elif turn_count == 2:
                index += 1
                index = index % len(self.dindex)
                out = self.dindex[index]
                turn_count += 1
            else:
                turn_count += 1
        return out, turn_count

    def process(self, fname):
        out = []
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip('\n')
                out.append([x for x in line])
        self.map = out
        
        cart_chars = '<>^v'
        for y, row in enumerate(out):
            for x, ch in enumerate(row):
                if ch in cart_chars:
                    coord = x, y
                    self.carts[coord] = self.carts.get(coord, []) + [(ch, 0)]
                    if ch in '<>':
                        self.set(x, y, '-')
                    elif ch in '^v':
                        self.set(x, y, '|')

    def next(self):
        keys = sorted(self.carts.keys(), key=lambda x: (x[1], x[0]))
        for coord in keys:
            for i, (cart, turn_count) in enumerate(self.carts[coord]):
                new_coord = tuple(a+b for a, b in zip(coord, self.directions[cart]))
                new_cart, new_turn_count = self.next_cart(cart, self.get(*new_coord), turn_count)
                self.carts[coord].pop(i)
                if len(self.carts[coord]) == 0:
                    del self.carts[coord]
                self.carts[new_coord] = self.carts.get(new_coord, []) + [(new_cart, new_turn_count)]
                if len(self.carts[new_coord]) > 1:
                    print(f'Found collision: {new_coord}')
                    return True
        return False

    def next_until_collision(self):
        collision = False
        while not collision:
            # print(self.draw())
            # input()
            collision = self.next()

    def draw(self):
        out = []
        for y, row in enumerate(self.map):
            line = []
            for x, ch in enumerate(row):
                if (x, y) in self.carts:
                    if len(self.carts[(x, y)]) > 1:
                        line.append('x')
                    else:
                        line.append(self.carts[(x, y)][0][0])
                else:
                    line.append(self.get(x, y))
            out.append(''.join(line))
        return '\n'.join(out)


if __name__ == '__main__':
    mctest = MineCart(test)
    mctest.next_until_collision()


    mc = MineCart(data)
    mc.next_until_collision()

