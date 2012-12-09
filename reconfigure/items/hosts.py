from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class HostsData (BoundData):
    pass


class HostData (BoundData):
    def template(self):
        return Node('line', children=[
            Node('token', children=[PropertyNode('value', '127.0.0.1')]),
            Node('token', children=[PropertyNode('value', 'localhost')]),
        ])


class AliasData (BoundData):
    def template(self):
        return Node()


HostsData.bind_collection('hosts', item_class=HostData)
HostData.bind_property('value', 'address', path=lambda x: x.children[0])
HostData.bind_property('value', 'name', path=lambda x: x.children[1])
HostData.bind_collection('aliases', item_class=AliasData, selector=lambda x: x.parent.indexof(x) > 1)
AliasData.bind_property('value', 'name')
