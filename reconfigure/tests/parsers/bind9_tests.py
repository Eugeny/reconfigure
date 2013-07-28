from reconfigure.tests.parsers.base_test import BaseParserTest
from reconfigure.parsers import BIND9Parser
from reconfigure.nodes import *


class BIND9ParserTest (BaseParserTest):
    parser = BIND9Parser()
    source = """p1 asd;

sec {
    s1p1 asd;
    /*s1p2 wqe;*/

    sec2 test {
        s2p1 qwe;
    };
};
"""

    @property
    def stringified(self):
        return """
  p1 asd;

sec {
    s1p1 asd;

    # s1p2 wqe;
    sec2 test {
        s2p1 qwe;
    };
};
"""

    parsed = RootNode(
        None,
        PropertyNode('p1', 'asd'),
        Node(
            'sec',
            PropertyNode('s1p1', 'asd'),
            Node(
                'sec2',
                PropertyNode('s2p1', 'qwe'),
                parameter='test',
                comment='s1p2 wqe;',
            ),
            parameter=None,
        )
    )


del BaseParserTest
