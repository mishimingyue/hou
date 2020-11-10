# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from test_selenium_demo.base import Base

'''
对于弹出警告框的处理
alert().accept()
'''


class TestAlert(Base):
    def test_alert1(self):
        self.driver.get("https://www.baidu.com")
        link = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(link)
        action.perform()
        sleep(3)
        self.driver.find_element_by_link_text("搜索设置").click()
        self.driver.find_element_by_class_name("prefpanelgo").click()
        sleep(3)
        self.driver.switch_to_alert().accept()
