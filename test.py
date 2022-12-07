import unittest
from kr import *

class Testsnakecase(unittest.TestCase):

    def test_snake(self):
        s = NameConverterSnake('Test_test-Testing')
        res = s.to_snake_case()
        self.assertEqual(res, 'test_test__testing')

class Testcamelcase(unittest.TestCase):

    def test_camel(self):
        d = NameConverterCamel('Test_test-Testing')
        res = d.to_camel_case()
        self.assertEqual(res, 'TestTestTesting')

if __name__ == '__main__':
    unittest.main()