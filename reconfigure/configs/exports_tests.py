from reconfigure.configs import ExportsConfig
from reconfigure.configs.base_test import BaseConfigTest


class ExportsConfigTest (BaseConfigTest):
    sources = {
        None: """
/another/exported/directory 192.168.0.3(rw,sync) \
192.168.0.4(ro) # test
/one 192.168.0.1 # comment
"""
    }
    result = {
        "exports": [
            {
                "comment": "test",
                "name": '/another/exported/directory',
                "clients": [
                    {
                        "name": "192.168.0.3",
                        "options": "rw,sync"
                    },
                    {
                        "name": "192.168.0.4",
                        "options": "ro"
                    }
                ]
            },
            {
                "comment": "comment",
                "name": '/one',
                "clients": [
                    {
                        "name": "192.168.0.1",
                        "options": ""
                    }
                ]
            }
        ]
    }

    config = ExportsConfig


del BaseConfigTest
