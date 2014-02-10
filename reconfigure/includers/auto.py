from reconfigure.includers.base import BaseIncluder
from reconfigure.nodes import *
import glob
import os


class AutoIncluder (BaseIncluder):
    """
    This base includer automatically walks the node tree and loads the include files from ``IncludeNode.files`` properties. ``files`` is supposed to contain absolute path, relative path or a shell wildcard.
    """

    def compose(self, origin, tree):
        self.compose_rec(origin, origin, tree)
        return tree

    def compose_rec(self, root, origin, node):
        if not node.origin:
            node.origin = origin
        for child in node.children:
            self.compose_rec(root, origin, child)
        for child in node.children:
            spec = self.is_include(child)
            if spec:
                files = spec
                if node.origin and not files.startswith('/'):
                    files = os.path.join(os.path.split(root)[0], files)
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
                    self.compose_rec(root, file, subtree)
                node.children[node.children.index(child)] = IncludeNode(spec)

    def decompose(self, tree):
        result = {}
        result[tree.origin] = self.decompose_rec(tree, result)
        return result

    def decompose_rec(self, node, result):
        for child in node.children:
            if child.__class__ == IncludeNode:
                replacement = self.remove_include(child)
                if replacement:
                    node.children[node.children.index(child)] = replacement
            else:
                if child.origin is None:
                    child.origin = node.origin
                if child.origin != node.origin:
                    node.children.remove(child)
                    result.setdefault(child.origin, RootNode()).children.append(self.decompose_rec(child, result))
                else:
                    self.decompose_rec(child, result)
        return node

    def is_include(self, node):
        """
        Should return whether the node is an include node and return file pattern glob if it is
        """

    def remove_include(self, node):
        """
        Shoud transform :class:`reconfigure.nodes.IncludeNode` into a normal Node to be stringified into the file
        """
