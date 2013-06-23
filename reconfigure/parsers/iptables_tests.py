from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import IPTablesParser
from reconfigure.nodes import *


class IPTablesParserTest (BaseParserTest):
    parser = IPTablesParser()
    source = """*filter
:INPUT ACCEPT [0:0] 
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT ! -s 202.54.1.2/32 -j DROP # test
-A INPUT -m state --state NEW,ESTABLISHED -j ACCEPT
COMMIT
"""
    parsed = RootNode(None,
        Node('filter',
            Node('INPUT',
                PropertyNode('default', 'ACCEPT'),
                Node('append',
                    Node('option',
                        Node('argument', PropertyNode('value', '202.54.1.2/32')),
                        PropertyNode('negative', True),
                        PropertyNode('name', 's')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'DROP')),
                        PropertyNode('negative', False),
                        PropertyNode('name', 'j')
                    ),
                    comment='test'
                ),
                Node('append',
                    Node('option',
                        Node('argument', PropertyNode('value', 'state')),
                        PropertyNode('negative', False),
                        PropertyNode('name', 'm')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'NEW,ESTABLISHED')),
                        PropertyNode('negative', False),
                        PropertyNode('name', 'state')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'ACCEPT')),
                        PropertyNode('negative', False),
                        PropertyNode('name', 'j')
                    ),
                ),
            ),
            Node('FORWARD',
                PropertyNode('default', 'DROP'),
            ),
            Node('OUTPUT',
                PropertyNode('default', 'ACCEPT'),
            ),
        )
    )


del BaseParserTest
