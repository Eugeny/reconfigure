from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import PasswdBuilder


class PasswdConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': PasswdBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
