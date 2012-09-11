from reconfigure.nodes import *
import glob
import os


class BaseIncluder: # pragma: no cover
	def __init__(self, parser=None, content_map={}):
		self.parser = parser
		self.content_map = content_map

	def compose(self, tree):
		pass

	def decompose(self, tree):
		pass


class NginxStyleIncluder (BaseIncluder):
	def compose(self, origin, tree):
		self.compose_rec(origin, tree)
		return tree

	def compose_rec(self, origin, node):
		if not node.origin:
			node.origin = origin
		for child in node.children:
			if isinstance(child, PropertyNode) and child.name == 'include':
				files = child.value
				if node.origin and not files.startswith('/'):
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
					self.compose_rec(file, subtree)
				node.children[node.children.index(child)] = IncludeNode(child.value)
			self.compose_rec(origin, child)

	def decompose(self, tree):
		result = {}
		result[tree.origin] = self.decompose_rec(tree, result)
		return result

	def decompose_rec(self, node, result):
		for child in node.children:
			if child.origin != node.origin:
				node.children.remove(child)
				result[child.origin] = self.decompose_rec(child, result)
			else:
				self.decompose_rec(child, result)
		return node
