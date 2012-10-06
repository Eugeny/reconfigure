from reconfigure.config import Reconfig
from reconfigure.builders import BaseBuilder
from includer import NginxIncluder
from parser import NginxParser
from items import *

__all__ = ['NginxParser', 'NginxIncluder', 'NginxConfig']

class Builder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()


class NginxConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': NginxParser(),
            'includer': NginxIncluder(),
            'builder': Builder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
