#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-30
# Desc: 圆有关函数

from math import cos, sin, pi

from math_tools import STRAIGHT_ANGLE, FULL_ANGLE, ZERO_ANGLE
from points import Point


def draw_circle_path(cx, cy, r, start_angle=ZERO_ANGLE, end_angle=FULL_ANGLE):
    """
    生成指定圆心的圆路径点
    :param cx: 圆心X坐标
    :param cy: 圆心Y坐标
    :param r: 该圆的半径
    :param start_angle:
    :param end_angle:
    :return:
    """
    points = []
    # points_path = ""
    angle_step = 2
    for angle in range(start_angle, end_angle + angle_step, angle_step):
        x = cx + r * cos(angle * pi / STRAIGHT_ANGLE)
        y = cy + r * sin(angle * pi / STRAIGHT_ANGLE)
        points.append(Point(x, y))
        # points_path += "{},{} ".format(x, y)

    # print("points_path: {}".format(points_path))
    return points


if __name__ == '__main__':
    print(len(draw_circle_path(10, 10, 5)))