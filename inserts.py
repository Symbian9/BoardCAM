#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 嵌件组生成


def gen_inserts(params, inserts_number, spacing, offset):
    """
    从竖中线向左右两侧生成嵌件位置
    :param params:
    :param inserts_number: 单侧单排嵌件个数
    :param spacing: 上下左右相邻嵌件之间的间距
    :param offset: 距离竖中线位置的偏移量
    :return: 嵌件组SVG代码
    """
    content = ""
    # 竖直中线
    vertical_mid_line = params.get("half_overall_length")

    # 水平中线
    horizontal_mid_line = params.get("half_nose_width")

    # 左右两侧嵌件组靠近竖中线的第一个嵌件位置
    left_start_cx, right_start_cx = vertical_mid_line - offset, vertical_mid_line + offset

    for i in range(inserts_number):
        left_start_cx -= spacing
        right_start_cx += spacing

        for j in [horizontal_mid_line - spacing, horizontal_mid_line + spacing]:
            # 左侧嵌件组
            content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                        stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(left_start_cx, j))
            content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                            stroke-width="1" fill="blue" fill-opacity="0.25"  />""".format(left_start_cx, j))

            # 圆心
            content += (
                """<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(left_start_cx, j))

            # 右侧嵌件组
            content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                                        stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(right_start_cx,
                                                                                                      j))
            content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                                            stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(
                right_start_cx, j))
            content += (
                """<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(right_start_cx, j))

    return content


def gen(left_start_cx, setback, horizontal_mid_line):
    content = ""
    left_start_cx += setback
    for i in [horizontal_mid_line-20, horizontal_mid_line+20]:
        content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                                stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(left_start_cx, i))
        content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                        stroke-width="1" fill="blue" fill-opacity="0.25"  />""".format(left_start_cx, i))

        # 圆心
        content += (
            """<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(left_start_cx, i))
    return content


def gen_inserts2(params, inserts_number, spacing):
    """
    从竖中线向左右两侧生成嵌件位置
    :param params:
    :param inserts_number: 单侧单排嵌件个数
    :param spacing: 上下左右相邻嵌件之间的间距
    :return: 嵌件组SVG代码
    """
    content = ""
    stand_width = params.get("stand_width")
    stand_setback = params.get("stand_setback")
    # 竖直中线
    vertical_mid_line = params.get("half_overall_length")

    # 水平中线
    horizontal_mid_line = params.get("half_nose_width")

    if inserts_number % 2 == 1:
        # 奇数
        # 左侧
        left_mid_line = vertical_mid_line - stand_width / 2
        for i in range(int((inserts_number - 1) / 2) + 1):
            content += gen(left_mid_line + spacing * i, stand_setback, horizontal_mid_line)
            content += gen(left_mid_line - spacing * i, stand_setback, horizontal_mid_line)

        # 右侧
        right_mid_line = vertical_mid_line + stand_width / 2
        for i in range(int((inserts_number - 1) / 2) + 1):
            content += gen(right_mid_line + spacing * i, stand_setback, horizontal_mid_line)
            content += gen(right_mid_line - spacing * i, stand_setback, horizontal_mid_line)
    elif inserts_number % 2 == 0:
        # 偶数
        left_mid_line = vertical_mid_line - stand_width / 2

        # 右侧
        for i in range(1, int(inserts_number / 2) + 1):
            if i == 1:
                content += gen(left_mid_line + spacing / 2, stand_setback, horizontal_mid_line)
            else:
                content += gen(left_mid_line + spacing / 2 + spacing * (i - 1), stand_setback, horizontal_mid_line)

        # 左侧
        for i in range(1, int(inserts_number / 2) + 1):
            if i == 1:
                content += gen(left_mid_line - spacing / 2, stand_setback, horizontal_mid_line)
            else:
                content += gen(left_mid_line - spacing * (i - 1) - spacing / 2, stand_setback, horizontal_mid_line)

        right_mid_line = vertical_mid_line + stand_width / 2

        # 右侧
        for i in range(1, int(inserts_number / 2) + 1):
            if i == 1:
                content += gen(right_mid_line + spacing / 2, stand_setback, horizontal_mid_line)
            else:
                content += gen(right_mid_line + spacing / 2 + spacing * (i - 1), stand_setback, horizontal_mid_line)

        # 左侧
        for i in range(1, int(inserts_number / 2) + 1):
            if i == 1:
                content += gen(right_mid_line - spacing / 2, stand_setback, horizontal_mid_line)
            else:
                content += gen(right_mid_line - spacing * (i - 1) - spacing / 2, stand_setback, horizontal_mid_line)

    return content
