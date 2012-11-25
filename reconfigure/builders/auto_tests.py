#coding: utf8
from reconfigure.builders import *
from reconfigure.parsers import *
import unittest


class AutoBuilderTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            p1 asd;

            http {
                s1p1 asd;
                s1p2 wqe;

                server {
                    s2p1 qwe;
                }
            }
        """

        parser = NginxParser()
        tree = parser.parse(content)
        #print tree
        b = NginxBuilder()
        #print repr(b.build(tree))
