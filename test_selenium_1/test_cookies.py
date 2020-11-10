#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import shelve


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    # def teardown_method(self, method):
    #     self.driver.quit()
    @pytest.mark.skip
    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    @pytest.mark.skip
    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)

    def test_cookie1(self):
        cookies = self.driver.get_cookies()
        print(cookies)

    def test_cookie(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850548696090'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325000182687'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'PDO7Bp4l5pz21J1GVFhIhZxm1bCEOg5mM-4tIJlp3EGCphMBr7frOD_QGdLLnf1F'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607600748, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1668080747, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1603101806,1603188257,1603189751'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True,
             'value': '6944625664'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': True,
             'value': '2163046706'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True,
             'value': 'o2163046706'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '75461a3126cbb39ff08f9bd58fe42c2d3b5c887a4e78ca4031e34ead02c3c44c'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3037908'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True,
             'value': '1_2163046706'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True,
             'value': '8205526055'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True,
             'value': '00010000fdcb43941d5ee20cf2e16bd1e33bc5c0500e95b36058fd986fb08c77642fbd12fb15c939a1bb8468'},
            {'domain': '.qq.com', 'expiry': 1605095147, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.15599625.1603101807'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'ycykxRqS4P'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True,
             'value': '1c9etn1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'BZICeAxkHsfHjMdbSzEZ-iFS5oEOYiCLAf-ewWlwUIqDJTXxL4SRgHHeE9OtI0bSYjR7xliaJfsVOMQSwHel2ZvHN2ZtSn_h9dZGYrETCe5gZNUa3DQvvnePqbuKVIGuh-FZfhID429S7aI-dl2nByeZMsIDyp6GhxVnXXZOxsK9Q3qc-7HXRv-YIuYc6JIaU0-7kotIRBXbQ4h2sDd-KUHJe2u3QEYZ6LQO-TGFl3mrz-Vxr_qdNuDvpCxXL0fUi4bgjn1n_JO3JeIZaEKfXg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850548696090'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1605040048, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8e0dbhv'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '4265340051991539'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "./123.xls")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "123.xls" == filename
        sleep(3)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    @pytest.mark.skip
    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "./123.xls")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "123.xls" == filename
        sleep(3)
