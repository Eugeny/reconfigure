from reconfigure.nodes import *
from reconfigure.parsers import BaseParser


class IPTablesParser (BaseParser):
    """
    A parser for ``iptables`` configuration as produced by ``iptables-save``
    """

    def parse(self, content):
        content = filter(None, [x.strip() for x in content.splitlines() if not x.startswith('#')])
        root = RootNode()
        cur_table = None
        chains = {}
        for l in content:
            if l.startswith('*'):
                cur_table = Node(l[1:])
                chains = {}
                root.append(cur_table)
            elif l.startswith(':'):
                name = l[1:].split()[0]
                node = Node(name)
                node.set_property('default', l.split()[1])
                chains[name] = node
                cur_table.append(node)
            else:
                comment = None
                if '#' in l:
                    l, comment = l.split('#')
                    comment = comment.strip()
                tokens = l.split()
                if tokens[0] == '-A':
                    tokens.pop(0)
                    node = Node('append')
                    node.comment = comment
                    chain = tokens.pop(0)
                    chains[chain].append(node)
                    while tokens:
                        token = tokens.pop(0)
                        option = Node('option')
                        option.set_property('negative', token == '!')
                        if token == '!':
                            token = tokens.pop(0)
                        option.set_property('name', token.strip('-'))
                        while tokens and not tokens[0].startswith('-') and tokens[0] != '!':
                            option.append(Node('argument', PropertyNode('value', tokens.pop(0))))
                        node.append(option)

        return root

    def stringify(self, tree):
        data = ''
        for table in tree.children:
            data += '*%s\n' % table.name
            for chain in table.children:
                data += ':%s %s [0:0]\n' % (chain.name, chain.get('default').value)
            for chain in table.children:
                for item in chain.children:
                    if item.name == 'append':
                        data += '-A %s %s%s\n' % (
                            chain.name,
                            ' '.join(
                                ('! ' if o.get('negative').value else '') +
                                ('--' if len(o.get('name').value) > 1 else '-') + o.get('name').value + ' ' +
                                ' '.join(a.get('value').value for a in o.children if a.name == 'argument')
                                for o in item.children
                                if o.name == 'option'
                            ),
                            ' # %s' % item.comment if item.comment else ''
                        )
            data += 'COMMIT\n'
        return data
