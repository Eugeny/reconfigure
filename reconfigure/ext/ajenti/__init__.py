from reconfigure.builders import BaseBuilder
from items import *


class Builder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()