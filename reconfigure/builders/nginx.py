from auto import AutoBaseBuilder


class NginxBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            http=node.children().pick(lambda x: x.name == 'http').build(NginxHTTP)[0],
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.http)


class NginxHTTP (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            servers=node.children().pick(name='server').build(NginxHTTPServer)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.servers)


class NginxHTTPServer (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            server_names=node.children().pick(name='server_name').each(lambda i, e: e.value),
            root=node.children().pick(name='root').first(lambda x: x.value),
            locations=node.children().pick(lambda x: x.name.startswith('location')).build(NginxHTTPServerLocation)
        )

    def _unbuild(self, obj, node):
        node \
            .set_all('server_name', obj.server_names) \
            .set('root', obj.root, condition=obj.root) \
            .append_unbuilt(obj.locations)


class NginxHTTPServerLocation (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            pattern=node.node.name.split(' ', 1)[1],
            root=node.children().pick(name='root').first(lambda x: x.value),
        )

    def _unbuild(self, obj, node):
        node.name('location %s' % obj.pattern) \
            .set('root', obj.root, condition=obj.root)
