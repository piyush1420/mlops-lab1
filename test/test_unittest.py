import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        # fun4(x, y) = fun1 + fun2 + fun3, e.g. (2+3) + (2-3) + (2*3) = 10
        self.assertEqual(calculator.fun4(2, 3), 10)
        self.assertEqual(calculator.fun4(5, 0), 10)
        self.assertEqual(calculator.fun4(-1, 1), -3)
        self.assertEqual(calculator.fun4(-1, -1), -1)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5)
        self.assertEqual(calculator.fun5(7, 2), 3.5)
        self.assertEqual(calculator.fun5(-9, 3), -3)
        with self.assertRaises(ValueError):
            calculator.fun5(5, 0)
        with self.assertRaises(ValueError):
            calculator.fun5("a", 2)

    def test_fun6(self):
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 0), 1)
        self.assertEqual(calculator.fun6(2, -1), 0.5)
        with self.assertRaises(ValueError):
            calculator.fun6(0, -1)

    def test_fun7(self):
        self.assertEqual(calculator.fun7([2, 4, 6]), 4)
        self.assertEqual(calculator.fun7([1.5, 2.5]), 2)
        with self.assertRaises(ValueError):
            calculator.fun7([])
        with self.assertRaises(ValueError):
            calculator.fun7([1, "a", 3])

    def test_fun8(self):
        self.assertEqual(calculator.fun8(16), 4)
        self.assertEqual(calculator.fun8(2.25), 1.5)
        with self.assertRaises(ValueError):
            calculator.fun8(-4)

    def test_rejects_true_and_false(self):
        with self.assertRaises(ValueError):
            calculator.fun1(True, 2)


if __name__ == '__main__':
    unittest.main()
