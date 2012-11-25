from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class SSVParser (BaseParser):
    def parse(self, content):
        lines = filter(None, [x.strip() for x in content.splitlines()])
        root = RootNode()
        for line in lines:
            if line.startswith('#') or len(line.split()) < 2:
                continue
            tokens = line.split()
            node = Node('line')
            for token in tokens:
                if token.startswith('#'):
                    break
                node.append(Node(
                    name='token',
                    children=[
                        PropertyNode(name='value', value=token)
                    ]
                ))
            root.append(node)
        return root

    def stringify(self, tree):
        r = ''
        for node in tree.children:
            r += '\t'.join(x.get('value').value for x in node.children) + '\n'
        return r
