from reconfigure.builders.base import BaseBuilder
from reconfigure.nodes import Node, PropertyNode


class AutoBaseBuilder (BaseBuilder):
    def build(self, tree):
        node = NodeBox(tree)
        built = self._build(node)
        built._source = tree
        return built

    def _build(self, node):
        pass

    def unbuild(self, tree):
        node = tree._source
        if not node:
            node = Node()
        self._unbuild(tree, NodeBox(node))
        return node

    def _unbuild(self, obj, node):
        pass

    @classmethod
    def object(cls, **props):
        d = Data(**props)
        d._builder = cls()
        return d


class Data (object):
    def __init__(self, **props):
        self.__dict__.update(props)

    def __str__(self):
        s = '{\n'
        s += '\n'.join('\t' + k + ' ' + str(getattr(self, k)) for k in self.__dict__ if not k in ['_source', '_builder'])
        return s + '}'

    def __repr__(self):
        return self.__str__()

    def unbuild(self):
        return self._builder.unbuild(self)


class NodeBox (object):
    def __init__(self, node):
        self.node = node

    def name(self, name):
        self.node.name = name
        return self

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

    def get(self, key):
        return self.node.get(key)

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

    def first(self, fx, default=None):
        if self.nodes:
            return fx(self.nodes[0])
        return default

    def each(self, fx):
        return [fx(i, self.nodes[i]) for i in range(0, len(self.nodes))]

    def build(self, buildercls):
        return [buildercls().build(x) for x in self.nodes]
