#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from lxr_robot.test_peizhi.page.base_page import BasePage


class AppMessage(BasePage):

    def app_message(self, app_name, app_configuration, app_protocol, app_port, app_ip, app_url):
        self.find(By.ID, "name").send_keys(app_name)

        # self.find(By.ID,"appType").find_elements_by_tag_name("option")[1].click()

        self.find(By.ID, "appType").find_elements_by_tag_name("option")[int(app_configuration)].click()

        # self.find(By.ID, "urlProtol").find_elements_by_tag_name("option")[1].click()
        # self.find(By.ID, "urlProtol").find_elements_by_xpath("//option[@value='HTTP']").click()

        Select(self.find(By.ID, "urlProtol")).select_by_value(app_protocol)
        self.find(By.ID, "port").clear()

        self.find(By.ID, "port").send_keys(int(app_port))

        self.find(By.ID, "loginAddr").send_keys(app_ip)

        self.find(By.ID, "loginUri").send_keys(app_url)

        self.find(By.ID, "app_submit").click()

        from lxr_robot.test_peizhi.page.add_app_page import AddApp
        return AddApp

# ,app_configuration,app_protocol,app_port,app_ip,app_url
