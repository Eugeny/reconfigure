class BaseConfigTest (object):
    sources = ""
    result = None
    config = None
    config_kwargs = {}

    def test_config(self):
        self.maxDiff = None

        config = self.config(content=self.sources[None], **self.config_kwargs)
        if config.includer:
            config.includer.content_map = self.sources
        config.load()
        #print 'RESULT', config.tree.to_dict()
        #print 'SOURCE', self.__class__.result
        #self.assertTrue(self.__class__.result== config.tree.to_dict())
        self.assertEquals(self.__class__.result, config.tree.to_dict())
        result = config.save()
        #print result
        for k, v in result.iteritems():
            self.assertEquals(self.__class__.sources[k].split(), v.split())
