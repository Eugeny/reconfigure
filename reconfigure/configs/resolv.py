from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import ResolvBuilder


class ResolvConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': ResolvBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
