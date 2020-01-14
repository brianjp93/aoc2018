"""day8.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

class Nav:
    def __init__(self, data):
        self.data = data
        self.tree = {}

    def process_node(self, i, name=None):
        """Process nodes recursively and build tree.
        """
        if name is None:
            name = i
        # print(f'Processing name: {name}')
        child_count = self.data[i]
        meta_count = self.data[i+1]
        fchild_i = i + 2
        node_len = 2
        child_len = 0
        next_index_offset = 0
        for _ in range(child_count):
            child_index = fchild_i + next_index_offset
            child_len = self.process_node(child_index)
            next_index_offset += child_len
            node_len += child_len

            # append child
            node_data = self.tree.get(name, {'children': [], 'meta': []})
            node_data['children'].append(child_index)
            self.tree[name] = node_data

        # add meta values
        for meta_i in range(i+node_len, i+node_len + meta_count):
            node_data = self.tree.get(name, {'children': [], 'meta': []})
            node_data['meta'].append(self.data[meta_i])
            self.tree[name] = node_data

        # total node len is header + children + meta
        node_len += meta_count
        return node_len

    def sum_meta(self):
        if not self.tree: self.process_node(0, name='root')
        return sum(sum(data['meta']) for data in self.tree.values())

if __name__ == '__main__':
    with open(dpath, 'r') as f:
        data = [int(x) for x in f.read().strip().split()]
        tdata = [int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]
        nav = Nav(data)
        meta_sum = nav.sum_meta()
        # print(nav.tree)
        print(f'Meta Sum: {meta_sum}')

