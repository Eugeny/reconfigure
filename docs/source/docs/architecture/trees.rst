Trees
*****

Reconfigure operates with three types of data:

  * Raw config text
  * Node tree
  * Data tree

Config text 
===========

This is a raw content, as read from the config file. It is fed to :ref:`Parsers` to produce the :ref:`Node trees`.

.. _Node trees:

Node trees
==========

Node tree is an object tree built from :class:`reconfigure.nodes.Node` objects, representing the syntax structure of the file. This is very similar to Abstract Syntax Trees.

Node trees are produced by :ref:`Parser` classes.

Example::

    >>> text = open('/etc/samba/smb.conf').read()
    >>> text
    '#\n# Sample configuration file for the Samba suite for Debian GNU/Linux.\
    ...
    >>> from reconfigure.parsers import IniFileParser
    >>> parser = IniFileParser()
    >>> node_tree = parser.parse(text)
    >>> print node_tree
    (None)
            (global)
                    workgroup = WORKGROUP
                    server string = %h server (Samba, Ubuntu)
                    dns proxy = no
                    log file = /var/log/samba/log.%m
                    max log size = 1000
                    syslog = 0
                    panic action = /usr/share/samba/panic-action %d
                    encrypt passwords = true
                    passdb backend = tdbsam
                    obey pam restrictions = yes
                    unix password sync = yes
                    passwd program = /usr/bin/passwd %u
                    passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
                    pam password change = yes
                    map to guest = bad user
                    usershare allow guests = yes
            (printers)
                    comment = All Printers
                    browseable = no
                    path = /var/spool/samba
                    printable = yes
                    guest ok = no
                    read only = yes
                    create mask = 0700
    >>> node_tree
    <reconfigure.nodes.RootNode object at 0x219a150>
    >>> node_tree.children[0]
    <reconfigure.nodes.Node object at 0x219a950>
    >>> node_tree.children[0].name
    'global'
    >>> node_tree.children[0].children[0]
    <reconfigure.nodes.PropertyNode object at 0x219aa10>
    >>> node_tree.children[0].children[0].name
    'workgroup'
    >>> node_tree.children[0].children[0].value
    'WORKGROUP'

:class:`reconfigure.nodes.Node`  reference page contains more information on how to manipulate node trees.

Parsers work both ways - you can call ``stringify()`` and get the text representation back. Even more, you can feed the node tree to *another* parser and get the config in other format::

    >>> from reconfigure.parsers import JsonParser
    >>> json_parser = JsonParser()
    >>> json_parser.stringify(node_tree)
    >>> print json_parser.stringify(node_tree)
    {
        "global": {
            "encrypt passwords": "true", 
            "pam password change": "yes", 
            "passdb backend": "tdbsam", 
            "passwd program": "/usr/bin/passwd %u", 
            ...
        }, 
        "print$": {
            "comment": "Printer Drivers", 
            "path": "/var/lib/samba/printers", 
            "read only": "yes", 
            ...

Node trees might look useful to you, but they are not nearly as cool as :ref:`Data trees`

.. _Data trees:

Data trees
==========

Data tree represents the actual, meaningful ideas stored in the config. Straight to example::

    >>> from reconfigure.builders import BoundBuilder
    >>> from reconfigure.items.samba import SambaData
    >>> builder = BoundBuilder(SambaData)
    >>> data_tree = builder.build(node_tree)
    >>> data_tree
    {
        "global": {
            "server_string": "%h server (Samba, Ubuntu)", 
            "workgroup": "WORKGROUP", 
            "interfaces": "", 
            "bind_interfaces_only": true, 
            "security": "user", 
            "log_file": "/var/log/samba/log.%m"
        }, 
        "shares": [
            {
                "comment": "All Printers", 
                "browseable": false, 
                "create_mask": "0700", 
                "name": "printers", 
                "directory_mask": "0755", 
                "read_only": true, 
                "guest_ok": false, 
                "path": "/var/spool/samba"
            }, 
            {
                "comment": "Printer Drivers", 
                "browseable": true, 
                "create_mask": "0744", 
                "name": "print$", 
                "directory_mask": "0755", 
                "read_only": true, 
                "guest_ok": false, 
                "path": "/var/lib/samba/printers"
            }
        ]
    }

    >>> data_tree.shares
    <reconfigure.items.bound.BoundCollection object at 0x23d0610>
    >>> [_.path for _ in data_tree.shares]
    ['/var/spool/samba', '/var/lib/samba/printers']

Data trees may consist of any Python objects, but the common approach is to use :class:`reconfigure.items.bound.BoundData`

Data trees can be manipulated as you wish::

    >>> from reconfigure.items.samba import ShareData
    >>> share = ShareData()
    >>> share.path = '/home/user'
    >>> share.comment = 'New share'
    >>> data_tree.shares.append(share)
    >>> data_tree
    {
        ....
        "shares": [
        {
            "comment": "All Printers", 
            "browseable": false, 
            "create_mask": "0700", 
            "name": "printers", 
            "directory_mask": "0755", 
            "read_only": true, 
            "guest_ok": false, 
            "path": "/var/spool/samba"
        }, 
        {
            "comment": "Printer Drivers", 
            "browseable": true, 
            "create_mask": "0744", 
            "name": "print$", 
            "directory_mask": "0755", 
            "read_only": true, 
            "guest_ok": false, 
            "path": "/var/lib/samba/printers"
        }, 
        {
            "comment": "New share", 
            "browseable": true, 
            "create_mask": "0744", 
            "name": "share", 
            "directory_mask": "0755", 
            "read_only": true, 
            "guest_ok": false, 
            "path": "/home/user"
        }
    ]

After you're done with the modifications, the data tree must be converted back to the node tree::

    >>> node_tree = builder.unbuild(data_tree)

