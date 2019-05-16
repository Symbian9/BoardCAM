#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: bezier curve -> SVG

import io

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from arc import gen_arc
from bezier import gen_bezier
from inserts import gen_inserts
from svg_export import init_svg, pack_svg


def draw_insert(canvas, x, y):
    """
    绘制嵌件位置
    :param canvas:
    :param x: 圆心X坐标
    :param y: 圆心Y坐标
    :return:
    """
    # r=0.5作为圆心
    radius = [0.5, 10, 18]
    for r in radius:
        canvas.circle(x * mm, y * mm, r * mm)
    return canvas


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

    # profile
    nose_tip_radius = 300
    camber = 15
    camber_setback = 0
    tail_tip_radius = 300

    # os.remove("board_profile.svg")
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
        "bezier_points": ((0, half_nose_width), (10, 250), (50, 40), (nose_length, 0)),
    }

    # 板头&板尾曲线路径生成
    upper_left_list, lower_left_list, upper_right_list, lower_right_list = gen_bezier(params)

    # 初始化SVG文件
    init_svg = init_svg(params)

    # 有效边刃路径生成
    points = []
    arc_svg, top_list, bottom_list = gen_arc(params)
    points.extend(lower_left_list)

    points.extend(top_list)
    points.extend(lower_right_list[::-1])
    points.extend(upper_right_list)
    points.extend(bottom_list[::-1])
    points.extend(upper_left_list[::-1])

    print(points)
    bezier_path = ""
    for index, point in enumerate(points, start=1):
        print(point)
        x = point[0]
        y = point[1]
        if index == 1:
            bezier_path += "M {} {}".format(x, y)
        else:
            bezier_path += "L {} {}".format(x, y)
    bezier_path = """<path stroke="#000000" id="svg_3" stroke-width="1" fill="none" d="{}" />""".format(bezier_path)

    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    canvas = canvas.Canvas(buffer, pagesize=(1520 * mm, 330 * mm))
    canvas.setLineWidth(4)
    canvas.setPageCompression(0)
    canvas._filename = "board_profile.pdf"
    canvas.setDash(10, 3)
    canvas.setStrokeAlpha(0.3)
    canvas.setLineWidth(0.5)

    # 虚线辅助线
    canvas.line(0, 150 * mm, 1520 * mm, 150 * mm)
    canvas.line(180 * mm, 0 * mm, 180 * mm, 300 * mm)
    canvas.line(760 * mm, 0 * mm, 760 * mm, 300 * mm)
    canvas.line(1340 * mm, 0 * mm, 1340 * mm, 300 * mm)

    path = canvas.beginPath()
    for index, point in enumerate(points, start=1):
        print(point)
        x = point[0]
        y = point[1]
        if index == 1:
            path.moveTo(x * mm, y * mm)
        else:
            path.lineTo(x * mm, y * mm)
            # path.close()

    canvas.setDash()
    canvas.setStrokeAlpha(1)
    canvas.setLineWidth(1)
    canvas.drawPath(path, stroke=1, fill=0)

    # 嵌件路径生成
    inserts_svg, insert_coordinate_list = gen_inserts(params, inserts_number, spacing)
    for insert in insert_coordinate_list:
        x = insert[0]
        y = insert[1]
        draw_insert(canvas, x, y)

    canvas.showPage()
    canvas.save()

    pack_svg(bezier_path + init_svg + arc_svg + inserts_svg)
    print(len(points))
