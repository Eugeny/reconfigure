from reconfigure.nodes import *


class Host (object):
    def _build(self, tree):
        self.source = tree
        self.name = tree.name
        self.address = tree.get('address').value
        self.aliases = [node.value for node in tree.get('aliases').children]
        return self

    def _unbuild(self):
        self.source.set('address', self.address)
        self.source.name = self.name
        self.source.get('aliases', default=Node('aliases')).children = [PropertyNode('alias', a) for a in self.aliases]
        return self.source


class Config (object):
    def __init__(self):
        pass

    def _build(self, tree):
        self.source = tree
        self.hosts = [Host()._build(node) for node in tree.children]
        return self

    def _unbuild(self):
        self.source.children = [c._unbuild() for c in self.hosts]
        return self.source
