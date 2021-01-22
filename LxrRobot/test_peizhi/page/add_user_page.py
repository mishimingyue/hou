#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lxr_robot.test_peizhi.page.base_page import BasePage


class AddUser(BasePage):

    def add_department_page(self):
        sleep(3)
        self.find(By.ID, "add-dept").click()
        from lxr_robot.test_peizhi.page.app_message import AppMessage
        from lxr_robot.test_peizhi.page.add_department_message import AppDepartmentMessage
        return AppDepartmentMessage(self.driver)

    def add_user_page(self):
        sleep(3)
