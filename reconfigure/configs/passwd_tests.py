#coding: utf8
import unittest
from reconfigure.configs import PasswdConfig


class PasswdConfigTest (unittest.TestCase):
    def test_config(self):
        content = """backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false"""
        config = PasswdConfig(content=content)
        config.load()
        newcontent = config.save()[None]
        self.assertTrue(newcontent.split() == content.split())


if __name__ == '__main__':
    unittest.main()
