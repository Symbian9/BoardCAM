#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: bezier curve -> SVG

import math
from math import pow, fsum

import numpy as np

from inserts import gen_inserts
from svg_export import write_code

# 计算步骤
STEP = 0.01


def cal_waist_width(running_length, sidecut_radius):
    """
    根据侧切半径和行程长度计算板腰宽度和有效边刃
    :param running_length: 行程长度
    :param sidecut_radius: 侧切半径
    :return:
    """
    # TODO 增加板头板尾的宽度控制
    # print(waist_remain)
    # waist_width = nose_width - waist_remain * 2
    # print(round(waist_width, 3))
    return math.sqrt(math.pow(sidecut_radius, 2) - math.pow(running_length / 2, 2))


def common_bezier(points):
    """
    参考通用贝塞尔通用计算公式
    :param points:
    :return:
    """
    code = ""
    code_sym = ""

    # 所有点的个数P0 P1... Pn
    points_no = len(points) - 1
    for i, t in enumerate(np.arange(0, 1.00 + STEP, STEP), start=1):
        x_list, y_list, y_sym = [], [], []
        for index, point in enumerate(points):
            x_value = point[0] * pow(1 - t, points_no - index) * pow(t, index)
            x_list.append(x_value)
            y_value = point[1] * pow(1 - t, points_no - index) * pow(t, index)
            # y_sym.append(300 - y_value)
            y_list.append(y_value)

        x = fsum(x_list)
        y = fsum(y_list)
        # y_ = fsum(y_sym)
        print("Step{}: {} {}".format(i, x, y))
        if i == 1:
            # moveto
            code += "M{} {} ".format(x, y)
        else:
            # lineto
            code += "L{} {} ".format(x, y)

        if i == 1:
            # moveto
            code_sym += "M{} {} ".format(x, 300 - y)
        else:
            # lineto
            code_sym += "L{} {} ".format(x, 300 - y)

    return code, code_sym


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
        "nose_width": nose_width,
        "half_nose_width": nose_width / 2,
        "half_tail_width": tail_width / 2,
        "tail_width": tail_width,
        "nose_length": nose_length,
        "tail_length": tail_length,
    }

    # 1390,10 1480,10
    # M1340,0 C1390,10 1480,10 1520,150
    right_points = ((1520, 150), (5190, 30), (4480, 30), (1340, 0))
    svg_title = "Cubic Bézier curve"
    write_code(
        """<svg width="" height="" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">""")
    write_code("""<g>""")
    write_code("""<title>{}</title>""".format(svg_title))
    # 左上角贝塞尔
    write_code(
        """<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(
            common_bezier(left_points)[0]))

    # 左下贝塞尔
    write_code(
        """<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(
            common_bezier(left_points)[1]))

    # 右上贝塞尔
    write_code(
        """<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(
            common_bezier(right_points)[0]))

    # 右下贝塞尔
    write_code(
        """<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(
            common_bezier(right_points)[1]))

    write_code("""<line x1="180" y1="0" x2="1380" y2="0"
style="stroke:#000000;stroke-width:1"/>""")
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
        style="stroke:#000000;stroke-width:1"/>""".format(0, nose_width / 2, overall_length, nose_width / 2))
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
            style="stroke:#000000;stroke-width:1"/>""".format(nose_length, 0, nose_length, nose_width))
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
               style="stroke:#000000;stroke-width:1"/>""".format(nose_length + running_length, 0,
                                                                 nose_length + running_length, tail_width))

    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
                   style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(overall_length / 2, 0,
                                                                                            overall_length / 2,
                                                                                            nose_width))

    # write_code(
    #     """<rect x="0" y="0" width="{}" height="{}" style="fill:blue;stroke:pink;stroke-width:5;fill-opacity:0.1;stroke-opacity:0.9" />""".format(
    #         overall_length, nose_width
    #     ))

    # 上圆弧
    write_code("""<circle cx="{}" cy="{}" r="{}" stroke="black"
stroke-width="1" fill="none"/>""".format(overall_length / 2, -cal_waist_width(running_length, sidecut_radius),
                                         sidecut_radius))

    # 下圆弧
    write_code("""<circle cx="{}" cy="{}" r="{}" stroke="black"
    stroke-width="1" fill="none"/>""".format(overall_length / 2,
                                             cal_waist_width(running_length, sidecut_radius) + nose_width,
                                             sidecut_radius))

    # 嵌件生成
    inserts_svg = gen_inserts(params, 4, 50, 80)
    write_code(inserts_svg)

    write_code("""</g></svg>""")
