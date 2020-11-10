from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import TouchActions

'''
ActionsChains 类提供了鼠标操作的常用方法：
perform()执行所有ActionsChains中存储的行为
context_click()右击
double_click()双击
drag_and_drop()拖动
move_to_element()鼠标悬停
'''


class TestAction():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elemenet_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        # 双击
        elemenet_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        # 右击
        elemenet_rightclick = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(elemenet_click)
        action.context_click(elemenet_rightclick)
        action.double_click(elemenet_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    # 将鼠标悬停在”设置“处
    # @pytest.mark.skip
    def test_movetoelment(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/draDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

        sleep(3)

    '''
    Keys()提供了键盘操作
    send_keys(Keys.BACK_SPACE)  
    send_keys(Keys.SPACE)
    send_keys(Keys.TAB)
    send_keys(Keys.ESCAPE)   回退（esc）
    send_keys(Keys.ENTER)    回车键
    send_keys(Keys.CONTROL,'a')

    '''

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("1234")
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(Keys.ENTER)

    '''
    1.打开浏览器
    2.打开百度
    3.输入“selenium”
    4.点击搜索
    5.滑动到最后
    6.关闭
    '''

    def test_case_1(self):
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        sleep(3)
        action_search = TouchActions(self.driver)
        action_search.tap(self.driver.find_element_by_id("su")).perform()
        el = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.scroll_from_element(el, 0, 10000).perform()
        sleep(3)
        self.driver.find_element_by_css_selector("#page > a.n").click()
        sleep(2)
