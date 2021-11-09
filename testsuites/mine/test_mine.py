#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: test_mine.py
@time: 2021/8/20 11:19
@desc: 
"""
import sys
from time import sleep
import pytest

from element.ele_mine import Mine
from common.page import Page

class TestMine:

    def test_my_page(self,browser):
        driver = Page(browser)
        driver.click(Mine.mine)
        driver.click(Mine.personal_data)
        driver.click(Mine.data_edit)
        driver.click(Mine.name_click_edit)
        driver.send_keys(Mine.name_edit,'test123')
        driver.click(Mine.name_edit_ok)
