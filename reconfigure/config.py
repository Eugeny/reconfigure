class Reconfig:
	def __init__(self, parser=None, builder=None, path=None, content=None):
		self.parser = parser()
		self.builder = builder()
		if path:
			self.content = open(path, 'r').read()
		else:
			self.content = content

