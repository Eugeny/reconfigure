from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.hosts import HostsData


class HostsConfig (Reconfig):
    """
    ``/etc/hosts``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(HostsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
