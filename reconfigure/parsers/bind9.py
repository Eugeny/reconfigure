from reconfigure.nodes import *
from reconfigure.parsers.nginx import NginxParser
import re


class BIND9Parser (NginxParser):
    """
    A parser for named.conf
    """

    tokens = [
        (r"[\w_]+\s*?.*?{", lambda s, t: ('section_start', t)),
        (r"[\w_]+?.+?;", lambda s, t: ('option', t)),
        (r"\s", lambda s, t: 'whitespace'),
        (r"$^", lambda s, t: 'newline'),
        (r"\#.*?\n", lambda s, t: ('comment', t)),
        (r"//.*?\n", lambda s, t: ('comment', t)),
        (r"/\*.*?\*/", lambda s, t: ('comment', t)),
        (r"\};", lambda s, t: 'section_end'),
    ]
    token_section_end = '};'
