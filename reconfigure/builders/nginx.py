from base import BaseBuilder
from reconfigure.items.nginx import Config


class NginxBuilder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()
