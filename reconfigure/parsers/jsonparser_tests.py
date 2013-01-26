from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import JsonParser
from reconfigure.nodes import *


class JsonParserTest (BaseParserTest):
    parser = JsonParser()
    source = """{
    "p2": 123,
    "s1": {
        "s1p1": "qwerty"
    }
}
"""

    parsed = RootNode(None,
        PropertyNode('p2',  123),
        Node('s1',
            PropertyNode('s1p1',  'qwerty'),
        ),
    )


del BaseParserTest
