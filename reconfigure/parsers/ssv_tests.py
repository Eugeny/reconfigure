from reconfigure.parsers.base_tests import BaseParserTest
from reconfigure.parsers import SSVParser
from reconfigure.nodes import *
import unittest


class SSVParserTest (BaseParserTest, unittest.TestCase):
    parser = SSVParser()
    source = """# line1
# long comment
a\tbc
efgh # line2
"""
    parsed = RootNode(None,
        Node('line',
            Node('token', PropertyNode('value',  'a')),
            Node('token', PropertyNode('value',  'bc')),
            comment='line1\nlong comment',
        ),
        Node('line',
            Node('token', PropertyNode('value',  'efgh')),
            comment='line2',
        ),
    )
