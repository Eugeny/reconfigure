from reconfigure.configs.base import Reconfig
from reconfigure.parsers import FSTabParser
from reconfigure.builders import FSTabBuilder


class FSTabConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': FSTabParser(),
            'builder': FSTabBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
