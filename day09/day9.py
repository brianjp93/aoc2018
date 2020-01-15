"""day9.py
"""

data = '447 players; last marble is worth 71510 points'
tdata = '10 players; last marble is worth 1618 points'

data2 = '447 players; last marble is worth 7151000 points'

class Marble:
    def __init__(self, data):
        self.nplayers = None
        self.last_points = None
        self.process(data)
        self.i = 0

    def process(self, data):
        dsplit = data.split()
        self.nplayers = int(dsplit[0])
        self.last_points = int(dsplit[-2])

    def play(self):
        i = 0
        marbles = [i]
        mlen = 1
        current = 0
        current_player = 1
        scores = [0] * self.nplayers
        while True:
            if i % 10000 == 0:
                print(f'checking marble {i:,}')
            i += 1
            if i % 23 == 0:
                prev7_index = (current - 7) % mlen
                add_score = i + marbles[prev7_index]
                scores[current_player] += add_score
                marbles.pop(prev7_index)
                mlen -= 1
                current = prev7_index % mlen
            else:
                current = (current + 2) % mlen
                if current == 0:
                    marbles.append(i)
                    current = mlen
                else:
                    marbles.insert(current, i)
                mlen += 1

            if i == self.last_points:
                break

            current_player = (current_player + 1) % self.nplayers
        return max(scores)


if __name__ == '__main__':
    m = Marble(data)
    print(m.nplayers, m.last_points)
    top = m.play()
    print(top)

