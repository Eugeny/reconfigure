#coding: utf8
import unittest
from reconfigure.configs import GroupConfig


class GroupConfigTest (unittest.TestCase):
    def test_config(self):
        content = """root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:eugeny
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:"""
        config = GroupConfig(content=content)
        config.load()
        newcontent = config.save()[None]
        self.assertTrue(newcontent.split() == content.split())


if __name__ == '__main__':
    unittest.main()
