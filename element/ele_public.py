#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: ele_public.py
@time: 2021/8/20 10:40
@desc: 
"""


class Public:
    authority_true = ('xpath=>//android.widget.Button[@text="始终允许"]', "通用手机权限 点击允许")
    authority_false = ('xpath=>//android.widget.Button[@text="拒绝"]', "通用手机权限 点击拒绝")