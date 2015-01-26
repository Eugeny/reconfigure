from reconfigure.configs import NetatalkConfig
from reconfigure.tests.configs.base_test import BaseConfigTest


class NetatalkConfigTest (BaseConfigTest):
    sources = {
        None: """
[Global]
afp port=123

[test]
path=/home ;comment
valid users=root
ea=sys
file perm=0755
"""
    }

    result = {
        "global": {
            "zeroconf": True,
            "cnid_listen": "localhost:4700",
            "uam_list": 'uams_dhx.so,uams_dhx2.so',
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
                "file_perm": '0755',
                "directory_perm": '',
            }
        ]
    }

    config = NetatalkConfig


del BaseConfigTest
