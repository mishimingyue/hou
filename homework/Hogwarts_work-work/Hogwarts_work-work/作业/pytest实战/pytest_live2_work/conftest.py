import pytest

from 作业.pytest实战.calc import Calc


@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calc()
    yield calc
    print("计算结束")
