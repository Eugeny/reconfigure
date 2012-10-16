import json

from reconfigure.nodes import *


class HttpBinding (object):
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8000

    def _build(self, tree):
        self.source = tree
        self.host = tree.get('host').value
        self.port = tree.get('port').value
        return self

    def _unbuild(self):
        return Node(name='bind', children=[
            PropertyNode(name='host', value=self.host),
            PropertyNode(name='port', value=self.port),
        ])


class SslParams (object):
    def __init__(self):
        self.enable = False
        self.certificate_path = ''
        self.key_path = ''

    def _build(self, tree):
        self.source = tree
        self.enable = tree.get('enable').value
        self.certificate_path = tree.get('certificate_path').value
        self.key_path = tree.get('key_path').value
        return self

    def _unbuild(self):
        return Node(name='ssl', children=[
            PropertyNode(name='enable', value=self.enable),
            PropertyNode(name='certificate_path', value=self.certificate_path),
            PropertyNode(name='key_path', value=self.key_path),
        ])


class User (object):
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.configs = {}
        self.permissions = []

    def _build(self, tree):
        self.source = tree
        self.name = tree.name
        self.password = tree['password'].value
        self.permissions = tree['permissions'].value
        for node in tree['configs']:
            self.configs[node.name] = json.loads(node.value)
        return self

    def _unbuild(self):
        return Node(name=self.name, children=[
            PropertyNode(name='password', value=self.password),
            PropertyNode(name='permissions', value=self.permissions),
            Node('configs', children=[
                PropertyNode(name=k, value=json.dumps(v))
                for k, v in self.configs.iteritems()
            ])
        ])


class Config (object):
    def __init__(self):
        self.http_binding = HttpBinding()
        self.ssl = SslParams()
        self.authentication = False
        self.users = {'root': User(name='root', password='root')}

    def _build(self, tree):
        self.source = tree
        self.authentication = tree.get('authentication').value
        self.http_binding = HttpBinding()._build(tree.get('bind'))
        self.ssl = SslParams()._build(tree.get('ssl'))
        self.users = {}
        for node in tree.get('users').children:
            self.users[node.name] = User()._build(node)
        return self

    def _unbuild(self):
        return RootNode(children=[
            PropertyNode(name='authentication', value=self.authentication),
            self.http_binding._unbuild(),
            self.ssl._unbuild(),
            Node(name='users', children=[x._unbuild() for x in self.users.values()])
        ])
