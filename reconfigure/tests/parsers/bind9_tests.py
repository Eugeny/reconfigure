from reconfigure.tests.parsers.base_test import BaseParserTest
from reconfigure.parsers import BIND9Parser
from reconfigure.nodes import *


class BIND9ParserTest (BaseParserTest):
    parser = BIND9Parser()
    source = """p1 asd;

key {
    s1p1 asd;
    /*s1p2 wqe;*/

    zone 
            test {
        ::1;
        s2p1 qwe;
    };
};
"""

    @property
    def stringified(self):
        return """
  p1 asd;

key {
    s1p1 asd;

    # s1p2 wqe;
    zone test {
        ::1;
        s2p1 qwe;
    };
};
"""

    parsed = RootNode(
        None,
        PropertyNode('p1', 'asd'),
        Node(
            'key',
            PropertyNode('s1p1', 'asd'),
            Node(
                'zone',
                PropertyNode('', '::1'),
                PropertyNode('s2p1', 'qwe'),
                parameter='test',
                comment='s1p2 wqe;',
            ),
            parameter=None,
        )
    )


del BaseParserTest



import unittest 

class BIND9ParserHangTest (unittest.TestCase):
    source = """
options {
        listen-on port 53 { 127.0.0.1; };
        listen-on-v6 port 53 { ::1; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        allow-query     { localhost; };

        /* 
         - If you are building an AUTHORITATIVE DNS server, do NOT enable recursion.
         - If you are building a RECURSIVE (caching) DNS server, you need to enable 
           recursion. 
         - If your recursive DNS server has a public IP address, you MUST enable access 
           control to limit queries to your legitimate users. Failing to do so will
           cause your server to become part of large scale DNS amplification 
           attacks. Implementing BCP38 within your network would greatly
           reduce such attack surface 
        */
        recursion yes;

        dnssec-enable yes;
        dnssec-validation yes;
        dnssec-lookaside auto;

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";

        pid-file "/run/named/named.pid";
        session-keyfile "/run/named/session.key";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;
        file "named.ca";
};
"""

    def test_hang(self):
        BIND9Parser().parse(self.source)

