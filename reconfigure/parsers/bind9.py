from reconfigure.nodes import *
from reconfigure.parsers.nginx import NginxParser


class BIND9Parser (NginxParser):
    """
    A parser for named.conf
    """

    tokens = [
        (r"(acl|key|masters|server|trusted-keys|managed-keys|controls|logging|lwres|options|view|zone|channel|category|listen-on|search|avoid-v4-udp-ports|avoid-v6-udp-ports|blackhole|listen-on|listen-on-v6|allow-recursion|allow-recursion-on|sortlist|topology|rrset-order|dual-stack-servers|disable-algorithms|dns64|forwarders|rrset-order|update-policy|also-notify|allow-notify|rate-limit)\s+?([^\s{}]*\s*)*{", lambda s, t: ('section_start', t)),
        (r"\#.*?\n", lambda s, t: ('comment', t)),
        (r"//.*?\n", lambda s, t: ('comment', t)),
        (r"/\*.*?\*/", lambda s, t: ('comment', t)),
        (r"((([^\s{};#]+)|({\s*([^\s{};#]+;\s*)*}))\s*?)+;", lambda s, t: ('option', t)),
        (r"\s", lambda s, t: 'whitespace'),
        (r"$^", lambda s, t: 'newline'),
        (r"\};", lambda s, t: 'section_end'),
    ]
    token_section_end = '};'
