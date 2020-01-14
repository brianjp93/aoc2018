"""day7.py
"""
import networkx as nx
import pathlib
import re
import matplotlib.pyplot as plt


cwd = pathlib.Path(__file__).parent.absolute()
data_path = pathlib.PurePath(cwd, 'data')
tdata_path = pathlib.PurePath(cwd, 'test')


ALPHA = 'abcdefghijklmnopqrstuvwxyz'.upper()


class Assemble:
    def __init__(self, fname):
        self.g = self.get_data(fname)

    @staticmethod
    def get_data(fname):
        g = nx.DiGraph()
        pattern = r'Step ([A-Z]).*step ([A-Z])'
        prog = re.compile(pattern)
        with open(fname, 'r') as f:
            for line in f:
                r = prog.search(line)
                groups = r.groups()
                g.add_edge(groups[0], groups[1])
        return g

    def draw(self):
        plt.subplot()
        # nx.draw(self.g, with_labels=True, font_weight='bold')
        nx.draw_shell(self.g, nlist=['ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'], with_labels=True, font_weight='bold')
        plt.show()

    def get_order(self):
        g = self.g.copy()
        order = []
        need = set(g.nodes)
        while need:
            allowed = []
            for node in need:
                in_edges = g.in_edges(node)
                if len(in_edges) == 0:
                    allowed.append(node)
            allowed.sort()
            newnode = allowed.pop(0)
            order.append(newnode)
            need.remove(newnode)
            g.remove_node(newnode)
        return order

    def ttf(self, l):
        return 60 + ALPHA.index(l) + 1


if __name__ == '__main__':
    # a = Assemble(tdata_path)
    # print(tdata_path)
    # print(a.g.nodes)
    a = Assemble(data_path)
    # a.draw()
    order = a.get_order()
    order_str = ''.join(order)
    print(f'Order: {order_str}')


