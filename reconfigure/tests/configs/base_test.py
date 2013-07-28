import unittest
import json


class BaseConfigTest (unittest.TestCase):
    sources = ""
    result = None
    config = None
    config_kwargs = {}
    stringify_filter = staticmethod(lambda x: x.split())

    def test_config(self):
        if not self.config:
            return

        self.maxDiff = None

        config = self.config(content=self.sources[None], **self.config_kwargs)
        if config.includer:
            config.includer.content_map = self.sources
        config.load()
        #print 'RESULT', config.tree.to_dict()
        #print 'SOURCE', self.__class__.result
        #self.assertTrue(self.__class__.result== config.tree.to_dict())
        a, b = self.__class__.result, config.tree.to_dict()
        if a != b:
            print 'SOURCE: %s\nGENERATED: %s\n' % (json.dumps(a, indent=4), json.dumps(b, indent=4))
        self.assertEquals(a, b)

        result = config.save()
        s_filter = self.__class__.stringify_filter
        #print s_filter(result[None])
        for k, v in result.iteritems():
            self.assertEquals(
                s_filter(self.__class__.sources[k]),
                s_filter(v)
            )
