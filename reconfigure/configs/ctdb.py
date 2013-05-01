from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.ctdb import NodesData, PublicAddressesData


class CTDBNodesConfig (Reconfig):
    """
    ``CTDB node list file``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(NodesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)


class CTDBPublicAddressesConfig (Reconfig):
    """
    ``CTDB public address list file``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(PublicAddressesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
