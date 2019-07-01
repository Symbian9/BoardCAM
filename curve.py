#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-13
# Desc: 曲线有关

from config import bezier_step
from path import mirror_path, move_path
from points import Point


def bezier(bezier_points):
    """
    贝塞尔通用函数
    :param bezier_points:
    :return: # TODO 考虑是否将返回值使用Path类
    """
    # P0和Pn是endpoints, P1,P2...Pn-1是control points
    end = 1
    step_count = int(end / bezier_step)
    points_no = len(bezier_points) - 1
    curve_points = []

    for t in range(step_count + 1):
        t *= bezier_step
        x, y = 0, 0
        for index, point in enumerate(bezier_points):
            x += point.x * pow(1 - t, points_no - index) * pow(t, index)
            y += point.y * pow(1 - t, points_no - index) * pow(t, index)

        curve_points.append(Point(x, y))
    return curve_points


def gen_curve(params):
    """
    板头&板尾曲线生成
    :param params:
    :return:
    """
    end_handle = params.get("end_handle")
    transition_handle = params.get("transition_handle")
    nose_length = params.get("nose_length")
    nose_width = params.get("nose_width")
    tail_length = params.get("tail_length")
    tail_width = params.get("tail_width")
    half_nose_width = nose_width / 2
    half_tail_width = tail_width / 2
    running_length = params.get("running_length")

    nose_tip = params.get("nose_tip")
    nose_top = params.get("nose_top")

    nose_bezier_points = (
        nose_tip, Point(0, half_nose_width * end_handle), Point(nose_length * transition_handle, 0), nose_top
    )

    tail_bezier_points = (
        Point(0, half_tail_width), Point(0, half_tail_width * end_handle), Point(tail_length * transition_handle, 0),
        Point(tail_length, 0)
    )

    upper_left_list = bezier(nose_bezier_points)
    # X轴对称变换
    lower_left_list = mirror_path(upper_left_list, 0, half_nose_width)

    temp = bezier(tail_bezier_points)
    # Y轴对称变换
    temp2 = mirror_path(temp, tail_length, 0)

    # 平移到对应位置
    offset = running_length + nose_length - tail_length
    upper_right_list = move_path(temp2[::-1], offset, 0)
    lower_right_list = mirror_path(upper_right_list, 0, half_tail_width)
    return upper_left_list[::-1], lower_left_list, upper_right_list[::-1], lower_right_list
