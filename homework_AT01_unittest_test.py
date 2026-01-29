import unittest
from homework_AT01_unittest import add, subtract, multiply, divide, remainder


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(4, 5), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(15, 5), 10)

    def test_multiply(self):
        self.assertEqual(multiply(7, 5), 35)
        self.assertEqual(multiply(15, 5), 75)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(15, 5), 3)

    def test_remainder(self):
        self.assertEqual(remainder(11, 5), 1)
        self.assertEqual(remainder(21, 6), 3)

    def test_remainder_by_zero(self):
        self.assertRaises(ValueError, divide, 10, 0)

