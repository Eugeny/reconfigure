from reconfigure.tests.parsers.base_test import BaseParserTest
from reconfigure.parsers import NSDParser
from reconfigure.nodes import *


class BIND9ParserTest (BaseParserTest):
    parser = NSDParser()
    source = """# asd
    server:
        ip4-only: no
key:
        name: "mskey"
"""

    parsed = RootNode(
        None,
        Node(
            'server',
            PropertyNode('ip4-only', 'no'),
            comment='asd'
        ),
        Node(
            'key',
            PropertyNode('name', '"mskey"'),
        )
    )


del BaseParserTest
