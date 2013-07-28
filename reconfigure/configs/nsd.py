from reconfigure.configs.base import Reconfig
from reconfigure.parsers import NSDParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.nsd import NSDData


class NSDConfig (Reconfig):
    """
    ``NSD DNS server nsd.conf``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': NSDParser(),
            'builder': BoundBuilder(NSDData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
