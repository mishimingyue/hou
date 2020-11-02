from homework.pytest_homework.cal_demo import Calculator
import pytest
import yaml


def get_data(method):
    with open("./cal.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        # print(datas['add'])
        # print(datas['add']['datas'])
        # print(datas['add']['datas'][0])
        if method == 'add':
            adds_data = datas['add']['datas']
            add_id = datas['add']['ids']
            return [adds_data, add_id]
        elif method == 'sub':
            sub_data = datas['sub']['datas']
            sub_id = datas['sub']['ids']
            return [sub_data, sub_id]
        elif method == 'mul':
            mul_data = datas['mul']['datas']
            mul_id = datas['mul']['ids']
            return [mul_data, mul_id]
        elif method == 'div':
            div_data = datas['div']['data']
            div_id = datas['div']['ids']
            return [div_data, div_id]
        else:
            print("不存在的运算方式")


class TestCalc:
    @pytest.mark.parametrize('a,b,expect', get_data('add')[0], ids=get_data('add')[1])
    @pytest.mark.run(order=1)
    def testcase_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_data('sub')[0], ids=get_data('sub'[1]))
    @pytest.mark.run(order=2)
    def testcase_sub(self, get_calc, a, b, expect):
        assert get_calc.sub(a, b) == expect

    @pytest.mark.parametrize('a,b,expect', get_data('mul')[0], ids=get_data('mul'[1]))
    @pytest.mark.run(order=3)
    def testcase_mul(self, get_calc, a, b, expect):
        assert round(get_calc.mul(a, b), 2) == expect

    @pytest.mark.parametrize('a,b,expect', get_data('div')[0], ids=get_data('div')[1])
    @pytest.mark.run(order=4)
    def testcase_div(self, get_calc, a, b, expect):
        assert get_calc.div(a, b) == expect
# print(get_data('add'))
# print(get_data('add')[0])
# print(get_data('add')[0][0])
