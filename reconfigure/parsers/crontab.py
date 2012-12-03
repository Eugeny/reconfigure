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
                name, value = line.split(' ', 1)
                special_node = Node('special')
                special_node.append(PropertyNode(name, value))
                root.append(special_node)
            else:
                splitted = line.split(' ', 5)
                if len(splitted) <= 3 and '=' in line:
                    name, value = [n.strip() for n in line.split('=')]
                    if not name:
                        continue
                    env_node = Node('env_setting')
                    env_node.append(PropertyNode(name, value))
                    root.append(env_node)
                elif len(splitted) < 6:
                    continue
                else:
                    task_node = Node('task')
                    task_node.append(PropertyNode('minute', splitted[0]))
                    task_node.append(PropertyNode('hour', splitted[1]))
                    task_node.append(PropertyNode('day_of_month', splitted[2]))
                    task_node.append(PropertyNode('month', splitted[3]))
                    task_node.append(PropertyNode('day_of_week', splitted[4]))
                    task_node.append(PropertyNode('command', splitted[5]))
                    root.append(task_node)
        return root







