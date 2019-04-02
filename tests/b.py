#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zhengxiang@boardcam.org>
# Date: 2019-03-06
# Desc: 

import matplotlib.pyplot as plt
from beziers.cubicbezier import CubicBezier
from beziers.path import BezierPath
from beziers.point import Point

b1 = CubicBezier(
    Point(412.0, 500.0), Point(308.0, 665.0), Point(163.0, 589.0), Point(163.0, 504.0)
)
b2 = CubicBezier(
    Point(163.0, 504.0), Point(163.0, 424.0), Point(364.0, 321.0), Point(366.0, 216.0)
)
b3 = CubicBezier(
    Point(366.0, 216.0), Point(368.0, 94.0), Point(260.0, 54.0), Point(124.0, 54.0)
)
path = BezierPath.fromSegments([b1, b2, b3])
path.closed = False
path.addExtremes()
path.balance()
path.translate(Point(-100.0, -100.0))

fig, ax = plt.subplots()
path.addExtremes()
# path.plot(ax)
plt.show()
