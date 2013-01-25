from reconfigure.configs.base import Reconfig
from reconfigure.parsers import JsonParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.squid import SquidData


class SquidConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': JsonParser(),
            'builder': BoundBuilder(SquidData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
