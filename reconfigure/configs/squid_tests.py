from reconfigure.configs import SquidConfig
from reconfigure.configs.base_test import BaseConfigTest


class SquidConfigTest (BaseConfigTest):
    sources = {
        None: """acl manager proto cache_object
acl SSL_ports port 443
http_access deny CONNECT !SSL_ports
http_port 3128
"""
    }
    result = {
       "http_access": [
            {
                "mode": "deny",
                "options": [
                    {
                        "value": "CONNECT"
                    },
                    {
                        "value": "!SSL_ports"
                    }
                ]
            }
        ],
        "http_port": [
            {
                "options": [],
                "port": "3128"
            }
        ],
        "https_port": [],
        "acl": [
            {
                "name": "manager",
                "options": [
                    {
                        "value": "proto"
                    },
                    {
                        "value": "cache_object"
                    }
                ]
            },
            {
                "name": "SSL_ports",
                "options": [
                    {
                        "value": "port"
                    },
                    {
                        "value": "443"
                    }
                ]
            }
        ]
    }

    config = SquidConfig


del BaseConfigTest
