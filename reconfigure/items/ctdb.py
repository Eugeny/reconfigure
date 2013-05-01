from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class NodesData (BoundData):
    pass


class NodeData (BoundData):
    def template(self):
        return Node('line', children=[
            Node('token', children=[PropertyNode('value', '127.0.0.1')]),
        ])


NodesData.bind_collection('nodes', item_class=NodeData)
NodeData.bind_property('value', 'address', path=lambda x: x.children[0])


class PublicAddressesData (BoundData):
    pass


class PublicAddressData (BoundData):
    def template(self):
        return Node('line', children=[
            Node('token', children=[PropertyNode('value', '127.0.0.1')]),
            Node('token', children=[PropertyNode('value', 'eth0')]),
        ])

PublicAddressesData.bind_collection('nodes', item_class=PublicAddressData)
PublicAddressData.bind_property('value', 'address', path=lambda x: x.children[0])
PublicAddressData.bind_property('value', 'interface', path=lambda x: x.children[1])
