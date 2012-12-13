class Node (object):
    def __init__(self, name=None, *args, **kwargs):
        self.name = name
        self.origin = None
        self.children = []
        for node in list(args) + kwargs.get('children', []):
            self.append(node)
        self.comment = kwargs.get('comment', None)

    def __str__(self):
        s = '(%s)' % self.name
        if self.comment:
            s += ' (%s)' % self.comment
        s += '\n'
        for child in self.children:
            s += '\n'.join('\t' + x for x in str(child).splitlines()) + '\n'
        return s

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return sum(hash(x) for x in [self.name, self.origin, self.comment] + self.children)

    def __eq__(self, other):
        if other is None:
            return False

        return \
            self.name == other.name and \
            self.comment == other.comment and \
            self.origin == other.origin and \
            set(self.children) == set(other.children)

    def __iter__(self):
        return iter(self.children)

    def __len__(self):
        return len(self.children)

    def __nonzero__(self):
        return True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, item):
        return item in self.children

    def indexof(self, node):
        if node in self.children:
            return self.children.index(node)
        else:
            return None

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
        if not node.origin:
            node.origin = self.origin
        self.children.append(node)
        node.parent = self

    def remove(self, node):
        self.children.remove(node)

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
        # raise Exception('Node.set deprecated')
        node = self.get(name)
        if not node:
            node = PropertyNode(name, value)
            self.append(node)
        node.value = value
        return self

    def set_property(self, name, value):
        node = self.get(name)
        if not node:
            node = PropertyNode(name, value)
            self.append(node)
        node.value = value
        return self


class RootNode (Node):
    pass


class PropertyNode (Node):
    def __init__(self, name, value, comment=None):
        Node.__init__(self, name, comment=comment)
        self.value = value

    def __eq__(self, other):
        if other is None:
            return False

        return \
            Node.__eq__(self, other) and \
            self.value == other.value

    def __str__(self):
        s = '%s = %s' % (self.name, self.value)
        if self.comment:
            s += ' (%s)' % self.comment
        return s


class IncludeNode (Node):
    def __init__(self, files):
        Node.__init__(self)
        self.name = '<include>'
        self.files = files

    def __str__(self):
        return '<include> %s' % self.files
