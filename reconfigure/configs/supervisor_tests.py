from reconfigure.configs import SupervisorConfig
from reconfigure.configs.base_test import BaseConfigTest


class SupervisorConfigTest (BaseConfigTest):
    sources = {
        None: """[unix_http_server]
file=/var/run//supervisor.sock ;comment
chmod=0700
[include]
files=test""",
        'test': """[program:test1]
command=cat
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


del BaseConfigTest
