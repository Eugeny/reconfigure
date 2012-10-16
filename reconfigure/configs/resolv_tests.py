#coding: utf8
import unittest
from reconfigure.configs import ResolvConfig


class ResolvConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            nameserver 1
            domain 2
            search 3 5
        """
        config = ResolvConfig(content=content)
        config.load()
        self.assertTrue(config.tree.items[2].value == '3 5')
        newcontent = config.save()[None]
        self.assertTrue(newcontent.split() == content.split())


if __name__ == '__main__':
    unittest.main()
