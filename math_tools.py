#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 

from math import sqrt, pow, fsum

import numpy as np


def cal_waist_width(running_length, sidecut_radius):
    """
    根据侧切半径和行程长度计算板腰宽度和有效边刃
    :param running_length: 行程长度
    :param sidecut_radius: 侧切半径
    :return:
    """
    # TODO 增加板头板尾的宽度控制
    # print(waist_remain)
    # waist_width = nose_width - waist_remain * 2
    # print(round(waist_width, 3))
    return sqrt(pow(sidecut_radius, 2) - pow(running_length / 2, 2))


def gen_bezier(points):
    """
    参考通用贝塞尔通用计算公式
    :param points:
    :return:
    """
    content = ""
    code = ""
    code_sym = ""
    # 计算步骤
    step = 0.01

    # 所有点的个数P0 P1... Pn
    points_no = len(points) - 1
    for i, t in enumerate(np.arange(0, 1.00 + step, step), start=1):
        x_list, y_list, y_sym = [], [], []
        for index, point in enumerate(points):
            x_value = point[0] * pow(1 - t, points_no - index) * pow(t, index)
            x_list.append(x_value)
            y_value = point[1] * pow(1 - t, points_no - index) * pow(t, index)
            # y_sym.append(300 - y_value)
            y_list.append(y_value)

        x = fsum(x_list)
        y = fsum(y_list)
        # y_ = fsum(y_sym)
        print("Step{}: {} {}".format(i, x, y))
        if i == 1:
            # moveto
            code += "M{} {} ".format(x, y)
        else:
            # lineto
            code += "L{} {} ".format(x, y)

        if i == 1:
            # moveto
            code_sym += "M{} {} ".format(x, 300 - y)
        else:
            # lineto
            code_sym += "L{} {} ".format(x, 300 - y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code))
    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code_sym))
    return content
