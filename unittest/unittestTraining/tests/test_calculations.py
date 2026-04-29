import unittest

from src.calculations import add, sub, mul


class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(n1=10, n2=5)
        self.assertEqual(res, 15, msg='Addition Err')

    def test_sub(self):
        res = sub(n1=10, n2=5)
        self.assertEqual(res, 5, "Subtraction Error")

    def test_mul(self):
        res = mul(n1=10, n2=5)
        self.assertEqual(res, 50, "Multiplication error")
