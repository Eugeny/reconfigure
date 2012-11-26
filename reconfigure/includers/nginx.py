from reconfigure.includers.auto import AutoIncluder
from reconfigure.nodes import PropertyNode


class NginxIncluder (AutoIncluder):
    def is_include(self, node):
        if isinstance(node, PropertyNode) and node.name == 'include':
            return node.value
