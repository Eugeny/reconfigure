from reconfigure.configs.base import Reconfig
from reconfigure.parsers import NginxParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.dhcpd import DHCPDData


class DHCPDConfig (Reconfig):
    """
    ``DHCPD``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': NginxParser(),
            'builder': BoundBuilder(DHCPDData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
