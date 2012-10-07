class BaseIncluder (object):  # pragma: no cover
    def __init__(self, parser=None, content_map={}):
        self.parser = parser
        self.content_map = content_map

    def compose(self, tree):
        pass

    def decompose(self, tree):
        pass
