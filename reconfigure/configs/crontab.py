from reconfigure.configs.base import Reconfig
from reconfigure.parsers import CrontabParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.crontab import CrontabData


class CrontabConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': CrontabParser(),
            'builder': BoundBuilder(CrontabData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
