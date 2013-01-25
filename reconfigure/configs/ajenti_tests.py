import unittest
import json

from reconfigure.configs import AjentiConfig
from reconfigure.configs.base_tests import BaseConfigTest


class AjentiConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: """{
    "authentication": false,
    "bind": {
        "host": "0.0.0.0",
        "port": 8000
    },
    "enable_feedback": true,
    "installation_id": null,
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
        "certificate_path": ""
    }
}
"""
    }
    result = {
        'authentication': False,
        'enable_feedback': True,
        'installation_id': None,
        'http_binding': {'host': '0.0.0.0', 'port': 8000},
        'ssl': {'certificate_path': '', 'enable': False},
        'users': {'test': {
            'configs': {'a': {'data': {}, 'name': 'a'}},
            'name': 'test',
            'password': 'sha512',
            'permissions': ['section:Dash']
        }}
    }

    config = AjentiConfig

    stringify_filter = staticmethod(json.loads)


if __name__ == '__main__':
    unittest.main()
