from reconfigure.configs import ResolvConfig
from reconfigure.configs.base_test import BaseConfigTest


class ResolvConfigTest (BaseConfigTest):
    sources = {
        None: """nameserver 1
domain 2
search 3 5
"""
    }
    result = {
        'items': [
            {
                'name': 'nameserver',
                'value': '1',
            },
            {
                'name': 'domain',
                'value': '2',
            },
            {
                'name': 'search',
                'value': '3 5',
            },
        ]
    }
    config = ResolvConfig


del BaseConfigTest
