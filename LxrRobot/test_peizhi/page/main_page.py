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
from lxr_robot.test_peizhi.page.add_host_page import AddHost
from lxr_robot.test_peizhi.page.add_user_page import AddUser
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

    def click_first_list(self, menu_text1, *args):
        sleep(2)

        self.find(By.XPATH, "//a/span[text()='%s']" % menu_text1).click()
        list_menu = []
        for i in args:
            list_menu.append(i)
        if len(list_menu) == 1:
            menu_text2 = list_menu[0]
            self.find(By.XPATH, "//a/span[text()='%s']" % menu_text2).click()
        else:
            menu_text2 = list_menu[0]
            menu_text3 = list_menu[1]
            self.find(By.XPATH, "//a/span[text()='%s']" % menu_text2).click()
            self.find(By.XPATH, "//a/span[text()='%s']" % menu_text3).click()

        if menu_text2 == '应用列表':
            return AddApp(self.driver)
        elif menu_text2 == '网络管理':
            return AddHost(self.driver)
        elif menu_text2 == '账号管理':
            return AddUser(self.driver)


        else:
            False
