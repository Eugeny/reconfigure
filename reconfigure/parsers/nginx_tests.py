from reconfigure.parsers import *
from reconfigure.nodes import *
import unittest


class NginxParserTest (unittest.TestCase):
    def test_parse_stringify(self):
        content = """
            p1 asd;
            
            sec {
                s1p1 asd;
                s1p2 wqe;

                sec2 {
                    s2p1 qwe;
                }
            }
        """

        parser = NginxParser()
        tree = parser.parse(content)
        newcontent = parser.stringify(tree)
        self.assertTrue(newcontent.split() == content.split())

    def test_raise(self):
        self.assertRaises(Exception, NginxParser().parse, 'sec { } end')
