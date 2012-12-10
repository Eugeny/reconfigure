import unittest

from reconfigure.configs import AjentiConfig
from reconfigure.configs.base_tests import BaseConfigTest


class AjentiConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """{
    "bind": {
        "host": "0.0.0.0",
        "port": 8000
    },
    "authentication": false,
    "users": {
        "test": {
            "configs": { "a": "{}" },
            "password": "sha512",
            "permissions": [
                "section:Dash"
            ]
        }
    },
    "ssl": {
        "enable": false,
        "certificate_path": "",
        "key_path": ""
    }
}
"""
    }
    result = {
        'authentication': False,
        'http_binding': {'host': '0.0.0.0', 'port': 8000},
        'ssl': {'certificate_path': '', 'enable': False, 'key_path': ''},
        'users': {'test': {
            'configs': {'a': {'data': {}, 'name': 'a'}},
            'name': 'test',
            'password': 'sha512',
            'permissions': ['section:Dash']
        }}
    }

    config = AjentiConfig


if __name__ == '__main__':
    unittest.main()
