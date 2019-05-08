#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 嵌件组生成


def gen_inserts(params, inserts_number, spacing, offset):
    """

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

    # 靠近竖中线的嵌件位置
    left_cx, right_cx = vertical_mid_line - offset, vertical_mid_line + offset

    for i in range(inserts_number):
        left_cx -= spacing
        right_cx += spacing

        for j in [horizontal_mid_line - spacing, horizontal_mid_line + spacing]:
            # 左侧嵌件组(4x2)
            content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                        stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(left_cx, j))
            content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                            stroke-width="1" fill="blue" fill-opacity="0.25"  />""".format(left_cx, j))

            # 圆心
            content += ("""<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(left_cx, j))

            # 右侧嵌件组(4x2)
            content += ("""<circle cx="{}" cy="{}" r="10" stroke="black"
                                        stroke-width="1" fill="blue" fill-opacity="0.25" />""".format(right_cx, j))
            content += ("""<circle cx="{}" cy="{}" r="18" stroke="black"
                                            stroke-width="1" fill="blue" fill-opacity="0.25"  />""".format(right_cx,
                                                                                                           j))
            content += ("""<circle cx="{}" cy="{}" r="1" fill-opacity="1" stroke-width="1" />""".format(right_cx, j))

    return content
