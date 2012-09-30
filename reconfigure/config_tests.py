#coding: utf8
import unittest
from reconfigure.parsers import *
from reconfigure.includers import *
from reconfigure.nodes import *
from reconfigure.config import Reconfig
from reconfigure.ext.nginx import NginxConfig


class ConfigTest (unittest.TestCase):
    def test_config(self):
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
        includer = NginxIncluder(content_map={'test': content2})

        config = Reconfig(parser=parser, includer=includer, content=content)
        config.load()

        self.assertTrue(len(config.tree.children[0].children) == 3)


class NginxConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            p1 1;
            include test;
        """
        content2 = """
            http {
                p2 2;

                location ~ /.+ {
                    lol wut;
                }
            }
        """

        includer = NginxIncluder(content_map={'test': content2})
        config = NginxConfig(includer=includer, content=content)
        config.load()
        for k,v in config.save().iteritems():
            print '\n', k, '\n', v




if __name__ == '__main__':
    unittest.main()