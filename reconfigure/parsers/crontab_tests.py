from reconfigure.parsers import CrontabParser
from reconfigure.nodes import RootNode, Node, PropertyNode
from reconfigure.parsers.base_test import BaseParserTest


class CrontabParserTest (BaseParserTest):
    parser = CrontabParser()

    source = '\n'.join(['#comment line',
                    '* * * * * date',
                    '@reboot ls -al',
                    '1 * 0 1 2 date -s',
                    'NAME = TEST',
                    ])
    parsed = RootNode(None,
            children=[
                Node('normal_task',
                    comment='comment line',
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
#    bad_source = '\n'.join(['* * * * dd',   #Wrong line
#                        ' = FAIL',      #wrong line
#    ])


del BaseParserTest
