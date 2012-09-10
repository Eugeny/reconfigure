from reconfigure.nodes import *
import glob
import os


class BaseIncluder: # pragma: no cover
	def __init__(self, parser=None, content_map={}):
		self.parser = parser
		self.content_map = content_map

	def combine(self, tree):
		pass


class NginxStyleIncluder (BaseIncluder):
	def combine(self, origin, tree):
		self.combine_rec(origin, tree)
		return tree

	def combine_rec(self, origin, node):
		node.origin = origin
		for child in node.children:
			if isinstance(child, PropertyNode) and child.name == 'include':
				files = child.value
				if not files.startswith('/'):
					files = os.path.join(os.path.split(origin)[0], files)
				if '*' in files or '.' in files:
					files = glob.glob(files)
				else:
					files = [files]
				for file in files:
					if file in self.content_map:
						content = self.content_map[file]
					else:
						content = open(file, 'r').read()
					subtree = self.parser.parse(content)
					node.children.extend(subtree.children)
				node.children[node.children.index(child)] = IncludeNode(child.value)
				self.combine_rec(file, child)
			else:
				self.combine_rec(origin, child)
