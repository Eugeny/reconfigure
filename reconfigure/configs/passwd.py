from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.passwd import PasswdData


class PasswdConfig (Reconfig):
    """
    ``/etc/passwd``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': BoundBuilder(PasswdData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
