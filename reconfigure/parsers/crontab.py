from reconfigure.nodes import RootNode, Node, PropertyNode
from reconfigure.parsers import BaseParser

class CrontabParser(BaseParser):

    def __init__(self, remove_comments=False):
        self.remove_comments = remove_comments

    def parse(self, content):
        root = RootNode()
        lines = [l.strip() for l in content.splitlines()]
        for line in lines:
            if line.startswith('#'):
                root.append(PropertyNode('comment', line[1:]))
            elif line.startswith('@'):
                special, command = line.split(' ', 1)
                special_node = Node('special_task')
                special_node.append(PropertyNode('special', special))
                special_node.append(PropertyNode('command', command))
                root.append(special_node)
            else:
                split_line = line.split(' ', 5)
                if len(split_line) <= 3 and '=' in line:
                    name, value = [n.strip() for n in line.split('=')]
                    if not name:
                        continue
                    env_node = Node('env_setting')
                    env_node.append(PropertyNode(name, value))
                    root.append(env_node)
                elif len(split_line) == 6:
                    task_node = Node('normal_task')
                    task_node.append(PropertyNode('minute', split_line[0]))
                    task_node.append(PropertyNode('hour', split_line[1]))
                    task_node.append(PropertyNode('day_of_month', split_line[2]))
                    task_node.append(PropertyNode('month', split_line[3]))
                    task_node.append(PropertyNode('day_of_week', split_line[4]))
                    task_node.append(PropertyNode('command', split_line[5]))
                    root.append(task_node)
                else:
                    continue
        return root




