from reconfigure.configs import PasswdConfig
from reconfigure.configs.base_test import BaseConfigTest


class PasswdConfigTest (BaseConfigTest):
    sources = {
        None: """backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
"""
    }
    result = {
        'users': [
            {
                'name': 'backup',
                'password': 'x',
                'uid': '34',
                'gid': '34',
                'comment': 'backup',
                'home': '/var/backups',
                'shell': '/bin/sh'
            },
            {
                'name': 'list',
                'password': 'x',
                'uid': '38',
                'gid': '38',
                'comment': 'Mailing List Manager',
                'home': '/var/list',
                'shell': '/bin/sh'
            },
        ]
    }
    config = PasswdConfig


del BaseConfigTest
