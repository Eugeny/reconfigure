from reconfigure.configs.base import Reconfig
from reconfigure.parsers import IniFileParser
from reconfigure.includers import SupervisorIncluder
from reconfigure.builders import BoundBuilder
from reconfigure.items.supervisor import SupervisorData


class SupervisorConfig (Reconfig):
    """
    ``/etc/supervisor/supervisord.conf``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'includer': SupervisorIncluder(),
            'builder': BoundBuilder(SupervisorData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
