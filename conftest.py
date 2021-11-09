import os
import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig
from common.read_yaml import Readyaml
from common.logger import logger

# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    logger.info('session级：打开浏览器')
    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "Android":
        device_conf = Readyaml().read()[1]# 读取配置文件，获取设备信息
        desired_caps = {}
        desired_caps['platformName'] = device_conf['desired_caps']['platformName']
        desired_caps['deviceName'] = device_conf['desired_caps']['deviceName']
        desired_caps['platformVersion'] = str(device_conf['desired_caps']['platformVersion'])
        desired_caps['udid'] = device_conf['desired_caps']['udid']
        desired_caps['appPackage'] = device_conf['desired_caps']['appPackage']
        desired_caps['appActivity'] = device_conf['desired_caps']['appActivity']
        desired_caps['automationName'] = device_conf['desired_caps']['automationName']
        desired_caps['unicodeKeyboard'] = device_conf['desired_caps']['unicodeKeyboard']
        desired_caps['resetKeyboard'] = device_conf['desired_caps']['resetKeyboard']
        desired_caps['noReset'] = device_conf['desired_caps']['noReset']
        desired_caps['noSign'] = device_conf['desired_caps']['noSign']
        # desired_caps['newCommandTimeout'] = 60
        RunConfig.devices = desired_caps
        driver = Remote(command_executor='http://localhost:4723/wd/hub',
                        desired_capabilities=desired_caps)
    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver

# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    logger.info('session级：关闭浏览器')
    driver.quit()


