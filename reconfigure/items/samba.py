from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class SambaData (BoundData):
    pass


class GlobalData (BoundData):
    pass


class ShareData (BoundData):
    fields = ['comment', 'path', 'guest ok', 'browseable', 'create mask', 'directory mask', 'read only']
    defaults = ['', '', 'no', 'yes', '0744', '0755', 'yes']

    def template(self):
        return Node('share',
            *[PropertyNode(x, y) for x, y in zip(ShareData.fields, ShareData.defaults)]
        )


SambaData.bind_child('global', lambda x: x.get('global'), item_class=GlobalData)
SambaData.bind_collection('shares', selector=lambda x: x.name != 'global', item_class=ShareData)

GlobalData.bind_property('workgroup', 'workgroup')
GlobalData.bind_property('server string', 'server_string')
GlobalData.bind_property('interfaces', 'interfaces')
GlobalData.bind_property('bind interfaces only', 'bind_interfaces_only')
GlobalData.bind_property('log file', 'log_file')
GlobalData.bind_property('security', 'security')

ShareData.bind_name('name')
for x, y in zip(ShareData.fields, ShareData.defaults):
    ShareData.bind_property(x, x.replace(' ', '_'), default=y)
