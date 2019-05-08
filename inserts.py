#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 嵌件组生成


def gen_circle(left_start_cx, setback, horizontal_mid_line):
    content = ""
    left_start_cx += setback
    for i in [horizontal_mid_line - 20, horizontal_mid_line + 20]:
        content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                                stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(left_start_cx, i))
        content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                        stroke-width="1" fill="blue" fill-opacity="0.25"  />""".format(left_start_cx, i))

        # 圆心
        content += (
            """<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(left_start_cx, i))
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
    stand_setback = params.get("stand_setback")
    # 竖直中线
    vertical_mid_line = params.get("half_overall_length")

    # 水平中线
    horizontal_mid_line = params.get("half_nose_width")

    if inserts_number % 2 == 1:
        # 嵌件为奇数
        mid_line = vertical_mid_line - stand_width / 2, vertical_mid_line + stand_width / 2
        for line in mid_line:
            for i in range(int((inserts_number - 1) / 2) + 1):
                content += gen_circle(line + spacing * i, stand_setback, horizontal_mid_line)
                content += gen_circle(line - spacing * i, stand_setback, horizontal_mid_line)

    elif inserts_number % 2 == 0:
        # 嵌件为偶数
        mid_line = vertical_mid_line - stand_width / 2, vertical_mid_line + stand_width / 2

        for line in mid_line:
            for i in range(1, int(inserts_number / 2) + 1):
                if i == 1:
                    content += gen_circle(line + spacing / 2, stand_setback, horizontal_mid_line)
                else:
                    content += gen_circle(line + spacing / 2 + spacing * (i - 1), stand_setback, horizontal_mid_line)

            for i in range(1, int(inserts_number / 2) + 1):
                if i == 1:
                    content += gen_circle(line - spacing / 2, stand_setback, horizontal_mid_line)
                else:
                    content += gen_circle(line - spacing * (i - 1) - spacing / 2, stand_setback, horizontal_mid_line)

    return content
