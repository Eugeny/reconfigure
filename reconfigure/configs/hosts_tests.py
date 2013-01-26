from reconfigure.configs import HostsConfig
from reconfigure.configs.base_test import BaseConfigTest


class FSTabConfigTest (BaseConfigTest):
    sources = {
        None: """a1 h1 a2 a3 a4
a5 h2
a6 h3 a7
"""
    }
    result = {
        'hosts': [
            {
                'address': 'a1',
                'name': 'h1',
                'aliases': [
                    {'name': 'a2'},
                    {'name': 'a3'},
                    {'name': 'a4'},
                ]
            },
            {
                'address': 'a5',
                'aliases': [],
                'name': 'h2',
            },
            {
                'address': 'a6',
                'name': 'h3',
                'aliases': [
                    {'name': 'a7'},
                ]
            },
        ]
    }
    config = HostsConfig


del BaseConfigTest
