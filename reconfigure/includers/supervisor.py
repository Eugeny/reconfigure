from reconfigure.includers.auto import AutoIncluder
from reconfigure.nodes import Node, PropertyNode


class SupervisorIncluder (AutoIncluder):
    def is_include(self, node):
        if node.name == 'include':
            return node.get('files').value

    def remove_include(self, node):
        return Node('include', children=[PropertyNode('files', node.files)])
