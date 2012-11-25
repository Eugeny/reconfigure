``` This is a project deep in development, not yet ready for production use ```

Reconfigure is an ORM for your config files. Direct translation of file into a Python objects makes it easy to do any kind of reconfiguration.
You can even extend reconfigure with your own classes for your custom configuration files!

Quick example:

```
>>> from reconfigure.configs import FSTabConfig
>>> from reconfigure.builders.fstab import FilesystemBuilder
>>> config = FSTabConfig(path='/etc/fstab')
>>> config.load()
>>> print config.tree
{
    filesystems [
        {
            type proc
            device proc
            mountpoint /proc
            freq 0
            passno 0
            options nodev,noexec,nosuid
        }, 
        {
            type ext4
            device UUID=83810b56-ef4b-44de-85c8-58dc589aef48
            mountpoint /
            freq 0
            passno 1
            options errors=remount-ro
        }
    ]
}
>>> config.tree.filesystems[1].device = '/dev/sda1'
>>> fs = FilesystemBuilder.empty()
>>> fs.device = '/dev/sdb1'
>>> fs.mountpoint = '/mnt/temp'
>>> config.tree.filesystems.append(fs)
>>> config.save()
>>> print open('/etc/fstab').read()
proc    /proc   proc    nodev,noexec,nosuid     0       0
/dev/sda1       /       ext4    errors=remount-ro       0       1
/dev/sdb1       /mnt/temp   none none none none
```
