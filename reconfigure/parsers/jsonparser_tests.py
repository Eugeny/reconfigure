from reconfigure.parsers import *
from reconfigure.nodes import *
import unittest


class JsonParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            {
                "p1": "qwe",
                "p2": 123,
                "s1": {
                    "s1p1": "qwerty"
                }
            }
        """

        import json
        parser = JsonParser()
        tree = parser.parse(content)
        newcontent = json.loads(parser.stringify(tree))
        content = json.loads(content)
        self.assertTrue(newcontent == content)

