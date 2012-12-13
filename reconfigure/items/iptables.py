from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class IPTablesData (BoundData):
    pass


class TableData (BoundData):
    def template(self):
        return Node('custom')


class ChainData (BoundData):
    def template(self):
        return Node('custom',
            PropertyNode('default', '-'),
        )


class RuleData (BoundData):
    def template(self):
        return Node('append',
            Node('option',
                Node('argument', PropertyNode('value', 'ACCEPT')),
                PropertyNode('name', 'j')
            )
        )


class OptionData (BoundData):
    pass


class ArgumentData (BoundData):
    pass


IPTablesData.bind_collection('tables', item_class=TableData)
TableData.bind_collection('chains', item_class=ChainData)
ChainData.bind_property('default', 'default')
ChainData.bind_collection('rules', selector=lambda x: x.name == 'append', item_class=RuleData)
RuleData.bind_collection('options', item_class=OptionData)
OptionData.bind_property('name', 'name')
OptionData.bind_collection('arguments', selector=lambda x: x.name == 'argument', item_class=ArgumentData)
ArgumentData.bind_property('value', 'value')
