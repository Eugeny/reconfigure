import unittest

from reconfigure.configs import IPTablesConfig
from reconfigure.configs.base_tests import BaseConfigTest


class IPTablesConfigTest (BaseConfigTest, unittest.TestCase):
    sources = {
        None: '''*filter
:INPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -s 202.54.1.2/32 -j DROP
-A INPUT -m state --state NEW,ESTABLISHED -j ACCEPT
COMMIT
'''
    }
    result = {
        'tables': [
            {
                'chains': [
                    {
                        'default': 'ACCEPT',
                        'rules': [
                            {
                                'options': [
                                    {
                                        'arguments': [
                                            {
                                                'value': '202.54.1.2/32'
                                            }
                                        ],
                                        'name': 's'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'DROP'
                                            }
                                        ],
                                        'name': 'j'
                                    }
                                ]
                            },
                            {
                                'options': [
                                    {
                                        'arguments': [
                                            {
                                                'value': 'state'
                                            }
                                        ],
                                        'name': 'm'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'NEW,ESTABLISHED'
                                            }
                                        ],
                                        'name': 'state'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'ACCEPT'
                                            }
                                        ],
                                        'name': 'j'
                                    }
                                ]
                            }
                        ],
                        'name': 'INPUT'
                    },
                    {
                        'default': 'DROP',
                        'rules': [],
                        'name': 'FORWARD'
                    },
                    {
                        'default': 'ACCEPT',
                        'rules': [],
                        'name': 'OUTPUT'
                    }
                ],
                'name': 'filter'
            }
        ]
    }

    config = IPTablesConfig


if __name__ == '__main__':
    unittest.main()
