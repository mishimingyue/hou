from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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

# 滑动页面
action = TouchAction(driver)
print(driver.get_window_rect())
window_rect = driver.get_window_rect()
width = window_rect['width']
height = window_rect['height']
x1 = int(width / 2)
y_start = int(height * 4 / 5)
y_end = int(height * 1 / 5)
action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
# action.press(x=353,y=462).move_to(x=353,y=1600).release().perform()


# element = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
# search_enabled = element.is_enabled()
# print(element.text)
# print(element.location)
# print(element.size)
# if search_enabled == True:
#     element.click()
#     driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")


# driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
# driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
# sleep(2)
# driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
# current_price = float(driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
