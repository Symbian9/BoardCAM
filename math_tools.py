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
            y_list.append(y_value)

        x = fsum(x_list)
        y = fsum(y_list)
        print("Step{}: {} {}".format(i, x, y))
        if i == 1:
            # moveto
            code += "M{} {} ".format(x, y)
        else:
            # lineto
            code += "L{} {} ".format(x, y)

        if i == 1:
            code_sym += "M{} {} ".format(x, 300 - y)
        else:
            code_sym += "L{} {} ".format(x, 300 - y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code))
    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code_sym))
    return content


# def ci(radius, _x, a, b):
#     """
#     圆的标准方程: (x - a)²+(y - b)²=r² => (y - b)² = r² - (x - a)²
#     :return:
#     """
#     # return sqrt(pow(radius, 2) - pow(_x - a, 2)) + b
#     return sqrt(pow(radius, 2) - pow(half_overall_length - x, 2))


if __name__ == "__main__":
    nose_width = 300
    nose_length = 180
    overall_length = 1520
    tail_width = 300
    tail_length = 180
    running_length = overall_length - tail_length - nose_length
    sidecut_radius = 10000
    setback = None
    stand_width = None
    inserts_number = 4
    half_overall_length = overall_length / 2

    left_points = ((0, 150), (50, 140), (90, 180), (180, 0))
    params = {
        "overall_length": overall_length,
        "half_overall_length": overall_length / 2,
        "running_length": running_length,
        "nose_width": nose_width,
        "half_nose_width": nose_width / 2,
        "half_tail_width": tail_width / 2,
        "tail_width": tail_width,
        "nose_length": nose_length,
        "tail_length": tail_length,
        "sidecut_radius": sidecut_radius,
    }
    step = 0.1
    content = ""
    code = ""
    for i, x in enumerate(np.arange(180, 1340.00 + step, step), start=1):
        # y = ci(sidecut_radius, x, overall_length / 2, cal_waist_width(running_length, sidecut_radius)+nose_width)
        y = sqrt(pow(sidecut_radius, 2) - pow(half_overall_length - x, 2))
        print(x)
        if i == 1:
            code += "M{} {} ".format(x, y)
        else:
            code += "L{} {} ".format(x, y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code))
