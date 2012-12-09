import unittest

from reconfigure.configs import NginxConfig
from reconfigure.configs.base_tests import BaseConfigTest


class NginxConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """p1 1;

http {
    include test;
}
""",
        'test': """server {
    root /srv/wp;
    index index.php index.htm;

    server_name c.d.local;
    server_name c.d.wifi;

    location / {
            root /home/user/Work/dash/public/static;
    }
}"""
    }
    result = {'http': {'servers': [{'locations': [{'pattern': '/',
 'root': '/home/user/Work/dash/public/static'}],
 'root': '/srv/wp',
 'server_names': ['c.d.local',
                  'c.d.wifi']}]}}

    config = NginxConfig
