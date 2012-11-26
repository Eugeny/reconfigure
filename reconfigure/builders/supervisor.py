from auto import AutoBaseBuilder


class SupervisorBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            programs=node.children().pick(lambda e: e.name.startswith('program:')).build(ProgramBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.programs)


class ProgramBuilder (AutoBaseBuilder):
    fields = ['command']

    @staticmethod
    def empty():
        return ProgramBuilder.object(
            **dict(
                (f, '') for f in ProgramBuilder.fields
            )
        )

    def _build(self, node):
        return self.object(
            **dict(
                (f, node.get(f).value if node.get(f) else '')
                for f in ProgramBuilder.fields
            )
        )

    def _unbuild(self, obj, node):
        for f in ProgramBuilder.fields:
            node.set(f, getattr(obj, f))
