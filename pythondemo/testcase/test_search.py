import unittest
from util.HTMLTestRunner_PY3 import HTMLTestRunner

class Search:

    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print('类结束了')

    def test_search1(self):
        print('search_test1')
        assert True == self.search.search_fun()

    def test_search2(self):
        print('search_test2')
        assert True == self.search.search_fun()

    def test_search3(self):
        print('search_test3')
        assert True == self.search.search_fun()

    def test_equal(self):
        print("判断是否相等")
        self.assertEqual(1,1,"1=1吗")

    def test_true(self):
        print("判断是否是true")
        self.assertTrue(1==1,'1是1吗')

class TestSearch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print('类结束了')

    def test_search1(self):
        print('search_test1')
        assert True == self.search.search_fun()

    def test_search2(self):
        print('search_test2')
        assert True == self.search.search_fun()

    def test_search3(self):
        print('search_test3')
        assert True == self.search.search_fun()

    def test_equal(self):
        print("判断是否相等")
        self.assertEqual(1,1,"1=1吗")

    def test_true(self):
        print("判断是否是true")
        self.assertTrue(1==1,'1是1吗')

if __name__ == '__main__':
    #方法一，执行所有的测试用例
    # unittest.main()
    #方法二，执行需要的用例(批量执行测试方法)
    suite = unittest.TestSuite()
    suite.addTest(TestSearch("test_equal"))
    suite.addTest(TestSearch("testtrue"))
    unittest.TextTestRunner().run(suite)
    #方法三：批量执行测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #增加测试报告
    # report_title = '用例执行报告 我的标题'
    # desc = '用于展示修改样式后的HTMLTestRunner'
    # report_file = './result.html'
    #
    # with open(report_file, 'wb') as report:
    #     runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
    #     runner.run(suite)