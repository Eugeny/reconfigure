from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from reconfigure.items.util import yn_getter, yn_setter


class CTDBData (BoundData):
    pass

CTDBData.bind_property('CTDB_RECOVERY_LOCK', 'recovery_lock_file', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_PUBLIC_INTERFACE', 'public_interface', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_PUBLIC_ADDRESSES', 'public_addresses_file', default='/etc/ctdb/public_addresses', path=lambda x: x.get(None))
CTDBData.bind_property(
    'CTDB_MANAGES_SAMBA', 'manages_samba', path=lambda x: x.get(None),
    getter=yn_getter, setter=yn_setter)
CTDBData.bind_property('CTDB_NODES', 'nodes_file', default='/etc/ctdb/nodes', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_LOGFILE', 'log_file', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_DEBUGLEVEL', 'debug_level', default='2', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_PUBLIC_NETWORK', 'public_network', default='', path=lambda x: x.get(None))
CTDBData.bind_property('CTDB_PUBLIC_GATEWAY', 'public_gateway', default='', path=lambda x: x.get(None))


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

PublicAddressesData.bind_collection('addresses', item_class=PublicAddressData)
PublicAddressData.bind_property('value', 'address', path=lambda x: x.children[0])
PublicAddressData.bind_property('value', 'interface', path=lambda x: x.children[1])
