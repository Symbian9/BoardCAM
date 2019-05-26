#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 对象操作函数库


def value_to_str(dict_obj):
    """
    将字典的所有key, value转换成string类型并返回
    :param dict_obj: 字典对象
    :return:
    """
    if not isinstance(dict_obj, dict):
        return "1"
    return {str(key): str(dict_obj.get(key)) for key in dict_obj}


def list_to_str(list_obj):
    """
    列表转成字符串(空格代替逗号分隔符)
    :param list_obj:
    :return:
    """
    list_obj = [str(i) for i in list_obj]
    list_obj = " ".join(list_obj)

    return "[{}]".format(list_obj)
