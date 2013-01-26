from reconfigure.configs import FSTabConfig
from reconfigure.configs.base_test import BaseConfigTest


class FSTabConfigTest (BaseConfigTest):
    sources = {
        None: """fs1\tmp1\text\trw\t1\t2
fs2\tmp2\tauto\tnone\t0\t0
"""
    }
    result = {
        'filesystems': [
            {
                'device': 'fs1',
                'mountpoint': 'mp1',
                'type': 'ext',
                'options': 'rw',
                'freq': '1',
                'passno': '2'
            },
            {
                'device': 'fs2',
                'mountpoint': 'mp2',
                'type': 'auto',
                'options': 'none',
                'freq': '0',
                'passno': '0'
            },
        ]
    }
    config = FSTabConfig


del BaseConfigTest
