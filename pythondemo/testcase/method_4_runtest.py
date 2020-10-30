import unittest
from util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    test_dir = ' ./testcase '
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)


    # 增加测试报告
    report_title = '用例执行报告 我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    #在当前目录生成html格式的报告
    report_file = './result.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)