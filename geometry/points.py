#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-11
# Desc: 3D-Space point

from math import sqrt


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    def __init__(self, x, y, z=0):
        super(Point3D, self).__init__(x, y)
        self.z = z

    def offset(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z

    def distance(self, other):
        """
        The Distance Formula in Three-Dimensional Space
        """
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def __lt__(self, other):
        """
        `<` operator
        :param other:
        :return:
        """
        self._is_point(other)
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
            elif self.y == other.y:
                if self.z < other.z:
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
        if not isinstance(other, Point3D):
            raise TypeError('Must be Point instance.')

    def __repr__(self):
        if self.z == 0:
            return "Point({}, {})".format(self.x, self.y)
        return "Point({}, {}, {})".format(self.x, self.y, self.z)
