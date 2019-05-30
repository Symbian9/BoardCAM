#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc:


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
    return [[abs(width * 2 - point[0]), abs(length * 2 - point[1])] for point in points]


def move_path(points, x_offset, y_offset):
    """
    平移函数
    :param points:
    :param x_offset: X坐标偏移量
    :param y_offset: Y坐标偏移量
    :return:
    """
    return [[point[0] + x_offset, point[1] + y_offset] for point in points]


def move(x, y, points):
    """
    将线段平移到某一点上
    :param x:
    :param y:
    :param points:
    :return:
    """
    x_diff = points[0][0] - x
    y_diff = points[0][1] - y

    return [[point[0] - x_diff, point[1] - y_diff] for point in points]
