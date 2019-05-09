#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 嵌件组生成


def gen_circle(cx, setback, horizontal_mid_line):
    """

    :param cx: 圆心 X坐标
    :param setback: 嵌件组水平偏移量(+:整体向后, -:整体向前)
    :param horizontal_mid_line:
    :return:
    """
    content = """<g style="stroke-width:1;">"""
    cx += setback
    for i in [horizontal_mid_line - 20, horizontal_mid_line + 20]:
        content += ("""<circle cx="{}" cy="{}" r="10" stroke="black" fill="red" fill-opacity="0.25" />""".format(cx, i))
        content += ("""<circle cx="{}" cy="{}" r="18" stroke="black" fill="red" fill-opacity="0.25" />""".format(cx, i))

        # 圆心
        content += ("""<circle cx="{}" cy="{}" r="1" fill-opacity="1" />""".format(cx, i))
    content += "</g>"
    return content


def gen_inserts(params, inserts_number, spacing):
    """
    从竖中线向左右两侧生成嵌件位置
    :param params:
    :param inserts_number: 单侧单排嵌件个数
    :param spacing: 上下左右相邻嵌件之间的间距
    :return: 嵌件组SVG代码
    """
    content = ""
    stand_width = params.get("stand_width")
    half_stand_width = stand_width / 2
    stand_setback = params.get("stand_setback")
    # 竖直中线
    vertical_mid_line = params.get("half_overall_length")

    # 水平中线
    horizontal_mid_line = params.get("half_nose_width")

    if inserts_number % 2 == 1:
        # 嵌件个数为奇数
        left_start = vertical_mid_line - half_stand_width - spacing * int(inserts_number / 2)
        right_start = vertical_mid_line + half_stand_width - spacing * int(inserts_number / 2)
        for i in range(inserts_number):
            content += gen_circle(left_start + spacing * i, stand_setback, horizontal_mid_line)
            content += gen_circle(right_start + spacing * i, stand_setback, horizontal_mid_line)

    elif inserts_number % 2 == 0:
        # 嵌件个数为偶数
        left_start = vertical_mid_line - half_stand_width - spacing / 2 - spacing * (int(inserts_number / 2) - 1)
        right_start = vertical_mid_line + half_stand_width - spacing / 2 - spacing * (int(inserts_number / 2) - 1)
        for i in range(inserts_number):
            content += gen_circle(left_start + spacing * i, stand_setback, horizontal_mid_line)
            content += gen_circle(right_start + spacing * i, stand_setback, horizontal_mid_line)

    return content
