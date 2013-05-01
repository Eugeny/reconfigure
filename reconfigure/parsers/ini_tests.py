from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import IniFileParser
from reconfigure.nodes import *


class IniParserTest (BaseParserTest):
    parser = IniFileParser(sectionless=True)
    source = """a=b

[section1] ;section comment
s1p1=asd ;comment 2
s1p2=123
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


del BaseParserTest
