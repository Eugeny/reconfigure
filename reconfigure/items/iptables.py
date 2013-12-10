from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class IPTablesData (BoundData):
    pass


class TableData (BoundData):
    def template(self):
        return Node('custom')


class ChainData (BoundData):
    def template(self):
        return Node(
            'CUSTOM',
            PropertyNode('default', '-'),
        )


class RuleData (BoundData):
    def template(self):
        return Node(
            'append',
            Node(
                'option',
                Node('argument', PropertyNode('value', 'ACCEPT')),
                PropertyNode('negative', False),
                PropertyNode('name', 'j'),
            )
        )

    @property
    def summary(self):
        return ' '.join((
            ('! ' if x.negative else '') +
            ('-' if len(x.name) == 1 else '--') + x.name + ' ' +
            ' '.join(a.value for a in x.arguments))
            for x in self.options
        )

    def verify(self):
        protocol_option = None
        for option in self.options:
            if option.name in ['p', 'protocol']:
                self.options.remove(option)
                self.options.insert(0, option)
                protocol_option = option
        for option in self.options:
            if 'port' in option.name:
                if not protocol_option:
                    protocol_option = OptionData.create('protocol')
                    self.options.insert(0, protocol_option)

    def get_option(self, *names):
        for name in names:
            for option in self.options:
                if option.name == name:
                    return option


class OptionData (BoundData):
    templates = {
        'protocol': ['protocol', ['tcp']],
        'match': ['match', ['multiport']],
        'source': ['source', ['127.0.0.1']],
        'mac-source': ['mac-source', ['00:00:00:00:00:00']],
        'destination': ['destination', ['127.0.0.1']],
        'in-interface': ['in-interface', ['lo']],
        'out-interface': ['out-interface', ['lo']],
        'source-port': ['source-port', ['80']],
        'source-ports': ['source-ports', ['80,443']],
        'destination-port': ['destination-port', ['80']],
        'destination-ports': ['destination-ports', ['80,443']],
        'state': ['state', ['NEW']],
        'reject-with': ['reject-with', ['icmp-net-unreachable']],
        'custom': ['name', ['value']],
    }

    @staticmethod
    def create(template_id):
        t = OptionData.templates[template_id]
        return OptionData(Node(
            'option',
            *(
                [Node('argument', PropertyNode('value', x)) for x in t[1]]
                + [PropertyNode('negative', False)]
                + [PropertyNode('name', t[0])]
            )
        ))

    @staticmethod
    def create_destination():
        return OptionData(Node(
            'option',
            Node('argument', PropertyNode('value', 'ACCEPT')),
            PropertyNode('negative', False),
            PropertyNode('name', 'j'),
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
RuleData.bind_attribute('comment', 'comment')
OptionData.bind_property('name', 'name')
OptionData.bind_property('negative', 'negative')
OptionData.bind_collection('arguments', selector=lambda x: x.name == 'argument', item_class=ArgumentData)
ArgumentData.bind_property('value', 'value')
