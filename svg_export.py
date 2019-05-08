#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: SVG生成


def write_code(code):
    with open("test2.svg", mode="a") as file:
        file.write(code)


def init_svg(params):
    """
    生成辅助线 框架
    :param params:
    :return:
    """

    half_nose_width = params.get("half_nose_width")
    half_overall_length = params.get("half_overall_length")
    nose_width = params.get("nose_width")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    overall_length = params.get("overall_length")
    tail_width = params.get("tail_width")

    # write_code("""<line x1="180" y1="0" x2="1380" y2="0" style="stroke:#000000;stroke-width:1"/>""")

    # 水平中线虚线
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
            style="stroke:#000000;stroke-width:1"  stroke-dasharray="5,5"/>""".format(0, half_nose_width,
                                                                                      overall_length, half_nose_width))

    # 板头虚线
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
                style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(nose_length, 0, nose_length,
                                                                                         nose_width))

    # 板尾虚线
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
                   style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(
        nose_length + running_length, 0,
        nose_length + running_length, tail_width))

    # TODO 超过部分裁剪掉
    # 竖直中线虚线
    write_code("""<line x1="{}" y1="{}" x2="{}" y2="{}"
                       style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(half_overall_length, 0,
                                                                                                half_overall_length,
                                                                                                nose_width))


def start_tag():
    write_code(
        """<svg width="" height="" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">""")


def close_tag():
    write_code("""</svg>""")
