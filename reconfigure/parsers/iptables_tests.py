from reconfigure.parsers.base_tests import BaseParserTest
from reconfigure.parsers import IPTablesParser
from reconfigure.nodes import *
import unittest


class IPTablesParserTest (BaseParserTest, unittest.TestCase):
    parser = IPTablesParser()
    source = """*filter
:INPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -s 202.54.1.2/32 -j DROP
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
                        PropertyNode('name', 's')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'DROP')),
                        PropertyNode('name', 'j')
                    ),
                ),
                Node('append',
                    Node('option',
                        Node('argument', PropertyNode('value', 'state')),
                        PropertyNode('name', 'm')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'NEW,ESTABLISHED')),
                        PropertyNode('name', 'state')
                    ),
                    Node('option',
                        Node('argument', PropertyNode('value', 'ACCEPT')),
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


if __name__ == '__main__':
    unittest.main()
