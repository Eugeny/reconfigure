from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IniFileParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.samba import SambaData


class SambaConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'builder': BoundBuilder(SambaData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
