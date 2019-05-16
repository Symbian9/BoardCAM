#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 有效边刃生成

from math import sqrt


def gen_arc(params):
    """
    有效边刃路径生成
    :param params: 参数
    :return:
    """
    half_overall_length = params.get("half_overall_length")
    sidecut_radius = params.get("sidecut_radius")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    nose_width = params.get("nose_width")
    content = ""

    step = 10
    code = ""
    code2 = ""
    offset = 0
    top_list = []
    bottom_list = []
    for i, x in enumerate(range(nose_length, running_length + nose_length + step, step), start=1):
    # for i, x in enumerate(np.arange(nose_length, nose_length + running_length + step, step), start=1):
        y = sqrt(pow(sidecut_radius, 2) - pow(half_overall_length - x, 2))
        y = sidecut_radius - y
        if i == 1:
            offset = nose_width - y
            y = offset + y
            code += "M{} {} ".format(x, y)
            code2 += "M{} {} ".format(x, nose_width - y)
        else:
            y += offset
            top_list.append([x, y])
            bottom_list.append([x, nose_width - y])
            code += "L{} {} ".format(x, y)
            code2 += "L{} {} ".format(x, nose_width - y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>\
                <path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(code, code2))

    print("top_list", top_list)
    return content, top_list, bottom_list
