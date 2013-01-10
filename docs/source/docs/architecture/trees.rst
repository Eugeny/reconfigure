Trees
*****

Reconfigure operates with three types of data:

  * Raw config text
  * Node tree
  * Data tree

Config text 
===========

This is a raw content, as read from the config file. It is fed to :ref:`Parsers` to produce the :ref:`Node tree`.

.. _Node tree:

Node tree
=========

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

