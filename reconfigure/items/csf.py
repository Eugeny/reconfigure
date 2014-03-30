from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from reconfigure.items.util import onezero_getter, onezero_setter, quote_getter, quote_setter


class CSFData (BoundData):
    pass


q10_g = lambda x: onezero_getter(quote_getter(x))
q10_s = lambda x: quote_setter(onezero_setter(x))

CSFData.bind_property('TESTING', 'testing', path=lambda x: x.get(None), getter=q10_g, setter=q10_s)
CSFData.bind_property('IPV6', 'ipv6', path=lambda x: x.get(None), getter=q10_g, setter=q10_s)

CSFData.bind_property('TCP_IN', 'tcp_in', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('TCP_OUT', 'tcp_out', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('UDP_IN', 'udp_in', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('UDP_OUT', 'udp_out', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('TCP6_IN', 'tcp6_in', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('TCP6_OUT', 'tcp6_out', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('UDP6_IN', 'udp6_in', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('UDP6_OUT', 'udp6_out', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('ETH_DEVICE', 'eth_device', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
CSFData.bind_property('ETH6_DEVICE', 'eth6_device', path=lambda x: x.get(None), getter=quote_getter, setter=quote_setter)
