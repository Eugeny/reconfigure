from auto import AutoBaseBuilder


class PasswdBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            users=node.children().pickall().build(UserBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.users)


class UserBuilder (AutoBaseBuilder):
    fields = ['name', 'password', 'uid', 'gid', 'comment', 'home', 'shell']

    def _build(self, node):
        return self.object(
            **dict(
                node.children().pickall().each(lambda i, n: (UserBuilder.fields[i], n.get('value').value))
            )
        )

    def _unbuild(self, obj, node):
        for f in UserBuilder.fields:
            node.make_child('token').set('value', getattr(obj, f))
