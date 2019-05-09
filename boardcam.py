#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: bezier curve -> SVG

import os

from arc import gen_arc
from bezier import gen_bezier
from inserts import gen_inserts
from svg_export import init_svg, pack_svg

if __name__ == "__main__":
    # 参数含义参考docs/Configuration.md
    origin = (0, 0)
    nose_width = 300
    half_nose_width = nose_width / 2
    nose_length = 180
    overall_length = 1520
    tail_width = 300
    half_tail_width = tail_width / 2
    tail_length = 180
    running_length = overall_length - tail_length - nose_length
    sidecut_radius = 8000
    stand_setback = 10
    stand_width = 550
    inserts_number = 4
    half_overall_length = overall_length / 2
    spacing = 40

    os.remove("board_profile.svg")
    params = {
        "overall_length": overall_length,
        "half_overall_length": overall_length / 2,
        "running_length": running_length,
        "nose_width": nose_width,
        "half_nose_width": half_nose_width,
        "half_tail_width": half_tail_width,
        "tail_width": tail_width,
        "nose_length": nose_length,
        "tail_length": tail_length,
        "sidecut_radius": sidecut_radius,
        "stand_width": stand_width,
        "stand_setback": stand_setback,
        "spacing": spacing,
        "left_points": ((0, half_nose_width), (10, 250), (50, 40), (nose_length, 0)),
        # "left_points": ((0, 0), (550, 450), (180, 150), (180, 150)),
        "right_points": ((overall_length, half_tail_width), (4570, 100), (4180, 50), (overall_length - tail_length, 0)),
    }

    # 板头&板尾曲线路径生成
    left_bezier_svg = gen_bezier(params.get("left_points"))
    # right_bezier_svg = gen_bezier(params.get("right_points"))

    # 初始化SVG文件
    init_svg = init_svg(params)

    # 有效边刃路径生成
    arc_svg = gen_arc(params)

    # 嵌件路径生成
    inserts_svg = gen_inserts(params, inserts_number, spacing)

    pack_svg(left_bezier_svg + init_svg + arc_svg + inserts_svg)
