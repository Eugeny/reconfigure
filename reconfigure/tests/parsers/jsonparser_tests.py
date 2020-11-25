import json
from reconfigure.tests.parsers.base_test import BaseParserTest
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

    def test_stringify(self):
        unparsed = self.parser.stringify(self.__class__.parsed)
        a, b = self.stringified, unparsed
        if json.loads(a) != json.loads(b):
            print('SOURCE: %s\n\nGENERATED: %s' % (a, b))
            self.assertEqual(a, b)

del BaseParserTest
