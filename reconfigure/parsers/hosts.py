from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
from ConfigParser import ConfigParser
from StringIO import StringIO


class HostsParser (BaseParser):
	def parse(self, content):
		lines = filter(None, [x.strip() for x in content.splitlines()])
		root = RootNode()
		for line in lines:
			if line.startswith('#'):
				continue
			tokens = line.split(None, 2)
			if len(tokens) == 2:
				tokens += ['']
			node = Node(tokens[1])
			node.set('address', tokens[0])
			node.append(Node(
				name='aliases',
				children=[PropertyNode('alias', x) for x in tokens[2].split()]
			))
			root.append(node)
		return root
	
	def stringify(self, tree):
		r = ''
		for host in tree.children:
			r += '%s\t%s\t%s\n' % (host.get('address').value, host.name, ' '.join(x.value for x in host.get('aliases').children))
		return r



