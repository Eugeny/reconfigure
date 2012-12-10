import unittest

from reconfigure.configs.base_tests import BaseConfigTest
from reconfigure.configs import SupervisorConfig


class SupervisorConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """[unix_http_server]
file = /var/run//supervisor.sock
chmod = 0700
[include]
files = test""",
        'test': """[program:test1]
command = cat
        """
    }
    result = {
        "programs": [
            {
                "autorestart": None,
                "name": "test1",
                "startsecs": None,
                "umask": None,
                "environment": None,
                "command": "cat",
                "user": None,
                "startretries": None,
                "directory": None,
                "autostart": None
            }
        ]
    }

    config = SupervisorConfig
