from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IPTablesParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.iptables import IPTablesData


class IPTablesConfig (Reconfig):
    """
    ``iptables-save`` and ``iptables-restore``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': IPTablesParser(),
            'builder': BoundBuilder(IPTablesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
