from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class SSVParser (BaseParser):
    def __init__(self, separator=None, comment='#', *args, **kwargs):
        self.separator = separator
        self.comment = comment
        BaseParser.__init__(self, *args, **kwargs)

    def parse(self, content):
        lines = filter(None, [x.strip() for x in content.splitlines()])
        root = RootNode()
        for line in lines:
            if line.startswith(self.comment) or len(line.split(self.separator)) < 2:
                continue
            tokens = line.split(self.separator)
            node = Node('line')
            for token in tokens:
                if token.startswith(self.comment):
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
            r += (self.separator or '\t').join(x.get('value').value for x in node.children) + '\n'
        return r
