#coding: utf8
import unittest
from reconfigure.configs import HostsConfig


class HostsConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            a1 h1 a2 a3 a4
            a5 h2
            a6 h3 a7
        """
        config = HostsConfig(content=content)
        config.load()
        newcontent = config.save()[None]
        self.assertTrue(newcontent.split() == content.split())


if __name__ == '__main__':
    unittest.main()
