#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-25
# Desc:

from points import Point


def test_eq():
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    assert p1 == p2

    p3 = Point(1, 2, 3)
    p4 = Point(4, 5, 6)
    assert p3 != p4


def test_gt():
    p1 = Point(2, 2, 3)
    p2 = Point(1, 2, 3)
    assert p1 > p2

    p3 = Point(2, 4, 3)
    p4 = Point(2, 2, 3)
    assert p3 > p4


def test_lt():
    p1 = Point(1, 2, 3)
    p2 = Point(3, 4, 5)
    assert p1 < p2

    p3 = Point(1, 2, 3)
    p4 = Point(1, 4, 3)
    assert p3 < p4


def test_ne():
    p1 = Point(1, 2, 3)
    p2 = Point(3, 4, 5)
    assert p1 != p2
