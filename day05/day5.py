"""day5.py
"""
import pathlib


CWD = pathlib.Path(__file__).parent.absolute()
DATA = pathlib.PurePath(CWD, 'data')

def get_data(fname):
    with open(fname) as f:
        return [x for x in f.read()]

def react(data):
    data = list(data)
    i = 0
    while i < len(data) - 1:
        a, b = data[i:i+2]
        if a != b and a.lower() == b.lower():
            del data[i: i+2]
            i -= 1 if i>0 else 0
        else:
            i += 1
    return data

def react_without(data, l):
    data = [x for x in data if x.lower() != l]
    return react(data)

if __name__ == '__main__':
    dat = get_data(DATA)
    out = react(dat)
    print(f'Part 1: {len(out)}')

    without = {x: len(react_without(dat, x)) for x in 'abcdefghijklmnopqrstuvwxyz'}
    best = min(without, key=lambda x: without[x])
    print(f'Part 2: {without[best]}')
