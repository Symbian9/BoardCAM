#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: BoardCAM主程序


from bezier import gen_curve
from edge import arc_edge
from gcode_export import export_gcode
from inserts import gen_inserts
from math_tools import cal_waist_width
from pdf_export import export_pdf, draw_profile
from points import Point
from svg_export import export_svg, gen_profile_path


def frame(params):
    """
    计算整块板的端点坐标
    :param params:
    :return:
    """
    nose_width = params.get("nose_width")
    tail_width = params.get("tail_width")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    tail_length = params.get("tail_length")
    overall_length = nose_length + running_length + tail_length
    sidecut_radius = params.get("sidecut_radius")

    # FIXME 腰宽并不应该以板头宽为基准
    waist_width = nose_width - cal_waist_width(running_length, sidecut_radius) * 2
    max_width = max(nose_width, waist_width, tail_width)

    params["nose_tip"] = Point(0, max_width / 2)
    params["tail_tip"] = Point(overall_length, max_width / 2)

    params["waist_top"] = Point(running_length / 2 + nose_length, 0)
    params["waist_below"] = Point(running_length / 2 + nose_length, (max_width - waist_width) / 2 + waist_width)

    params["nose_top"] = Point(nose_length, 0)
    params["nose_below"] = Point(nose_length, (max_width - nose_width) / 2 + nose_width)

    params["tail_top"] = Point(nose_length + running_length, 0)
    params["tail_below"] = Point(nose_length + running_length, (max_width - tail_width) / 2 + tail_width)
    return params


if __name__ == "__main__":
    # 参数含义参考docs/Configuration.md
    params = {
        # Nose Shape
        "nose_width": 300,
        "nose_length": 180,

        # Tail Shape
        "tail_width": 300,
        "tail_length": 180,

        "running_length": 1160,
        "sidecut_radius": 8000,

        # inserts
        "stand_width": 550,
        "stand_setback": 0,
        "horizontal_spacing": 40,
        "vertical_spacing": 40,
        "inserts_number": 4,

        # curve
        "end_handle": 0.4,
        "transition_handle": 2,

        # profile
        "tip_radius": 300,
        "camber": 15,
        "thickness": 7,
        "camber_setback": 0,
    }

    params = frame(params)

    # 板头&板尾曲线路径生成
    upper_left_list, lower_left_list, upper_right_list, lower_right_list = gen_curve(params)

    # 路径生成
    top_list, bottom_list = arc_edge(params)
    points = lower_left_list + top_list + lower_right_list + upper_right_list + bottom_list + upper_left_list

    # 嵌件路径生成
    insert_coordinate_list = gen_inserts(params)

    # export
    export_pdf(params, points, insert_coordinate_list)
    export_svg(params, points, insert_coordinate_list)
    export_gcode(points)
    profile_points, height = gen_profile_path(params)
    draw_profile(profile_points, height)
