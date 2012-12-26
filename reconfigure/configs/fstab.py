from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.fstab import FSTabData


class FSTabConfig (Reconfig):
    """
    ``/etc/fstab``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(FSTabData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
