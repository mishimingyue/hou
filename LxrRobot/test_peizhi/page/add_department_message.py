#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from lxr_robot.test_peizhi.page.base_page import BasePage


class AppDepartmentMessage(BasePage):

    def add_department_message(self, dep_name, dep_code):
        sleep(2)
        self.find(By.ID, "name").send_keys(dep_name)
        self.find(By.ID, "code").send_keys(dep_code)
        self.find(By.ID, "submit-dept").click()
        sleep(2)
        self.driver.switch_to_alert().accept()
        from lxr_robot.test_peizhi.page.add_host_page import AddHost
        return AddHost
