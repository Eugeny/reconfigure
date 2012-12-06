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
        last_comment = None
        for line in lines:
            line = line.strip()
            if line.startswith(self.comment):
                c = line.strip(self.comment).strip()
                if last_comment:
                    last_comment += '\n' + c
                else:
                    last_comment = c
                continue
            if len(line.split(self.separator)) < 2:
                continue
            tokens = line.split(self.separator)
            node = Node('line')
            if last_comment:
                node.comment = last_comment
                last_comment = None
            for token in tokens:
                if token.startswith(self.comment):
                    node.comment = ' '.join(tokens[tokens.index(token):]).strip(self.comment)
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
