from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
from ConfigParser import ConfigParser
from StringIO import StringIO


class IniFileParser (BaseParser):
	def parse(self, content):
		content = '\n'.join(filter(None, [x.strip() for x in content.splitlines()]))
		data = StringIO(content)
		cp = ConfigParser()
		cp.readfp(data)

		root = RootNode()
		for section in cp.sections():
			section_node = Node(name=section)
			for option in cp.options(section):
				section_node.children.append(PropertyNode(option, cp.get(section, option)))
			root.children.append(section_node)
		return root
	
	def stringify(self, tree):
		data = StringIO()
		cp = ConfigParser()
		
		for section in tree.children:
			cp.add_section(section.name)
			for option in section.children:
				if not isinstance(option, PropertyNode):
					raise TypeError('Third level nodes should be PropertyNodes')
				cp.set(section.name, option.name, option.value)

		cp.write(data)
		return data.getvalue()



