from base import BaseBuilder
from reconfigure.items.resolv import Config


class ResolvBuilder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()
