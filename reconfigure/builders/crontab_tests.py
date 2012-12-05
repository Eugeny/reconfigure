
from reconfigure.builders import CrontabBuilder
from reconfigure.builders.auto import Data
from reconfigure.nodes import RootNode, Node, PropertyNode
import unittest

class CrontabBuilderTest (unittest.TestCase):
    def setUp(self):
        self.builder = CrontabBuilder()
        self.tree = RootNode(None, 
            [
                PropertyNode('comment', 'comment line'),
                Node('normal_task', 
                    [
                        PropertyNode('minute', '*'),
                        PropertyNode('hour', '*'),
                        PropertyNode('day_of_month', '*'),
                        PropertyNode('month', '*'),
                        PropertyNode('day_of_week', '*'),
                        PropertyNode('command', 'date'),
                    ]
                ),
                Node('special_task',
                    [
                        PropertyNode('special', '@reboot'),
                        PropertyNode('command', 'ls -al'),
                    ]
                ),
                Node('normal_task', 
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
                        PropertyNode('name', 'NAME'),
                        PropertyNode('value', 'TEST'),
                    ]
                ),
            ]
        )
        self.data = Data(lines=[
            Data(**{'line_type': 'comment', 'comment': 'comment line'}),
            Data(**{'line_type': 'normal_task',
                    'command': 'date',
                    'minute': '*',
                    'hour': '*',
                    'day_of_month': '*',
                    'month': '*',
                    'day_of_week': '*',
                    
                    }),
            Data(**{'line_type': 'special_task',
                    'special': '@reboot',
                    'command': 'ls -al'
                    }),
            Data(**{'line_type': 'normal_task',
                    'command': 'date -s',
                    'minute': '1',
                    'hour': '*',
                    'day_of_month': '0',
                    'month': '1',
                    'day_of_week': '2',
                    
                    }),
            Data(**{'line_type': 'env_setting',
                    'name': 'NAME',
                    'value': 'TEST',
                    })
            ])
        self.maxDiff = None
        

    def test_build(self):
        built_data = self.builder.build(self.tree)
        self.assertEqual(str(built_data.to_json()), str(self.data.to_json()))

    

if __name__ == '__main__':
    unittest.main()