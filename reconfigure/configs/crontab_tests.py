from reconfigure.configs import CrontabConfig
from reconfigure.configs.base_test import BaseConfigTest


class CrontabConfigTest (BaseConfigTest):
    sources = {
        None: """#comment line
* * * * * date
@reboot ls -al
1 * 0 1 2 date -s
NAME = TEST"""
    }
    result = {
        'normal_tasks': [
            {
                'minute': '*',
                'hour': '*',
                'day_of_month': '*',
                'month': '*',
                'day_of_week': '*',
                'command': 'date',
                'comment': 'comment line'
            },
            {
                'minute': '1',
                'hour': '*',
                'day_of_month': '0',
                'month': '1',
                'day_of_week': '2',
                'command': 'date -s',
                'comment': None,
            },

        ],
        'special_tasks': [
            {
                'special': '@reboot',
                'command': 'ls -al',
                'comment': None,
            }
        ],
        'env_settings': [
            {
                'name': 'NAME',
                'value': 'TEST',
                'comment': None
            }
        ]
    }
    config = CrontabConfig


del BaseConfigTest
