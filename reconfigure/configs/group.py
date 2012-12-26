from reconfigure.configs.base import Reconfig
from reconfigure.parsers import SSVParser
from reconfigure.builders import BoundBuilder
from reconfigure.items.group import GroupsData


class GroupConfig (Reconfig):
    """
    ``/etc/group``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': BoundBuilder(GroupsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
