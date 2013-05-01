from reconfigure.configs import CTDBConfig, CTDBNodesConfig, CTDBPublicAddressesConfig
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


class CTDBConfigTest (BaseConfigTest):
    sources = {
        None: """CTDB_RECOVERY_LOCK="/dadoscluster/ctdb/storage"
CTDB_PUBLIC_INTERFACE=eth0
CTDB_PUBLIC_ADDRESSES=/etc/ctdb/public_addresses
CTDB_MANAGES_SAMBA=yes
CTDB_NODES=/etc/ctdb/nodes
CTDB_LOGFILE=/var/log/log.ctdb
CTDB_DEBUGLEVEL=2
CTDB_PUBLIC_NETWORK="10.0.0.0/24"
CTDB_PUBLIC_GATEWAY="10.0.0.9"
"""
    }
    result = {
        "recovery_lock_file": "\"/dadoscluster/ctdb/storage\"",
        "public_interface": "eth0",
        "public_addresses_file": "/etc/ctdb/public_addresses",
        "nodes_file": "/etc/ctdb/nodes",
        "debug_level": "2",
        "public_gateway": "\"10.0.0.9\"",
        "public_network": "\"10.0.0.0/24\"",
        "log_file": "/var/log/log.ctdb",
        "manages_samba": True
    }

    config = CTDBConfig


del BaseConfigTest
