class Node (object):
    def __init__(self, name=None, children=None):
        self.name = name
        self.origin = None
        self.children = children or []

    def __str__(self):
        s = '(%s)\n' % self.name
        for child in sorted(self.children, key=lambda x: x.name):
            s += '\n'.join('\t' + x for x in str(child).splitlines()) + '\n'
        return s

    def __repr__(self):
        return str(self)

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
        self.name = '<include>'
        self.files = files

    def __str__(self):
        return '<include> %s' % self.files

class NodeBox (object):
    def __init__(self, node):
        self.node = node

    def name(self, name=None):
        if name:
            self.node.name = name
            return self
        else:
            return self.node.name

    def children(self):
        return NodeSet(self.node.children)

    def append(self, child=None):
        if not child:
            nodes = [Node()]
        elif child.__class__ != list:
            nodes = [child]
        else:
            nodes = child
        for c in nodes:
            self.node.append(c)

        if len(nodes) == 1:
            return NodeBox(nodes[0])
        else:
            return NodeSet(nodes)

    def has(self, key):
        return any(self.children().each(lambda i, e: e.name == key))

    def get(self, key):
        l = self.children().pick(lambda e: e.name == key)
        return None if len(l.nodes) == 0 else l[0]

    def set(self, key, value, condition=True):
        if condition:
            self.node.set(key, value)
        return self

    def set_all(self, key, values):
        self.children().pick(name=key)
        for v in values:
            self.node.append(PropertyNode(key, v))
        return self

    def append_unbuilt(self, obj):
        if obj.__class__ != list:
            obj = [obj]
        for o in obj:
            self.append(o.unbuild())

    def make_child(self, name):
        node = Node(name)
        self.node.append(node)
        return NodeBox(node)

    def is_property_node(self):
        return isinstance(self.node, PropertyNode)

    def value(self, value=None):
        if self.is_property_node():
            if value:
                self.node.value = value
                return value
            else:
                return self.node.value
        else:
            return None


class NodeSet (object):
    def __init__(self, nodes):
        self.nodes = nodes

    def __getitem__(self, key):
        return self.nodes[key]

    def pick(self, cond=lambda x: True, **props):
        fx = lambda x: cond(x) and all(getattr(x, k) == v for k, v in props.iteritems())
        r = filter(fx, self.nodes)
        for n in r:
            self.nodes.remove(n)
        return NodeSet(r)

    def pickall(self):
        r = [x for x in self.nodes]
        del self.nodes[:]
        return NodeSet(r)

    def slice(self, f, to=None):
        if to is not None:
            return NodeSet(self.nodes[f:to])
        else:
            return NodeSet(self.nodes[f:])

    def nth(self, n):
        return NodeBox(self.nodes[n])

    def first(self, fx, default=None):
        if self.nodes:
            return fx(self.nodes[0])
        return default

    def each(self, fx):
        return [fx(i, self.nodes[i]) for i in range(0, len(self.nodes))]

    def build(self, buildercls):
        return [buildercls().build(x) for x in self.nodes]
