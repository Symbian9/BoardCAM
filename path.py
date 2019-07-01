#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 路径处理

from points import Point


class Path:
    # TODO 将以下方法添加到该类里
    # TODO 解决需要反转points的问题
    def __init__(self, points):
        self.points = points

    def push_path(self):
        pass

    def __add__(self, other):
        # return Path(self.points + other.points)
        # TODO 需要判断连接在最前面 还是最后面
        print(self.points[-1] - other[0])
        print(self.points[-1] - other[-1])
        if (self.points[-1] - other[0]) < (self.points[-1] - other[-1]):
            print("1")
            return Path(self.points + other.points)
        else:
            return Path(self.points + other[::-1])

    def __repr__(self):
        return "Path: {} -> {}".format(self.points[0], self.points[-1])

    def __reversed__(self):
        return Path(self.points[::-1])

    def __radd__(self, other):
        # TODO 需要判断连接在最前面 还是最后面
        print(self.points[-1] - other[0])
        print(self.points[-1] - other[-1])
        if (self.points[-1] - other[0]) < (self.points[-1] - other[-1]):
            print("1")
            return self.__add__(other)
        else:
            return self.__add__(other[::-1])

    # 排序函数
    # def __


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


if __name__ == '__main__':
    a = Path([Point(1, 1), Point(2, 2)])
    b = Path([Point(4, 4), Point(3, 3)])
    # print(a)
    # print(reversed(a))
    a += b
    print(a.points)
    # d = [1, 3, 6, 2]
    # d.sort()
    # print(d)
