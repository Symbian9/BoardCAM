#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: bezier curve -> SVG

from arc import gen_arc
from bezier import gen_bezier
from inserts import gen_inserts
from svg_export import init_svg, pack_svg

if __name__ == "__main__":
    # 参数含义参考docs/Configuration.md
    nose_width = 300
    half_nose_width = nose_width / 2
    nose_length = 180
    overall_length = 1520
    tail_width = 300
    half_tail_width = tail_width / 2
    tail_length = 180
    running_length = overall_length - tail_length - nose_length
    sidecut_radius = 10000
    stand_setback = 10
    stand_width = 550
    inserts_number = 4
    half_overall_length = overall_length / 2

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
        "left_points": ((0, half_nose_width), (50, 140), (90, 180), (nose_length, 0)),
        "right_points": ((overall_length, half_tail_width), (4590, 10), (4080, 70), (overall_length - tail_length, 0)),
    }

    # 板头&板尾曲线路径生成
    left_bezier_svg = gen_bezier(params.get("left_points"))
    right_bezier_svg = gen_bezier(params.get("right_points"))

    # 初始化SVG文件
    init_svg = init_svg(params)

    # 有效边刃路径生成
    arc_svg = gen_arc(params)

    # 嵌件路径生成
    inserts_svg = gen_inserts(params, inserts_number, 40)

    pack_svg(left_bezier_svg + right_bezier_svg + init_svg + arc_svg + inserts_svg)
