from reconfigure.config import Reconfig
from reconfigure.parsers import HostsParser

from reconfigure.builders import BaseBuilder
from items import *


class Builder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()


class HostsConfig (Reconfig):
	def __init__(self, **kwargs):
		k = {
			'parser': HostsParser(), 
			'builder': Builder(), 
		}
		k.update(kwargs)
		Reconfig.__init__(self, **k)
