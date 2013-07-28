from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class NSDParser (BaseParser):
    """
    A parser for NSD DNS server nsd.conf file
    """

    def parse(self, content):
        lines = content.splitlines()
        root = RootNode()
        last_comment = None
        node = root
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('#'):
                    c = line.strip('#').strip()
                    if last_comment:
                        last_comment += '\n' + c
                    else:
                        last_comment = c
                    continue

                key, value = line.split(':')
                value = value.strip()
                key = key.strip()
                if key in ['server', 'zone', 'key']:
                    node = Node(key, comment=last_comment)
                    root.append(node)
                else:
                    node.append(PropertyNode(key, value, comment=last_comment))
                last_comment = None
        return root

    def stringify_comment(self, line, comment):
        if comment:
            return ''.join('# %s\n' % x for x in comment.splitlines()) + line
        return line

    def stringify(self, tree):
        r = ''
        for node in tree.children:
            r += self.stringify_comment(node.name + ':', node.comment) + '\n'
            for subnode in node.children:
                l = '%s: %s' % (subnode.name, subnode.value)
                r += self.stringify_comment(l, subnode.comment) + '\n'
            r += '\n'
        return r
