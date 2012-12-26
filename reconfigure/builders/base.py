class BaseBuilder (object):
    """
    A base class for builders
    """

    def build(self, tree):
        """
        :param tree: :class:`reconfigure.nodes.Node` tree
        :returns: Data tree
        """

    def unbuild(self, tree):
        """
        :param tree: Data tree
        :returns: :class:`reconfigure.nodes.Node` tree
        """
