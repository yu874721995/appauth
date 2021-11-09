#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''页面基类，存放所有页面操作方法'''
import time
import os.path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from common.logger import logger

class BassPage(object):

    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()
        logger.info(u'测试完毕关闭浏览器')

    def forward(self):
        self.driver.forward()
        logger.info(u'点击浏览器前进')

    def back(self):
        self.driver.back()
        logger.info(u'点击浏览器退后')

        #隐形等待，一个脚本中设置一次，整个脚本任何一次操作都适用
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info(u'隐性等待%d ms' %seconds)

        #关闭
    def close(self):
        try:
            self.driver.close()
            logger.info(u'关闭浏览器')
        except NameError as e:
            logger.error(u'%s' %e)

        #截图
    def get_window(self):
        file_path = os.path.dirname(os.getcwd())+'/image/'
        file_time = time.strftime('%y%m%d%H%m',time.localtime(time.time()))
        file_name = file_path+file_time+'.png'
        try:
            self.driver.get_screenshot_as_file(file_name)
            logger.info(u'截图并保存至：%s'%file_name)
        except NameError as a:
            logger.error(u'截图失败，失败原因：%s'%a)
            self.get_window()

        #定位
    def app_find_element(self,selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        print('select_by',selector_by,'select_id',selector_value)
        #id
        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info(u'通过%s定位到了%s这个元素'% (selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error(u'NoSuchElementException: %s'%e)
                self.get_window()
        #name
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        #class
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        #定位文字链接（a标签）
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        #通过链接中的部分文字定位
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        #标签名称
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        #绝对路径或相对路径（相对-可以使用布尔逻辑："//span[@id=’input-container’ and/or @name='xxx']/input"，绝对："/html/body/div[2]/form/span/input"）
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                #logging.info(u'通过%s 定位了：%s'%(selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error(e)
                self.get_window()
        elif selector_by == 's' or selector_by == 'selector_selector':
            self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError('Please enter a vaild type of targeing elements.')
        return element

    #输入，不需要先点击
    def type(self,selector,text):
        el = self.find_element(selector)
        #el.clear()
        try:
            el.send_keys(text)
            logger.info(u'输入文字：%s' %text)
        except NameError as e:
            logger.error(e)
            self.get_window()
    #切换frame
    def frame(self,text):
        self.driver.switch_to.frame(text)
        logger.info(u'切换frame')

    #切换回主文档/主frame，同级frame之间无法互相切换
    def first_frame(self):
        self.driver.switch_to.default_content()
        logger.info(u'frame切换回主文档')

    #清除
    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('clear input')
        except NameError as e:
            logger.error(e)
            self.get_window()
    #点击
    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info(u'点击了一下元素')
        except NameError as e:
            logger.error(e)
            self.get_window()

    #获取页面标题
    def get_page_title(self):
        logger.info('get_page_title')
        return self.driver.title

    #获取当前页面的URL
    def _get_URL(self):
        logger.info('get_now_URL')
        return self.driver.current_url


    #滑动页面至指定的元素处
    def drag(self,selector):
        span = self.find_element(selector)
        try:
            #调用js必须要driver对象来调用
            self.driver.execute_script("return arguments[0].scrollIntoView();",span)
            logger.info(u'拖动页面到指定位置')
        except NoSuchElementException as e:
            logger.error('error: %s'%e)

    #选择下拉菜单，用value时必须‘1’这样得格式，也可以用index（1）
    def select_ment(self,selector,text):
        el = self.find_element(selector)
        try:
            Select(el).select_by_value(text)
            logger.info(u'选择下来菜单中的第:%s个'%text)
        except NoSuchElementException as e:
            logger.error(e)
    #右键点击元素
    def right_click(self,selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).context_click(el).perform()
            logger.info(u'右键点击元素')
        except NoSuchElementException as a:
            logger.error(u"找不到元素")
    #双击元素
    def double_click(self,selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).double_click(el).perform()
            logger.info(u'定位元素并双击')
        except NoSuchElementException as e:
            logger.error(u'没有找到该元素')

    #拖动元素至指定地点
    def drag_and_drop(self,from_selector,to_selector):
        el = self.find_element(from_selector)
        els = self.find_element(to_selector)
        try:
            ActionChains(self.driver).drag_and_drop(el,els).perform()
            logger.info(u'拖动该元素至指定地点')
        except NoSuchElementException as e:
            logger.error(u'错误信息：',e)

    #鼠标左键长时间在某元素上停留
    def move_to_element(self,selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info(u'鼠标停留再该元素处')
        except NoSuchElementException as e:
            logger.error(u'错误信息：',e)

    #按下鼠标左键在某元素上
    def click_and_hold(self,selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).click_and_hold(el).perform()
            logger.info(u'鼠标左键长按该元素')
        except NoSuchElementException as e:
            logger.error(u'错误信息：',e)

    def Keys_jianpan(self,selector,num):
        el = self.find_element(selector)
        if num == 1:
            el.send_keys(Keys.BACK_SPACE)
        if num == 2:
            el.send_keys(Keys.SPACE)
        if num == 3:
            el.send_keys(Keys.CONTROL,'a')
        if num == 4:
            el.send_keys(Keys.CONTROL,'v')
        if num == 5:
            el.send_keys(Keys.CONTROL,'z')
        if num == 6:
            el.send_keys(Keys.ENTER)
        if num == 7:
            el.send_keys(Keys.TAB)
        if num == 8:
            el.send_keys(Keys.CONTROL,'c')

    #选中所有单选框，复选，需要传入标签名称tag——name以及 标签的内容
    def get_our_input(self,selector,text):
        el = self.find_element(selector)
        try:
            for i in el:
                if i.get_attribute('type') == text:
                    i.click()
            logger.info(u'点击所有该项')
        except NoSuchElementException as e:
            logger.error(u'错误信息：')

    #自动切换窗口至当前需要操作的窗口
    def get_windows(self):
        nowhandle = self.driver.current_window_handle
        ourhandles = self.driver.window_handles
        for handle in ourhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)


    #切换窗口回到当前窗口
    def get_now_window(self):
        nowhandle = self.driver.current_window_handle
        self.driver.switch_to_window(nowhandle)

    #处理alert弹窗
    def get_alert(self,test,input):
        alert = self.driver.switch_to_alert()
        #点击确定
        if test == 1:
            alert.accept()
        #返回文本窗的内容
        if test == 2:
            return alert.text()
        #点击取消
        if test == 3:
            alert.dismiss()
        #在弹窗中输入内容
        if test == 4:
            alert.send_keys(input)

    #等待某一元素加载完成
    def wait_element(self,selector,time):
        wait = WebDriverWait(self.driver,time)
        wait.until(lambda d:d.find_element_by_xpath(selector.split('=>')[1]))

    #定位元素中元素
    def click_form(self,selector,form):
        el = self.find_element(selector).find_element(form)
        el.click()

    #执行JS，例如设置隐藏元素display为block
    def querySelector(self,js):
        self.driver.execute_script(js)
        logger.info('执行JS:',js)










