# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "Android Emulator"
caps["appPackage"] = "com.topsec.topsap"
caps["appActivity"] = "com.topsec.topsap.ui.WelcomeActivity"
caps["automationName"] = "Uiautomator2"
caps["noReset"] = "True"  # 是否重置

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.topsec.topsap:id/ip")
el1.send_keys("https://172.18.31.236")
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText")
el2.send_keys("test")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText")
el3.send_keys("123456")
el4 = driver.find_element_by_id("com.topsec.topsap:id/btn_login")
el4.click()
el5 = driver.find_element_by_id("android:id/button1")
el5.click()
sleep(3)
driver.back()
sleep(2)
driver.back()

driver.quit()
