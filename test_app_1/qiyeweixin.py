#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "Android Emulator"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.WwMainActivity"
# noReset 保留缓存， 比如登录状态
caps["noReset"] = "True"
# 不停止应用，直接运行测试用例
caps["dontStopAppOnReset"] = "true"
caps['skipDeviceInitialization'] = 'true'
caps['skipServerInstallation'] = 'true'
# caps["settings[waitForIdleTimeout]"] = 0
# 关键  localhost:4723  本机ip:server端口
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)
