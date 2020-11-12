#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_selenium_3.test_demo1.page.main_page import MainPage
import pytest


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaa5"
        account = "aaaaaah_hogwar5"
        phonenum = "13400010005"
        # assert self.main.goto_addmember().add_member()
        addmemebr = self.main.goto_addmember()
        addmemebr.add_member(username, account, phonenum)
        assert username in addmemebr.get_member(username)
