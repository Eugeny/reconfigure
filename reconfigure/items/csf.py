from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from reconfigure.items.util import onezero_getter, onezero_setter


class CSFData (BoundData):
    pass


CSFData.bind_property('TESTING', 'testing', getter=onezero_getter, setter=onezero_setter)
CSFData.bind_property('IPV6', 'ipv6', getter=onezero_getter, setter=onezero_setter)

CSFData.bind_property('TCP_IN', 'tcp_in')
CSFData.bind_property('TCP_OUT', 'tcp_out')
CSFData.bind_property('UDP_IN', 'udp_in')
CSFData.bind_property('UDP_OUT', 'udp_out')
CSFData.bind_property('TCP6_IN', 'tcp6_in')
CSFData.bind_property('TCP6_OUT', 'tcp6_out')
CSFData.bind_property('UDP6_IN', 'udp6_in')
CSFData.bind_property('UDP6_OUT', 'udp6_out')
CSFData.bind_property('ETH_DEVICE', 'eth_device')
CSFData.bind_property('ETH6_DEVICE', 'eth6_device')
