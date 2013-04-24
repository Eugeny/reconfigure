import unittest


class BaseParserTest (unittest.TestCase):
    source = ""
    parsed = None
    parser = None

    @property
    def stringified(self):
        return self.source

    def test_parse(self):
        if not self.__class__.parser:
            return

        nodetree = self.parser.parse(self.__class__.source)
        if self.__class__.parsed != nodetree:
            print 'TARGET: %s\n\nPARSED: %s' % (self.__class__.parsed, nodetree)
        self.assertEquals(self.__class__.parsed, nodetree)

    def test_stringify(self):
        if not self.__class__.parser:
            return

        unparsed = self.parser.stringify(self.__class__.parsed)
        a, b = self.stringified, unparsed
        if a.split() != b.split():
            print 'SOURCE: %s\n\nGENERATED: %s' % (a, b)
            self.assertEquals(a.split(), b.split())
