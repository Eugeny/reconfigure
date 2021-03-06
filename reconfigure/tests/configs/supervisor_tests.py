from reconfigure.configs import SupervisorConfig
from reconfigure.tests.configs.base_test import BaseConfigTest


class SupervisorConfigTest (BaseConfigTest):
    sources = {
        None: """[unix_http_server]
file=/var/run//supervisor.sock ;comment
chmod=0700
[include]
files=test""",
        'test': """[program:test1]
command=cat
stopasgroup=true
        """
    }
    result = {
        "programs": [
            {
                "comment": None,
                "autorestart": None,
                "name": "test1",
                "startsecs": None,
                "umask": None,
                "environment": None,
                "command": "cat",
                "user": None,
                "startretries": None,
                "directory": None,
                "autostart": None,
                "stopasgroup": True,
                "killasgroup": None,
            }
        ]
    }

    config = SupervisorConfig


del BaseConfigTest
