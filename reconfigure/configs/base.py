class Reconfig (object):
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
        if self.origin:
            self.content = open(self.origin, 'r').read()
        self.nodetree = self.parser.parse(self.content)
        if self.includer is not None:
            self.nodetree = self.includer.compose(self.origin, self.nodetree)
        if self.builder is not None:
            self.tree = self.builder.build(self.nodetree)

    def save(self):
        tree = self.tree
        if self.builder is not None:
            nodetree = self.builder.unbuild(tree) or self.nodetree
        if self.includer is not None:
            nodetree = self.includer.decompose(nodetree)
        else:
            nodetree = {self.origin: nodetree}

        result = {}
        for k in nodetree:
            result[k or self.origin] = self.parser.stringify(nodetree[k])

        if self.origin is not None:
            for k in result:
                open(k, 'w').write(result[k])
        return result
