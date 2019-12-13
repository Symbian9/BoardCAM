#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-11
# Desc: 3D-Space point

from math import sqrt


class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def offset(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z

    # TODO 使用__sub__ 用于两点计算距离可能并不合理
    def __sub__(self, other):
        return sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2) + pow(abs(self.z - other.z), 2))

    def __lt__(self, other):
        """
        `<` operator
        :param other:
        :return:
        """
        self._is_point(other)
        if self.x < other.x or self.y < other.y or self.z < other.z:
            return True

        return False

    def __gt__(self, other):
        """
        `>` operator
        :param other:
        :return:
        """
        if self.__eq__(other):
            return False

        return not self.__lt__(other)

    def __eq__(self, other):
        """
        `==` operator
        :param other:
        :return:
        """
        self._is_point(other)

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def _is_point(other):
        if not isinstance(other, Point):
            raise TypeError('Must be Point class.')

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.x, self.y, self.z)
