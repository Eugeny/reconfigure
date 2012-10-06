from parser import *
import unittest


class HostsParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            a1 h1 a2 a3 a4
            a5 h2
            a6 h3 a7
        """

        parser = HostsParser()
        tree = parser.parse(content)
        newcontent = parser.stringify(tree)
        self.assertTrue(newcontent.split() == content.split())

