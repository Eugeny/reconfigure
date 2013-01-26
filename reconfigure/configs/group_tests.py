from reconfigure.configs import GroupConfig
from reconfigure.configs.base_test import BaseConfigTest


class GroupConfigTest (BaseConfigTest):
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


del BaseConfigTest
