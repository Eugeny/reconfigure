from base import BaseBuilder
from reconfigure.items.fstab import Config


class FSTabBuilder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()
