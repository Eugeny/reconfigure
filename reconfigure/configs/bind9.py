from reconfigure.configs.base import Reconfig
from reconfigure.parsers import BIND9Parser
from reconfigure.includers import BIND9Includer
from reconfigure.builders import BoundBuilder
from reconfigure.items.bind9 import BIND9Data


class BIND9Config (Reconfig):
    """
    ``named.conf``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': BIND9Parser(),
            'includer': BIND9Includer(),
            'builder': BoundBuilder(BIND9Data),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
