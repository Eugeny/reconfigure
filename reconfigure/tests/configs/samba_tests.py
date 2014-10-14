from reconfigure.configs import SambaConfig
from reconfigure.tests.configs.base_test import BaseConfigTest


class SambaConfigTest (BaseConfigTest):
    sources = {
        None: """
[global]
workgroup=WORKGROUP
server string=%h server (Samba, Ubuntu)
interfaces=127.0.0.0/8 eth0
bind interfaces only=yes
log file=/var/log/samba/log.%m
security=user

[homes]
comment=Home Directories
browseable=no
preopen:names=/*.frm/
preopen:num_bytes=123
preopen:helpers=2
preopen:queuelen=20

[profiles]
comment=Users profiles
path=/home/samba/profiles
guest ok=no
browseable=no
create mask=0600
directory mask=0700
"""
    }

    result = {
        "global": {
            "server_string": "%h server (Samba, Ubuntu)",
            "workgroup": "WORKGROUP",
            "interfaces": "127.0.0.0/8 eth0",
            "bind_interfaces_only": True,
            "security": "user",
            "log_file": "/var/log/samba/log.%m"
        },
        "shares": [
            {
                "name": "homes",
                "comment": "Home Directories",
                "browseable": False,
                "create_mask": "0744",
                "directory_mask": "0755",
                'follow_symlinks': True,
                "read_only": True,
                "guest_ok": False,
                "path": "",
                'wide_links': False,
                "fstype": "",
                "force_create_mode": "000",
                "force_directory_mode": "000",
                "veto_files": "",
                "write_list": "",
                "dfree_command": "",
                "force_group": "",
                "force_user": "",
                "valid_users": "",
                "read_list": "",
                "dfree_cache_time": "",
                "oplocks": True,
                "locking": True,
                "preopen:queuelen": "20", 
                "preopen:names": "/*.frm/", 
                "preopen:num_bytes": "123", 
                "preopen:helpers": "2", 
            },
            {
                "name": "profiles",
                "comment": "Users profiles",
                "browseable": False,
                "create_mask": "0600",
                "directory_mask": "0700",
                'follow_symlinks': True,
                "read_only": True,
                "guest_ok": False,
                "path": "/home/samba/profiles",
                'wide_links': False,
                "fstype": "",
                "force_create_mode": "000",
                "force_directory_mode": "000",
                "veto_files": "",
                "write_list": "",
                "dfree_command": "",
                "force_group": "",
                "force_user": "",
                "valid_users": "",
                "read_list": "",
                "dfree_cache_time": "",
                "oplocks": True,
                "locking": True,
                "preopen:queuelen": "", 
                "preopen:names": "", 
                "preopen:num_bytes": "", 
                "preopen:helpers": "", 
            }
        ]
    }

    config = SambaConfig


del BaseConfigTest
