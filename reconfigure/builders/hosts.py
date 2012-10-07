from base import BaseBuilder
from reconfigure.items.hosts import Config


class HostsBuilder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()
