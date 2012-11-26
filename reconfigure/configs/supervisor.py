from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IniFileParser
from reconfigure.includers import NginxIncluder
from reconfigure.builders import SupervisorBuilder


class SupervisorConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'includer': NginxIncluder(),
            'builder': SupervisorBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
