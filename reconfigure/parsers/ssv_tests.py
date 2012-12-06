from reconfigure.parsers import *
from reconfigure.nodes import *
import unittest


class SSVParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            # line1
            # long comment
            a bc d
            efgh #line2
        """

        parser = SSVParser()
        tree = parser.parse(content)
        print tree
        newcontent = parser.stringify(tree)
        print newcontent

