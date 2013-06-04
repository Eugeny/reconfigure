from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from util import yn_getter, yn_setter


class SambaData (BoundData):
    pass


class GlobalData (BoundData):
    pass


class ShareData (BoundData):
    fields = [
        'comment', 'path', 'guest ok', 'browseable', 'create mask', 'directory mask', 'read only',
        'follow symlinks', 'wide links',
    ]
    defaults = [
        '', '', 'no', 'yes', '0744', '0755', 'yes',
        'yes', 'no',
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
ShareData.bind_property('path', 'path', default='')
ShareData.bind_property('comment', 'comment', default='')
ShareData.bind_property('create mask', 'create_mask', default='0744')
ShareData.bind_property('directory mask', 'directory_mask', default='0755')

for x, y in [
    ('guest ok', False),
    ('browseable', True),
    ('read only', True),
    ('follow symlinks', True),
    ('wide links', False),
]:
    ShareData.bind_property(
        x, x.replace(' ', '_'), default=y,
        getter=yn_getter, setter=yn_setter)
