from reconfigure.nodes import RootNode, Node, PropertyNode
from reconfigure.parsers import BaseParser


class CrontabParser(BaseParser):

    def __init__(self, remove_comments=False):
        self.remove_comments = remove_comments

    def parse(self, content):
        root = RootNode()
        lines = [l.strip() for l in content.splitlines() if l]
        comment = None
        for line in lines:
            if line.startswith('#'):
                comment = '\n'.join([comment, line]) if comment else line[1:]
                continue
            elif line.startswith('@'):
                special, command = line.split(' ', 1)
                node = Node('special_task', comment=comment)
                node.append(PropertyNode('special', special))
                node.append(PropertyNode('command', command))

            else:
                split_line = line.split(' ', 5)
                if len(split_line) <= 3 and '=' in line:
                    name, value = [n.strip() for n in line.split('=')]
                    if not name:
                        continue
                    node = Node('env_setting', comment=comment)
                    node.append(PropertyNode('name', name))
                    node.append(PropertyNode('value', value))
                elif len(split_line) == 6:
                    node = Node('normal_task', comment=comment)
                    node.append(PropertyNode('minute', split_line[0]))
                    node.append(PropertyNode('hour', split_line[1]))
                    node.append(PropertyNode('day_of_month', split_line[2]))
                    node.append(PropertyNode('month', split_line[3]))
                    node.append(PropertyNode('day_of_week', split_line[4]))
                    node.append(PropertyNode('command', split_line[5]))
                else:
                    continue
            root.append(node)
            comment = None
        root.comment = comment
        return root

    def stringify(self, tree):
        result_lines = []
        stringify_func = {
            'special_task': self.stringify_special_task,
            'env_setting': self.stringify_env_setting,
            'normal_task': self.stringify_normal_task,
        }
        for node in tree:
            if isinstance(node, Node):
                string_line = stringify_func.get(node.name, lambda x: '')(node)
                if node.comment:
                    result_lines.append('#' + node.comment)
                result_lines.append(string_line)
        return '\n'.join([line for line in result_lines if line])

    def stringify_special_task(self, node):
        special_node = node.get('special')
        command_node = node.get('command')
        if isinstance(special_node, PropertyNode) and isinstance(command_node, PropertyNode):
            return ' '.join([special_node.value, command_node.value])
        return ''

    def stringify_env_setting(self, node):
        name = node.get('name')
        value = node.get('value')
        if isinstance(name, PropertyNode) and isinstance(value, PropertyNode):
                return ' = '.join([name.value, value.value])
        return ''

    def stringify_normal_task(self, node):
        if all([isinstance(child, PropertyNode) for child in node.children]):
            values_list = [str(pr_node.value).strip() for pr_node in node.children if pr_node.value]
            if len(values_list) == 6:
                return ' '.join(values_list)
        return ''
