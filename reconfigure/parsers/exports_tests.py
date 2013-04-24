from reconfigure.parsers.base_test import BaseParserTest
from reconfigure.parsers import ExportsParser
from reconfigure.nodes import *


class ExportsParserTest (BaseParserTest):
    parser = ExportsParser()
    source = """
/another/exported/directory 192.168.0.3(rw,sync) \
192.168.0.4(ro)
# comment
/one 192.168.0.1
"""
    parsed = RootNode(
        None,
        Node(
            '/another/exported/directory',
            Node(
                'clients',
                Node(
                    '192.168.0.3',
                    PropertyNode('options', 'rw,sync')
                ),
                Node(
                    '192.168.0.4',
                    PropertyNode('options', 'ro')
                ),
            ),
        ),
        Node(
            '/one',
            Node(
                'clients',
                Node(
                    '192.168.0.1',
                    PropertyNode('options', '')
                ),
            ),
            comment='comment'
        )
    )

    @property
    def stringified(self):
        return """/another/exported/directory\t192.168.0.3(rw,sync)\t192.168.0.4(ro)
/one\t192.168.0.1\t# comment
"""


del BaseParserTest
