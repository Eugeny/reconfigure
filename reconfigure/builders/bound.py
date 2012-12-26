from reconfigure.builders.base import BaseBuilder


class BoundBuilder (BaseBuilder):
    """
    A builder that uses :class:`reconfigure.items.bound.BoundData` to build stuff

    :param root_class: a ``BoundData`` class that used as processing root
    """

    def __init__(self, root_class):
        self.root_class = root_class

    def build(self, nodetree):
        return self.root_class(nodetree)

    def unbuild(self, tree):
        pass
