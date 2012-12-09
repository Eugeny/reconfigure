import unittest

from reconfigure.configs import GroupConfig
from reconfigure.configs.base_tests import BaseConfigTest


class GroupConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """sys:x:3:
adm:x:4:eugeny
"""
    }
    result = {
        'groups': [
            {
                'name': 'sys',
                'password': 'x',
                'gid': '3',
                'users': '',
            },
            {
                'name': 'adm',
                'password': 'x',
                'gid': '4',
                'users': 'eugeny',
            },
        ]
    }
    config = GroupConfig


if __name__ == '__main__':
    unittest.main()
