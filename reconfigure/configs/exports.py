from reconfigure.configs.base import Reconfig
from reconfigure.parsers import ExportsParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.exports import ExportsData


class ExportsConfig (Reconfig):
    """
    ``/etc/fstab``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': ExportsParser(),
            'builder': BoundBuilder(ExportsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
