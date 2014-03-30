from reconfigure.configs.base import Reconfig
from reconfigure.parsers import ShellParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.csf import CSFData


class CSFConfig (Reconfig):
    """
    ``CSF main config``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': ShellParser(),
            'builder': BoundBuilder(CSFData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
