from reconfigure.nodes import *


class Server (object):
    def __init__(self):
        self.names = []
        self.ports = []
        self.source = None

    def _build(self, tree):
        self.source = tree
        self.names = [n.value for n in tree.get_all('server_name')]
        self.ports = [n.value for n in tree.get_all('listen')]
        self.simple_name = (self.names[0] if self.names else '*') + ':' + (self.ports[0] if self.ports else '80')
        return self

    def _unbuild(self):
        self.source.replace('server_name', [PropertyNode('server_name', n) for n in self.names])
        self.source.replace('listen', [PropertyNode('listen', n) for n in self.ports])
        return self.source


class HttpParams (object):
    def _build(self, tree):
        self.source = tree
        self.servers = []
        for node in tree.children:
            if node.name == 'server':
                self.servers.append(Server()._build(node))
        return self

    def _unbuild(self):
        self.source.children = [c for c in self.source.children if c.name != 'server']
        for s in self.servers:
            self.source.children.append(s._build())
        return self.source


class Config (object):
    def __init__(self):
        pass

    def _build(self, tree):
        self.source = tree
        self.http = HttpParams()._build(tree.get('http'))
        return self

    def _unbuild(self):
        self.source.replace('http', self.http._build())
        return self.source
