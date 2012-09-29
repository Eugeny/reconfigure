from reconfigure.config import Reconfig
from reconfigure.parsers import NginxParser
from reconfigure.includers import NginxIncluder

from reconfigure.builders import BaseBuilder
from items import *


class Builder (BaseBuilder):
    def build(self, tree):
        return Config()._build(tree)

    def unbuild(self, tree):
        return tree._unbuild()


class NginxConfig (Reconfig):
	def __init__(self, **kwargs):
		Reconfig.__init__(self, 
			parser=NginxParser(), 
			includer=NginxIncluder(), 
			builder=Builder(), 
			**kwargs)