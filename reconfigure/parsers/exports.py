from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
from reconfigure.parsers.ssv import SSVParser


class ExportsParser (BaseParser):
    """
    A parser for NFS' /etc/exports
    """

    def __init__(self, *args, **kwargs):
        BaseParser.__init__(self, *args, **kwargs)
        self.inner = SSVParser(continuation='\\')

    def parse(self, content):
        tree = self.inner.parse(content)
        root = RootNode()
        for export in tree:
            export_node = Node(export[0].get('value').value.strip('"'))
            export_node.comment = export.comment
            clients_node = Node('clients')
            export_node.append(clients_node)
            root.append(export_node)

            for client in export[1:]:
                s = client.get('value').value
                name = s.split('(')[0]
                options = ''
                if '(' in s:
                    options = s.split('(', 1)[1].rstrip(')')
                client_node = Node(name)
                client_node.set_property('options', options)
                clients_node.append(client_node)
        return root

    def stringify(self, tree):
        root = RootNode()
        for export in tree:
            export_node = Node('line', comment=export.comment)
            export_node.append(Node('token', PropertyNode('value', '"%s"' % export.name)))
            for client in export['clients']:
                s = client.name
                if client['options'].value:
                    s += '(%s)' % client['options'].value
                export_node.append(Node('token', PropertyNode('value', s)))
            root.append(export_node)
        return self.inner.stringify(root)
