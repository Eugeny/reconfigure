class HttpBinding (object):
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8000

    def _build(self, tree):
        self.source = tree
        self.host = tree.get('host').value
        self.port = tree.get('port').value
        return self


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


class User (object):
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def _build(self, tree):
        self.source = tree
        self.name = tree.name
        self.password = tree.get('password').value
        return self


class Config (object):
    def __init__(self):
        self.http_binding = HttpBinding()
        self.ssl = SslParams()
        self.authentication = False
        self.users = { 'root': User(name='root', password='root') }

    def _build(self, tree):
        self.source = tree
        self.authentication = tree.get('authentication').value
        self.http_binding = HttpBinding()._build(tree.get('bind'))
        self.ssl = SslParams()._build(tree.get('ssl'))
        self.users = {}
        for node in tree.get('users').children:
            self.users[node.name] = User()._build(node)
        return self
