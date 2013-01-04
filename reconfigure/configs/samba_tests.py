import unittest

from reconfigure.configs import SambaConfig
from reconfigure.configs.base_tests import BaseConfigTest


class SambaConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """
[global]
workgroup = WORKGROUP
server string = %h server (Samba, Ubuntu)
interfaces = 127.0.0.0/8 eth0
bind interfaces only = yes
log file = /var/log/samba/log.%m
security = user

[homes]
comment = Home Directories
browseable = no

[profiles]
comment = Users profiles
path = /home/samba/profiles
guest ok = no
browseable = no
create mask = 0600
directory mask = 0700
"""
    }

    result = {
        "global": {
            "server_string": "%h server (Samba, Ubuntu)",
            "workgroup": "WORKGROUP",
            "interfaces": "127.0.0.0/8 eth0",
            "bind_interfaces_only": "yes",
            "security": "user",
            "log_file": "/var/log/samba/log.%m"
        },
        "shares": [
            {
                "comment": "Home Directories",
                "browseable": "no",
                "create_mask": "0744",
                "directory_mask": "0755",
                "read_only": "yes",
                "guest_ok": "no",
                "path": ""
            },
            {
                "comment": "Users profiles",
                "browseable": "no",
                "create_mask": "0600",
                "directory_mask": "0700",
                "read_only": "yes",
                "guest_ok": "no",
                "path": "/home/samba/profiles"
            }
        ]
    }

    config = SambaConfig


if __name__ == '__main__':
    unittest.main()
