from reconfigure.configs.base import Reconfig
from reconfigure.parsers import HostsParser
from reconfigure.builders import HostsBuilder


class HostsConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': HostsParser(),
            'builder': HostsBuilder(),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
