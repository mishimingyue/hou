#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lxr_robot.test_peizhi.page.base_page import BasePage


class AddHost(BasePage):
    def add_host_page(self):
        sleep(3)
        self.find(By.ID, "hosts_add").click()
        from lxr_robot.test_peizhi.page.add_host_message import AddHostMessage
        return AddHostMessage(self.driver)
