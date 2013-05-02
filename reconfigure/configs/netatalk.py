from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IniFileParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.netatalk import NetatalkData


class NetatalkConfig (Reconfig):
    """
    Netatalk afp.conf
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'builder': BoundBuilder(NetatalkData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
