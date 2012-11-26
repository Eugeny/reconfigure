from reconfigure.includers.auto import AutoIncluder


class SupervisorIncluder (AutoIncluder):
    def is_include(self, node):
        if node.name == 'include':
            return node.get('files').value
