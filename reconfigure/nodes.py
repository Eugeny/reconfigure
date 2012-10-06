class Node (object):

    def __init__(self, name=None, children=None):
        self.name = name
        self.origin = None
        self.children = children or []

    def __str__(self):
        s = '(%s)\n' % self.name
        for child in self.children:
            s += '\n'.join('\t' + x for x in str(child).splitlines()) + '\n'
        return s

    def __repr__(self):
        return str(self)

    def get(self, name, default=None):
        for child in self.children:
            if child.name == name:
                return child
        if default:
            self.append(default)
        return default

    def get_all(self, name):
        return [n for n in self.children if n.name == name]

    def append(self, node):
        self.replace(None, node)

    def replace(self, name, node=None):
        if name:
            self.children = [c for c in self.children if c.name != name]
        if node is not None:
            if type(node) == list:
                for n in node:
                    self.children.append(n)
            else:
                self.children.append(node)

    def set(self, name, value):
        node = self.get(name)
        if not node:
            node = PropertyNode(name, value)
            self.append(node)
        node.value = value
        return self


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
