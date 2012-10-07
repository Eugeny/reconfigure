from reconfigure.configs.base import Reconfig
from reconfigure.parsers import NginxParser
from reconfigure.includers import NginxIncluder
from reconfigure.builders import NginxBuilder


class NginxConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': NginxParser(),
            'includer': NginxIncluder(),
            'builder': NginxBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
