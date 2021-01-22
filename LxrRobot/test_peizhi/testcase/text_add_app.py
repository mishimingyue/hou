#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxr_robot.test_peizhi.page.main_page import MainPage
from time import sleep
import yaml

with open('../datas/apps.yml') as f:
    my_apps = yaml.safe_load(f)
    app1 = my_apps['apps1']
    app2 = my_apps['apps2']
    app3 = my_apps['apps3']
    app4 = my_apps['apps4']

    app1_name = app1['app_name']
    app1_configuration = app1['app_configuration']
    app1_protocol = app1['app_protocol']
    app1_port = app1['app_port']
    app1_ip = app1['app_ip']
    app1_url = app1['app_url']


class TestLXR:
    def setup(self):
        self.main = MainPage()

    def test_add_app(self):
        username = "superman"
        password = "talent"
        self.main.login(username, password)
        sleep(3)
        self.main.click_first_list('应用管理', '应用列表').add_app_page().app_message(app1_name, app1_configuration,
                                                                              app1_protocol, app1_port, app1_ip,
                                                                              app1_url)

        # self.main.click_first_list('应用管理', '应用列表').add_app_page().app_message({app1_name}, {app1_configuration},{app1_protocol}, {app1_port}, {app1_ip},{app1_url})

    def test_add_hosts(self):
        username = "superman"
        password = "talent"
        self.main.login(username, password)
        sleep(3)
        self.main.click_first_list('系统管理', '网络管理', 'HOST').add_host_page().add_host_message('1.1.1.1', 'hou1.test')

    def test_add_user(self):
        username = "superman"
        password = "talent"
        self.main.login(username, password)
        sleep(3)
        self.main.click_first_list('用户管理', '账号管理')
        # .add_department_page().add_department_message('dep_1','code_1')
