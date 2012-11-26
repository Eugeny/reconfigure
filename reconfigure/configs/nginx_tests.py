#coding: utf8
import unittest
from reconfigure.includers import NginxIncluder
from reconfigure.configs import NginxConfig


class NginxConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            p1 1;

            http {
                include test;
            }
        """
        content2 = """
                server {
                    root /srv/wp;
                    index index.php index.htm;

                    server_name c.d.local;
                    server_name c.d.wifi;

                    location / {
                            root /home/user/Work/dash/public/static;
                    }
                }
        """

        includer = NginxIncluder(content_map={'test': content2})
        config = NginxConfig(includer=includer, content=content)
        config.load()

        print config.tree

        #print config.save()['test']
        # TODO
