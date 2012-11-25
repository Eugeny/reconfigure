from auto import AutoBaseBuilder


class ResolvBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            items=node.children().pickall().build(ItemBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.items)


class ItemBuilder (AutoBaseBuilder):
    @staticmethod
    def empty():
        return ItemBuilder.object(
            name='nameserver',
            value='127.0.0.1'
        )

    def _build(self, node):
        nodes = node.children().pickall()
        return self.object(
            name=nodes.nth(0).get('value').value,
            value=' '.join(nodes.slice(1).each(lambda i, e: e.get('value').value)),
        )

    def _unbuild(self, obj, node):
        node.make_child('token').set('value', obj.name)
        node.make_child('token').set('value', obj.value)
