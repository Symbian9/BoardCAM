#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 有效边刃生成

from math import sqrt


def gen_arc(params):
    """
    有效边刃路径生成
    :param params: 参数
    :return:
    """
    sidecut_radius = params.get("sidecut_radius")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    nose_width = params.get("nose_width")

    step = 10
    offset = 0
    top_list = []
    bottom_list = []
    for i, x in enumerate(range(nose_length, running_length + nose_length + step, step), start=1):
        y = sqrt(pow(sidecut_radius, 2) - pow(nose_length + running_length / 2 - x, 2))
        y = sidecut_radius - y
        if i == 1:
            offset = nose_width - y
            y = offset + y
        else:
            y += offset
        top_list.append([x, y])
        bottom_list.append([x, nose_width - y])

    return top_list, bottom_list
