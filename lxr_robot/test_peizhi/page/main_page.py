#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from lxr_robot.test_peizhi.page.add_app_page import AddAppPage
from lxr_robot.test_peizhi.page.add_app_page import AddApp
from lxr_robot.test_peizhi.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://192.168.71.12:8080/"

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    def login(self, username, password):
        self.find(By.ID, "name").send_keys(username)
        self.find(By.ID, "password").send_keys(password)
        self.find(By.CSS_SELECTOR, ".login-con-div2").click()

    def click_first_list(self, menu_text1, menu_text2):
        sleep(2)

        self.find(By.XPATH, "//a/span[text()='%s']" % menu_text1).click()
        self.find(By.XPATH, "//a/span[text()='%s']" % menu_text2).click()
        return AddApp(self.driver)

