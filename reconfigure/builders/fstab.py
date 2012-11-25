from auto import AutoBaseBuilder


class FSTabBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            filesystems=node.children().pickall().build(FilesystemBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.filesystems)


class FilesystemBuilder (AutoBaseBuilder):
    fields = ['device', 'mountpoint', 'type', 'options', 'freq', 'passno']

    @staticmethod
    def empty():
        return FilesystemBuilder.object(
            **dict(
                (f, 'none') for f in FilesystemBuilder.fields
            )
        )

    def _build(self, node):
        return self.object(
            **dict(
                node.children().pickall().each(lambda i, n: (FilesystemBuilder.fields[i], n.get('value').value))
            )
        )

    def _unbuild(self, obj, node):
        for f in FilesystemBuilder.fields:
            node.make_child('token').set('value', getattr(obj, f))
