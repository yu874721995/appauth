#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: conftest.py
@time: 2021/8/17 15:53
@desc: 
"""
# 启动app
import pytest
from time import sleep
from element.ele_login import Login
from element.ele_index import Index
from element.ele_public import Public
from common.page import Page

@pytest.fixture(scope='module', autouse=True)
def test_old_login(browser):
    """
    名称：打开app进入首页 老用户
    """
    driver = Page(browser)
    driver.click(Public.authority_true)
    driver.click(Login.protocol_true)
    driver.click(Login.other_phone_login)
    driver.send_keys(Login.phone,'18511110003')
    driver.send_keys(Login.code,'80008')
    driver.click(Login.login_define)
    driver.click(Public.authority_true)
    driver.click(Index.guide_one)
    driver.click(Index.guide_tow)
    driver.click(Index.guide_three)
    driver.click(Index.guide_four)
    return driver

@pytest.fixture(scope='module')
def test_new_login(browser):
    """
    名称：打开app进入首页 新用户
    """
    driver = Page(browser)
    driver.click(Public.authority_true)
    driver.click(Login.window_false)
    driver.click(Login.protocol_true)
    driver.click(Login.other_phone_login)
    driver.send_keys(Login.phone,'18511110012')
    driver.send_keys(Login.code,'80008')
    driver.click(Login.login_define)
    driver.click(Login.sex_boy)
    driver.click(Login.sex_define)
    driver.click(Login.random_name)
    driver.click(Login.set_avatar)
    driver.click(Login.select_from_album)
    driver.click(Public.authority_true)
    driver.click(Public.authority_true)
    sleep(2)
    driver.click(Login.tvCheck)
    driver.click(Login.picture_right)
    driver.click(Login.menu_crop)
    sleep(2)
    driver.click(Login.info_define)
    driver.click(Index.guide_one)
    driver.click(Index.guide_tow)
    driver.click(Index.guide_three)
    driver.click(Index.guide_four)
    return driver

