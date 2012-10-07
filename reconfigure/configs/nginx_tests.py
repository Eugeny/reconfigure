#coding: utf8
import unittest
from reconfigure.includers import NginxIncluder
from reconfigure.configs import NginxConfig


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
        # TODO
