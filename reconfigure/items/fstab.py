from reconfigure.nodes import *


class Filesystem (object):
    fields = ['device', 'mountpoint', 'type', 'options', 'freq', 'passno']

    def __init__(self):
        self._build(Node('', [PropertyNode(x, 'none') for x in self.fields]))

    def _build(self, tree):
        self.source = tree
        for k in self.fields:
            setattr(self, k, tree[k].value)
        return self

    def _unbuild(self):
        for k in self.fields:
            self.source[k] = getattr(self, k)
        return self.source


class Config (object):
    def __init__(self):
        pass

    def _build(self, tree):
        self.source = tree
        self.filesystems = [Filesystem()._build(node) for node in tree.children]
        return self

    def _unbuild(self):
        self.source.children = [c._unbuild() for c in self.filesystems]
        return self.source
