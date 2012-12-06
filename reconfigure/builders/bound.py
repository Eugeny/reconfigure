from reconfigure.builders.base import BaseBuilder


class BoundBuilder (BaseBuilder):
    def __init__(self, root_class):
        self.root_class = root_class

    def build(self, nodetree):
        return self.root_class(nodetree)

    def unbuild(self, tree):
        pass
