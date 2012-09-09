#coding: utf8
import unittest
from reconfigure.parsers import IniFileParser
from reconfigure.nodes import *


class IniParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            [section1]
            s1p1 = asd
            s1p2 = 123
            s1p3 = asd=543

            [section2]
            юни = код
        """

        parser = IniFileParser()
        tree = parser.parse(content)
        newcontent = parser.stringify(tree)
        self.assertTrue(newcontent.split() == content.split())

    def test_raise(self):
        tree = RootNode()
        tree.children.append(Node(name='test'))
        tree.children[0].children.append(Node())
        parser = IniFileParser()

        self.assertRaises(TypeError, parser.stringify, tree)
        


if __name__ == '__main__':
    unittest.main()