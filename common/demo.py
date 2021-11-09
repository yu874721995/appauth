#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: demo.py
@time: 2021/8/23 17:48
@desc: 
"""
from common.read_yaml import Readyaml

devices = Readyaml().read()[0]
# 从这个位置读取配置文件
desired_caps = {}
desired_caps['platformName'] = devices['desired_caps']['platformName']
desired_caps['deviceName'] = devices['desired_caps']['deviceName']
desired_caps['platformVersion'] = devices['desired_caps']['platformVersion']
desired_caps['appPackage'] = devices['desired_caps']['appPackage']
desired_caps['appActivity'] = devices['desired_caps']['appActivity']
desired_caps['automationName'] = devices['desired_caps']['automationName']
desired_caps['unicodeKeyboard'] = devices['desired_caps']['unicodeKeyboard']
desired_caps['resetKeyboard'] = devices['desired_caps']['resetKeyboard']
desired_caps['noReset'] = devices['desired_caps']['noReset']
desired_caps['noSign'] = devices['desired_caps']['noSign']
desired_caps['udid'] = devices['desired_caps']['udid']
desired_caps['newCommandTimeout'] = 120
print(desired_caps)