from reconfigure.nodes import *


class Item (object):
    def __init__(self):
        self._build(Node('nameserver').set('value', '8.8.8.8'))

    def _build(self, tree):
        self.source = tree
        self.name = tree.name
        self.value = tree['value'].value
        return self

    def _unbuild(self):
        self.source.name = self.name
        self.source['value'] = self.value
        return self.source


class Config (object):
    def __init__(self):
        pass

    def _build(self, tree):
        self.source = tree
        self.items = [Item()._build(node) for node in tree.children]
        return self

    def _unbuild(self):
        self.source.children = [c._unbuild() for c in self.items]
        return self.source
