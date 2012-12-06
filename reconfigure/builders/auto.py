import pprint

from reconfigure.builders.base import BaseBuilder
from reconfigure.nodes import Node, NodeBox, NodeSet
from reconfigure.items.base import Data

class AutoBaseBuilder (BaseBuilder):
    def build(self, tree):
        node = NodeBox(tree)
        built = self._build(node)
        built._source = tree
        return built

    def _build(self, node):
        pass

    def unbuild(self, tree):
        if hasattr(tree, '_source'):
            node = tree._source
        else:
            node = None
        if not node:
            node = Node()
        self._unbuild(tree, NodeBox(node))
        return node

    def _unbuild(self, obj, node):
        pass

    @classmethod
    def object(cls, data_class=Data, **props):
        d = data_class(**props)
        d._builder = cls()
        return d

