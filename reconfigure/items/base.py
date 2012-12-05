import pprint

class Data (object):
    def __init__(self, **props):
        self.__dict__.update(props)

    def to_dict(self):
        res_dict = {}
        for attr_key in self.__dict__:
            if not attr_key.startswith('_') and not callable(attr_key):
                attr_value = getattr(self, attr_key)
                if isinstance(attr_value, Data):
                    res_dict[attr_key] = attr_value.to_json()
                else:
                    res_dict[attr_key] = attr_value
        return res_dict

    def to_json(self):
        return self.to_dict()

    def __str__(self):
        return pprint.pformat(self.to_json(), width=2)

    def __repr__(self):
        return self.__str__()

    def unbuild(self):
        return self._builder.unbuild(self)