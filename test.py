import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 5) == 10



    def test_division_success(self):
        assert self.calc.division(self, 10, 5) == 2


    def test_substraction_success(self):
        assert self.calc.subtraction(self, 12, 5) == 7


    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 5) == 25


    def teardown(self):
        print('выполнение метода Teardown')
