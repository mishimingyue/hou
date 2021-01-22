#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from LxrRobot.test_peizhi.page.base_page import BasePage


class AddHostMessage(BasePage):

    def add_host_message(self, ip, domain):
        sleep(2)
        self.find(By.ID, "add_hosts_ip").send_keys(ip)
        self.find(By.ID, "add_hosts_main").send_keys(domain)
        self.find(By.ID, "host_add_submit").click()
        sleep(2)
        from LxrRobot.test_peizhi.page.add_host_page import AddHost
        return AddHost
