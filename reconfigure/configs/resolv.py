from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.resolv import ResolvData


class ResolvConfig (Reconfig):
    """
    ``/etc/resolv.conf``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(maxsplit=1),
            'builder': BoundBuilder(ResolvData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
