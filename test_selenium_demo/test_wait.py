from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestWait:
    # def setup(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.get("https://home.testing-studio.com/")
    #     self.driver.implicitly_wait(3)
    # def test_wait_1(self):
    #     self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()
    #     #等待直到出现“最新的页签”
    #     def wait(x):
    #         return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >1
    #         # return len([1,2]) >=1
    #     WebDriverWait(self.driver,10).until(wait)
    #     self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
    #     print("yes")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def test_baidu(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃茨")
        s
