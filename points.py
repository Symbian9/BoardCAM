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
        `<` operator
        :param other:
        :return:
        """
        self._is_point(other)

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
        `>` operator
        :param other:
        :return:
        """
        self._is_point(other)
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

    @staticmethod
    def _is_point(other):
        if not isinstance(other, Point):
            raise TypeError('Must be Point class.')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.x, self.y, self.z)


if __name__ == '__main__':
    p1 = Point(2, 5, 1)
    p2 = Point(2, 5, 1)
    print([p1, p2])
    print(p1 > p2)
