#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-30
# Desc: Circle class

from math import cos, sin, pi

from math_tools import STRAIGHT_ANGLE, FULL_ANGLE, ZERO_ANGLE
from points import Point


class Circle:
    def __init__(self, cx, cy, r):
        """
        :param cx: Center X coordinate
        :param cy: Center Y coordinate
        :param r: Radius
        :return:
        """
        self.cx = cx
        self.cy = cy
        self.r = r

    @property
    def diameter(self):
        """
        d=2r
        :return:
        """
        return self.r * 2

    @property
    def perimeter(self):
        """
        C=2πr
        :return:
        """
        return 2 * pi * self.r

    @property
    def area(self):
        """
        S=πr²
        :return:
        """
        return pi * self.r ** 2

    def draw_path(self, start_angle=ZERO_ANGLE, end_angle=FULL_ANGLE):
        """

        :param start_angle:
        :param end_angle:
        :return:
        """
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

    def belong(self, other):
        """
        Determine if a point is on the circle
        :param other: Point instance
        :return:
        """
        return (self.cx - other.x) ** 2 + (self.cy - other.y) ** 2 == self.r ** 2

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """
        standard equation of circle
        :return:
        """
        return "f(x,y) = (x%+-d)² + (y%+-d)² = %d" % (self.cx, self.cy, self.r ** 2)


class Ellipse:
    # 椭圆
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def draw(self):
        pass


class Hyperbola:
    # 双曲线
    pass


class Parabola:
    # 抛物线
    pass
