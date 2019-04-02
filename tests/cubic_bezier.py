#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zhengxiang@boardcam.org>
# Date: 2019-03-06
# Desc: 给定4个点 生成贝塞尔曲线的SVG
# Coordinates are given as points in the complex plane

from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from svgpathtools import Path, CubicBezier, wsvg, Arc, smoothed_path, kinks

from tests.board_cal import cal_waist_width

# 需要提供的参数
running_length = 1250
nose_length = 180
tail_length = 180
half_nose_width = 149
half_tail_width = 149
sidecut_radius = 10000

# 板头&板尾贝塞尔控制点
tail_curve = nose_curve = (0, 60), (90-50, 75+80)
# tail_curve = (0, 70), (90, 160)

# 计算出来的参数
waist_remain = cal_waist_width(running_length, sidecut_radius)
half_running_length = running_length / 2

# 滑雪板总长度 又叫Board Length
overall_length = nose_length + running_length + tail_length
print("Overall Length: {}mm.".format(overall_length))

origin = 0

seg1 = CubicBezier(origin, complex(nose_curve[0][0], -nose_curve[0][1]), complex(nose_curve[1][0], -nose_curve[1][1]),
                   complex(nose_length, -half_nose_width))

seg2 = Arc(start=complex(nose_length, -half_nose_width), radius=complex(half_running_length, waist_remain),
           end=complex((nose_length + running_length), -half_tail_width), rotation=0, large_arc=1, sweep=0)

seg3 = CubicBezier(complex((nose_length + running_length), -half_tail_width),
                   complex((overall_length - tail_curve[1][0]), -tail_curve[1][1]),
                   complex((overall_length - tail_curve[0][0]), -tail_curve[0][1]),
                   (nose_length + running_length + tail_length))

seg4 = CubicBezier((nose_length + running_length + tail_length),
                   complex((overall_length - tail_curve[0][0]), tail_curve[0][1]),
                   complex((overall_length - tail_curve[1][0]), tail_curve[1][1]),
                   complex((nose_length + running_length), half_tail_width))

seg5 = Arc(start=complex((nose_length + running_length), half_tail_width),
           radius=complex(half_running_length, -waist_remain),
           end=complex(nose_length, half_nose_width), rotation=0,
           large_arc=1, sweep=0)

seg6 = CubicBezier(complex(nose_length, half_nose_width), complex(nose_curve[1][0], nose_curve[1][1]),
                   complex(nose_curve[0][0], nose_curve[0][1]), origin)

path = Path(seg1, seg2, seg3, seg4, seg5, seg6)
print("steel_edge_length: {}mm.".format(path.length()))
spath = smoothed_path(path)
print("spath contains non-differentiable points? ", len(kinks(spath)) > 0)
print(spath)

# 面积暂时计算不出来 Arc' object has no attribute 'poly'
# print("board_area: {}".format(path.area()))

wsvg(path, filename='output2.svg')

# 生成PDF
drawing = svg2rlg("output2.svg")
renderPDF.drawToFile(drawing, "file2.pdf")
