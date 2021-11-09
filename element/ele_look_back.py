#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: ele_index.py
@time: 2021/8/17 17:05
@desc: 
"""
from common.page import Page


class Look_back(Page):
    '''回看列表'''
    like_or_nolike = ("id=>com.dengta.date:id/tv_like_and_noninductive","喜欢and无感数量")
    user = ("id=>com.dengta.date:id/iv_item_look_back","回看列表第一个人")
    user_name = ("id=>com.dengta.date:id/tv_item_look_back_name", "回看列表第一个人昵称")
    like_or_nolike_tag = ("id=>com.dengta.date:id/tv_item_look_back_already_like","喜欢或无感标签")
    like_or_nolike_button = ("id=>com.dengta.date:id/tv_item_look_back_islike","喜欢或无感按钮")
    today = ('xpath=>//android.widget.TextView[@text="今天"]','今天')
    yestoday = ('xpath=>//android.widget.TextView[@text="昨天"]','昨天')
    before_yesterday = ('xpath=>//android.widget.TextView[@text="前天"]','前天')
    back = ("id=>com.dengta.date:id/top_bar_left_iv","回看列表返回按钮")
    more =("id=>com.dengta.date:id/top_bar_right_iv","更多")
    lookback_like_or_nolike_tag = ("id=>com.dengta.date:id/tv_info_love_status","喜欢或无感标签")
    nolike = ('id=>com.dengta.date:id/iv_look_back_unlike', '不喜欢')
    like = ('id=>com.dengta.date:id/iv_look_back_like','喜欢')
    to_black_list = ('xpath=>//candroid.widget.TextView[@text="拉黑"]','拉黑')
    report = ('xpath=>//candroid.widget.TextView[@text="举报"]', '举报')
    Ta_index = ('xpath=>//candroid.widget.TextView[@text="Ta的主页"]', 'Ta的主页')

