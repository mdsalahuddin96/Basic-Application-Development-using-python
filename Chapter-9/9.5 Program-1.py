import unittest
from my_unittest import add, check_even
class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 3), 7)

    def test_check_even(self):
        self.assertTrue(check_even(4))
if __name__ == '__main__':
    unittest.main()
