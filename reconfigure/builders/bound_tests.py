from reconfigure.items.bound import BoundData
from reconfigure.nodes import Node, PropertyNode
import unittest


class BoundDataTest (unittest.TestCase):

    def test_bind_property(self):
        class TestBoundData (BoundData):
            pass
        TestBoundData.bind_property('prop', 'dataprop', getter=lambda x: 'd' + x, setter=lambda x: x[1:])

        n = Node('name', children=[
                PropertyNode('prop', 'value')
            ])

        d = TestBoundData(n)

        self.assertEqual(d.dataprop, 'dvalue')
        d.dataprop = 'dnew'
        self.assertEqual(d.dataprop, 'dnew')
        self.assertEqual(n.get('prop').value, 'new')

    def test_bind_collection(self):
        class TestBoundData (BoundData):
            pass

        class TestChildData (BoundData):
            def template(self):
                return Node('', children=[PropertyNode('value', None)])

        TestBoundData.bind_collection('items', item_class=TestChildData, selector=lambda x: x.name != 'test')
        TestChildData.bind_property('value', 'value')
        n = Node('name', children=[
                Node('1', children=[PropertyNode('value', 1)]),
                Node('2', children=[PropertyNode('value', 2)]),
                Node('test', children=[PropertyNode('value', 3)]),
                Node('3', children=[PropertyNode('value', 3)]),
            ])

        d = TestBoundData(n)
        self.assertEqual(d.items[0].value, 1)
        self.assertEqual(len(d.items), 3)
        c = TestChildData()
        c.value = 4
        d.items.append(c)
        self.assertEqual(len(d.items), 4)
        self.assertEqual(d.items[-1].value, 4)


if __name__ == '__main__':
    unittest.main()
