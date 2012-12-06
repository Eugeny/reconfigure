
from reconfigure.parsers import CrontabParser
from reconfigure.nodes import RootNode, Node, PropertyNode
import unittest

class CrontabParserTest (unittest.TestCase):
    def setUp(self):
        self.parser = CrontabParser()
        self.content = '\n'.join(['#comment line', 
                            '* * * * * date',
                            '@reboot ls -al',
                            '1 * 0 1 2 date -s',
                            'NAME = TEST',
                            '* * * * dd',   #Wrong line
                            ' = FAIL',      #wrong line
                            ])
        self.fixed_content = '\n'.join(['#comment line', 
                            '* * * * * date',
                            '@reboot ls -al',
                            '1 * 0 1 2 date -s',
                            'NAME = TEST',
                            ])
        self.tree = RootNode(None, 
            children=[
                Node('comment',
                    children=[
                        PropertyNode('text', 'comment line'),
                    ]
                ),
                Node('normal_task', 
                    children=[
                        PropertyNode('minute', '*'),
                        PropertyNode('hour', '*'),
                        PropertyNode('day_of_month', '*'),
                        PropertyNode('month', '*'),
                        PropertyNode('day_of_week', '*'),
                        PropertyNode('command', 'date'),
                    ]
                ),
                Node('special_task',
                    children=[
                        PropertyNode('special', '@reboot'),
                        PropertyNode('command', 'ls -al'),
                    ]
                ),
                Node('normal_task', 
                    children=[
                        PropertyNode('minute', '1'),
                        PropertyNode('hour', '*'),
                        PropertyNode('day_of_month', '0'),
                        PropertyNode('month', '1'),
                        PropertyNode('day_of_week', '2'),
                        PropertyNode('command', 'date -s'),
                    ]
                ),
                Node('env_setting',
                    children=[
                        PropertyNode('name', 'NAME'),
                        PropertyNode('value', 'TEST'),
                    ]
                ),
            ]
        )
        

    def test_parse(self):
        parsed_tree = self.parser.parse(self.content)
        self.assertEqual(str(self.tree), str(parsed_tree))

    def test_stringify(self):
        content = self.parser.stringify(self.tree)
        self.assertEqual(self.fixed_content, content)

    def test_parse_stringify(self):
        parsed_tree = self.parser.parse(self.content)
        self.assertEqual(self.fixed_content, self.parser.stringify(parsed_tree))

if __name__ == '__main__':
    unittest.main()