#!/usr/bin/python3
"""unit test module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class testing(unittest.TestCase):
    """testing for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_integer_2(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer_3(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_integer_4(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_max_integer_5(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max_integer_6(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_7(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3, "should be 3")

    def wrong_input(self):
        with self.assertRaises(TypeError):
            max_integer((1, 2))

    def test_empty(self):
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
