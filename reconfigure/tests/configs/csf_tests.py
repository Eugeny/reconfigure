from reconfigure.configs import CSFConfig
from reconfigure.tests.configs.base_test import BaseConfigTest


class CSFConfigTest (BaseConfigTest):
    sources = {
        None: """
TESTING = "1"
TCP_IN = "20,21,22,25,53,80,110,143,443,465,587,993,995"
TCP_OUT = "20,21,22,25,53,80,110,113,443"
UDP_IN = "20,21,53"
UDP_OUT = "20,21,53,113,123"
IPV6 = "0"
TCP6_IN = "20,21,22,25,53,80,110,143,443,465,587,993,995"
TCP6_OUT = "20,21,22,25,53,80,110,113,443"
UDP6_IN = "20,21,53"
UDP6_OUT = "20,21,53,113,123"
ETH_DEVICE = ""
ETH6_DEVICE = ""
"""
    }
    result = {
        "tcp6_out": "20,21,22,25,53,80,110,113,443",
        "testing": True,
        "eth_device": "",
        "tcp_in": "20,21,22,25,53,80,110,143,443,465,587,993,995",
        "tcp6_in": "20,21,22,25,53,80,110,143,443,465,587,993,995",
        "udp6_in": "20,21,53",
        "tcp_out": "20,21,22,25,53,80,110,113,443",
        "udp6_out": "20,21,53,113,123",
        "ipv6": False,
        "udp_in": "20,21,53",
        "eth6_device": "",
        "udp_out": "20,21,53,113,123"
    }

    config = CSFConfig
