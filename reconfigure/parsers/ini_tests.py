#coding: utf8
from reconfigure.parsers import *
from reconfigure.nodes import *
import unittest


class IniParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """[section1]
s1p1 = asd
s1p2 = 123
s1p3 = asd=543

[section2]
юни = код"""

        parser = IniFileParser()
        tree = parser.parse(content)
        newcontent = parser.stringify(tree)
        self.assertEqual(newcontent.split(), content.split())

    def test_sectionless_parse_stringify(self):
        content = """KEYMAP = us
FONT = lat9w-16
FONT_MAP = 8859-1_to_uni"""

        parser = IniFileParser(True)
        tree = parser.parse(content)
        self.assertTrue(tree.get(None) is not None)
        newcontent = parser.stringify(tree)
        self.assertEqual(newcontent.split('\n'), content.split('\n'))

    def test_raise(self):
        tree = RootNode()
        tree.children.append(Node(name='test'))
        tree.children[0].children.append(Node())
        parser = IniFileParser()

        self.assertRaises(TypeError, parser.stringify, tree)
