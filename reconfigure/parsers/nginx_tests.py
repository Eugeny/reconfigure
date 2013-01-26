from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import NginxParser
from reconfigure.nodes import *


class NginxParserTest (BaseParserTest):
    parser = NginxParser()
    source = """p1 asd;

sec {
    s1p1 asd;
    s1p2 wqe;

    sec2 {
        s2p1 qwe;
    }
}
"""
    parsed = RootNode(None,
        PropertyNode('p1', 'asd'),
        Node('sec',
            PropertyNode('s1p1', 'asd'),
            PropertyNode('s1p2', 'wqe'),
            Node('sec2',
                PropertyNode('s2p1', 'qwe'),
            )
        )
    )


del BaseParserTest
