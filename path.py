#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 路径处理

from points import Point


class Path:
    # TODO 将以下方法添加到该类里
    def __init__(self, points):
        self.points = points

    def push_path(self):
        pass

    def __add__(self, other):
        pass


def mirror_path(points, width, length):
    """
    生成镜像路径
    :param points: 路径
    :param width: 按Y轴进行轴对称变化, width置0
    :param length: 按X轴进行轴对称变化, length置0
    :return:
    """
    width = int(width)
    length = int(length)
    return [Point(abs(width * 2 - point.x), abs(length * 2 - point.y)) for point in points]


def move_path(points, x_offset, y_offset):
    """
    平移函数
    :param points:
    :param x_offset: X坐标偏移量
    :param y_offset: Y坐标偏移量
    :return:
    """
    return [Point(point.x + x_offset, point.y + y_offset) for point in points]


def move(points, x, y):
    """
    将线段平移到某一点上
    :param x:
    :param y:
    :param points:
    :return:
    """
    x_diff = points[0].x - x
    y_diff = points[0].y - y

    return [Point(point.x - x_diff, point.y - y_diff) for point in points]
