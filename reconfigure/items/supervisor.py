from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class SupervisorData (BoundData):
    pass


class ProgramData (BoundData):
    fields = ['command', 'autostart', 'autorestart', 'startsecs', 'startretries', \
        'user', 'directory', 'umask', 'environment']

    def template(self):
        return Node('program:new',
            PropertyNode('command', 'false'),
        )


SupervisorData.bind_collection('programs', item_class=ProgramData, selector=lambda x: x.name.startswith('program:'))
ProgramData.bind_name('name', getter=lambda x: x[8:], setter=lambda x: 'program:%s' % x)
ProgramData.bind_attribute('comment', 'comment')
for i in range(0, len(ProgramData.fields)):
    ProgramData.bind_property(ProgramData.fields[i], ProgramData.fields[i], default_remove=[None, ''])
