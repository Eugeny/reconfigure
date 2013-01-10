class BaseIncluder (object):  # pragma: no cover
    """
    A base includer class

    :param parser: Parser instance that was used to parse the root config file
    :param content_map: a dict that overrides config content for specific paths
    """

    def __init__(self, parser=None, content_map={}):
        self.parser = parser
        self.content_map = content_map

    def compose(self, origin, tree):
        """
        Should locate the include nodes in the Node tree, replace them with :class:`reconfigure.nodes.IncludeNode`, parse the specified include files and append them to tree, with correct node ``origin`` attributes
        """

    def decompose(self, origin, tree):
        """
        Should detach the included subtrees from the Node tree and return a ``{ origin: content-node-tree }`` dict.
        """
