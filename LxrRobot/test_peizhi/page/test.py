from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://192.168.71.12:8080/")
driver.find_element_by_id("name").send_keys("superman")
driver.find_element_by_id("password").send_keys("talent")
driver.find_element_by_css_selector(".login-con-div2").click()
sleep(3)
driver.find_element_by_xpath("//a/span[text()='应用管理']").click()
sleep(2)
driver.find_element_by_xpath("//a/span[text()='应用列表']").click()
