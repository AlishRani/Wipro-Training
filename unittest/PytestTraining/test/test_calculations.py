import pytest

from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    def test_add(self):
        res = self.calc.add(10 , 5)
        assert res == 15,'Add Error'

    def test_sub(self):
        res =self.calc.sub(10,5)
        assert res == 5, 'Sub Error'

    def test_mul(self):
        res = self.calc.mul(10,5)
        assert res == 50, 'mul Error'

    def test_div(self):
        res = self.calc.div(10,5)
        assert res == 2 , 'div error'