from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
import json


class JsonParser (BaseParser):
    """
    A parser for JSON files (using ``json`` module)
    """

    def parse(self, content):
        node = RootNode()
        self.load_node_rec(node, json.loads(content))
        return node

    def load_node_rec(self, node, json):
        for k in sorted(json.keys()):
            v = json[k]
            if isinstance(v, dict):
                child = Node(k)
                node.children.append(child)
                self.load_node_rec(child, v)
            else:
                node.children.append(PropertyNode(k, v))

    def stringify(self, tree):
        return json.dumps(self.save_node_rec(tree), indent=4)

    def save_node_rec(self, node):
        r = {}
        for child in node.children:
            if isinstance(child, PropertyNode):
                r[child.name] = child.value
            else:
                r[child.name] = self.save_node_rec(child)
        return r
