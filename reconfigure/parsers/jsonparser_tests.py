from reconfigure.parsers.base_tests import BaseParserTest
from reconfigure.parsers import JsonParser
from reconfigure.nodes import *
import unittest


class JsonParserTest (BaseParserTest, unittest.TestCase):
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
