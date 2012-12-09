from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class ResolvData (BoundData):
    pass


class ItemData (BoundData):
    def template(self):
        return Node('line', children=[
            Node('token', children=[PropertyNode('value', 'nameserver')]),
            Node('token', children=[PropertyNode('value', '8.8.8.8')]),
        ])


ResolvData.bind_collection('items', item_class=ItemData)
ItemData.bind_property('value', 'name', path=lambda x: x.children[0])
ItemData.bind_property('value', 'value', path=lambda x: x.children[1])
