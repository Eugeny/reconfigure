from auto import AutoBaseBuilder


class SupervisorBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            programs=node.children().pick(lambda e: e.name.startswith('program:')).build(ProgramBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.programs)


class ProgramBuilder (AutoBaseBuilder):
    fields = ['command', 'autostart', 'autorestart', 'startsecs', 'startretries', \
        'user', 'directory', 'umask', 'environment']

    @staticmethod
    def empty():
        return ProgramBuilder.object(
            **dict(
                (f, '') for f in ProgramBuilder.fields
            )
        )

    def _build(self, node):
        return self.object(
            name=node.name().split(':')[1],
            **dict(
                (f, node.get(f).value if node.has(f) else '')
                for f in ProgramBuilder.fields
            )
        )

    def _unbuild(self, obj, node):
        node.name('program:%s' % obj.name)
        for f in ProgramBuilder.fields:
            v = getattr(obj, f)
            if v != '':
                node.set(f, v)
