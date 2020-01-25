"""day14.py
"""


class Recipe:
    def __init__(self):
        self.data = [3, 7]
        self.elves = [0, 1]

    def next(self):
        score = sum(self.data[x] for x in self.elves)
        score_str = str(score)
        for digit in score_str:
            self.data.append(int(digit))
        for i, elf in enumerate(self.elves):
            self.elves[i] = (elf + 1 + self.data[elf]) % len(self.data)
        return len(score_str)

    def get_next(self, n):
        for i in range(n):
            self.next()

    def stop_at(self, n):
        while len(self.data) < n:
            self.next()

    def find_num(self, n):
        n = [int(x) for x in str(n)]
        nlen = len(n)
        while True:
            new_add = self.next()
            for i in range(new_add):
                part = self.data[-(i+1+nlen): -(i+1)]
                if part == n:
                    return len(self.data[:-(i+1+nlen)])


if __name__ == '__main__':
    r = Recipe()
    stop_num = 509671
    r.stop_at(stop_num + 10)
    out = ''.join(str(x) for x in r.data[stop_num: stop_num+10])
    print(f'part 1: {out}')
    r = Recipe()
    out = r.find_num(stop_num)
    print(f'part 2: {out}')

