from reconfigure.configs import CTDBNodesConfig, CTDBPublicAddressesConfig
from reconfigure.configs.base_test import BaseConfigTest


class CTDBNodesConfigTest (BaseConfigTest):
    sources = {
        None: """10.10.1.1
10.10.1.2
"""
    }
    result = {
        'nodes': [
            {
                'address': '10.10.1.1',
            },
            {
                'address': '10.10.1.2',
            },
        ]
    }
    config = CTDBNodesConfig


class CTDBPublicAddressesConfigTest (BaseConfigTest):
    sources = {
        None: """10.10.1.1 eth0
10.10.1.2 eth1
"""
    }
    result = {
        'addresses': [
            {
                'address': '10.10.1.1',
                'interface': 'eth0',
            },
            {
                'address': '10.10.1.2',
                'interface': 'eth1',
            },
        ]
    }
    config = CTDBPublicAddressesConfig

del BaseConfigTest
