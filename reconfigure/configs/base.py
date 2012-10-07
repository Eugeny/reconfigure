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
            self.content = open(path, 'r').read()
        else:
            self.origin = None
            self.content = content

    def load(self):
        self.tree = self.parser.parse(self.content)
        if self.includer is not None:
            self.tree = self.includer.compose(self.origin, self.tree)
        if self.builder is not None:
            self.tree = self.builder.build(self.tree)

    def save(self):
        tree = self.tree
        if self.builder is not None:
            tree = self.builder.unbuild(tree)
        if self.includer is not None:
            tree = self.includer.decompose(tree)
        else:
            tree = {self.origin: tree}

        result = {}
        for k in tree:
            result[k] = self.parser.stringify(tree[k])
        if self.origin is not None:
            for k in result:
                open(k, 'w').write(result[k])
        return result
