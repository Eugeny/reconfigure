from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class SSVParser (BaseParser):
    """
    A parser for files containing space-separated value (notably, ``/etc/fstab`` and friends)

    :param separator: separator character, defaults to whitespace
    :param maxsplit: max number of tokens per line, defaults to infinity
    :param comment: character denoting comments
    :param continuation: line continuation character, None to disable
    """

    def __init__(self, separator=None, maxsplit=-1, comment='#', continuation=None, *args, **kwargs):
        self.separator = separator
        self.maxsplit = maxsplit
        self.comment = comment
        self.continuation = continuation
        BaseParser.__init__(self, *args, **kwargs)

    def parse(self, content):
        rawlines = content.splitlines()
        lines = []
        while rawlines:
            l = rawlines.pop(0).strip()
            while self.continuation and rawlines and l.endswith(self.continuation):
                l = l[:-len(self.continuation)]
                l += rawlines.pop(0)
            lines.append(l)
        root = RootNode()
        last_comment = None
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith(self.comment):
                    c = line.strip(self.comment).strip()
                    if last_comment:
                        last_comment += '\n' + c
                    else:
                        last_comment = c
                    continue
                if len(line) == 0:
                    continue
                tokens = line.split(self.separator, self.maxsplit)
                node = Node('line')
                if last_comment:
                    node.comment = last_comment
                    last_comment = None
                for token in tokens:
                    if token.startswith(self.comment):
                        node.comment = ' '.join(tokens[tokens.index(token):])[1:].strip()
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
            if node.comment and '\n' in node.comment:
                r += ''.join('%s %s\n' % (self.comment, x) for x in node.comment.splitlines())
            r += (self.separator or '\t').join(x.get('value').value for x in node.children)
            if node.comment and not '\n' in node.comment:
                r += ' # %s' % node.comment
            r += '\n'
        return r
