#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-30
# Desc: Circle class

from math import cos, sin, pi, pow

from math_tools import STRAIGHT_ANGLE, FULL_ANGLE, ZERO_ANGLE
from points import Point


class Circle:
    def __init__(self, cx, cy, r):
        """
        :param cx: 圆心X坐标
        :param cy: 圆心Y坐标
        :param r: 该圆的半径
        :return:
        """
        self.cx = cx
        self.cy = cy
        self.r = r

    def area(self):
        # S=πr²
        return pi * pow(self.r, 2)

    def draw_path(self, start_angle=ZERO_ANGLE, end_angle=FULL_ANGLE):
        points = []
        # points_path = ""
        angle_step = 2
        for angle in range(start_angle, end_angle + angle_step, angle_step):
            x = self.cx + self.r * cos(angle * pi / STRAIGHT_ANGLE)
            y = self.cy + self.r * sin(angle * pi / STRAIGHT_ANGLE)
            points.append(Point(x, y))
            # points_path += "{},{} ".format(x, y)

        # print("points_path: {}".format(points_path))
        return points

    def __str__(self):
        return "Circle O({},{})".format(self.cx, self.cy)
