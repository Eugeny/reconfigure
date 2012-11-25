#coding: utf8
import unittest
from reconfigure.configs import FSTabConfig


class FSTabConfigTest (unittest.TestCase):
    def test_config(self):
        content = """
            fs1 mp1  ext rw 1 2
            fs2 mp2 auto none 0 0
        """
        config = FSTabConfig(content=content)
        config.load()
        newcontent = config.save()[None]
        self.assertTrue(newcontent.split() == content.split())


if __name__ == '__main__':
    unittest.main()
