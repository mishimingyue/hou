import pytest
def fun(x):
    return x +1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,11),
    ('a','a1')
])

def test_demo1(a,b):
    assert fun(a) == b



# def test_demo2():
#     assert fun(3) == 4

@pytest.fixture()
def login():
    username = 'Jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f"test_a        username= {login}")

    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    pytest.main(['test_1.py::TestDemo','-v'])