import json


class BoundCollection (object):
    def __init__(self, node, item_class, selector=lambda x: True):
        self.node = node
        self.selector = selector
        self.item_class = item_class
        self.data = []
        self.sorting = lambda x: x
        self.rebuild()

    def sort(self, sorting):
        self.sorting = sorting
        self.rebuild()

    def rebuild(self):
        del self.data[:]
        for node in self.node.children:
            if self.selector(node):
                self.data.append(self.item_class(node))

    def to_dict(self):
        return [x.to_dict() if hasattr(x, 'to_dict') else x for x in self]

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, index):
        return self.data.__getitem__(index)

    def __len__(self):
        return len(self.data)

    def append(self, item):
        self.node.append(item._node)
        self.data.append(item)

    def remove(self, item):
        self.node.remove(item._node)
        self.data.remove(item)


class BoundDictionary (BoundCollection):
    def __init__(self, key=None, **kwargs):
        self.key = key
        BoundCollection.__init__(self, **kwargs)

    def rebuild(self):
        BoundCollection.rebuild(self)
        self.datadict = dict((self.key(x), x) for x in self.data)

    def to_dict(self):
        return dict((k, x.to_dict() if hasattr(x, 'to_dict') else x) for k, x in self.iteritems())

    def __getitem__(self, key):
        return self.datadict[key]

    def __setitem__(self, key, value):
        if not key in self:
            self.append(value)
        self.datadict[key] = value

    def __contains__(self, key):
        return key in self.datadict

    def __iter__(self):
        return self.datadict.__iter__()

    def iteritems(self):
        return self.datadict.iteritems()

    def setdefault(self, k, v):
        if not k in self:
            self[k] = v
            self.append(v)
        return self[k]

    def values(self):
        return self.data

    def update(self, other):
        for k, v in other.iteritems():
            self[k] = v

    def pop(self, key):
        if key in self:
            self.remove(self[key])


class BoundData (object):
    def __init__(self, node=None):
        if not node:
            node = self.template()
        self._node = node

    def template(self):
        return None

    def to_dict(self):
        res_dict = {}
        for attr_key in self.__class__.__dict__:
            if attr_key in self.__class__._bound:
                attr_value = getattr(self, attr_key)
                if isinstance(attr_value, BoundData):
                    res_dict[attr_key] = attr_value.to_dict()
                elif isinstance(attr_value, BoundCollection):
                    res_dict[attr_key] = attr_value.to_dict()
                else:
                    res_dict[attr_key] = attr_value
        return res_dict

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    @classmethod
    def bind(cls, data_property, getter, setter):
        if not hasattr(cls, '_bound'):
            cls._bound = []
        cls._bound.append(data_property)
        setattr(cls, data_property, property(getter, setter))

    @classmethod
    def bind_property(cls, node_property, data_property, default=None, \
            path=lambda x: x, getter=lambda x: x, setter=lambda x: x):
        def pget(self):
            prop = path(self._node).get(node_property)
            if prop:
                return getter(prop.value)
            else:
                return getter(default)

        def pset(self, value):
            path(self._node).set_property(node_property, setter(value))

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_attribute(cls, node_property, data_property, default=None, \
            path=lambda x: x, getter=lambda x: x, setter=lambda x: x):
        def pget(self):
            prop = getattr(path(self._node), node_property)
            if prop:
                return getter(prop)
            else:
                return getter(default)

        def pset(self, value):
            path(self._node).set_property(node_property, setter(value))

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_collection(cls, data_property, path=lambda x: x, selector=lambda x: True, item_class=None, \
        collection_class=BoundCollection, **kwargs):
        def pget(self):
            if not hasattr(self, '__' + data_property):
                setattr(self, '__' + data_property,
                    collection_class(
                        node=path(self._node),
                        item_class=item_class,
                        selector=selector,
                        **kwargs
                    )
                )
            return getattr(self, '__' + data_property)

        cls.bind(data_property, pget, None)

    @classmethod
    def bind_name(cls, data_property, getter=lambda x: x, setter=lambda x: x):
        def pget(self):
            return getter(self._node.name)

        def pset(self, value):
            self._node.name = setter(value)

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_child(cls, data_property, path=lambda x: x, item_class=None):
        def pget(self):
            if not hasattr(self, '__' + data_property):
                setattr(self, '__' + data_property,
                    item_class(
                        path(self._node),
                    )
                )
            return getattr(self, '__' + data_property)

        cls.bind(data_property, pget, None)
