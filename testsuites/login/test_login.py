#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: test_login.py
@time: 2021/8/17 10:57
@desc: 
"""
import sys
from time import sleep
import pytest

from element.ele_login import Login
from common.page import Page

class TestLogin:
    """首页"""

    def test_login(self, browser):
        """
        名称：首页-点击登录
        步骤：
        1、打开浏览器
        检查点：
        * 检查页面标题是否包含关键字。
        """
        driver = Page(browser)
        driver.send_keys(Login.code,'80008')
        driver.click(Login.login_define)

    def test_login2(self, browser):
        """
        名称：首页-点击登录
        步骤：
        1、打开浏览器
        检查点：
        * 检查页面标题是否包含关键字。
        """
        driver = Page(browser)
        driver.send_keys(Login.code,'80008')
