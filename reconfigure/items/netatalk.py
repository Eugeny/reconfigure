from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData
from reconfigure.items.util import yn_getter, yn_setter


class NetatalkData (BoundData):
    pass


class GlobalData (BoundData):
    pass


class ShareData (BoundData):
    fields = ['path', 'appledouble', 'valid users', 'cnid scheme', 'ea', 'password', 'file perm', 'directory perm']
    defaults = ['', 'ea', '', 'dbd', 'none', '', '', '']

    def template(self):
        return Node(
            'share',
            *[PropertyNode(x, y) for x, y in zip(ShareData.fields, ShareData.defaults)]
        )


NetatalkData.bind_child('global', lambda x: x.get('Global'), item_class=GlobalData)
NetatalkData.bind_collection('shares', selector=lambda x: x.name != 'Global', item_class=ShareData)


GlobalData.bind_property('afp port', 'afp_port', default='548')
GlobalData.bind_property('cnid listen', 'cnid_listen', default='localhost:4700')
GlobalData.bind_property('uam list', 'uam_list', default='uams_dhx.so,uams_dhx2.so')
GlobalData.bind_property(
    'zeroconf', 'zeroconf', default=True,
    getter=yn_getter, setter=yn_setter)

ShareData.bind_name('name')
ShareData.bind_attribute('comment', 'comment', path=lambda x: x.get('path'), default='')
for f, d in zip(ShareData.fields, ShareData.defaults):
    ShareData.bind_property(f, f.replace(' ', '_'), default=d, default_remove=[d, None])
