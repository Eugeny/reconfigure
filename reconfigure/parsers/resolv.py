from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class ResolvParser (BaseParser):
    def parse(self, content):
        lines = filter(None, [x.strip() for x in content.splitlines()])
        root = RootNode()
        for line in lines:
            if line.startswith('#') or len(line.split()) < 2:
                continue
            tokens = line.split(None, 1)
            node = Node(tokens[0])
            node.set('value', tokens[1])
            root.append(node)
        return root

    def stringify(self, tree):
        r = ''
        for item in tree.children:
            r += '%s\t%s\n' % (item.name, item['value'].value)
        return r
