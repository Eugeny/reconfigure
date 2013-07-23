from reconfigure.includers.auto import AutoIncluder
from reconfigure.nodes import PropertyNode


class BIND9Includer (AutoIncluder):
    def is_include(self, node):
        if isinstance(node, PropertyNode) and node.name == 'include':
            return node.value.strip('"')

    def remove_include(self, node):
        return PropertyNode('include', '"%s"' % node.files)
