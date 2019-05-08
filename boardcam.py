#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: bezier curve -> SVG

from arc import gen_arc
from inserts import gen_inserts
from math_tools import gen_bezier
from svg_export import write_code, init_svg, start_tag, close_tag

if __name__ == "__main__":
    # P0和P3是endpoints, P1和P2是control points
    # points = ((0, 0), (40, 140), (90, 280), (180, 150))
    nose_width = 300
    nose_length = 180
    overall_length = 1520
    tail_width = 300
    tail_length = 180
    running_length = overall_length - tail_length - nose_length
    sidecut_radius = 10000
    setback = None
    stand_width = None
    inserts_number = 4

    left_points = ((0, 150), (50, 140), (90, 180), (180, 0))
    params = {
        "overall_length": overall_length,
        "half_overall_length": overall_length / 2,
        "running_length": running_length,
        "nose_width": nose_width,
        "half_nose_width": nose_width / 2,
        "half_tail_width": tail_width / 2,
        "tail_width": tail_width,
        "nose_length": nose_length,
        "tail_length": tail_length,
        "sidecut_radius": sidecut_radius,
    }

    # 1390,10 1480,10
    # M1340,0 C1390,10 1480,10 1520,150
    right_points = ((1520, 150), (5190, 30), (4480, 30), (1340, 0))
    start_tag()

    # 板头&板尾生成
    left_bezier_svg = gen_bezier(left_points)
    write_code(left_bezier_svg)
    right_bezier_svg = gen_bezier(right_points)
    write_code(right_bezier_svg)

    #
    init_svg(params)

    # 有效边刃生成
    arc_svg = gen_arc(params)
    write_code(arc_svg)

    # 嵌件生成
    inserts_svg = gen_inserts(params, 4, 50, 80)
    write_code(inserts_svg)

    close_tag()
