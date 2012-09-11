class Node:
	def __init__(self, name=None):
		self.name = name
		self.origin = None
		self.children = []

	def __str__(self):
		s = '(%s)\n' % self.name 
		for child in self.children:
			s += '\n'.join('\t' + x for x in str(child).splitlines()) + '\n'
		return s

	def __repr__(self):
		return str(self)


class RootNode (Node):
	pass


class PropertyNode (Node):
	def __init__(self, name, value):
		Node.__init__(self, name)
		self.value = value

	def __str__(self):
		return '%s = %s' % (self.name, self.value)


class IncludeNode (Node):
	def __init__(self, files):
		Node.__init__(self)
		self.files = files

	def __str__(self):
		return '<include> %s' % self.files