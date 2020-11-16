from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "Android Emulator"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
caps["dontStopAppOnReset"] = "true"
caps["skipDeviceInitialization"] = "true"
caps["noReset"] = "True"  # 是否重置

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu:id/current_price']")
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator))
ele = driver.find_element(*locator)
print(ele.text)
