from base import BaseBuilder
from reconfigure.items.ajenti import Config


class AjentiBuilder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()
