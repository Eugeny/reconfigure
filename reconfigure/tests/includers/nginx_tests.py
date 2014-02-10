#coding: utf8
import unittest
from reconfigure.parsers import NginxParser
from reconfigure.includers import NginxIncluder


class IncludersTest (unittest.TestCase):
    def test_compose_decompose(self):
        content = """
            sec1 {
                p1 1;
                include test;
            }
        """
        content2 = """
            sec2 {
                p2 2;
            }
        """

        parser = NginxParser()
        includer = NginxIncluder(parser=parser, content_map={'test': content2})
        tree = parser.parse(content)
        tree = includer.compose(None, tree)
        self.assertTrue(len(tree.children[0].children) == 3)

        treemap = includer.decompose(tree)
        self.assertTrue(len(treemap.keys()) == 2)
        self.assertTrue(treemap['test'].children[0].name == 'sec2')
