from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class IPTablesData (BoundData):
    pass


class TableData (BoundData):
    def template(self):
        return Node('custom')


class ChainData (BoundData):
    def template(self):
        return Node('CUSTOM',
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

    @property
    def summary(self):
        return ' '.join(
            (('-' if len(x.name) == 1 else '--') + x.name + ' ' +
            ' '.join(a.value for a in x.arguments))
            for x in self.options
        )


class OptionData (BoundData):
    templates = {
        'source': Node('option',
            Node('argument', PropertyNode('value', '127.0.0.1')),
            PropertyNode('name', 'source')
        ),
    }

    @staticmethod
    def create(template_id):
        return OptionData(OptionData.templates[template_id])

    @staticmethod
    def create_destination():
        return OptionData(Node('option',
            Node('argument', PropertyNode('value', 'ACCEPT')),
            PropertyNode('name', 'j')
        ))


class ArgumentData (BoundData):
    pass


IPTablesData.bind_collection('tables', item_class=TableData)
TableData.bind_collection('chains', item_class=ChainData)
TableData.bind_name('name')
ChainData.bind_property('default', 'default')
ChainData.bind_collection('rules', selector=lambda x: x.name == 'append', item_class=RuleData)
ChainData.bind_name('name')
RuleData.bind_collection('options', item_class=OptionData)
OptionData.bind_property('name', 'name')
OptionData.bind_collection('arguments', selector=lambda x: x.name == 'argument', item_class=ArgumentData)
ArgumentData.bind_property('value', 'value')
