#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lxr_robot.test_peizhi.page.base_page import BasePage


class AddApp(BasePage):

    def add_app_page(self):
        sleep(3)
        self.find(By.ID, "add_app").click()
        from lxr_robot.test_peizhi.page.app_message import AppMessage
        return AppMessage(self.driver)
