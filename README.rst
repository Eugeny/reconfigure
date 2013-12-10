====================================================
Reconfigure - Python object mapping for config files
====================================================

.. image:: https://travis-ci.org/Eugeny/reconfigure.png

`Browse API on SourceGraph <https://sourcegraph.com/github.com/Eugeny/reconfigure/tree>`_

----------
Quickstart
----------

::

    >>> from reconfigure.configs import FSTabConfig 
    >>> from reconfigure.items.fstab import FilesystemData
    >>> 
    >>> config = FSTabConfig(path='/etc/fstab')
    >>> config.load()
    >>> print config.tree
    {
        "filesystems": [
            {
                "passno": "0", 
                "device": "proc", 
                "mountpoint": "/proc", 
                "freq": "0", 
                "type": "proc", 
                "options": "nodev,noexec,nosuid"
            }, 
            {
                "passno": "1", 
                "device": "UUID=dfccef1e-d46c-45b8-969d-51391898c55e", 
                "mountpoint": "/", 
                "freq": "0", 
                "type": "ext4", 
                "options": "errors=remount-ro"
            }
        ]
    }
    >>> tmpfs = FilesystemData()
    >>> tmpfs.mountpoint = '/srv/cache'
    >>> tmpfs.type = 'tmpfs'
    >>> tmpfs.device = 'none'
    >>> config.tree.filesystems.append(tmpfs)
    >>> config.save()
    >>> quit()
    $ cat /etc/fstab
    proc    /proc   proc    nodev,noexec,nosuid     0       0
    UUID=dfccef1e-d46c-45b8-969d-51391898c55e / ext4 errors=remount-ro 0 1
    none    /srv/cache      tmpfs   none    0       0

This is actually a shortcut to::

    >>> from reconfigure.parsers import SSVParser
    >>> from reconfigure.builders import BoundBuilder
    >>> from reconfigure.items.fstab import FSTabData
    >>> content = open('/etc/fstab').read()
    >>> syntax_tree = SSVParser().parse(content)
    >>> syntax_tree
    <reconfigure.nodes.RootNode object at 0x7f1319eeec50>
    >>> print syntax_tree
    (None)
            (line)
                    (token)
                            value = proc
                    (token)
                            value = /proc
                    (token)
                            value = proc
                    (token)
                            value = nodev,noexec,nosuid
                    (token)
                            value = 0
                    (token)
                            value = 0
            (line)
                    (token)
                            value = UUID=83810b56-ef4b-44de-85c8-58dc589aef48
                    (token)
                            value = /
                    (token)
                            value = ext4
                    (token)
                            value = errors=remount-ro
                    (token)
                            value = 0
                    (token)
                            value = 1

    >>> builder = BoundBuilder(FSTabData)
    >>> data_tree = builder.build(syntax_tree)
    >>> print data_tree
    {
        "filesystems": [
            {
                "passno": "0", 
                "device": "proc", 
                "mountpoint": "/proc", 
                "freq": "0", 
                "type": "proc", 
                "options": "nodev,noexec,nosuid"
            }, 
            {
                "passno": "1", 
                "device": "UUID=83810b56-ef4b-44de-85c8-58dc589aef48", 
                "mountpoint": "/", 
                "freq": "0", 
                "type": "ext4", 
                "options": "errors=remount-ro"
            }
        ]
    }

Parsers and builders can be paired in almost any possible combination.

Reconfigure can be easily extended with your own parsers and builders - read the docs!

Supported configs:

  * Ajenti (``ajenti``)
  * BIND9 DNS (``bind9``)
  * Crontabs (``crontab``)
  * Samba CTDB (``ctdb``)
  * ISC DHCPD / uDHCPD (``dhcpd``)
  * NFS /etc/exports (``exports``)
  * /etc/fstab (``fstab``)
  * /etc/group (``group``)
  * /etc/hosts (``hosts``)
  * iptables-save dump (``iptables``)
  * Netatalk afp.conf (``netatalk``)
  * NSD DNS (``nsd``)
  * /etc/passwd (``passwd``)
  * /etc/resolv.conf (``resolv``)
  * Samba (``samba``)
  * Squid 3 (``squid``)
  * Supervisord (``supervisor``)

Included parsers:

  * BIND9 config (``bind9``)
  * Crontab (``crontab``)
  * NFS Exports (``exports``)
  * .ini (``ini``)
  * iptables-save (``iptables``)
  * nginx-like (``nginx``)
  * squid (``squid``)
  * nsd (``nsd``)
  * CSV-like space-separated values (``ssv``)
  * JSON (``jsonparser``)
