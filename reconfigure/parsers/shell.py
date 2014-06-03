from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class ShellParser (BaseParser):
    """
    A parser for shell scripts with variables
    """

    def __init__(self, *args, **kwargs):
        self.comment = '#'
        self.continuation = '\\'
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

                name, value = line.split('=', 1)
                comment = None
                if '#' in value:
                    value, comment = value.split('#', 1)
                    last_comment = (last_comment or '') + comment.strip()
                node = PropertyNode(name.strip(), value.strip().strip('"'))
                if last_comment:
                    node.comment = last_comment
                    last_comment = None
                root.append(node)
        return root

    def stringify(self, tree):
        r = ''
        for node in tree.children:
            if node.comment and '\n' in node.comment:
                r += '\n' + ''.join('# %s\n' % x for x in node.comment.splitlines())
            r += '%s="%s"' % (node.name, node.value)
            if node.comment and not '\n' in node.comment:
                r += ' # %s' % node.comment
            r += '\n'
        return r
