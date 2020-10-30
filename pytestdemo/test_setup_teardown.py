from library.calc_demo import Calculator
import pytest


class TestHou:
    # 方法前后执行steup，teardown
    def setup(self):
        print("方法开始了：")

    def teardown(self):
        print("方法结束了：")

    # 类前后执行steup_class，teardown_class
    def setup_class(self):
        print("类开始了:")

    def teardown_class(self):
        print('类结束了')

    def test_add(self):
        calc = Calculator()
        result = calc.add(1, 1)
        print("运行中")
        assert result == 2

# def test_a():
#     print("123")
# 方法前后执行steup_function，teardown_function
# def setup_function():
#     print("456")
# def teardown_function():
#     print("789")
