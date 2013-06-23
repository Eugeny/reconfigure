from reconfigure.configs import IPTablesConfig
from reconfigure.configs.base_test import BaseConfigTest


class IPTablesConfigTest (BaseConfigTest):
    sources = {
        None: '''*filter
:INPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT ! -s 202.54.1.2/32 -j DROP
-A INPUT -m state --state NEW,ESTABLISHED -j ACCEPT # test
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
                                        'negative': True,
                                        'name': 's'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'DROP'
                                            }
                                        ],
                                        'negative': False,
                                        'name': 'j'
                                    }
                                ],
                                'comment': None,
                            },
                            {
                                'options': [
                                    {
                                        'arguments': [
                                            {
                                                'value': 'state'
                                            }
                                        ],
                                        'negative': False,
                                        'name': 'm'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'NEW,ESTABLISHED'
                                            }
                                        ],
                                        'negative': False,
                                        'name': 'state'
                                    },
                                    {
                                        'arguments': [
                                            {
                                                'value': 'ACCEPT'
                                            }
                                        ],
                                        'negative': False,
                                        'name': 'j'
                                    }
                                ],
                                'comment': 'test',
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


del BaseConfigTest
