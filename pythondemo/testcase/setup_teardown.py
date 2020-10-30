# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestHou(unittest.TestCase):
    def setUp(self) -> None:
        print('准备工作')

    def tearDown(self) -> None:
        print('结束了')

    @classmethod
    def setUpClass(cls) -> None:
        print('类开始了')

    @classmethod
    def tearDownClass(cls) -> None:
        print('类结束了')

    @unittest.skip
    def test_first(self):
        self.assertEqual(8,8)
        print('111')

    def test_second(self):
        self.assertEqual(9,9)
        print('222')

if __name__ == '__main__':
    unittest.main()












