#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''基类，存放所有操作方法'''
import time
import os.path
from datetime import datetime

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import wraps
from selenium.webdriver.support import expected_conditions as EC
from config import RunConfig
from common.logger import logger

# Map PageElement constructor arguments to webdriver locator enums
LOCATOR_LIST = {
    # selenium
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    # appium
    'ios_uiautomation': MobileBy.IOS_UIAUTOMATION,
    'ios_predicate': MobileBy.IOS_PREDICATE,
    'ios_class_chain': MobileBy.IOS_CLASS_CHAIN,
    'android_uiautomator': MobileBy.ANDROID_UIAUTOMATOR,
    'android_viewtag': MobileBy.ANDROID_VIEWTAG,
    'android_data_matcher': MobileBy.ANDROID_DATA_MATCHER,
    'android_view_matcher': MobileBy.ANDROID_VIEW_MATCHER,
    'windows_uiautomation': MobileBy.WINDOWS_UI_AUTOMATION,
    'accessibility_id': MobileBy.ACCESSIBILITY_ID,
    'image': MobileBy.IMAGE,
    'custom': MobileBy.CUSTOM,
}


class Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.desc = None
        self.element = True

    def pre_func(func):
        @wraps(func)
        def wrapper(self, *args):
            logger.info('执行函数：{}'.format(func.__name__))
            if len(args) == 1:
                try:
                    self.element = args[0]
                    el = self.find_element(self.element)
                    return func(self, el)
                except Exception as e:
                    self.get_window()
                    raise NameError('定位元素错误')
            else:
                repit = []
                self.element = args[0]
                for i in range(len(args)):
                    if i == 0:
                        el = self.find_element(self.element)
                        repit.append(el)
                        continue
                    repit.append(args[i])
                repit = tuple(repit)
                return func(self, *repit)
        return wrapper

    def contexts(self):
        '''返回当前会话中的所有上下文，使用后可以识别H5页面的控件'''
        contexts = self.driver.contexts()
        logger.info(u'查询当前上下文：{}'.format(contexts))
        return contexts

    def current_context(self):
        '''返回当前会话的"当前上下文",即当前处于哪一个上下文'''
        current_context = self.driver.current_context()
        return current_context

    def context(self):
        '''返回当前会话的当前上下文'''
        context = self.driver.context()
        return context

    def close_app(self):
        '''关闭app'''
        try:
            self.driver.close_app()
            logger.info(u'关闭app')
        except NameError as e:
            logger.error(u'%s' % e)

    def get_window(self):
        '''截图，file方法截取的图片为全屏，另外两个截图方法分别为get_screenshot_as_base64和get_screenshot_as_png'''
        file_path = RunConfig.PRO_PATH + '/image/'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = file_path + file_time + self.desc + '.png'
        try:
            self.driver.get_screenshot_as_file(file_name)
            logger.error('用例执行至 {} 失败 截图并保存至：{}'.format(self.desc, file_name))
        except NameError as a:
            logger.error(u'截图失败，失败原因：%s' % a)

    def element_is_display(self, element):
        '''场景无法使用'''
        def element_loc(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                logger.info('执行函数：{}'.format(func.__name__))
                elements = WebDriverWait(self.driver, 3, 0.5).until(self.find_element(element))
                if elements:
                    return func(*args, **kwargs)
                else:
                    raise NoSuchElementException('没有找到元素')
            return wrapper
        return element_loc

    def find_element(self, kwargs):
        index = None
        if len(kwargs) > 3:
            logger.error('最多指定三个参数')
            raise ValueError("最多指定三个参数")
        selector = kwargs[0]
        self.desc = kwargs[1]
        if len(kwargs) == 3:
            index = kwargs[2]
        if '=>' not in selector:
            logger.error("请指定定位器或定位器格式有误 元素信息:".format(selector))
            raise ValueError("请指定定位器或定位器格式有误")
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by in LOCATOR_LIST.keys():
            selector_by = LOCATOR_LIST[selector_by]
        else:
            logger.error('不支持 {} 类型的元素'.format(selector_by))
            raise ValueError('不支持 {} 类型的元素'.format(selector_by))
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((selector_by, selector_value)))
            if index == None:
                element = self.driver.find_element(selector_by, selector_value)
            else:
                element = self.driver.find_elements(selector_by, selector_value)[index]
            logger.info("✅ 查找元素: {} ".format(selector))
            return element
        except Exception as e:
            error_msg = "❌ 查找元素: {}".format(selector)
            logger.error(error_msg)
            raise Exception(str(e))

    def scroll(self, origin_el, destination_el):
        element1 = WebDriverWait(self.driver, 3, 0.5).until(self.find_element(origin_el))
        element2 = WebDriverWait(self.driver, 3, 0.5).until(self.find_element(destination_el))
        if element1 and element2:
            pass
        else:
            return NoSuchElementException('没有找到元素')
        '''从元素origin_el滚动至元素destination_el'''
        self.driver.scroll(origin_el, destination_el)

    def drag_and_drop(self, origin_el, destination_el):
        element1 = WebDriverWait(self.driver, 3, 0.5).until(self.find_element(origin_el))
        element2 = WebDriverWait(self.driver, 3, 0.5).until(self.find_element(destination_el))
        if element1 and element2:
            pass
        else:
            return NoSuchElementException('没有找到元素')
        '''将元素origin_el拖到目标元素destination_el'''
        self.driver.drag_and_drop(origin_el, destination_el)

    def tap(self, positions, duration=None):
        '''模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）'''
        '''
        positions:手指点击的位置，class:list
        duration:毫秒，为空时单击，设置后为长按
        '''
        self.driver.tap(positions, duration)

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        '''
        从A点滑动至B点，滑动时间为毫秒
        :param start_x:开始的位置 x坐标
        :param start_y:开始的位置 y坐标
        :param end_x:结束的位置 x坐标
        :param end_y:结束的位置 y坐标
        :param duration:滑动时间
        :return:
        '''
        self.driver.swipe(start_x, start_y, end_x, end_y, 500)

    def flick(self, start_x, start_y, end_x, end_y):
        '''
        按住A点后快速滑动至B点
        :param start_x:开始的位置 x坐标
        :param start_y:开始的位置 y坐标
        :param end_x:结束的位置 x坐标
        :param end_y:结束的位置 y坐标
        :return:
        '''
        self.driver.flick(start_x, start_y, end_x, end_y)

    def pinch(self, element, percent=200, steps=50):
        '''
        在元素上执行模拟双指捏（缩小操作）
        :param element:缩小的元素
        :param percent:缩小的比例
        :param steps:
        :return:
        '''
        self.find_element(element)
        self.driver.pinch(element)

    def zoom(self, element, percent=200, steps=50):
        '''
        在元素上执行放大操作
        :param element:
        :param percent:
        :param steps:
        :return:
        '''
        self.find_element(element)
        self.driver.zoom(element)

    def reset(self):
        '''
        重置app
        :return:
        '''
        self.driver.reset()

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        '''
        隐藏键盘,iOS使用key_name隐藏，安卓不使用参数
        :param key_name: ios需要，android不需要
        :param key:
        :param strategy:
        :return:
        '''
        if key_name != None:
            self.driver.hide_keyboard(key_name)
        else:
            self.driver.hide_keyboard()

    def keyevent(self, keycode, metastate=None):
        '''
        按键码，例如返回、桌面等手机自带按钮,还有一个keycode方法与其功能一致
        :param keycode: 按键码
            左上键（菜单） ：KEYCODE_MENU 82
            电话键： KEYCODE_CALL 5
            上键： KEYCODE_DPAD_UP 19
            左键： KEYCODE_DPAD_LEFT 21
            下键： KEYCODE_DPAD_DOWN 20
            右键： KEYCODE_DPAD_RIGHT 22
            返回键： KEYCODE_BACK 4
            1键： KEYCODE_1 8
            2键： KEYCODE_2 9
            3键： KEYCODE_3 10
            4键： KEYCODE_4 11
            5键： KEYCODE_5 12
            6键： KEYCODE_6 13
            7键： KEYCODE_7 14
            8键： KEYCODE_8 15
            9键： KEYCODE_9 16
            *键： KEYCODE_STAR 19
            0键： KEYCODE_0 7
            #键： KEYCODE_POUND 18
        :param metastate:
        :return:
        '''
        self.driver.keyevent(keycode)

    def long_press_keycode(self, keycode, metastate=None):
        '''
        发送一个长按的按键码（长按某键）
        :param keycode:
        :param metastate:
        :return:
        '''
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        '''
        获取当前的activity
        :return:
        '''
        return self.driver.current_activity()

    def wait_activity(self, activity, timeout, interval=1):
        '''
        等待指定的activity出现直至超时
        :param activity: 指定的activity
        :param timeout:超时时间
        :param interval:扫描间隔
        :return:
        '''
        self.driver.wait_activity(activity, timeout, interval)

    def background_app(self, seconds):
        '''
        后台运行app
        :param seconds: 后台运行时间
        :return:
        '''
        self.driver.background_app(seconds)

    def is_app_installed(self, appPackages):
        '''
        检查app是否安装
        :param bundle_id:包名
        :return:
        '''
        self.driver.is_app_installed(appPackages)

    def install_app(self, app_path):
        '''
        install app
        :param app_path:
        :return:
        '''
        self.driver.install_app(app_path)

    def remove_app(self, appPackages):
        '''
        uninstall app
        :param appPackages:
        :return:
        '''
        self.driver.remove_app(appPackages)

    def launch_app(self):
        '''
        start app
        :return:
        '''
        self.driver.launch_app()

    def start_activity(self, app_package, app_activity, **opts):
        '''
        在测试过程中打开任意活动。如果活动属于另一个应用程序，该应用程序的启动和活动被打开。
        :param app_package:
        :param app_activity:
        :param opts:
        - app_wait_package - 在该app启动后开始自动化 (optional).
        - app_wait_activity - 在该活动启动后开始自动化(optional).
        - intent_action - Intent to start (optional).
        - intent_category - Intent category to start (optional).
        - intent_flags - Flags to send to the intent (optional).
        - optional_intent_arguments - Optional arguments to the intent (optional).
        - stop_app_on_reset - Should the app be stopped on reset (optional)?
        :return:
        '''
        self.driver.start_activity(app_package, app_activity)

    def lock(self, seconds):
        '''
        锁屏，仅ios可用
        :param seconds:
        :return:
        '''
        self.driver.lock(seconds)

    def shake(self):
        '''
        摇一摇手机
        :return:
        '''
        self.driver.shake()

    def open_notifications(self):
        '''
        打开系统通知栏，仅支持android
        :return:
        '''
        self.driver.open_notifications()

    def network_connection(self):
        '''
        获取当前网络类型
        :return:
        '''
        self.driver.network_connection()

    def set_network_connection(self, type):
        '''
        设置网络类型
        :param type:
            无网络 = 0
            飞行模式 = 1
            只使用wifi = 2
            只使用数据流量 = 4
            所有网络都打开 = 6
        :return:
        '''
        self.driver.set_network_connection(type)

    def available_ime_engines(self):
        '''
        返回android设备所有可用的输入法
        :return:
        '''
        return self.driver.available_ime_engines()

    def activate_ime_engine(self, engine):
        '''
        激活某一输入法，需要先使用available_ime_engines获取
        :param engine:
        :return:
        '''
        self.driver.activate_ime_engine(engine)

    def toggle_location_services(self):
        '''
        :return:位置信息
        '''
        return self.driver.toggle_location_services()

    def set_location(self, latitude, longitude, altitude):
        '''
        设置经纬度
        :param latitude: 纬度
        :param longitude:经度
        :param altitude:高度
        :return:
        '''
        self.driver.set_location(latitude, longitude, altitude)

    @pre_func
    def text(self, element):
        '''
        返回元素的text
        :return:
        '''
        return element.text

    @pre_func
    def click(self, element):
        '''
        点击
        :return:
        '''
        logger.info("🖱 点击元素: {}".format(self.desc))
        element.click()
        time.sleep(0.5)

    @pre_func
    def clear(self, element):
        '''
        清除输入的内容
        :return:
        '''
        logger.info("clear element: {}".format(self.desc))
        element.clear()

    @pre_func
    def get_attribute(self, element, name):
        '''
        获取元素的属性，暂时用不上
        :param element:元素
        :param name: 要取的属性
        :return:
        '''
        return element.get_attribute(name)

    def is_enabled(self, element):
        '''
        返回元素是否可用
        :return:
        '''
        return self.driver.is_enabled(element)

    def is_selected(self, element):
        '''
        检查一个元素是否被选中
        :return:
        '''
        return self.driver.is_selected(element)

    @pre_func
    def send_keys(self, element, text):
        '''
        输入
        :param element: 输入元素
        :param text: 文字内容
        :return:
        '''
        logger.info("🖋 在 {} 输入: {}".format(self.desc, text))
        element.send_keys(text)

    @pre_func
    def is_displayed(self, element):
        '''
        元素是否可见，确定是否被挡住、隐藏、是否可点击等（selenium可使用，appnium不可）
        :return:
        '''
        element.is_displayed()

    @pre_func
    def size(self, element):
        '''
        返回元素的大小
        :param element:
        :return:
        '''
        return element.size()

    @pre_func
    def location(self, element, type):
        '''
        返回元素的坐标
        :param element: 元素
        :param type: x为纵坐标，y为横坐标
        :return:
        '''
        return element.location.get(type)

    @pre_func
    def rect(self, element):
        '''
        一次性返回元素的位置和大小
        :return: dict
        '''
        return element.rect()

    def get_window_size(self):
        '''
        获取当前屏幕分辨率
        :return:
        '''
        return self.driver.get_window_size()

    def back(self):
        '''

        :return:
        '''
        self.driver.back()
