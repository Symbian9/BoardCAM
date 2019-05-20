#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 


def value_to_str(dict_obj):
    """
    将字典的所有value转换成string类型并返回
    :param dict_obj: 字典对象
    :return:
    """
    if not isinstance(dict_obj, dict):
        return "1"
    return {key: str(dict_obj.get(key)) for key in dict_obj}
