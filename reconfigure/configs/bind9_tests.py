from reconfigure.configs import BIND9Config
from reconfigure.configs.base_test import BaseConfigTest


class DHCPDConfigTest (BaseConfigTest):
    sources = {
        None: """
zone "asd" {
    type master;
    file "/file";
};

"""
    }
    result = {
        "zones": [
            {
                "type": "master",
                "name": "asd",
                "file": "/file"
            }
        ]
    }

    config = BIND9Config


del BaseConfigTest
