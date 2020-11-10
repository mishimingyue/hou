# -*- coding:utf-8 -*-
from test_selenium_demo.base import Base
from time import sleep
import pytest

'''
1.获取当前窗口句柄（driver.current_window_handle）
2.获取所有窗口句柄（driver.windows_handles）
3.判断是否是想要的窗口，如果是就执行，如果不是就跳转至另一个，对另一个进行操作switch_to_window()
示例：百度注册
'''


class TestWindows(Base):
    @pytest.mark.skip
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        window_current = self.driver.current_window_handle
        self.driver.find_element_by_link_text("立即注册").click()
        windows = self.driver.window_handles
        for handle in windows:
            if handle != window_current:
                self.driver.switch_to_window(handle)
                print('now is register window')
                self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("hou")
                sleep(5)
                self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys(17829080570)
                sleep(3)

    '''
    示例：
    https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    Web中存在表单嵌套的情况，webdriver只可以在一个页面上定位，无法定位内嵌页面上的元素
    Frame分类：frameset  frame   iframe
    切换方式：
    driver.switch_to.frame()
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()

    嵌套的情况：
    先进父，后进子：
    driver.switch_to.frame(“父”)
    driver.switch_to.frame(“子”)

    '''

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("droppable"))
        sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
