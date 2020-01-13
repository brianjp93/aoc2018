"""day7.py
"""
import networkx as nx
import pathlib
import re
import matplotlib.pyplot as plt


cwd = pathlib.Path(__file__).parent.absolute()
data_path = pathlib.PurePath(cwd, 'data')

class Assemble:
    def __init__(self, fname):
        self.g = self.get_data(fname)

    @staticmethod
    def get_data(fname):
        g = nx.DiGraph()
        pattern = r'Step ([A-Z]).*step ([A-Z])'
        prog = re.compile(pattern)
        with open(data_path, 'r') as f:
            for line in f:
                r = prog.search(line)
                groups = r.groups()
                g.add_edge(groups[0], groups[1])
        return g

    def draw(self):
        plt.subplot()
        nx.draw(self.g, with_labels=True, font_weight='bold')
        plt.show()

if __name__ == '__main__':
    a = Assemble(data_path)
    # print(a.g.edges)
    # a.draw()
    

