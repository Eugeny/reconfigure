from auto import AutoBaseBuilder


class CrontabBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            lines=node.children().pickall().build(LineBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.lines)


class LineBuilder (AutoBaseBuilder):
    def _build(self, node):
        res_dict = {'line_type': node.name()}
        # if node.is_property_node():
        #     res_dict[node.name()] = node.value()
        #     return self.object(**{'line_type': node.name(), node.name(): node.value()})
        res_dict.update(dict([(n.name, n.value) for n in node.children().pickall().nodes]))
        return self.object(**res_dict)

    def _unbuild(self, obj, node):
        node.name(name=obj.line_type)
        attributes = [attr for attr in obj.__dict__ if attr != 'line_type' and
                                            not attr.startswith('_') and
                                            not callable(getattr(obj, attr))]
        for name in attributes:
            node.set(name, getattr(obj, name))
