
from reconfigure.builders import AutoBaseBuilder
from reconfigure.builders.crontab import CrontabBuilder, LineBuilder
from reconfigure.items.base import Data
from reconfigure.nodes import RootNode, Node, PropertyNode
import unittest

class CrontabBuilderTest (unittest.TestCase):
    def setUp(self):
        self.builder = CrontabBuilder()
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
        self.data = Data(lines=[
            Data(**{'_builder': LineBuilder(),
                    'line_type': 'comment',
                    'text': 'comment line'
                    }),
            Data(**{'_builder': LineBuilder(), 
                    'line_type': 'normal_task',
                    'command': 'date',
                    'minute': '*',
                    'hour': '*',
                    'day_of_month': '*',
                    'month': '*',
                    'day_of_week': '*',
                    
                    }),
            Data(**{'_builder': LineBuilder(), 
                    'line_type': 'special_task',
                    'special': '@reboot',
                    'command': 'ls -al'
                    }),
            Data(**{'_builder': LineBuilder(), 
                    'line_type': 'normal_task',
                    'command': 'date -s',
                    'minute': '1',
                    'hour': '*',
                    'day_of_month': '0',
                    'month': '1',
                    'day_of_week': '2',
                    
                    }),
            Data(**{'_builder': LineBuilder(), 
                    'line_type': 'env_setting',
                    'name': 'NAME',
                    'value': 'TEST',
                    })
            ],
            _builder = CrontabBuilder())
        # self.data._builder = AutoBaseBuilder
        self.maxDiff = None
        

    def test_build(self):
        built_data = self.builder.build(self.tree)
        self.assertEqual(str(built_data.to_json()), str(self.data.to_json()))

    def test_build_class(self):
        built_data = self.builder.build(self.tree)
        #self.assertTrue(isinstance(built_data, CrontabData))

    def test_unbuild(self):
        unbuilt_tree = self.builder.unbuild(self.data)
        #print(unbuilt_tree)
        #print(self.tree)
        self.assertEqual(str(unbuilt_tree), str(self.tree))

if __name__ == '__main__':
    unittest.main()