from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class IPTablesParser (BaseParser):
    def parse(self, content):
        content = filter(None, [x.strip() for x in content.splitlines() if not x.startswith('#')])
        root = RootNode()
        cur_table = None
        for l in content:
            if l.startswith('*'):
                cur_table = Node(l[1:])
                root.append(cur_table)
            elif l.startswith(':'):
                node = Node('default',
                    PropertyNode('chain', l[1:].split()[0]),
                    PropertyNode('destination', l.split()[1]),
                )
                cur_table.append(node)
            else:
                tokens = l.split()
                if tokens[0] == '-A':
                    tokens.pop(0)
                    node = Node('append')
                    cur_table.append(node)
                    node.set_property('chain', tokens.pop(0))
                    while tokens:
                        token = tokens.pop(0)
                        option = Node('option')
                        option.set_property('name', token.strip('-'))
                        while tokens and not tokens[0].startswith('-'):
                            option.append(Node('argument', PropertyNode('value', tokens.pop(0))))
                        node.append(option)

        return root

    def stringify(self, tree):
        data = ''
        for table in tree.children:
            data += '*%s\n' % table.name
            for item in table.children:
                if item.name == 'default':
                    data += ':%s %s [0:0]\n' % (item.get('chain').value, item.get('destination').value)
            for item in table.children:
                if item.name == 'append':
                    data += '-A %s %s\n' % (
                        item.get('chain').value,
                        ' '.join(
                            ('--' if len(o.get('name').value) > 1 else '-') + o.get('name').value + ' ' +
                            ' '.join(a.get('value').value for a in o.children if a.name == 'argument')
                            for o in item.children
                            if o.name == 'option'
                        )
                    )
        data += 'COMMIT\n'
        return data
