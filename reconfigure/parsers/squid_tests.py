from reconfigure.parsers.base_tests import BaseParserTest
from reconfigure.parsers import SquidParser
from reconfigure.nodes import *
import unittest


class SquidParserTest (BaseParserTest, unittest.TestCase):
    parser = SquidParser()
    source = """# line1
# long comment
a\tbc
efgh # line2
"""
    parsed = RootNode(None,
        Node('line',
            PropertyNode('name',  'a'),
            PropertyNode('argument1',  'bc'),
            comment='line1\nlong comment',
        ),
        Node('line',
            PropertyNode('name',  'efgh'),
            comment='line2',
        ),
    )
