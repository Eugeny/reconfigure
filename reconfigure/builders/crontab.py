from auto import AutoBaseBuilder
from reconfigure.nodes import PropertyNode


class CrontabBuilder (AutoBaseBuilder):
    def _build(self, node):
        return self.object(
            lines = node.children().pickall().build(LineBuilder)
        )

    def _unbuild(self, obj, node):
        node.append_unbuilt(obj.lines)


class LineBuilder (AutoBaseBuilder):
    def _build(self, node):
        res_dict = {'line_type': node.name()}
        if node.is_property_node():
            res_dict[node.name()] = node.value()
            return self.object(**{'line_type': node.name(), node.name(): node.value()})
        res_dict.update(dict([(n.name, n.value) for n in node.children().pickall().nodes]))
        return self.object(**res_dict)
