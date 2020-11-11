#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_selenium_2.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # assert self.index.goto_login().goto_register().register()
        assert self.index.goto_register().register()
