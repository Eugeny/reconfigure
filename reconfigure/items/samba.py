from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from reconfigure.items.util import yn_getter, yn_setter


class SambaData (BoundData):
    pass


class GlobalData (BoundData):
    pass


class ShareData (BoundData):
    fields = [
        'comment', 'path', 'guest ok', 'browseable', 'create mask', 'directory mask', 'read only',
        'follow symlinks', 'wide links', 'fstype', 'write list', 'veto files',
        'force create mode', 'force directory mode', 'dfree command', 'force user', 'force group',
        'valid_users', 'read_list',
    ]
    defaults = [
        '', '', 'no', 'yes', '0744', '0755', 'yes',
        'yes', 'no', 'NTFS', '', '', '000', '000', '',
        '', '', '', '',
    ]
    default_values = [
        '', '', False, True, '0744', '0755', True,
        True, False, '', '', '', '000', '000', '',
        '', '', '', '',
    ]

    def template(self):
        return Node(
            'share',
            *[PropertyNode(x, y) for x, y in zip(ShareData.fields, ShareData.defaults)]
        )


SambaData.bind_child('global', lambda x: x.get('global'), item_class=GlobalData)
SambaData.bind_collection('shares', selector=lambda x: x.name != 'global', item_class=ShareData)


GlobalData.bind_property('workgroup', 'workgroup', default='')
GlobalData.bind_property('server string', 'server_string', default='')
GlobalData.bind_property('interfaces', 'interfaces', default='')
GlobalData.bind_property(
    'bind interfaces only', 'bind_interfaces_only', default=True,
    getter=yn_getter, setter=yn_setter)
GlobalData.bind_property('log file', 'log_file', default='')
GlobalData.bind_property('security', 'security', default='user')

ShareData.bind_name('name')
for f, d in zip(ShareData.fields, ShareData.default_values):
    if d not in [True, False]:
        ShareData.bind_property(f, f.replace(' ', '_'), default=d)
    else:
        ShareData.bind_property(
            f, f.replace(' ', '_'), default=d,
            getter=yn_getter, setter=yn_setter)
