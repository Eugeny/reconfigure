from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import SSVParser
from reconfigure.nodes import *


class SSVParserTest (BaseParserTest):
    parser = SSVParser(continuation='\\')
    source = """# line1
# long comment
a\tbc\\
\tdef
efgh # line2
"""
    parsed = RootNode(
        None,
        Node(
            'line',
            Node('token', PropertyNode('value',  'a')),
            Node('token', PropertyNode('value',  'bc')),
            Node('token', PropertyNode('value',  'def')),
            comment='line1\nlong comment',
        ),
        Node(
            'line',
            Node('token', PropertyNode('value',  'efgh')),
            comment='line2',
        ),
    )

    @property
    def stringified(self):
        return """# line1
# long comment
a\tbc\tdef
efgh # line2
"""


del BaseParserTest
