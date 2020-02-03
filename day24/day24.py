"""day24.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

re_compile = '([0-9]+) units each with ([0-9]+) hit points \(?(?:([a-z]+) to ((?:(?:[a-z]+),? ?)*)|);? ?(?:([a-z]+) to ((?:(?:[a-z]+),? ?)*)|)\)?.*with an attack that does ([0-9]+) ([a-z]+) damage at initiative ([0-9]+)'

RADIATION = 'radiation'
COLD = 'cold'
SLASHING = 'slashing'
BLUDGEONING = 'bludgeoning'
FIRE = 'fire'
WEAK_AGAINST = {
    
}

class Army:
    def __init__(self, count, hp, weak_to, immune_to, initiative, dmg, dmg_type):
        self.count = count
        self.hp = hp
        self.weak_to = weak_to
        self.immune_to = immune_to
        self.initiative = initiative
        self.dmg = dmg
        self.dmg_type = dmg_type

    def __repr__(self):
        return f'Army(count={self.count}, hp={self.hp}, weak_to={self.weak_to}, immune_to={self.immune_to}, initiative={self.initiative}, dmg={self.dmg}, dmg_type={self.dmg_type})'

    def power(self):
        return self.count * self.dmg

    def calculate_damage(self, enemy):
        pass

    def attack(self, enemy):
        pass

def get_armies(immune_data, infection_data):
        immune_system = []
        infection = []
        program = re.compile(re_compile)
        for j, side in enumerate([immune_data, infection_data]):
            for line in side.split('\n'):
                r = program.match(line)
                g = r.groups()
                weak_to = None
                immune_to = None
                for i in range(len(g)):
                    if g[i] == 'immune':
                        immune_to = tuple(x.strip() for x in g[i+1].split(','))
                    elif g[i] == 'weak':
                        weak_to = tuple(x.strip() for x in g[i+1].split(','))
                a = Army(int(g[0]), int(g[1]), weak_to, immune_to, int(g[8]), int(g[6]), g[7])
                if j == 0:
                    immune_system.append(a)
                elif j == 1:
                    infection.append(a)
        return immune_system, infection


if __name__ == '__main__':
    with open(dpath, 'r') as f:
        immune_data, infection_data = f.read().split('Infection:')
        immune_data = immune_data.strip('Immune System:').strip()
        infection_data = infection_data.strip()
        immune_system, infection = get_armies(immune_data, infection_data)
        print(immune_system)
        print(infection)

