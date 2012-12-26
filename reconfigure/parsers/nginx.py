from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
import re


class NginxParser (BaseParser):
    """
    A parser for nginx configs
    """

    def parse(self, content):
        scanner = re.Scanner([
                (r"[\w_]+?.+?;", lambda s, t: ('option', t)),
                (r"\s", lambda s, t: 'whitespace'),
                (r"$^", lambda s, t: 'newline'),
                (r"\#.*?\n", lambda s, t: ('comment', t)),
                (r"[\w_]+\s*?.*?{", lambda s, t: ('section_start', t)),
                (r"\}", lambda s, t: 'section_end'),
            ])
        tokens, remainder = scanner.scan(' '.join(filter(None, content.split(' '))))
        if remainder:
            raise Exception('Invalid tokens: %s' % remainder)

        node = RootNode()
        node_stack = []

        while len(tokens) > 0:
            token = tokens[0]
            tokens = tokens[1:]
            if token in ['whitespace', 'newline']:
                continue
            if token == 'section_end':
                node = node_stack.pop()
            if token[0] == 'option':
                k, v = token[1].split(None, 1)
                node.children.append(PropertyNode(k.strip(), v[:-1].strip()))
            if token[0] == 'section_start':
                section = Node(token[1][:-1].strip())
                node_stack += [node]
                node.children.append(section)
                node = section

        return node

    def stringify(self, tree):
        return ''.join(self.stringify_rec(node) for node in tree.children)

    def stringify_rec(self, node):
        if isinstance(node, PropertyNode):
            return '%s %s;\n' % (node.name, node.value)
        if isinstance(node, IncludeNode):
            return 'include %s;\n' % (node.files)
        result = '\n%s {\n' % node.name
        for child in node.children:
            result += '\n'.join('\t' + x for x in self.stringify_rec(child).splitlines()) + '\n'
        result += '}\n'
        return result
