'''
作业1：

1、补全计算器（加减乘除）的测试用例
2、使用数据的数据驱动，节省代码编写量
3、创建 Fixture 方法实现，测试开始前打印【开始计算】，测试结束后打印【计算结束】
4、将 Fixture 方法存放在conftest.py ，设置scope=module

作业2：

1、控制用例执行顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
3、结合allure 生成测试结果报告
'''

import pytest
import yaml


def get_datas():
    with open("./test_calc_yaml_fixture.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']  # 通过add这个key拿到datas这个key,然后赋值给add_datas
    sub_datas = datas['sub']['datas']
    mul_datas = datas['mul']['datas']
    div_datas = datas['div']['datas']
    return [add_datas, sub_datas, mul_datas, div_datas]


class TestCalc():

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[1])
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[2])
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[3])
    @pytest.mark.run(order=-1)
    def test_div(self, get_calc, a, b, expect):
        if b == 0:
            print("除数不能为0")
        else:
            result = get_calc.div(a, b)
            assert result == expect
