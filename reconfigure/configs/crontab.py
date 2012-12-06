from reconfigure.configs.base import Reconfig
from reconfigure.parsers import CrontabParser
from reconfigure.builders import CrontabBuilder


class CrontabConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': CrontabParser(),
            'builder': CrontabBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
