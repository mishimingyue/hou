import pytest
import yaml

from homework.pytest_homework.cal_demo import Calculator


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    print("【开始计算】")
    yield calc
    print("【计算结束】")
