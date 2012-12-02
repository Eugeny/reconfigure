#coding: utf8
import unittest
from reconfigure.includers import SupervisorIncluder
from reconfigure.configs import SupervisorConfig


class NginxConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            [unix_http_server]
            file=/var/run//supervisor.sock   ; (the path to the socket file)
            chmod=0700
            [include]
            files = test
        """
        content2 = """
            [program:test1]
            command=cat
        """

        includer = SupervisorIncluder(content_map={'test': content2})
        config = SupervisorConfig(includer=includer, content=content)
        config.load()

        # TODO
