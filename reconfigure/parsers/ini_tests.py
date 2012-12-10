from reconfigure.parsers.base_tests import BaseParserTest
from reconfigure.parsers import IniFileParser
from reconfigure.nodes import *
import unittest


class IniParserTest (BaseParserTest, unittest.TestCase):
    parser = IniFileParser(sectionless=True)
    source = """a = b

[section1] ;section comment
s1p1 = asd ;comment 2
s1p2 = 123
"""
    parsed = RootNode(None,
        Node(None,
            PropertyNode('a',  'b'),
        ),
        Node('section1',
            PropertyNode('s1p1', 'asd', comment='comment 2'),
            PropertyNode('s1p2', '123'),
            comment='section comment'
        ),
    )


if __name__ == '__main__':
    unittest.main()
