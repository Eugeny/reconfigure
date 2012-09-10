#coding: utf8
import unittest
from reconfigure.parsers import *
from reconfigure.includers import *
from reconfigure.nodes import *


class IncludersTest (unittest.TestCase):
    def test_combine(self):
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

        parser = NginxStyleParser()
        includer = NginxStyleIncluder(parser=parser, content_map={'test': content2})
        tree = parser.parse(content)
        tree = includer.combine('', tree)
        self.assertTrue(len(tree.children[0].children) == 3)


        #print
        #tree = parser.parse(open('/etc/nginx/nginx.conf').read())
        #print includer.combine('/etc/nginx/nginx.conf', tree)