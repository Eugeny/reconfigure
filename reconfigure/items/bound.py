class BoundCollection (object):
    def __init__(self, node, item_class, selector=lambda x: True):
        self.node = node
        self.selector = selector
        self.item_class = item_class
        self.data = []
        self.rebuild()

    def rebuild(self):
        del self.data[:]
        for node in self.node.children:
            if self.selector(node):
                self.data.append(self.item_class(node))

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


class BoundData (object):
    def __init__(self, node=None):
        if not node:
            node = self.template()
        self._node = node

    def template(self):
        return None

    @classmethod
    def bind(cls, data_property, getter, setter):
        setattr(cls, data_property, property(getter, setter))

    @classmethod
    def bind_property(cls, node_property, data_property, default=None, \
            object=lambda x: x, getter=lambda x: x, setter=lambda x: x):
        def pget(self):
            prop = object(self._node).get(node_property)
            if prop:
                return getter(prop.value)
            else:
                return getter(default)

        def pset(self, value):
            object(self._node).set_property(node_property, setter(value))

        BoundData.bind(data_property, pget, pset)

    @classmethod
    def bind_collection(cls, data_property, object=lambda x: x, selector=lambda x: True, item_class=None, \
        collection_class=BoundCollection):
        def pget(self):
            if not hasattr(self, '__' + data_property):
                setattr(self, '__' + data_property,
                    collection_class(
                        node=object(self._node),
                        item_class=item_class,
                        selector=selector
                    )
                )
            return getattr(self, '__' + data_property)

        BoundData.bind(data_property, pget, None)
