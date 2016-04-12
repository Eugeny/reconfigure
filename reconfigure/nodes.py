class Node (object):
    """
    A base node class for the Node Tree.
    This class represents a named container node.
    """

    def __init__(self, name=None, *args, **kwargs):
        """
        :param name: Node name
        :param *args: Children
        :param comment: Node comment string
        :param origin: Node's source location (usually path to the file)
        """
        self.name = name
        self.origin = None
        self.children = []
        self._extra_content = kwargs.pop('extra_content', None)
        for node in list(args) + kwargs.pop('children', []):
            self.append(node)
        self.comment = kwargs.pop('comment', None)
        self.__dict__.update(kwargs)

    def __str__(self):
        s = '(%s)' % self.name
        if self.comment:
            s += ' (%s)' % self.comment
        s += '\n'
        for child in self.children:
            if child.origin != self.origin:
                s += '\t@%s\n' % child.origin
            s += '\n'.join('\t' + x for x in str(child).splitlines()) + '\n'
        return s

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
        if type(key) in (int, slice):
            return self.children[key]
        return self.get(key)

    def __setitem__(self, key, value):
        if type(key) is int:
            self.children[key] = value
        self.set_property(key, value)

    def __contains__(self, item):
        return item in self.children

    def indexof(self, node):
        """
        :returns: index of the node in the children array or ``None`` if it's not a child
        """
        if node in self.children:
            return self.children.index(node)
        else:
            return None

    def get(self, name, default=None):
        """
        :returns: a child node by its name or ``default``
        """
        for child in self.children:
            if child.name == name:
                return child
        if default:
            self.append(default)
        return default

    def get_all(self, name):
        """
        :returns: list of child nodes with supplied ``name``
        """
        return [n for n in self.children if n.name == name]

    def append(self, node):
        if not node.origin:
            node.origin = self.origin
        self.children.append(node)
        node.parent = self

    def remove(self, node):
        self.children.remove(node)

    def replace(self, name, node=None):
        """
        Replaces the child nodes by ``name``

        :param node: replacement node or list of nodes

        ::

            n.append(Node('a'))
            n.append(Node('a'))
            n.replace('a', None)
            assert(len(n.get_all('a')) == 0)

        """
        if name:
            self.children = [c for c in self.children if c.name != name]
        if node is not None:
            if type(node) == list:
                for n in node:
                    self.children.append(n)
            else:
                self.children.append(node)

    def set_property(self, name, value):
        """
        Creates or replaces a child :class:`PropertyNode` by name.
        """
        node = self.get(name)
        if node is None:
            node = PropertyNode(name, value)
            self.append(node)
        node.value = value
        return self


class RootNode (Node):
    """
    A special node class that indicates tree root
    """


class PropertyNode (Node):
    """
    A node that serves as a property of its parent node.
    """

    def __init__(self, name, value, comment=None):
        """
        :param name: Property name
        :param value: Property value
        """
        Node.__init__(self, name, comment=comment)
        self.value = value

    def __eq__(self, other):
        if other is None:
            return False

        return \
            Node.__eq__(self, other) and \
            self.value == other.value

    def __hash__(self):
        return Node.__hash__(self) + hash(self.value)

    def __str__(self):
        s = '%s = %s' % (self.name, self.value)
        if self.comment:
            s += ' (%s)' % self.comment
        return s


class IncludeNode (Node):
    """
    A node that indicates a junction point between two config files
    """

    def __init__(self, files):
        """
        :param files: an includer-dependent config location specifier
        """
        Node.__init__(self)
        self.name = '<include>'
        self.files = files

    def __str__(self):
        return '<include> %s' % self.files
