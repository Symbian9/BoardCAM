#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-11
# Desc: 3D-Space point


class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def offset(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z

    def __lt__(self, other):
        """
        小于比较操作
        :param other: 另一个对象
        :return:
        """
        if not isinstance(other, Point):
            raise TypeError('运算对象必须是Point')

        if self.x < other.x:
            return True
        if self.x > other.x:
            return False

        if self.y < other.y:
            return True
        if self.y > other.y:
            return False

        if self.z < other.z:
            return True
        if self.z > other.z:
            return False

        return False

    def __gt__(self, other):
        """
        大于比较操作
        :param other: 另一个对象
        :return:
        """
        if not isinstance(other, Point):
            raise TypeError('运算对象必须是Point')

        if self.x > other.x:
            return True
        if self.x < other.x:
            return False

        if self.y > other.y:
            return True
        if self.y < other.y:
            return False

        if self.z > other.z:
            return True
        if self.z < other.z:
            return False

        return False

    def __eq__(self, other):
        """
        判断两个Point对象是否相等
        :param other: 另一个对象
        :return:
        """
        if not isinstance(other, Point):
            raise TypeError('运算对象必须是Point')

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.x, self.y, self.z)


if __name__ == '__main__':
    p1 = Point(1, 1, 2)
    p2 = Point(1, 1, 2)
    print([p1, p2])
    print(p1 < p2)
