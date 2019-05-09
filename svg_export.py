#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: SVG生成


def write_code(code):
    with open("board_profile.svg", mode="a", encoding="utf-8") as file:
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
    init_content = """"""

    # init_content += """<rect width="1600" height="350" style="fill:none;stroke-width:1;stroke:rgb(0,0,0)" />"""

    # 板头虚线
    init_content += """<line x1="{}" y1="{}" x2="{}" y2="{}"
                style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(nose_length, 0 + 5,
                                                                                         nose_length,
                                                                                         nose_width - 5)

    # 板尾虚线
    init_content += """<line x1="{}" y1="{}" x2="{}" y2="{}"
                   style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(
        nose_length + running_length, 0 + 5,
        nose_length + running_length, tail_width - 5)

    # TODO 超过部分裁剪掉
    # 水平中线虚线
    init_content += """<line x1="{}" y1="{}" x2="{}" y2="{}"
                style="stroke:#000000;stroke-width:1"  stroke-dasharray="5,5"/>""".format(0, half_nose_width,
                                                                                          overall_length,
                                                                                          half_nose_width)
    # 竖直中线虚线
    init_content += """<line x1="{}" y1="{}" x2="{}" y2="{}"
                       style="stroke:#000000;stroke-width:1" stroke-dasharray="5,5"/>""".format(half_overall_length,
                                                                                                0 + 20,
                                                                                                half_overall_length,
                                                                                                nose_width - 20)
    # 版权信息
    init_content += """
    <text x="800" y="200" fill="black" fill-opacity="0.6">
      <a href="https://BoardCAM.org" target="new">
        © BoardCAM
      </a>
    </text>"""
    return init_content


def pack_svg(content):
    """

    :param content: SVG code
    :return:
    """
    write_code("""<svg width="" height="" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
    {}</svg>""".format(content))
