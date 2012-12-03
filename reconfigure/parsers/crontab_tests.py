
from reconfigure.parsers import CrontabParser
from reconfigure.nodes import RootNode, Node, PropertyNode
import unittest

class CrontabParserTest (unittest.TestCase):
    def setUp(self):
        self.content = '\n'.join(['#comment line', 
                            '* * * * * date',
                            '@reboot ls -al',
                            '1 * 0 1 2 date -s',
                            'NAME = TEST',
                            '* * * * dd',   #Wrong line
                            ' = FAIL',      #wrong line
                            ])
        self.tree = RootNode(None, 
            [
                PropertyNode('comment', 'comment line'),
                Node('task', 
                    [
                        PropertyNode('minute', '*'),
                        PropertyNode('hour', '*'),
                        PropertyNode('day_of_month', '*'),
                        PropertyNode('month', '*'),
                        PropertyNode('day_of_week', '*'),
                        PropertyNode('command', 'date'),
                    ]
                ),
                Node('special',
                    [
                        PropertyNode('@reboot', 'ls -al'),
                    ]
                ),
                Node('task', 
                    [
                        PropertyNode('minute', '1'),
                        PropertyNode('hour', '*'),
                        PropertyNode('day_of_month', '0'),
                        PropertyNode('month', '1'),
                        PropertyNode('day_of_week', '2'),
                        PropertyNode('command', 'date -s'),
                    ]
                ),
                Node('env_setting',
                    [
                        PropertyNode('NAME', 'TEST'),
                    ]
                ),
            ]
        )
        

    def test_parse(self):
        parser = CrontabParser()
        parsed_tree = parser.parse(self.content)
        self.assertEqual(str(parsed_tree), str(self.tree))

if __name__ == '__main__':
    unittest.main()