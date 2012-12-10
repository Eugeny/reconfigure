from reconfigure.configs.base import Reconfig
from reconfigure.parsers import JsonParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.ajenti import AjentiData


class AjentiConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': JsonParser(),
            'builder': BoundBuilder(AjentiData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
