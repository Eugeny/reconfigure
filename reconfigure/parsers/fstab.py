from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class FSTabParser (BaseParser):
    fields = ['device', 'mountpoint', 'type', 'options', 'freq', 'passno']

    def parse(self, content):
        lines = filter(None, [x.strip() for x in content.splitlines()])
        root = RootNode()
        for line in lines:
            if line.startswith('#') or len(line.split()) < 2:
                continue
            tokens = line.split()
            node = Node('filesystem')
            for i in range(0, len(self.fields)):
                node[self.fields[i]] = tokens[i]
            root.append(node)
        return root

    def stringify(self, tree):
        r = ''
        for node in tree.children:
            r += '\t'.join(node[x].value for x in self.fields) + '\n'
        return r
