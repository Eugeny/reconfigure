from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import GroupBuilder


class GroupConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': GroupBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
