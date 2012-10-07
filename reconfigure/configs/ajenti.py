from reconfigure.configs.base import Reconfig
from reconfigure.parsers import JsonParser
from reconfigure.builders import AjentiBuilder


class AjentiConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': JsonParser(),
            'builder': AjentiBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
