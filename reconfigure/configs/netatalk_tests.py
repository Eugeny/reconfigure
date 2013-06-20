from reconfigure.configs import NetatalkConfig
from reconfigure.configs.base_test import BaseConfigTest


class NetatalkConfigTest (BaseConfigTest):
    sources = {
        None: """
[Global]
afp port=123

[test]
path=/home ;comment
valid users=root
ea=sys
"""
    }

    result = {
        "global": {
            "zeroconf": True,
            "cnid_listen": "localhost:4700",
            "afp_port": "123",
        },
        "shares": [
            {
                "comment": "comment",
                "appledouble": "ea",
                "name": "test",
                "ea": "sys",
                "valid_users": "root",
                "cnid_scheme": "dbd",
                "path": "/home",
                "password": '',
            }
        ]
    }

    config = NetatalkConfig


del BaseConfigTest
