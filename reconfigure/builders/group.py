from auto import AutoBaseBuilder


class GroupBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            groups=node.children().pickall().build(GroupEntryBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.groups)


class GroupEntryBuilder (AutoBaseBuilder):
    fields = ['name', 'password', 'gid', 'users']

    def _build(self, node):
        return self.object(
            **dict(
                node.children().pickall().each(lambda i, n: (GroupEntryBuilder.fields[i], n.get('value').value))
            )
        )

    def _unbuild(self, obj, node):
        for f in GroupEntryBuilder.fields:
            node.make_child('token').set('value', getattr(obj, f))
