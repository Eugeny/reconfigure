.. _Bound data:

Bound Data
**********

Bound data (:class:`reconfigure.items.bound.BoundData`) is a special class that can be subclassed and stuffed with properties, which will act as proxies to an underlying :ref:`Node tree<node-tree>`. This can be confusing, so let's go with an example::


    >>> from reconfigure.nodes import Node, PropertyNode
    >>> from reconfigure.items.bound import BoundData
    >>> 
    >>> node = Node('test')
    >>> node.append(PropertyNode('name', 'Alice'))
    >>> node.append(PropertyNode('age', '25'))
    >>> node.append(PropertyNode('gender', 'f'))
    >>> print node
    (test)
            name = Alice
            age = 25
            gender = f

Here we have a very simple :ref:`Node tree <node-tree>`. 
Note that all values are ``str`` and the ``gender`` is coded in a single character (we have probably parsed this tree from some .ini file).
Now let's define a BoundData class::

    >>> class HumanData (BoundData):
    ...     pass
    ... 
    >>> HumanData.bind_property('name', 'name')
    >>> HumanData.bind_property('age', 'age', getter=int, setter=str)
    >>> HumanData.bind_property('gender', 'gender', 
    ...     getter=lambda x: 'Male' if x == 'm' else 'Female',
    ...     setter=lambda x: 'm' if x == 'Male' else 'f')

    >>> human = HumanData(node)
    >>> human
    <__main__.MyData object at 0x114ddd0>
    >>> print human
    {
        "gender": "Female", 
        "age": 25, 
        "name": "Alice"
    }

First, we've defined our ``BoundData`` subclass. Then, we have defined three properties in it:

  * ``name`` is the simplest property, it's directly bound to "name" child ``PropertyNode``
  * ``age`` also has a getter and setter. These are invoked when the property is read or written. In this case, we use ``int()`` to parse a number from the node tree and ``str()`` to stringify it when writing back.
  * ``gender`` is similar to ``age`` but has more complex getter and setter that transform "m" and "f" to a human-readable description.

When the properties are mutated, the modifications are applied to Node tree immediately and vice versa::

    >>> human.age
    25
    >>> human.age = 30
    >>> node.get('age').value
    '30'
    >>> node.get('age').value = 27
    >>> human.age
    27


Using collections
=================

Let's try a more complex node tree::

    >>> nodes = Node('', 
    ...     Node('Alice',
    ...             PropertyNode('Phone', '1234-56-78')
    ...     ),
    ...     Node('Bob', 
    ...             PropertyNode('Phone', '8765-43-21')
    ...     )
    ... )
    >>> print nodes
    ()
            (Alice)
                    Phone = 1234-56-78
            (Bob)
                    Phone = 8765-43-21

Bound data classes::

    >>> class PersonData (BoundData):
    ...     def template(self, name, phone):
    ...             return Node(name,
    ...                     PropertyNode('Phone', phone)
    ...             )
    ... 
    >>> class PhonebookData (BoundData):
    ...     pass
    ... 
    >>> PersonData.bind_property('Phone', 'phone')
    >>> PersonData.bind_name('name')
    >>>
    >>> PhonebookData.bind_collection('entries', item_class=PersonData)
    >>>
    >>> phonebook = PhonebookData(nodes)
    >>> print phonebook
    {
        "entries": [
            {
                "phone": "1234-56-78", 
                "name": "Alice"
            }, 
            {
                "phone": "8765-43-21", 
                "name": "Bob"
            }
        ]
    }

Here, ``bind_collection`` method is used to create a collection property from child nodes. ``item_class`` class will be used to wrap these nodes.

Alternatively, you can employ :class:`reconfigure.items.bound.BoundDictionary` class to create a dict-like property::

    >>> PhonebookData.bind_collection('entries', collection_class=BoundDictionary, item_class=PersonData, key=lambda x: x.name)
    >>> print phonebook
    {
        "entries": {
            "Bob": {
                "phone": "8765-43-21", 
                "name": "Bob"
            }, 
            "Alice": {
                "phone": "1234-56-78", 
                "name": "Alice"
            }
        }
    }