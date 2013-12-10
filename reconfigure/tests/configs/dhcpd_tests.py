from reconfigure.configs import DHCPDConfig
from reconfigure.tests.configs.base_test import BaseConfigTest


class DHCPDConfigTest (BaseConfigTest):
    sources = {
        None: """
default-lease-time 600;
max-lease-time 7200;

 subnet 10.17.224.0 netmask 255.255.255.0 {
    option routers rtr-224.example.org;
    range 10.0.29.10 10.0.29.230;
  }
shared-network 224-29 {
  subnet 10.17.224.0 netmask 255.255.255.0 {
    option routers rtr-224.example.org;
  }
  pool {
    deny members of "foo";
    range 10.0.29.10 10.0.29.230;
  }
}

"""
    }
    result = {
        "subnets": [
            {
                "ranges": [
                    {
                        "range": "10.0.29.10 10.0.29.230"
                    }
                ],
                "subnets": [],
                "name": "10.17.224.0 netmask 255.255.255.0",
                "options": [
                    {
                        "value": "routers rtr-224.example.org"
                    }
                ]
            }
        ],
        "options": []
    }

    config = DHCPDConfig


del BaseConfigTest
