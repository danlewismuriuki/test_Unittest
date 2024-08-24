from math_functions import add, subtract, divide, multiply

import unittest


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

        with self.assertRaises(ValueError):
            divide(4, 0)

        with self.assertRaises(TypeError):
            divide(4, 2, 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 1), 2)


if __name__ == "__main__":
    unittest.main()
