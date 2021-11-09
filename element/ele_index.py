#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: ele_index.py
@time: 2021/8/17 17:05
@desc: 
"""
from common.page import Page


class Index(Page):
    '''首页'''
    guide_one = ("id=>com.dengta.date:id/rl_info_base_info","新手引导第一步")
    guide_tow = ("id=>com.dengta.date:id/rl_info_base_info","新手引导第二步")
    guide_three = ("id=>com.dengta.date:id/rl_info_base_info","新手引导第三步")
    guide_four = ("id=>com.dengta.date:id/tv_recommend_complete_material","新手引导第四步")
    nolike_tag_title = ('class=>android.widget.TextView', '不喜欢的标签框标题', 0)
    nolike_tag = ('class=>android.widget.TextView','不喜欢时选择第一个标签',1)
    nolike_tag_ok = ('id=>com.dengta.date:id/dialog_comm_confirm_tv','不喜欢标签选择后确定按钮')
    nolike = ('id=>com.dengta.date:id/iv_main_recommend_unlike','不喜欢按钮')
    like = ('id=>com.dengta.date:id/iv_main_recommend_like', '喜欢按钮')
    call = ('id=>com.dengta.date:id/rl_main_recommend_call', '语音通话按钮')
    name = ('id=>com.dengta.date:id/tv_info_name','名称')
    count_down = ('id=>com.dengta.date:id/tv_info_time', '倒计时')
    look_back = ('id=>com.dengta.date:id/tv_recommend_look_back', '回看')
    perfect_date = ('id=>com.dengta.date:id/tv_recommend_complete_material', '完善资料')

