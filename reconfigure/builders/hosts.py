from auto import AutoBaseBuilder


class HostsBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            hosts=node.children().pickall().build(HostBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.hosts)


class HostBuilder (AutoBaseBuilder):
    @staticmethod
    def empty():
        return HostBuilder.object(
            name='localhost',
            address='127.0.0.1',
            aliases=[]
        )

    def _build(self, node):
        nodes = node.children().pickall()
        return self.object(
            address=nodes.nth(0).get('value').value,
            name=nodes.nth(1).get('value').value,
            aliases=nodes.slice(2).build(AliasBuilder)
        )

    def _unbuild(self, obj, node):
        node.make_child('token').set('value', obj.address)
        node.make_child('token').set('value', obj.name)
        node.append_unbuilt(obj.aliases)


class AliasBuilder (AutoBaseBuilder):
    @staticmethod
    def empty():
        return AliasBuilder.object(
            name='localhost'
        )

    def _build(self, node):
        return AliasBuilder.object(
            name=node.get('value').value
        )

    def _unbuild(self, obj, node):
        node.set('value', obj.name)
