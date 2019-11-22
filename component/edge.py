#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-01
# Desc: 侧边路径

from math import sqrt

from until.config import side_step
from geometry.points import Point


class Edge:
    def __init__(self):
        # TODO 开始点 结束点
        pass

    def flat(self):
        pass

    def arh(self):
        pass

    def __repr__(self):
        return "Edge:"


def flat_edge(params):
    """
    平直有效边刃路径生成
    :param params:
    :return:
    """
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    nose_width = params.get("nose_width")

    top_list = []
    bottom_list = []

    for x in range(nose_length, running_length + nose_length + side_step, side_step):
        y = nose_width
        top_list.append(Point(x, y))
        bottom_list.append(Point(x, 0))
    return top_list, bottom_list[::-1]


def arc_edge(params):
    """
    弧形有效边刃路径生成
    :param params: 参数
    :return:
    """
    sidecut_radius = params.get("sidecut_radius")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    nose_width = params.get("nose_width")

    offset = 0
    top_list = []
    bottom_list = []
    for i, x in enumerate(range(nose_length, running_length + nose_length + side_step, side_step), start=1):
        y = sqrt(pow(sidecut_radius, 2) - pow(nose_length + running_length / 2 - x, 2))
        y = sidecut_radius - y
        if i == 1:
            offset = nose_width - y
            y = offset + y
        else:
            y += offset
        top_list.append(Point(x, y))
        bottom_list.append(Point(x, nose_width - y))

    return top_list, bottom_list[::-1]
