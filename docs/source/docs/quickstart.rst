Quickstart
==========

Adding lines to ``fstab``::

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

Changing Samba settings::

    >>> from reconfigure.configs import SambaConfig
    >>> config = SambaConfig(path='/etc/samba/smb.conf')
    >>> config.load()
    >>> print config.tree.shares
    [
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
    >>> config.tree.shares[0].guest_ok = True
    >>> print config.tree.shares
    [
        {
            "comment": "All Printers", 
            "browseable": false, 
            "create_mask": "0700", 
            "name": "printers", 
            "directory_mask": "0755", 
            "read_only": true, 
            "guest_ok": true, 
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
    >>> config.save()
