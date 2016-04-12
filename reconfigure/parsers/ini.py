import sys

from reconfigure.nodes import *
from reconfigure.parsers import BaseParser
from reconfigure.parsers.iniparse import INIConfig

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class IniFileParser (BaseParser):
    """
    A parser for standard ``.ini`` config files.

    :param sectionless: if ``True``, allows a section-less attributes appear in the beginning of file
    """

    def __init__(self, sectionless=False, nullsection='__default__'):
        self.sectionless = sectionless
        self.nullsection = nullsection

    def _get_comment(self, container):
        c = container.contents[0].comment
        return c.strip() if c else None

    def _set_comment(self, container, comment):
        if comment:
            container.contents[0].comment = comment
            container.contents[0].comment_separator = ';'

    def parse(self, content):
        content = '\n'.join(filter(None, [x.strip() for x in content.splitlines()]))
        if self.sectionless:
            content = '[' + self.nullsection + ']\n' + content
        data = StringIO(content)
        cp = INIConfig(data, optionxformvalue=lambda x: x)

        root = RootNode()
        for section in cp:
            name = section
            if self.sectionless and section == self.nullsection:
                name = None
            section_node = Node(name)
            section_node.comment = self._get_comment(cp[section]._lines[0])
            section_node._extra_content = {}
            for option in cp[section]:
                if option in cp[section]._options:
                    node = PropertyNode(option, cp[section][option])
                    node.comment = self._get_comment(cp[section]._options[option])
                    section_node.children.append(node)
            root.children.append(section_node)
        return root

    def stringify(self, tree):
        cp = INIConfig()
        for section in tree.children:
            if self.sectionless and section.name is None:
                sectionname = self.nullsection
            else:
                sectionname = section.name
            cp._new_namespace(sectionname)
            for option in section.children:
                if not isinstance(option, PropertyNode):
                    raise TypeError('Third level nodes should be PropertyNodes')
                cp[sectionname][option.name] = option.value
                if option.comment:
                    self._set_comment(cp[sectionname]._options[option.name], option.comment)

            if section._extra_content:
                for k, v in section._extra_content.items():
                    cp[sectionname][k] = v

            if hasattr(cp[sectionname], '_lines'):
                self._set_comment(cp[sectionname]._lines[0], section.comment)

        data = (str if sys.version_info[0] >= 3 else unicode)(cp) + u'\n'
        if self.sectionless:
            data = data.replace('[' + self.nullsection + ']\n', '')
        return data
