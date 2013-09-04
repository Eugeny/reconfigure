import chardet


class Reconfig (object):
    """
    Basic config class. Derivatives normally only need to override the constructor.

    Config data is loaded either from ``path`` or from ``content``

    :param parser: overrides the Parser instance
    :param includer: overrides the Includer instance
    :param builder: overrides the Builder instance
    :param path: config file path. Not compatible with ``content``
    :param content: config file content. Not compatible with ``path``
    """

    def __init__(self, parser=None, includer=None, builder=None, path=None, content=None):
        self.parser = parser
        self.builder = builder
        self.includer = includer
        if self.includer is not None:
            if not self.includer.parser:
                self.includer.parser = self.parser
        if path:
            self.origin = path
            self.content = None
        else:
            self.origin = None
            self.content = content

    def load(self):
        """
        Loads the config data, parses and builds it. Sets ``tree`` attribute to point to Data tree.
        """
        if self.origin:
            self.content = open(self.origin, 'r').read()

        try:
            self.content = self.content.decode('utf8')
            self.encoding = 'utf8'
        except UnicodeDecodeError:
            self.encoding = chardet.detect(self.content)['encoding']
            self.content = self.content.decode(self.encoding)

        self.nodetree = self.parser.parse(self.content)
        if self.includer is not None:
            self.nodetree = self.includer.compose(self.origin, self.nodetree)
        if self.builder is not None:
            self.tree = self.builder.build(self.nodetree)
        return self

    def save(self):
        """
        Unbuilds, stringifies and saves the config. If the config was loaded from string, returns ``{ origin: data }`` dict
        """
        tree = self.tree
        if self.builder is not None:
            nodetree = self.builder.unbuild(tree) or self.nodetree
        if self.includer is not None:
            nodetree = self.includer.decompose(nodetree)
        else:
            nodetree = {self.origin: nodetree}

        result = {}
        for k in nodetree:
            result[k or self.origin] = self.parser.stringify(nodetree[k]).encode(self.encoding)

        if self.origin is not None:
            for k in result:
                open(k, 'w').write(result[k])
        return result
