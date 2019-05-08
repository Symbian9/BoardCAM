#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 有效边刃生成

from math import sqrt

import numpy as np


def gen_arc(params):
    """
    有效边刃生成
    :param params: 参数
    :return:
    """
    half_overall_length = params.get("half_overall_length")
    sidecut_radius = params.get("sidecut_radius")
    content = ""

    # 以下为圆弧代码
    # # 上圆弧
    # content += ("""<circle cx="{}" cy="{}" r="{}" stroke="black"
    # stroke-width="1" fill="none"/>""".format(half_overall_length, -cal_waist_width(running_length, sidecut_radius),
    #                                          sidecut_radius))
    #
    # # 下圆弧
    # content += ("""<circle cx="{}" cy="{}" r="{}" stroke="black"
    #     stroke-width="1" fill="none"/>""".format(half_overall_length,
    #                                              cal_waist_width(running_length, sidecut_radius) + nose_width,
    #                                              sidecut_radius))

    step = 1
    code = ""
    code2 = ""
    offset = 0
    for i, x in enumerate(np.arange(180, 1340.00 + step, step), start=1):
        y = sqrt(pow(sidecut_radius, 2) - pow(half_overall_length - x, 2))
        y = 10000 - y
        if i == 1:
            offset = 300 - y
            y = offset + y
            code += "M{} {} ".format(x, y)
            code2 += "M{} {} ".format(x, 300 - y)
        else:
            y += offset
            code += "L{} {} ".format(x, y)
            code2 += "L{} {} ".format(x, 300 - y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code))

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code2))

    return content


if __name__ == "__main__":
    pass
