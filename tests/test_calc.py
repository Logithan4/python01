import unittest
from math_operations import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_add_positive_and_negative_numbers(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

    def test_add_float_numbers(self):
        result = add_numbers(2.5, 1.5)
        self.assertEqual(result, 4.0)

if __name__ == '__main__':
    unittest.main()