import json


class BoundCollection (object):
    """
    Binds a list-like object to a set of nodes

    :param node: target node (its children will be bound)
    :param item_class: :class:`BoundData` class for items
    :param selector: ``lambda x: bool``, used to filter out a subset of nodes
    """

    def __init__(self, node, item_class, selector=lambda x: True):
        self.node = node
        self.selector = selector
        self.item_class = item_class
        self.data = []
        self.rebuild()

    def rebuild(self):
        """
        Discards cached collection and rebuilds it from the nodes
        """
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

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, index):
        return self.data.__getitem__(index)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def append(self, item):
        self.node.append(item._node)
        self.data.append(item)

    def remove(self, item):
        self.node.remove(item._node)
        self.data.remove(item)

    def insert(self, index, item):
        self.node.children.insert(index, item._node)
        self.data.insert(index, item)

    def pop(self, index):
        d = self[index]
        self.remove(d)
        return d


class BoundDictionary (BoundCollection):
    """
    Binds a dict-like object to a set of nodes. Accepts same params as :class:`BoundCollection` plus ``key``

    :param key: ``lambda value: object``, is used to get key for value in the collection
    """

    def __init__(self, key=None, **kwargs):
        self.key = key
        BoundCollection.__init__(self, **kwargs)

    def rebuild(self):
        BoundCollection.rebuild(self)
        self.rebuild_dict()

    def rebuild_dict(self):
        self.datadict = dict((self.key(x), x) for x in self.data)

    def to_dict(self):
        return dict((k, x.to_dict() if hasattr(x, 'to_dict') else x) for k, x in self.items())

    def __getitem__(self, key):
        self.rebuild_dict()
        return self.datadict[key]

    def __setitem__(self, key, value):
        self.rebuild_dict()
        if not key in self:
            self.append(value)
        self.datadict[key] = value
        self.rebuild_dict()

    def __contains__(self, key):
        self.rebuild_dict()
        return key in self.datadict

    def __iter__(self):
        self.rebuild_dict()
        return self.datadict.__iter__()

    def iteritems(self):
        self.rebuild_dict()
        return self.datadict.items()

    items = iteritems

    def setdefault(self, k, v):
        if not k in self:
            self[k] = v
            self.append(v)
        return self[k]

    def values(self):
        self.rebuild_dict()
        return self.data

    def update(self, other):
        for k, v in other.items():
            self[k] = v

    def pop(self, key):
        if key in self:
            self.remove(self[key])


class BoundData (object):
    """
    Binds itself to a node.

    ``bind_*`` classmethods should be called on module-level, after subclass declaration.

    :param node: all bindings will be relative to this node
    :param kwargs: if ``node`` is ``None``, ``template(**kwargs)`` will be used to create node tree fragment
    """

    def __init__(self, node=None, **kwargs):
        if node is None:
            node = self.template(**kwargs)
        self._node = node
        self.bind_attribute('_extra_content', '_extra_content')

    def template(self, **kwargs):
        """
        Override to create empty objects.

        :returns: a :class:`reconfigure.nodes.Node` tree that will be used as a template for new BoundData instance
        """
        return None

    def to_dict(self):
        res_dict = {}
        for attr_key in self.__class__.__dict__:
            if attr_key in self.__class__._bound:
                if attr_key == '_extra_content':
                    continue
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

    @classmethod
    def bind(cls, data_property, getter, setter):
        """
        Creates an arbitrary named property in the class with given getter and setter. Not usually used directly.

        :param data_property: property name
        :param getter: ``lambda: object``, property getter
        :param setter: ``lambda value: None``, property setter
        """
        if not hasattr(cls, '_bound'):
            cls._bound = []
        cls._bound.append(data_property)
        setattr(cls, data_property, property(getter, setter))

    @classmethod
    def bind_property(cls, node_property, data_property, default=None, \
            default_remove=[], \
            path=lambda x: x, getter=lambda x: x, setter=lambda x: x):
        """
        Binds the value of a child :class:`reconfigure.node.PropertyNode` to a property

        :param node_property: ``PropertyNode``'s ``name``
        :param data_property: property name to be created
        :param default: default value of the property (is ``PropertyNode`` doesn't exist)
        :param default_remove: if setting a value contained in default_remove, the target property is removed
        :param path: ``lambda self.node: PropertyNode``, can be used to point binding to another Node instead of ``self.node``.
        :param getter: ``lambda object: object``, used to transform value when getting
        :param setter: ``lambda object: object``, used to transform value when setting
        """
        def pget(self):
            prop = path(self._node).get(node_property)
            if prop is not None:
                return getter(prop.value)
            else:
                return default

        def pset(self, value):
            if setter(value) in default_remove:
                node = path(self._node).get(node_property)
                if node is not None:
                    path(self._node).remove(node)
            else:
                path(self._node).set_property(node_property, setter(value))

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_attribute(cls, node_attribute, data_property, default=None, \
            path=lambda x: x, getter=lambda x: x, setter=lambda x: x):
        """
        Binds the value of node object's attribute to a property

        :param node_attribute: ``Node``'s attribute name
        :param data_property: property name to be created
        :param default: default value of the property (is ``PropertyNode`` doesn't exist)
        :param path: ``lambda self.node: PropertyNode``, can be used to point binding to another Node instead of ``self.node``.
        :param getter: ``lambda object: object``, used to transform value when getting
        :param setter: ``lambda object: object``, used to transform value when setting
        """
        def pget(self):
            prop = getattr(path(self._node), node_attribute)
            if prop is not None:
                return getter(prop)
            else:
                return getter(default)

        def pset(self, value):
            setattr(path(self._node), node_attribute, setter(value))

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_collection(cls, data_property, path=lambda x: x, selector=lambda x: True, item_class=None, \
        collection_class=BoundCollection, **kwargs):
        """
        Binds the subset of node's children to a collection property

        :param data_property: property name to be created
        :param path: ``lambda self.node: PropertyNode``, can be used to point binding to another Node instead of ``self.node``.
        :param selector: ``lambda Node: bool``, can be used to filter out a subset of child nodes
        :param item_class: a :class:`BoundData` subclass to be used for collection items
        :param collection_class: a :class:`BoundCollection` subclass to be used for collection property itself
        """
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
        """
        Binds the value of node's ``name`` attribute to a property

        :param data_property: property name to be created
        :param getter: ``lambda object: object``, used to transform value when getting
        :param setter: ``lambda object: object``, used to transform value when setting
        """
        def pget(self):
            return getter(self._node.name)

        def pset(self, value):
            self._node.name = setter(value)

        cls.bind(data_property, pget, pset)

    @classmethod
    def bind_child(cls, data_property, path=lambda x: x, item_class=None):
        """
        Directly binds a child Node to a BoundData property

        :param data_property: property name to be created
        :param path: ``lambda self.node: PropertyNode``, can be used to point binding to another Node instead of ``self.node``.
        :param item_class: a :class:`BoundData` subclass to be used for the property value
        """
        def pget(self):
            if not hasattr(self, '__' + data_property):
                setattr(self, '__' + data_property,
                    item_class(
                        path(self._node),
                    )
                )
            return getattr(self, '__' + data_property)

        cls.bind(data_property, pget, None)
