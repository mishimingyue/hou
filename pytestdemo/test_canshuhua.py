from library.calc_demo import Calculator
import pytest
import yaml


class Test2:
    def setup(self):
        print("计算开始了")
        self.calc = Calculator()

    def teardown(self):
        print("结束了")

    @pytest.mark.parametrize('a,b,expect', [(1, 1, 2), (2, 2, 4), (3, 3, 6)])
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

# class Test2:
#     @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
#     def test_data(self,a,b):
#        print(a+b)
