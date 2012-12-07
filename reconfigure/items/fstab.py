from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class FSTabData (BoundData):
    pass


class FilesystemData (BoundData):
    fields = ['device', 'mountpoint', 'type', 'options', 'freq', 'passno']

    def template(self):
        return Node('line', children=[
            Node('token', children=[PropertyNode('value', 'none')]),
            Node('token', children=[PropertyNode('value', 'none')]),
            Node('token', children=[PropertyNode('value', 'auto')]),
            Node('token', children=[PropertyNode('value', 'none')]),
            Node('token', children=[PropertyNode('value', '0')]),
            Node('token', children=[PropertyNode('value', '0')]),
        ])

FSTabData.bind_collection('filesystems', item_class=FilesystemData)
for i in range(0, len(FilesystemData.fields)):
    object = lambda i: lambda x: x.children[i]
    FilesystemData.bind_property('value', FilesystemData.fields[i], object=object(i))
