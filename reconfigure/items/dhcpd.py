from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class DHCPDData (BoundData):
    pass


class SubnetData (BoundData):
    def template(self):
        return Node(
            'subnet',
            parameter='192.168.0.0 netmask 255.255.255.0',
        )


class RangeData (BoundData):
    def template(self):
        return PropertyNode('range', '192.168.0.1 192.168.0.100')


class OptionData (BoundData):
    def template(self):
        return PropertyNode('option', '')


DHCPDData.bind_collection('subnets', selector=lambda x: x.name == 'subnet', item_class=SubnetData)
SubnetData.bind_attribute('parameter', 'name')
SubnetData.bind_collection('subnets', selector=lambda x: x.name == 'subnet', item_class=SubnetData)
SubnetData.bind_collection('ranges', selector=lambda x: x.name == 'range', item_class=RangeData)
RangeData.bind_attribute('value', 'range')
OptionData.bind_attribute('value', 'value')

for x in [DHCPDData, SubnetData]:
    x.bind_collection('options', selector=lambda x: x.name == 'option', item_class=OptionData)
