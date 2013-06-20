from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class ExportsData (BoundData):
    pass


class ExportData (BoundData):
    def template(self):
        return Node(
            '/',
            Node('clients')
        )


class ClientData (BoundData):
    def template(self):
        return Node(
            'localhost',
            PropertyNode('options', '')
        )


ExportsData.bind_collection('exports', item_class=ExportData)
ExportData.bind_name('name')
ExportData.bind_attribute('comment', 'comment', default='')
ExportData.bind_collection('clients', path=lambda x: x['clients'], item_class=ClientData)
ClientData.bind_name('name')
ClientData.bind_property('options', 'options')
