from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class SquidData (BoundData):
    pass


class ACLData (BoundData):
    def template(self, name=None, *args):
        children = [PropertyNode('1', name)]
        index = 2
        for arg in args:
            children += [PropertyNode(str(index), arg)]
            index += 1
        return Node(
            'line',
            PropertyNode('name', 'acl'),
            Node(
                'arguments',
                *children
            )
        )

    def describe(self):
        return ' '.join(x.value for x in self.options)


class HTTPAccessData (BoundData):
    def template(self):
        return Node(
            'line',
            PropertyNode('name', 'http_access'),
            Node('arguments', PropertyNode('1', ''))
        )


class HTTPPortData (BoundData):
    def template(self):
        return Node(
            'line',
            PropertyNode('name', 'http_port'),
            Node('arguments', PropertyNode('1', '3128'))
        )


class HTTPSPortData (BoundData):
    def template(self):
        return Node(
            'line',
            PropertyNode('name', 'https_port'),
            Node('arguments', PropertyNode('1', '3128'))
        )


class ArgumentData (BoundData):
    def template(self):
        return PropertyNode('value', 'none')


def __bind_by_name(cls, prop, name, itemcls):
    cls.bind_collection(
        prop,
        selector=lambda x: x.get('name').value == name,
        item_class=itemcls
    )

__bind_by_name(SquidData, 'acl', 'acl', ACLData)
__bind_by_name(SquidData, 'http_access', 'http_access', HTTPAccessData)
__bind_by_name(SquidData, 'http_port', 'http_port', HTTPPortData)
__bind_by_name(SquidData, 'https_port', 'https_port', HTTPSPortData)


def __bind_first_arg(cls, prop):
    cls.bind_attribute('value', prop, path=lambda x: x.get('arguments').children[0])


def __bind_other_args(cls, prop, itemcls):
    cls.bind_collection(
        prop, path=lambda x: x.get('arguments'),
        selector=lambda x: x.parent.children.index(x) > 0, item_class=itemcls
    )

__bind_first_arg(ACLData, 'name')
__bind_other_args(ACLData, 'options', ArgumentData)

__bind_first_arg(HTTPAccessData, 'mode')
__bind_other_args(HTTPAccessData, 'options', ArgumentData)

__bind_first_arg(HTTPPortData, 'port')
__bind_other_args(HTTPPortData, 'options', ArgumentData)
__bind_first_arg(HTTPSPortData, 'port')
__bind_other_args(HTTPSPortData, 'options', ArgumentData)

ArgumentData.bind_attribute('value', 'value')
