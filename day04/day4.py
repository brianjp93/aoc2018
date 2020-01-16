"""day4.py
"""
import re
import pathlib
from datetime import datetime, timedelta
from collections import defaultdict

cwd = pathlib.Path(__file__).parent.absolute()
data = pathlib.PurePath(cwd, 'data')

if __name__ == '__main__':
    with open(data, 'r') as f:
        d = f.read().splitlines()
        d.sort(key=lambda x: x.split(']')[0])
        pattern = re.compile('([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)')
        sleeptime = {}
        for event in d:
            s = pattern.search(event)
            year, month, day, hour, minute = s.groups()
            dt = datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute))
            if 'Guard' in event:
                guard_id = re.search('#([0-9]+)', event).groups()[0]
                if guard_id not in sleeptime:
                    sleeptime[guard_id] = set()
            elif 'falls' in event:
                prev_time = dt
            elif 'wakes' in event:
                cur = prev_time
                while cur < dt:
                    sleeptime[guard_id].add(cur)
                    cur = cur + timedelta(minutes=1)

        guard_id = max(sleeptime, key=lambda x: len(sleeptime[x]))
        most_slept_time = defaultdict(int)
        for val in sleeptime[guard_id]:
            most_slept_time[val.minute] += 1
        minute = max(most_slept_time, key=lambda x: most_slept_time[x])
        part1 = int(guard_id) * int(minute)
        print(f'Part 1: {part1}')

        guardsleep = {}
        for g, val in sleeptime.items():
            most_slept_time = defaultdict(int)
            for val in sleeptime[g]:
                most_slept_time[val.minute] += 1
            if most_slept_time:
                minute = max(most_slept_time, key=lambda x: most_slept_time[x])
                times_slept = most_slept_time[minute]
                guardsleep[g] = (minute, times_slept)

        guard_most_sleep = max(guardsleep, key=lambda x: guardsleep[x][1])
        part2 = int(guard_most_sleep) * guardsleep[guard_most_sleep][0]
        print(f'Part 2: {part2}')
