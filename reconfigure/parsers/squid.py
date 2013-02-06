from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class SquidParser (BaseParser):
    """
    A parser for Squid configs
    """

    def parse(self, content):
        lines = filter(None, [x.strip() for x in content.splitlines()])
        root = RootNode()
        last_comment = None
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                c = line.strip('#').strip()
                if last_comment:
                    last_comment += '\n' + c
                else:
                    last_comment = c
                continue
            if len(line) == 0:
                continue
            tokens = line.split()
            node = Node('line', Node('arguments'))
            if last_comment:
                node.comment = last_comment
                last_comment = None

            index = 0
            for token in tokens:
                if token.startswith('#'):
                    node.comment = ' '.join(tokens[tokens.index(token):])[1:].strip()
                    break
                if index == 0:
                    node.set_property('name', token)
                else:
                    node.get('arguments').set_property(str(index), token)
                index += 1
            root.append(node)
        return root

    def stringify(self, tree):
        r = ''
        for node in tree.children:
            if node.comment and '\n' in node.comment:
                r += ''.join('%s %s\n' % ('#', x) for x in node.comment.splitlines())
            r += node.get('name').value + ' ' + ' '.join(x.value for x in node.get('arguments').children)
            if node.comment and not '\n' in node.comment:
                r += ' # %s' % node.comment
            r += '\n'
        return r
