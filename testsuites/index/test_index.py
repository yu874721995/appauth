#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: test_index.py
@time: 2021/8/17 17:17
@desc: 
"""
import sys
from time import sleep
import pytest
from common.page import Page

class TestIndex:
    """首页"""

    def test_index(self, browser):
        """
        名称：首页-点击登录
        步骤：
        1、打开浏览器
        检查点：
        * 检查页面标题是否包含关键字。
        """
        pass
        # driver = Index(browser)
        # driver.cha.click()