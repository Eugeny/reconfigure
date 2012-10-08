from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
from ConfigParser import ConfigParser
from StringIO import StringIO


class IniFileParser (BaseParser):
    def __init__(self, sectionless=False, nullsection='__default__'):
        self.sectionless = sectionless
        self.nullsection = nullsection

    def parse(self, content):
        content = '\n'.join(filter(None, [x.strip() for x in content.splitlines()]))
        if self.sectionless:
            content = '[' + self.nullsection + ']\n' + content
        data = StringIO(content)
        cp = ConfigParser()
        cp.optionxform = str
        cp.readfp(data)

        root = RootNode()
        for section in cp.sections():
            name = section
            if self.sectionless and section == self.nullsection:
                name = None
            section_node = Node(name)
            for option in cp.options(section):
                section_node.children.append(PropertyNode(option, cp.get(section, option)))
            root.children.append(section_node)
        return root

    def stringify(self, tree):
        data = StringIO()
        cp = ConfigParser()
        cp.optionxform = str

        for section in tree.children:
            if self.sectionless and section.name is None:
                section.name = self.nullsection
            cp.add_section(section.name)
            for option in section.children:
                if not isinstance(option, PropertyNode):
                    raise TypeError('Third level nodes should be PropertyNodes')
                cp.set(section.name, option.name, option.value)

        cp.write(data)
        data = data.getvalue()
        if self.sectionless:
            data = data.replace('[' + self.nullsection + ']\n', '')
        return data
