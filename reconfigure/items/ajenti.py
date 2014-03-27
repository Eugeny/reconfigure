import json

from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData, BoundDictionary


class AjentiData (BoundData):
    pass


class HttpData (BoundData):
    pass


class SSLData (BoundData):
    pass


class UserData (BoundData):
    def template(self):
        return Node(
            'unnamed',
            PropertyNode('configs', {}),
            PropertyNode('password', ''),
            PropertyNode('permissions', []),
        )


class ConfigData (BoundData):
    def template(self):
        return PropertyNode('', '{}')


AjentiData.bind_property('authentication', 'authentication')
AjentiData.bind_property('language', 'language')
AjentiData.bind_property('installation_id', 'installation_id')
AjentiData.bind_property('enable_feedback', 'enable_feedback')
AjentiData.bind_child('http_binding', lambda x: x.get('bind'), item_class=HttpData)
AjentiData.bind_child('ssl', lambda x: x.get('ssl'), item_class=SSLData)
AjentiData.bind_collection('users', path=lambda x: x.get('users'), item_class=UserData, collection_class=BoundDictionary, key=lambda x: x.name)


HttpData.bind_property('host', 'host')
HttpData.bind_property('port', 'port')

SSLData.bind_property('certificate_path', 'certificate_path')
SSLData.bind_property('enable', 'enable')

ConfigData.bind_name('name')

UserData.bind_name('name')
UserData.bind_property('email', 'email')
UserData.bind_property('password', 'password')
UserData.bind_property('permissions', 'permissions')
UserData.bind_collection('configs', lambda x: x.get('configs'), item_class=ConfigData, collection_class=BoundDictionary, key=lambda x: x.name)

ConfigData.bind_attribute('value', 'data', getter=json.loads, setter=json.dumps)
