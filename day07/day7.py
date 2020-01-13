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
        # nx.draw(self.g, with_labels=True, font_weight='bold')
        nx.draw_shell(self.g, nlist=['ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ'], with_labels=True, font_weight='bold')
        plt.show()

    def get_order(self):
        order = []
        allowed = []
        added = set()
        for node in self.g.nodes:
            in_edges = self.g.in_edges(node)
            if len(in_edges) == 0:
                allowed.append(node)

        while allowed:
            allowed.sort()
            node = allowed.pop(0)
            order.append(node)
            for edge in self.g.out_edges(node):
                new_node = edge[1]
                if new_node not in added:
                    allowed.append(new_node)
                    added.add(new_node)
        return order

if __name__ == '__main__':
    a = Assemble(data_path)
    # a.draw()
    order = a.get_order()
    order_str = ''.join(order)
    print(f'Order: {order_str}')

