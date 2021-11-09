#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os.path
from appium import webdriver
import time
from .read_yaml import Readyaml
import threading
from common.logger import logger


#定义浏览器类
class BrowserEngine(object):
    #浏览器的路径，因为只有谷歌的weidriver，所以只加了一个
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
        #初始化这个类
    def __init__(self,driver,noReset=False):
        self.driver = driver
        self.noReset = noReset
        self.devices_num = 2

    def open_app(self,devices_numb,devices=None):
        if devices == None:
            devices = Readyaml().read()[devices_numb]
        #从这个位置读取配置文件
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
        driver = webdriver.Remote('http://localhost:{}/wd/hub'.format(devices['port']), desired_caps)
        driver.implicitly_wait(3)
        driver.get_screenshot_as_png()
        return driver

    def theading(self):
        devices = Readyaml().read()
        threads = []
        for i in devices:
            thread = threading.Thread(target=self.open_app,args=[i])
            threads.append(thread)
        for i in threads:
            i.start()
        for i in threads:
            i.join()




    #退出的方法
    def quit_browser(self):
        logger.info(' Now,close the browser')
        self.driver.quit()


