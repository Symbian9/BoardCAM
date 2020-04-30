#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-25
# Desc:

from geometry.points import Point3D


def test_eq():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(1, 2, 3)
    assert p1 == p2

    p3 = Point3D(1, 2, 3)
    p4 = Point3D(4, 5, 6)
    assert p3 != p4


def test_gt():
    p1 = Point3D(2, 2, 3)
    p2 = Point3D(1, 2, 3)
    assert p1 > p2

    p3 = Point3D(2, 4, 3)
    p4 = Point3D(2, 2, 3)
    assert p3 > p4


def test_lt():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(3, 4, 5)
    assert p1 < p2

    p3 = Point3D(1, 2, 3)
    p4 = Point3D(1, 4, 3)
    assert p3 < p4


def test_ne():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(3, 4, 5)
    assert p1 != p2


def test_distance():
    p1 = Point3D(1, 1, 1)
    p2 = Point3D(1, 1, 2)
    assert int(p1.distance(p2)) == 1