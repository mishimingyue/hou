from library.calc_demo import Calculator
import pytest


class Test2:
    def setup(self):
        print("计算开始了")
        self.calc = Calculator()

    def teardown(self):
        print("结束了")

    def test_add1(self):
        result = self.calc.add(1, 1)
        assert result == 2

    def test_add2(self):
        result = self.calc.add(1, 3)
        assert result == 4

    def test_add3(self):
        result = self.calc.add(2, 1)
        assert result == 3
