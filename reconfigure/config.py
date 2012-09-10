class Reconfig:
	def __init__(self, parser=None, includer=None, builder=None, path=None, content=None):
		self.parser = parser
		self.builder = builder
		self.includer = includer
		if not self.includer.parser:
			self.includer.parser = self.parser
		if path:
			self.content = open(path, 'r').read()
		else:
			self.content = content

	def load(self):
		self.tree = self.parser.parse(self.content)
		self.includer.combine()