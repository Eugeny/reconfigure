from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import SquidParser
from reconfigure.nodes import *


class SquidParserTest (BaseParserTest):
    parser = SquidParser()
    source = """# line1
# long comment
a\tbc
efgh # line2
"""
    parsed = RootNode(None,
        Node('line',
            PropertyNode('name',  'a'),
            Node('arguments',
                PropertyNode('1',  'bc'),
            ),
            comment='line1\nlong comment',
        ),
        Node('line',
            PropertyNode('name',  'efgh'),
            Node('arguments'),
            comment='line2',
        ),
    )


del BaseParserTest
