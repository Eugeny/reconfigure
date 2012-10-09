#coding: utf8
from reconfigure.parsers import *
from reconfigure.nodes import *
import unittest


class FSTabParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            fs1 mp1  ext rw 1 2
            fs2 mp2 auto none 0 0
        """

        parser = FSTabParser()
        tree = parser.parse(content)
        newcontent = parser.stringify(tree)
        assert newcontent.split() == content.split()
        assert len(tree.children) == 2
        assert len(tree.children[0].children) == 6
        assert tree.children[0].children[0].value == 'fs1'
