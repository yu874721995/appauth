#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: dxl
@file: ele_login.py
@time: 2021/8/16 11:29
@desc: 
"""

class Login:
    '''登录流程'''
    login = ('xpath=>//android.widget.TextView[@text="首页"]', "首页")
    window_false = ("id=>android:id/button2", "悬浮窗权限 暂不开启")
    window_true = ("id=>android:id/button1", "悬浮窗权限 现去开启")
    protocol_true = ("id=>com.dengta.date:id/btn_user_privacy_policy_summary_agree", "隐私协议 同意")
    protocol_false = ("id=>com.dengta.date:id/tv_user_privacy_policy_summary_disagree", "隐私协议 不同意")
    other_phone_login = ("id=>com.dengta.date:id/ll_login_select_cellphone_login_register", "其他号码登录")
    local_phone_login = ("id=>com.dengta.date:id/ll_login_select_cellphone_login_quick", "本机号码一键登录")
    wechart_login = ("id=>com.dengta.date:id/iv_login_select_wechat", "微信登录")
    phone = ("id=>com.dengta.date:id/et_login_phone_number_new", "输入手机号")
    area_code = ("id=>com.dengta.date:id/tv_area_code", "选择手机区号")
    list_area_code = ("id=>android.widget.LinearLayout", "选择国家和地区")
    code = ("id=>com.dengta.date:id/et_login_code", "输入验证码")
    get_code = ("id=>com.dengta.date:id/tv_login_get_code", "获取验证码")
    login_define = ("id=>com.dengta.date:id/btn_login_sure", "登录确定")
    sex_boy = ("id=>com.dengta.date:id/iv_register_sex_boy", "性别选择 男")
    sex_girl = ("id=>com.dengta.date:id/iv_register_sex_girl", "性别选择 女")
    sex_define = ("id=>com.dengta.date:id/btn_register_sex_sure", "性别 确定")
    name = ("id=>com.dengta.date:id/et_nick_name", "输入昵称")
    random_name = ("id=>com.dengta.date:id/ll_register_info_nickname", "随机昵称")
    set_avatar = ("id=>com.dengta.date:id/iv_register_avatar_set_avatar", "上传头像")
    select_from_album = ("id=>com.dengta.date:id/tv_select_avatar_select_from_album", "从相册选择")
    take_a_photo = ("id=>com.dengta.date:id/tv_select_avatar_take_a_photo", "拍照")
    avatar_cancel = ("id=>com.dengta.date:id/tv_select_avatar_cancel", "取消")
    tvCheck = ("id=>com.dengta.date:id/tvCheck", "选择照片")
    picture_right = ("id=>com.dengta.date:id/picture_right", "相册 完成")
    menu_crop = ("id=>com.dengta.date:id/menu_crop", "相册 裁剪")
    info_define = ("id=>com.dengta.date:id/btn_register_info_next_step", "基本信息 完成")