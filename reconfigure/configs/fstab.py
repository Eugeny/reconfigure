from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import FSTabBuilder


class FSTabConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': FSTabBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
