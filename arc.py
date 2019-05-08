#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 有效边刃生成

from math_tools import cal_waist_width


def gen_arc(params):
    """
    有效边刃生成
    :param params: 参数
    :return:
    """
    half_overall_length = params.get("half_overall_length")
    sidecut_radius = params.get("sidecut_radius")
    running_length = params.get("running_length")
    nose_width = params.get("nose_width")
    content = ""
    # 上圆弧
    content += ("""<circle cx="{}" cy="{}" r="{}" stroke="black"
    stroke-width="1" fill="none"/>""".format(half_overall_length, -cal_waist_width(running_length, sidecut_radius),
                                             sidecut_radius))

    # 下圆弧
    content += ("""<circle cx="{}" cy="{}" r="{}" stroke="black"
        stroke-width="1" fill="none"/>""".format(half_overall_length,
                                                 cal_waist_width(running_length, sidecut_radius) + nose_width,
                                                 sidecut_radius))

    return content


if __name__ == "__main__":
    pass
