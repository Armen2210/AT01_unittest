import unittest
# from main import add, subtract, multiply, divide
# from main import check
from main import divide

# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 5), 7)
#         self.assertEqual(add(2, 5), 9)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(7, 5), 2)
#         self.assertEqual(subtract(15, 5), 4)
#
#     def test_multiply(self):
#         self.assertEqual(multiply(7, 5), 35)
#         self.assertEqual(multiply(15, 5), 4)
#
#     def test_divide(self):
#         self.assertEqual(divide(10, 5), 2)
#         self.assertEqual(divide(15, 5), 4)



# class TestCheck(unittest.TestCase):
#     def test_check(self):
#         self.assertTrue(check(2))
#         self.assertTrue(check(5))
#         self.assertTrue(check(50))
#
#         self.assertTrue(not check(1))
#         self.assertTrue(not check(3))
#         self.assertTrue(not check(57))
#
#         self.assertFalse(not check(1))
#         self.assertFalse(not check(3))
#         self.assertFalse(not check(57))


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)



if __name__ == '__main__':
    unittest.main()